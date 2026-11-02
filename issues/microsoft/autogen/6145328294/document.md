# fix(core): release queue slot on intervention drop/raise to unblock stop_when_idle

## Summary

Fixes a deadlock in `SingleThreadedAgentRuntime.stop_when_idle()`: when an intervention handler drops a message (returns `DropMessage`) or raises, the message queue's unfinished count is never decremented, so `Queue.join()` never completes and `stop_when_idle()` hangs forever.

This continues the work started in #7642, which contained the same core fix but was closed for process reasons (not `wontfix`). This PR reapplies the substantive fix and adds regression tests.

## Root cause

In `_process_next()`, the three intervention-handler blocks (send / publish / response) have six early-return paths — `DropMessage` and exception, for each kind:

- send: `future.set_exception(e)` / `future.set_exception(MessageDroppedException())`, then `return`
- publish: log error / `return`
- response: `future.set_exception(e)` / `future.set_exception(MessageDroppedException())`, then `return`

All six return without calling `self._message_queue.task_done()`. The envelope was already consumed via `queue.get()`, so the queue's unfinished task count leaks one slot per dropped/failed message. `stop_when_idle()` awaits `_message_queue.join()`, which only returns when that count reaches zero → permanent hang.

Every other exit path in the same file already calls `task_done()` (in `_process_send`, `_process_publish`, `_process_response`), so the intervention paths are the only ones missing it.

Note: the queue cannot be swapped under our feet here — `stop()`/`stop_when_idle()`/`stop_when()` replace `self._message_queue` only after the run-loop task completes, and `_process_next()` is awaited by that loop, so `self._message_queue` still refers to the queue the envelope was fetched from. (Open PRs #7963/#8177 address a different race — in-flight background tasks outliving `stop()` — and do not touch these paths.)

## Changes

- `_single_threaded_agent_runtime.py`: call `self._message_queue.task_done()` before each of the six early returns (+6 lines).
- `tests/test_intervention.py`: switch the existing intervention drop/raise tests from `stop()` to `stop_when_idle()` behind a fail-fast timeout helper, and add `test_intervention_drop_publish` / `test_intervention_raise_exception_on_publish` (the publish path had no drop/raise coverage).

## Verification

- Repro script (publish + `DropMessage` handler, `stop_when_idle()` under `asyncio.wait_for`):
  - before: `BUG CONFIRMED: stop_when_idle() hung forever (Queue.join() never completes)`
  - after: `NO BUG: stop_when_idle() returned`
- Without the fix, `test_intervention_drop_send` fails fast with `Failed: stop_when_idle() did not return in time...`; with the fix all tests pass.
- `pytest tests/test_intervention.py tests/test_runtime.py` → 22 passed (Python 3.12, editable install of this commit).