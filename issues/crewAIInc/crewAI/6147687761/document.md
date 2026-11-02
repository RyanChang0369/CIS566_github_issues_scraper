# fix(events): route aemit through dependency-aware dispatch

Fixes #8913

## Problem

`CrewAIEventsBus.aemit()` never consulted `_handler_dependencies`, so events emitted through the async entry point always bypassed dependency-aware dispatch and went straight to `asyncio.gather` over all registered async handlers. The other two dispatch entry points (`emit()` and `replay()`) both check `has_dependencies` and route to `_emit_with_dependencies()`; `aemit()` was the only one that did not.

Consequences for events emitted via `aemit()`:

1. Async `depends_on` chains execute concurrently and out of order instead of level by level.
2. Sync handlers that async handlers depend on are never executed at all, while the dependent async handlers still run.

## Fix

In `aemit()`, read `has_dependencies` inside the existing `r_locked()` block (same pattern as `emit()`), and when true, call `await self._emit_with_dependencies(...)` directly (aemit already runs on the event loop thread, so no `run_coroutine_threadsafe` is needed). The no-dependency behavior is unchanged: only async handlers run, concurrently.

## Relation to #8716

Completely independent: #8716 fixes mixed sync/async handler future tracking in `emit()` (flush() semantics). This PR only touches `aemit()`'s dispatch path — a different function and a different failure mode.

## Verification

- New tests in `lib/crewai/tests/events/test_depends.py`:
  - `test_aemit_respects_async_dependency_chain` — async dependency chain executes in `depends_on` order under `aemit` (failed before the fix, passes after).
  - `test_aemit_runs_sync_dependency_handlers` — sync handler that an async handler depends on is executed under `aemit` (failed before the fix, passes after).
  - `test_aemit_ignores_dependencies` renamed to `test_aemit_without_dependencies_runs_async_only` to reflect preserved no-dependency semantics.
- `test_depends.py`: 12/12 passed.
- Full `tests/events` suite: only pre-existing environment failures (litellm not installed, lancedb `ColumnOrdering` import error); the failure set is identical with and without this change (29 failed / 166 passed both ways, same files), so no regressions.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Changes core event dispatch ordering for async emit paths; wrong ordering could affect listeners that rely on depends_on, but the change aligns with existing emit/replay behavior.
> 
> **Overview**
> **`CrewAIEventsBus.aemit()`** now matches **`emit()`** and **`replay()`** when handlers use **`depends_on`**: it checks **`_handler_dependencies`** and **`await`s `_emit_with_dependencies()`** instead of always **`asyncio.gather`**-ing async handlers.
> 
> That fixes async **`depends_on`** chains running out of order under **`aemit`**, and sync prerequisite handlers being skipped while dependents still ran. When no dependencies are registered, behavior is unchanged—only async handlers run, concurrently.
> 
> Tests rename the old “ignores dependencies” case and add coverage for async chains and sync→async dependency under **`aemit`**.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 2bc43f5bcefd43c0c2dc2477201f869c8ebff0f4. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->