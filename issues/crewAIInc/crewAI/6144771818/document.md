# [BUG] Async native tools run on a per-call event loop, so caller-loop-bound resources fail under kickoff_async

### Description

Async native tools lose the kickoff caller's event loop. When a crew is started with `kickoff_async()` (or `AgentExecutor.invoke_async()`), the sync lane runs in worker threads, and the native tool call path awaits the tool's coroutine via a bare `asyncio.run()` on a **fresh, unrelated event loop per call**.

Any resource bound to the caller's loop — a caller-loop `asyncio.Future`, an `httpx.AsyncClient` created before kickoff, a websocket/socket — therefore fails deterministically:

```
Error executing tool: The future belongs to a different loop than the one specified as the loop argument
```

(same family as #7630, still present on `main` after #8192 promoted `AgentExecutor` out of experimental; the loop-affinity surface just moved from "`asyncio.run` inside the running loop" to "`asyncio.run` in a worker thread").

### Steps to Reproduce

```python
import asyncio, json
from typing import Any

from crewai import Agent, Crew, Process, Task
from crewai.llms.base_llm import BaseLLM
from crewai.tools import tool

HOLDER: dict[str, asyncio.Future] = {}


@tool("async_probe")
async def async_probe(query: str) -> str:
    """Await a caller-loop-bound future, then report what it returned."""
    fut = HOLDER.pop("fut", None)
    if fut is None:
        return f"async-ok:{query}"
    return f"got:{await asyncio.wait_for(fut, timeout=2)}"


class ScriptedLLM(BaseLLM):
    """Stub LLM: emit one native tool call, then a final answer."""

    def __init__(self, responses: list[Any]) -> None:
        super().__init__(model="stub-model")
        self._responses = list(responses)
        self.calls: list[list[dict[str, Any]]] = []

    def supports_function_calling(self) -> bool:
        return True

    def supports_stop_words(self) -> bool:
        return True

    def call(self, messages, tools=None, available_functions=None, **kwargs):
        self.calls.append(list(messages))
        step = self._responses.pop(0)
        if isinstance(step, tuple) and step[0] == "tool":
            return step[1]
        return str(step)


tool_call = [{
    "id": "call_1",
    "type": "function",
    "function": {"name": "async_probe", "arguments": json.dumps({"query": "hello"})},
}]
llm = ScriptedLLM([("tool", tool_call), "final answer"])
agent = Agent(
    role="worker", goal="use the tools", backstory="agent", llm=llm,
    tools=[async_probe], allow_delegation=False, max_iter=6,
)
task = Task(description="use the tool", expected_output="the result", agent=agent)
crew = Crew(agents=[agent], tasks=[task], process=Process.sequential)


async def scenario() -> None:
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    loop.call_later(0.05, fut.set_result, "expected-item")
    HOLDER["fut"] = fut
    await crew.kickoff_async()


asyncio.run(scenario())
```

1. Save the snippet as `repro.py` and run it on current `main` (`f04cce923`).
2. The async tool's coroutine runs on a per-call loop, so awaiting the caller-loop future raises.
3. The LLM sees the failure as the tool result.

### Expected behavior

An async native tool executed during an async kickoff should run with the kickoff caller's loop affinity, so loop-bound resources created before kickoff keep working. The tool result the LLM sees should be `got:expected-item`.

### Screenshots/Code snippets

A/B on `main` @ `f04cce923` (same script, only the source tree differs):

```
# pristine main
TOOL RESULT SEEN BY LLM: Error executing tool: The future belongs to a different loop than the one specified as the loop argument

# with the proposed patch
TOOL RESULT SEEN BY LLM: got:expected-item
```

### Operating System

macOS Sonoma

### Python Version

3.11

### crewAI Version

1.15.33 (source checkout of `main` @ `f04cce923`)

### crewAI Tools Version

1.15.33

### Virtual Environment

Venv

### Evidence

Stack shape on `main`: the sync lane runs the tool call in a worker thread (`asyncio.to_thread` in the flow runtime / `AgentExecutor`), and the native tool path ends in `Tool.run`, whose async branch calls `asyncio.run(self._arun(**kwargs))`. That fresh loop cannot await objects owned by the kickoff caller's loop, and `asyncio.wait_for`/`Future.__await__` raises `RuntimeError: ... different loop`.

This also silently degrades tools that are correct but not loop-independent: an `httpx.AsyncClient` created before kickoff raises on first use, and the exception is swallowed into the tool result string, so the agent reports a tool error instead of a crash.

### Possible Solution

Capture the kickoff caller's loop at the async entry points (`Crew.kickoff_async`, `AgentExecutor.invoke_async`) in a `ContextVar` — ContextVars propagate through `asyncio.to_thread` and the flow runtime's `copy_context`, so every worker lane can see it. Then, in the native tool execution helper, when a caller loop is present **and** the tool has a real async implementation, run the coroutine on that loop (e.g. `asyncio.run_coroutine_threadsafe(tool.arun(**args), caller_loop).result()`, which blocks only the worker thread). Fall back to the exact historical `run()` path for sync tools, sync callers, closed loops, or when already on the target loop.

Sync/`kickoff()` behavior must stay byte-identical; `available_functions` should remain authoritative so cache wrappers and test doubles keep working.

### Additional context

Happy to take this one — I have a patch with regression coverage ready (unit tests for the bridge, sync fallbacks, exactly-once error propagation, and an end-to-end `kickoff_async` test that fails on pristine `main` with the error above and passes with the patch). Will link the PR once this issue exists so the contribution meets the "open issue required" rule.
