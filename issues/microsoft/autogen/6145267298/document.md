# fix(agentchat): pass cancellation_token in MagenticOne structured_output ledger call

## Summary

Fixes a missed `cancellation_token` propagation in the MagenticOne orchestrator's progress-ledger model call for the `structured_output` branch, introduced when structured output support was added in #5863.

In `_orchestrate_step`, the ledger retry loop has three branches. The `structured_output` branch was the only `model_client.create()` call in `MagenticOneOrchestrator` that did not forward `cancellation_token`:

```python
if self._model_client.model_info.get("structured_output", False):
    response = await self._model_client.create(
        self._get_compatible_context(context), json_output=LedgerEntry  # no cancellation_token
    )
elif self._model_client.model_info.get("json_output", False):
    response = await self._model_client.create(
        self._get_compatible_context(context), cancellation_token=cancellation_token, json_output=True
    )
else:
    response = await self._model_client.create(
        self._get_compatible_context(context), cancellation_token=cancellation_token
    )
```

Consequence: when a user cancels a MagenticOne run and the model client supports structured output (e.g. OpenAI), the in-flight progress-ledger LLM call is not interrupted, delaying cancellation by a full orchestration round. All other `create()` calls in the orchestrator already forward the token.

This PR also fixes an off-by-variable bug in the ledger parse error message in the same loop: it reported `len(progress_ledger)` (the parsed ledger dict) instead of `len(output_json)` (the extracted JSON objects actually being validated).

## Changes

- `_magentic_one_orchestrator.py`: pass `cancellation_token=cancellation_token` in the `structured_output` ledger call; fix the error message to report `len(output_json)`.
- `test_magentic_one_group_chat.py`: add `test_magentic_one_group_chat_structured_output_cancellation_token` — runs a MagenticOne team with a `ReplayChatCompletionClient` configured with `structured_output=True` and asserts every recorded `create()` call received the run's `CancellationToken`.

## Testing

- New regression test fails on `main` (ledger call recorded `cancellation_token=None`) and passes with the fix.
- `pytest tests/test_magentic_one_group_chat.py` -> 8 passed.
- `pytest tests/test_group_chat.py` -> 91 passed; the 2 failures (`test_declarative_groupchats_with_config`) are pre-existing and unrelated to this change (missing OpenAI credentials; fail identically on pristine `main`).
- `ruff check` / `ruff format --check` clean on the changed files.
