# [BUG] create_model_from_schema crashes on draft-07 tuple-form items

## Description

`create_model_from_schema` supports `"type": "array"` with a single `items` schema, but it crashes when `items` is a list of positional schemas (JSON Schema draft-07 tuple validation). The 2020-12 equivalent, `prefixItems`, is ignored entirely and silently degrades to an untyped `list`.

In `_json_schema_to_pydantic_type`, the value of `items` is passed straight into the recursive call, which then reads `json_schema.get("$ref")`. A list has no `.get`, so the whole conversion fails with `AttributeError: 'list' object has no attribute 'get'`.

This is reachable from MCP tool registration (`MCPToolResolver._json_schema_to_pydantic`), so a server that declares a tuple-typed argument breaks tool discovery for every tool it exposes. It is also reachable from `structured_tool._deserialize_schema` when a stored tool `args_schema` is restored.

## Steps to Reproduce

```python
from crewai.utilities.pydantic_schema_utils import create_model_from_schema

schema = {
    "type": "object",
    "properties": {
        "pair": {
            "type": "array",
            "items": [{"type": "string"}, {"type": "integer"}],
        },
    },
    "required": ["pair"],
}
create_model_from_schema(schema)
```

```
Traceback (most recent call last):
  ...
  File ".../crewai/utilities/pydantic_schema_utils.py", line 1266, in _json_schema_to_pydantic_type
    item_type = _json_schema_to_pydantic_type(
  File ".../crewai/utilities/pydantic_schema_utils.py", line 1170, in _json_schema_to_pydantic_type
    ref = json_schema.get("$ref")
AttributeError: 'list' object has no attribute 'get'
```

Reproduced on crewAI 1.15.33. `pydantic_schema_utils.py` is identical on `main` at 97bbfb6.

## Expected behavior

The call returns a model. Positional element schemas should constrain the element type instead of crashing: with the schema above, `pair=["a", 1]` validates and `pair=[None]` is rejected.

## Screenshots/Code snippets

The same failure through the MCP path:

```python
schema = {
    "type": "object",
    "properties": {"coords": {"type": "array", "items": [{"type": "number"}, {"type": "number"}]}},
}
# MCPToolResolver._json_schema_to_pydantic("tool", schema) -> AttributeError
```

## Additional context

- OS: Windows 11 (the schema path is platform independent)
- Python: 3.12
- crewAI: 1.15.33

A fix should handle both `items: [...]` (draft-07) and `prefixItems: [...]` (2020-12). Flattening the positional schemas into one element union (`list[Union[...]]`) keeps the existing single-schema behavior unchanged and never rejects an array the schema considers valid, because tuple-form `items` allows extra elements unless `additionalItems`/`items` is `false`.

This issue and the linked pull request were prepared with AI assistance.