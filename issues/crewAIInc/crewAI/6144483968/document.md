# fix(spider): honor the configured default URL

## Related issue
Fixes #8902

## Summary
`SpiderTool(website_url=...)` documents a default URL, but both its input schema and `_run` required a URL on every call. Select an input schema with an optional URL only when a default is configured, and allow `_run` to reach its existing fallback. Keep the unconfigured schema's URL requirement, mode selection, and explicit runtime URL overrides.

## Verification
- [x] Sixteen offline cases cover configured/unconfigured tools, omitted/overridden URLs, public `run()`/structured `invoke()`, and scrape/crawl modes.
- [x] Tests use the actual Spider SDK's request construction while mocking its API dispatch boundary. They verify the target URL, scrape/crawl limits, custom parameters, response propagation, and required-URL validation for unconfigured tools.
- [x] Before: 4 failures, 12 passing controls. After: all 16 pass with both spider-client 0.1.93 and the repository-locked 0.1.88.
- [x] Ruff, Ruff format, mypy, pre-commit and `git diff --check` pass on main `1a3089fd`.

Command: `OTEL_SDK_DISABLED=true CREWAI_DISABLE_TELEMETRY=true CREWAI_TRACING_ENABLED=false uv run --no-sync pytest lib/crewai-tools/tests/tools/test_spider_default_url.py -o addopts='' --block-network --tb=short -q`.

## Additional context
No live API request or real credential was used. The optional SDK was installed only in the validation environment; dependency files are unchanged, and the test module skips if it is absent. URL validation, custom parameters and existing error handling are retained.

AI disclosure: prepared and tested by Codex at the account owner's request. No independent human review is claimed. Please apply `llm-generated`; the integration's label API request returned 403. Maintainer approval and repository CI remain outstanding.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Scoped to SpiderTool input validation and URL resolution with regression tests; no auth, data, or dependency changes.
> 
> **Overview**
> **SpiderTool** now matches its documented behavior when constructed with a default `website_url`: callers can omit the URL at run time and the tool uses the configured value, while tools without a default still require one.
> 
> When a default URL is set at init, the tool switches to an input schema where `website_url` is optional and refreshes its description; `_run` accepts an optional URL so the existing `website_url or self.website_url` fallback actually runs. Runtime overrides and scrape/crawl mode behavior are unchanged.
> 
> Adds parametrized offline tests (configured vs unconfigured, override vs omit, `run()` vs structured `invoke()`, scrape vs crawl) that mock the Spider API and assert the resolved URL, limits, and custom params reach the request.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit a2169df5a7277abb9bec0016ddc83d19ec2cd9cf. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->