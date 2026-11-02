# fix(tools): preserve GithubSearchTool content types

Fixes #8888`n`n## What changed`n`n- persist `content_types` passed to `GithubSearchTool` so later `add()` calls use the configured default;`n- add regression coverage for constructor configuration used by `_run()`.`n`n## Validation`n`n- `CREWAI_TRACING_ENABLED=false uv run pytest --override-ini="addopts=" lib/crewai-tools/tests/tools/test_search_tools.py::test_github_search_tool_constructor_content_types_are_used_for_later_add -q``n- `git diff --check``n`nThe targeted test passed (1 passed). The repository default parallel test setup could not initialize its local tracing encryption key, so the targeted test was rerun with tracing disabled and addopts cleared. AI assistance was used to inspect the issue and prepare the patch; the change and validation were reviewed manually.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Narrow initialization fix in a search tool with new unit test coverage; no auth, data migration, or API contract changes.
> 
> **Overview**
> Fixes constructor-configured **`content_types`** on **`GithubSearchTool`** being ignored when the repo is supplied later via **`_run()`** instead of at initialization.
> 
> **`__init__`** now assigns **`self.content_types`** whenever **`content_types`** is passed, so deferred **`add()`** calls (via **`content_types or self.content_types`**) use the configured scope (e.g. **`repo`** only) rather than the default full list. A regression test covers initializing with **`content_types`** only and searching after passing **`github_repo`** at run time.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 4e3898e6e3cf584b30b53c99c3a9f908c9d84c7e. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->