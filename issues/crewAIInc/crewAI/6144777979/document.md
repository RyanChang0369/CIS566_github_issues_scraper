# fix(agents): run async native tools on the kickoff caller's event loop

Fixes #8904.

Follow-up to #7630 (the closed #7634 was the pre-#8192 fix for the same family).

## The bug (reproduced on `main`)

After #8192, every sync Flow method runs in a worker thread (`asyncio.to_thread`, flow runtime `_execute_method`). An async native tool's coroutine therefore goes through the bare `asyncio.run()` inside `Tool.run` — on a **fresh, unrelated event loop per call**. Anything bound to the kickoff caller's loop fails deterministically:

```
RuntimeError: Task ... got Future <Future pending> attached to a different loop
```

Minimal repro on unpatched `main`: a Crew with one `@tool async def`; the tool awaits a `Future` created on the `kickoff_async` caller's loop after `asyncio.run(crew.kickoff_async())` → the tool result the LLM sees is `Error executing tool: ... attached to a different loop`. Same shape for any caller-loop-bound resource (`httpx.AsyncClient` created before kickoff, sockets).

## The fix

- The async kickoffs capture the caller's event loop into a **ContextVar** (`Crew.kickoff_async` non-stream branch, `AgentExecutor.invoke_async`). `Crew.kickoff_async` is `await asyncio.to_thread(self.kickoff, ...)`, so capturing **before** the thread boundary is what makes the loop visible inside every worker lane — ContextVars propagate through `to_thread` and the Flow runtime's `copy_context` (including the `ThreadPoolExecutor` in `execute_native_tool`).
- `agent_utils.run_native_tool_result(...)` executes the tool: when a caller loop is present **and** the tool has a working async implementation, bridge `tool.arun(**args)` onto the caller loop via `run_coroutine_threadsafe(...).result()` (the worker thread blocks; the coroutine runs with caller-loop affinity). Otherwise the exact historical sync behavior — the `available_functions` mapping stays authoritative, so test doubles and cache wrappers are untouched.
- Async-capability detection: `Tool`-wrapped functions are async iff the wrapped function is a coroutine function (`Tool` always overrides `_arun`, even for sync funcs); class-based `BaseTool`s qualify when their type overrides the `NotImplementedError`-raising `BaseTool._arun`.

## Tests

New `lib/crewai/tests/agents/test_native_async_tool_loop_affinity.py`:

- worker-thread bridge onto a caller-loop `Future` (unit, with and without caller loop),
- full `Crew` + scripted-LLM `kickoff_async` path asserting the caller-loop Future **resolves** instead of the cross-loop error.

## Verification

- `ruff check` clean on all touched files.
- A/B vs pristine `main`: `pytest lib/crewai/tests/agents -k "native or agent_executor or invoke"` — **identical failure sets** (3 pre-existing `TestDeferredNativeToolResults` / `TestResponseFormatWithKickoff` failures reproduce on pristine `main` in this environment; 172 pass on both), plus 4 new green tests.
- With the patch, the repro above returns `got:expected-item` instead of the error.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Changes core async kickoff and native-tool concurrency (ContextVar bridging, thread pools, blocking waits); behavior is scoped and heavily tested but affects all async kickoff + async tool combinations.
> 
> **Overview**
> Fixes async native tools breaking under **`kickoff_async`** when sync Flow work runs in worker threads: coroutines no longer spin up a fresh loop per call, so caller-loop-bound resources (e.g. **`httpx.AsyncClient`**, **`Future`s**) stop failing with *attached to a different loop*.
> 
> **Caller-loop capture:** **`Crew.kickoff_async`** (streaming and non-streaming) and **`AgentExecutor.invoke_async`** store the running loop in a **ContextVar** for the duration of the run, so worker-thread tool paths can see it after **`to_thread`** / context copy.
> 
> **Tool execution:** Native tool dispatch in **`agent_executor`** and **`agent_utils`** now goes through **`run_native_tool_result`**, which schedules **`tool.arun`** on that loop via **`run_coroutine_threadsafe`** when the tool is async; sync tools and missing-loop cases keep the old **`run()`** behavior. Bridging skips when already on the target loop (deadlock guard), propagates tool errors without double execution, and times out after **`CREWAI_NATIVE_TOOL_BRIDGE_TIMEOUT`** (default 300s) with coroutine cancellation.
> 
> **Executor pool split:** Sync **`kickoff`** bodies move from the loop’s default **`asyncio.to_thread`** pool to a dedicated **`run_in_kickoff_thread`** pool so kickoff threads waiting on bridged tools don’t starve the default pool when tools use **`asyncio.to_thread`** inside their coroutines.
> 
> Regression coverage is added in **`test_native_async_tool_loop_affinity.py`** (bridge behavior, E2E **`kickoff_async`**, streaming path, concurrent kickoffs, inherited **`_arun`**).
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit d874b95caf0e2da18912fb231882b06371998440. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->

