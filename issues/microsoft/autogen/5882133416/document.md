# CancellationToken.link_future() cancels asyncio futures from the wrong thread

### What happened?


### Describe the bug

`CancellationToken.link_future()` directly calls `future.cancel()` when the cancellation token is cancelled.

If cancellation happens from a different thread than the future's owning asyncio event loop, this can raise:

`RuntimeError: Non-thread-safe operation invoked on an event loop other than the current one`

The future may already be marked as cancelled even though its completion callbacks were not scheduled correctly.

### To reproduce

This example requires no LLM, external API, or credentials.

```python
import asyncio
import threading
from autogen_core import CancellationToken


async def main():
    loop = asyncio.get_running_loop()
    loop.set_debug(True)

    token = CancellationToken()
    future = token.link_future(loop.create_future())

    future.add_done_callback(lambda _: None)

    worker = threading.Thread(target=token.cancel)
    worker.start()
    worker.join(timeout=2)

    print("Future cancelled:", future.cancelled())


asyncio.run(main())
```

**Observed in an isolated reproduction using the upstream implementation:**

```text
RuntimeError: Non-thread-safe operation invoked on an event loop other than the current one
Future cancelled: True
```

The exception occurs in the worker thread while invoking the cancellation callback.

### Expected behavior

Cancelling a `CancellationToken` from a worker thread should safely cancel its linked asyncio future on the future's owning event loop, without raising a cross-thread exception.

The future's completion callbacks and waiting tasks should be notified correctly.

### Root cause

The registered cancellation callback directly invokes `future.cancel()`:

```python
def _cancel() -> None:
    future.cancel()
```

However, `CancellationToken.cancel()` executes registered callbacks synchronously in the calling thread.

When cancellation originates from another thread, `Future.cancel()` therefore runs outside the owning event loop.

The path handling futures linked to an already-cancelled token also invokes `future.cancel()` directly.

Source:
https://github.com/microsoft/autogen/blob/main/python/packages/autogen-core/src/autogen_core/_cancellation_token.py

A possible fix would schedule cancellation through the owning event loop using `loop.call_soon_threadsafe()`, accounting for event-loop shutdown and cancellation races.

### Screenshots

Not applicable. The problem is reproducible without a graphical interface.

### Additional context

Related PR: https://github.com/microsoft/autogen/pull/8289

PR #8289 addresses callback reentrancy and deadlocks caused by invoking callbacks while holding a non-reentrant lock. Its stated scope explicitly excludes asyncio future/thread-safety changes.

This appears to be a separate issue.

**Validation scope:**

- Python: 3.13
- Source: current upstream `main` implementation
- Reproduction: isolated Python test using the upstream `CancellationToken` methods
- No model or external API required
- Full `autogen-core` package and test suite not executed

The behavior was reproduced using the extracted upstream implementation rather than a fully installed AutoGen release.


### Which packages was the bug in?

Python Core (autogen-core)

### AutoGen library version.

Python dev (main branch)

### Other library version.

_No response_

### Model used

_No response_

### Model provider

_No response_

### Other model provider

_No response_

### Python version

3.13

### .NET version

_No response_

### Operating system

Ubuntu