# fix(schema): handle tuple-form items and prefixItems

## Related issue

Fixes #8891

## Summary

`create_model_from_schema` crashed on JSON Schema draft-07 tuple validation (`"items": [...]`): the list was handed to the single-schema conversion path, which reads `$ref` from it, so the call failed with `AttributeError: 'list' object has no attribute 'get'`. The 2020-12 `prefixItems` keyword was ignored entirely, and those arrays silently became untyped `list`s.

The change leaves the existing `items: {schema}` path untouched. When `items` is a list, or `prefixItems` is present, the positional schemas are converted and flattened into one element union (`list[Union[...]]`), together with a draft-07 `additionalItems` schema when one is declared. Tuple-form `items` allows extra elements unless `items`/`additionalItems` is `false`, so unioning the declared element types keeps every array the schema accepts valid while still constraining each element.

## Verification

- `pytest lib/crewai/tests/utilities/test_pydantic_schema_utils.py -q` → 98 passed (95 existing + 3 new)
- All three new tests fail on `main` (the two tuple/prefix cases with the reported `AttributeError`, the `additionalItems` case with a validation error) and pass with the change
- `ruff format --check` clean; `ruff check` reports the same 3 pre-existing findings as `main`; `mypy` reports no new errors
- Pydantic's own `tuple[str, int]` schema (2020-12 `prefixItems` + `minItems`/`maxItems` and no `items` key) now yields `list[Union[str, int]]` instead of an untyped `list`

- [x] Tests added or updated for the changed behavior
- [x] Relevant tests and quality checks pass locally

## Additional context

AI-assisted change, as disclosed per `CONTRIBUTING.md`. I cannot apply the `llm-generated` label myself; please add it.

Compatibility: no new syntax beyond `list[...]`/`Union[...]`, which this module already uses, so Python 3.10+ is unaffected.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Changes are confined to JSON-schema-to-Pydantic conversion in a utility module; impact is limited to how external/tool schemas validate array fields, with regression tests for the new paths.
> 
> **Overview**
> Fixes **`create_model_from_schema`** so positional array schemas no longer crash or degrade to untyped lists.
> 
> When JSON Schema uses **Draft-07 tuple validation** (`items` as a list) or **2020-12 `prefixItems`** (optionally with a trailing `items` / `additionalItems` schema), conversion now collects those per-position schemas and builds **`list[Union[...]]`** instead of passing a list into the single-`items` path (which raised **`AttributeError: 'list' object has no attribute 'get'`**). Homogeneous **`items: { ... }`** arrays behave as before.
> 
> Three tests cover tuple **`items`**, **`additionalItems`**, and **`prefixItems` + `items`**, including rejection of invalid elements.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit d009388b16fcbcfd03e22862a68c9103775361d7. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->