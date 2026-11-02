# Replace deprecated asyncio.get_event_loop() with asyncio.get_running_loop() in coroutine contexts

## Summary

`asyncio.get_event_loop()` is deprecated since Python 3.12 (and raises `RuntimeError` in Python 3.14 when no current loop exists). In coroutine contexts the recommended replacement is `asyncio.get_running_loop()`, which returns exactly the same loop with no deprecation.

This PR replaces the three usages in `lib/crewai` that are always executed inside a running event loop:

- `src/crewai/tools/structured_tool.py` — inside `async def _arun`, so a loop is always running
- `src/crewai/rag/chromadb/client.py` — inside `async def _alocked`, so a loop is always running
- `src/crewai/utilities/streaming.py` — the `use_async=True` branch of `create_streaming_state`, which is only reached from async kickoff paths (`Crew.kickoff_async` / streaming kickoff), so a loop is always running

## Changes

One-line, behavior-identical replacement of `asyncio.get_event_loop()` with `asyncio.get_running_loop()` in each of the three files above.

## Verification

- `py_compile` passes for all three files
- `ruff check --no-fix` reports no new findings on the changed lines (existing findings in these files are pre-existing and untouched)
- Call-path analysis confirms each site executes only inside a coroutine, so `get_running_loop()` returns the same loop `get_event_loop()` would

Fixes #8912

Note: this PR supersedes #8910, which was submitted without an issue reference and auto-closed by the first-time-contributor gate as a result (reopen is not permitted for external contributors).

## LLM disclosure

This change was prepared with the assistance of an AI coding agent and reviewed before submission. Per the repository's contribution guidelines, please add the `llm-generated` label to this PR if appropriate (I don't have permission to add labels myself).

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Mechanical asyncio API update with no intended behavior change; each site is already inside a running coroutine.
> 
> **Overview**
> Replaces **deprecated** `asyncio.get_event_loop()` with `asyncio.get_running_loop()` in three `lib/crewai` call sites that always run inside an active event loop, avoiding Python 3.12+ deprecation warnings and Python 3.14 failures when no default loop exists.
> 
> The swap is one line each in **ChromaDB async locking** (`_alocked`), **sync tool execution from** `ainvoke` via `run_in_executor`, and **async streaming setup** when `create_streaming_state(use_async=True)` (and the same pattern already used in frame streaming). Runtime behavior should be unchanged: the running loop is the same object the old API would return in these paths.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 20d369f413194293dd496f3a19814913ea477205. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->