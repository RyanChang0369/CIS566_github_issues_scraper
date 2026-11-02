# fix(core): support positional-only arguments in FunctionTool.run()

Fixes #8319

### Summary
In `FunctionTool.run()`, arguments extracted from the validated `args` model were previously all passed as keywords via `**kwargs`. When a tool function defines positional-only parameters (`/`), Python raises `TypeError: <func>() got some positional-only arguments passed as keyword arguments`. Similarly, if `cancellation_token` was declared as a positional-only parameter, passing it as a keyword argument caused a `TypeError`.

This PR:
1. Inspects parameter kind in `self._signature.parameters`.
2. Gathers positional-only arguments (including positional-only cancellation tokens) into `pos_args` and remaining parameters into `kwargs`.
3. Calls `self._func(*pos_args, **kwargs)` across both synchronous (via executor/partial) and asynchronous executions.
4. Adds unit tests covering synchronous and asynchronous functions with positional-only parameters and positional-only cancellation tokens.