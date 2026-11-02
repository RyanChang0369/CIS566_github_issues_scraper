# fix(core): threadsafe asyncio future cancellation in CancellationToken

Closes #8358

### Summary
Fixes cross-thread cancellation in `CancellationToken.link_future()` when cancellation originates from a background thread or thread pool worker.

### Problem
Previously, `CancellationToken.cancel()` executed callbacks synchronously in the invoking thread, calling `future.cancel()` directly outside the future's owning event loop. Under debug mode or cross-thread execution, this raised:
`RuntimeError: Non-thread-safe operation invoked on an event loop other than the current one`

### Solution
- Introduced threadsafe future cancellation via `loop.call_soon_threadsafe(future.cancel)` when the future's owning event loop is running.
- Falls back to direct cancellation when the loop is not running or shutdown.
- Added unit test `test_cancellation_token_threadsafe_link_future` verifying safe future cancellation from worker threads.