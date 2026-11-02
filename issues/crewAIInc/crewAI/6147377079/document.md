# Replace deprecated asyncio.get_event_loop() with asyncio.get_running_loop() in Snowflake search tool

## Summary

`asyncio.get_event_loop()` is deprecated since Python 3.12 (and raises `RuntimeError` in Python 3.14 when no current loop exists). In coroutine contexts the recommended replacement is `asyncio.get_running_loop()`, which returns exactly the same loop with no deprecation.

## Changes

One-line, behavior-identical replacement in `lib/crewai-tools`:

- `src/crewai_tools/tools/snowflake_search_tool/snowflake_search_tool.py` — `_get_connection()` is an `async def`, so a loop is always running when `await asyncio.get_running_loop().run_in_executor(...)` is reached.

Note: the Snowflake tool's sibling `stagehand_tool.py` uses `get_event_loop()` in sync bridge methods; that pattern requires a slightly larger refactor (handling the no-running-loop case), so it is intentionally left out of this minimal PR.

## Verification

- `py_compile` passes
- `ruff check --no-fix` reports no new findings on the changed line (existing findings in this file are pre-existing and untouched)

Fixes #8912

Note: this PR supersedes #8911, which was submitted without an issue reference and auto-closed by the first-time-contributor gate as a result (reopen is not permitted for external contributors).

## LLM disclosure

This change was prepared with the assistance of an AI coding agent and reviewed before submission. Per the repository's contribution guidelines, please add the `llm-generated` label to this PR if appropriate (I don't have permission to add labels myself).

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Single-line asyncio API swap in an async method with no logic or connection-handling changes.
> 
> **Overview**
> Updates **`SnowflakeSearchTool._get_connection()`** so that when the connection pool is empty, blocking Snowflake connection creation still runs via **`run_in_executor`**, but the event loop is obtained with **`asyncio.get_running_loop()`** instead of the deprecated **`asyncio.get_event_loop()`**.
> 
> This is a behavior-preserving change for Python 3.12+ (and avoids **`RuntimeError`** when no loop is set in 3.14), because **`_get_connection`** is only called from async code paths where a loop is already running.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 2b079d0a02a3dd4c9e1ab507b9df8723ad82c903. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->