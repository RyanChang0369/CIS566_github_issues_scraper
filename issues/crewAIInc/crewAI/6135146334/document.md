# fix(qdrant): isolate per-search filter conditions

## Related issue
Fixes #8884

## Summary
Searching `red` then `blue` with a configured Qdrant filter appended both conditions to its shared `must` list, so the second search returned nothing and later calls retained old constraints. Deep-copy the configured filter before appending a per-call condition.

## Verification
- [x] A real local `:memory:` Qdrant collection, fixed embeddings, and three records exercise consecutive red, blue, and unfiltered searches. The configured tenant filter continues excluding the other tenant; the original filter remains unchanged.
- [x] Three parameterized cases cover no configured filter, an empty `must`, and an existing tenant condition. Before: two fail, one passes. After: all three pass.
- [x] Ruff, Ruff format, mypy, pre-commit, and `git diff --check` pass.

Tested with Python 3.13.12 and qdrant-client 1.20.0. The optional client was installed only in the validation environment; no dependency files changed. The module skips if qdrant-client is unavailable.

Command: `OTEL_SDK_DISABLED=true CREWAI_DISABLE_TELEMETRY=true CREWAI_TRACING_ENABLED=false uv run --no-sync pytest lib/crewai-tools/tests/tools/test_qdrant_filter_isolation.py -o addopts='' --block-network --tb=short -q`.

## Additional context
No live Qdrant server or embedding API was used. This changes only copy isolation, not filtering semantics.

AI disclosure: prepared and tested by Codex at the account owner's request. No independent human review is claimed. Please apply `llm-generated`; the integration cannot apply labels (403).

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Single-line copy behavior fix in the vector search tool with no auth or data-model changes; regression covered by new tests.
> 
> **Overview**
> Fixes a bug where **each search reused and mutated** the shared `QdrantConfig.filter`, so `filter_by` / `filter_value` conditions stacked in `must` and later queries could return no results.
> 
> **`QdrantVectorSearchTool._run`** now calls **`model_copy(deep=True)`** instead of a shallow copy before appending per-call field conditions, so the configured filter stays unchanged across calls.
> 
> Adds **`test_qdrant_filter_isolation`**, an in-memory Qdrant test (skipped without `qdrant-client`) that runs red, blue, and unfiltered searches in sequence and asserts results and that the original configured filter is unchanged—covering no filter, empty `must`, and a tenant constraint.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit be9c28ddf9fcdfe7c62f07a6715bb42e190aae03. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->