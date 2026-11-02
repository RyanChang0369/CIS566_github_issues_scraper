# [BUG] Deprecated asyncio.get_event_loop() calls in lib/crewai and lib/crewai-tools

### Description

Several places in the monorepo call `asyncio.get_event_loop()`. This API is deprecated since Python 3.12, and as of Python 3.14 it raises `RuntimeError` whenever no current event loop exists. All the affected sites below execute inside coroutines, where the recommended, behavior-identical replacement is `asyncio.get_running_loop()`.

Affected locations (all reached only inside `async def` execution paths):

**lib/crewai**
- `src/crewai/tools/structured_tool.py` — `CrewStructuredTool._arun` runs sync tools via `asyncio.get_event_loop().run_in_executor(...)`
- `src/crewai/rag/chromadb/client.py` — `ChromaDBClient._alocked` captures the loop to acquire/release the cross-process lock in an executor
- `src/crewai/utilities/streaming.py` — `create_streaming_state(use_async=True)` captures the loop for async queue wake-ups (only called from async kickoff paths, e.g. `Crew.kickoff_async` / streaming kickoff)

**lib/crewai-tools**
- `src/crewai_tools/tools/snowflake_search_tool/snowflake_search_tool.py` — `SnowflakeSearchTool._get_connection` creates new connections in a thread-pool executor

### Steps to Reproduce

1. Install Python 3.14 and enable deprecation warnings (`python -W error::DeprecationWarning` or `warnings.simplefilter("always")`).
2. Exercise any of the code paths above (e.g. call a sync tool through `CrewStructuredTool._arun`, or run a crew with `stream=True` via the async kickoff).
3. Each call to `asyncio.get_event_loop()` triggers the CPython deprecation; on 3.14 the API is scheduled to raise `RuntimeError` whenever no current loop exists.

### Expected behavior

No deprecated asyncio API usage in these coroutine contexts: `asyncio.get_running_loop()` returns the same loop that `get_event_loop()` would return inside a running loop, without the deprecation.

### Possible Solution

One-line replacement of `asyncio.get_event_loop()` with `asyncio.get_running_loop()` at each of the four sites above. I have two PRs implementing exactly this change — #8914 (lib/crewai, three sites) and #8915 (lib/crewai-tools, Snowflake tool) — both of which were auto-closed pending an associated issue, and both reference this issue going forward.

### Additional context

The stagehand tool (`stagehand_tool.py`) also uses `get_event_loop()` in its sync bridge methods, but that pattern requires a slightly larger refactor to handle the no-running-loop case correctly, so it is intentionally left for a separate change.
