# fix(flow): re-run loop methods that completed after a checkpoint resume

## Related issue

Fixes #8927

## Summary

A flow with a loop, restored from a checkpoint after a method failed, stopped after one pass and skipped the remaining passes and the listener that ends the loop. No error was raised.

Root cause: while a restored flow is resuming, `_execute_single_listener` skips any method in `_completed_methods`. The resuming flag stays set for the whole run, so a method that completed after the resume was treated like one the checkpoint recorded, and the loop was cut short.

Fix: track the methods that ran since the resume (`_executed_since_resume`) and only skip a completed method if it is not in that set. A method the checkpoint recorded as completed is skipped once, then added to the set, so a later visit in the same run executes it.

## Verification

- [x] Tests added or updated for the changed behavior
- [x] Relevant tests and quality checks pass locally

- `test_cyclic_flow_resumed_from_checkpoint_keeps_looping` reproduces the flow from the issue. It fails without the fix (`[0, 0] != [0, 0, 1, 2]`) and passes with it. The test writes the checkpoint directly with `_do_checkpoint`, so it does not depend on event-bus thread timing.
- `pytest tests/test_flow_resumability_regression.py`: 5 passed, repeated 25 times in random order.
- `ruff format --check` and `ruff check` clean on the changed test file.
- `mypy lib/crewai/src/crewai/flow/runtime/__init__.py` (1.19.1): 6 errors, the same 6 on the base commit (unfollowed imports in this environment).

## Additional context

This does not address the case where the method fails in a later pass after the router already completed (#8437 / #8446). The change was checked with unit tests only.

Drafted with AI assistance (Claude); not yet reviewed by the author.
