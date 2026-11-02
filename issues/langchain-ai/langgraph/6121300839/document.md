# sdk-py: get_client(url=None) accepts timeout= but never applies it — in-process calls cannot be bounded

### Checked other resources

- [x] This is a bug, not a usage question.
- [x] I added a clear and descriptive title that summarizes this issue.
- [x] I used the GitHub search to find a similar question and didn't find it.
- [x] I am sure that this is a bug in LangGraph rather than my code.
- [x] The bug is not resolved by updating to the latest stable version of LangGraph (or the specific integration package).
- [x] This is not related to the langchain-community package.
- [x] I posted a self-contained, minimal, reproducible example. A maintainer can copy it and run it AS IS.

### Related Issues / PRs

- #6654 — `runs.stream` with `url=None` buffering or hanging in v0.6 (closed). Same transport,
  different symptom: that report is about streaming updates arriving late, this one is about
  `timeout=` never being applied. Not a duplicate.
- #9499 — same class of failure on the network path (server heartbeats reset the read timeout).
  Separate symptom and separate layer, so a separate issue.

### Reproduction Steps / Example Code (Python)

Installing a LangGraph server locally to reproduce is heavy, so this supplies the loopback
transport directly, with a handler that sleeps 10 s. `langgraph-sdk` and `httpx` only:

```python
import asyncio, time
import httpx

async def slow_app(scope, receive, send):
    if scope["type"] != "http":
        return
    await asyncio.sleep(10)                     # a handler that outlives any client budget
    await send({"type": "http.response.start", "status": 200,
                "headers": [(b"content-type", b"application/json")]})
    await send({"type": "http.response.body", "body": b'{"thread_id": "x"}'})

async def main():
    import langgraph_sdk._async.client as lgclient
    # url=None builds its transport from this factory; substitute one that serves slow_app
    lgclient.get_asgi_transport = lambda *a, **kw: (
        lambda app=None, root_path="": httpx.ASGITransport(app=slow_app)
    )
    client = lgclient.get_client(url=None, timeout=1.0)
    print(client.http.client.timeout)           # Timeout(timeout=1.0)
    t = time.perf_counter()
    await client.threads.get("x")               # no exception, no bound
    print(f"returned after {time.perf_counter() - t:.1f}s")

asyncio.run(main())
```

When a LangGraph server package is installed, the factory supplies its own transport instead of this
one; the measurement quoted below uses that transport, unmodified.

### Error Message and Stack Trace (if applicable)

```
client timeout = Timeout(timeout=1.0)
returned after 10.1s        # the handler's whole duration; timeout=1.0 was never applied
```

Python 3.11.16, `langgraph-sdk` 0.4.10, `httpx` 0.28.1, in a clean environment with only the SDK
installed.

Same result through the transport the SDK actually builds when a LangGraph server package is
installed, driven by a handler that sleeps 10 s: before any fix, `get_client(url=None, timeout=1.0)`
returned after 10.00 s with no exception.

### Description

* I am using `get_client(url=None)` from inside a node and passing `timeout=` to bound a slow or
  stuck handler. The docstring describes `url=None` as attempting an in-process connection first.
* I expect the call to raise `ReadTimeout` after the configured interval, the way it does against
  a URL.
* Instead the argument is accepted but never applied: the caller waits for the handler however long
  it takes. Replace the 10 s sleep with a handler that never returns and the call never returns
  either.

The same setting against `url="http://..."`, pointed at a server that accepts the connection and never
answers, does what it should: `httpx.ReadTimeout` after 1.02 s. So `timeout=1.0` is honoured on the
network path and dropped on the loopback path.

Note that `get_sync_client(url=None)` always goes over TCP, so this affects the async factory only.

This is the path used inside a node, which is exactly where a stuck handler parks a request slot,
so the missing bound is what turns one slow call into a hung worker.

Wrapping the call in `asyncio.timeout(...)` works as a workaround, but `timeout=` being accepted
and silently ignored is the bug.

Requesting assignment so I can open the PR. I have the patch and tests ready; the change applies
the client's existing timeout to the loopback path rather than adding a new option, and
`timeout=None` keeps meaning "wait indefinitely".
