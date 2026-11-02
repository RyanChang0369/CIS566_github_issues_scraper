# fix(scrapegraph): preserve configured extraction prompt

## Related issue
Fixes #8900

## Summary
The README's Custom Prompt example passes an extraction prompt at construction and only a URL to `run()`. The dynamic schema inserted its generic prompt, overriding the configured instruction. Treat the per-call prompt as optional and choose the per-call value, then constructor configuration, then the existing generic default.

## Verification
- [x] Nine offline tests use the actual locked scrapegraph-py 1.47.0 SDK's built-in mock mode and inspect the JSON prepared for SmartScraper.
- [x] Public `run()` and structured `invoke()` both preserve a configured prompt, accept an explicit override, and retain the generic fallback. A fixed-URL control preserves its configured prompt.
- [x] Before: 2 failures, 7 passing controls. After: all 9 pass.
- [x] Ruff, Ruff format, mypy, pre-commit and `git diff --check` pass on main `1a3089fd`.

Command: `OTEL_SDK_DISABLED=true CREWAI_DISABLE_TELEMETRY=true CREWAI_TRACING_ENABLED=false uv run --no-sync pytest lib/crewai-tools/tests/tools/test_scrapegraph_prompt_configuration.py -o addopts='' --block-network --tb=short -q`.

## Additional context
No live requests or real credentials were used. The optional SDK was installed only in the validation environment; dependency declarations and the supported v1 constraint remain unchanged. The test module skips if the optional SDK is absent. The SDK emits its existing v1 deprecation warning. Client lifecycle and URL validation are unchanged.

AI disclosure: prepared and tested by Codex at the account owner's request. No independent human review is claimed. Please apply `llm-generated`; the integration's label API request returned 403. Maintainer approval and repository CI remain outstanding.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Narrow behavior fix in optional prompt handling for one tool; tests lock in precedence without touching auth or core infrastructure.
> 
> **Overview**
> Fixes a bug where **constructor-configured extraction prompts were ignored** when `run()` or structured `invoke()` only passed a URL. The dynamic tool schema used to default `user_prompt` to the generic main-content string, so that value overwrote `self.user_prompt` via `kwargs.get(..., self.user_prompt)`.
> 
> **`user_prompt` is now optional on the schema** (`None` by default), and `_run` resolves the prompt in order: **runtime override → tool configuration → generic fallback** (`"Extract the main content of the webpage"`).
> 
> Adds offline tests (mocked `scrapegraph-py` client) covering `run()` and structured invoke across configured/runtime prompt combinations, plus fixed-URL tools that call `run()` with no args.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 39453cb567dd07b20eee97aa6ba5454c114f0ee8. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->