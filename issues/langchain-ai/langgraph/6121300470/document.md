# sdk-py: timeout= does not bound runs.stream() — server SSE heartbeats reset the read timeout forever

### Checked other resources

- [x] This is a bug, not a usage question.
- [x] I added a clear and descriptive title that summarizes this issue.
- [x] I used the GitHub search to find a similar question and didn't find it.
- [x] I am sure that this is a bug in LangGraph rather than my code.
- [x] The bug is not resolved by updating to the latest stable version of LangGraph (or the specific integration package).
- [x] This is not related to the langchain-community package.
- [x] I posted a self-contained, minimal, reproducible example. A maintainer can copy it and run it AS IS.

### Related Issues / PRs

- #9299 — comment-only SSE heartbeats, same traffic, different symptom (phantom event after an
  event ID). Not a duplicate: it is about decoding, this is about the call never returning.
- #6654 — in-process streaming behaviour in v0.6 (closed). Background, not a duplicate.

### Reproduction Steps / Example Code (Python)

A local socket server that answers `text/event-stream` and then writes the same comment-only
heartbeat the server writes, every second, and nothing else. Standard library plus
`langgraph-sdk` only.

```python
import socket, threading, time
from langgraph_sdk import get_sync_client

s = socket.socket()
s.bind(("127.0.0.1", 0))
s.listen(1)
PORT = s.getsockname()[1]

def serve():
    conn, _ = s.accept()
    conn.recv(65536)                                   # request line + headers, ignored
    conn.sendall(b"HTTP/1.1 200 OK\r\n"
                 b"Content-Type: text/event-stream\r\n"
                 b"Cache-Control: no-cache\r\n\r\n")
    while True:
        conn.sendall(b": heartbeat\n\n")               # bytes, never an event
        time.sleep(1)

threading.Thread(target=serve, daemon=True).start()
time.sleep(0.1)

client = get_sync_client(url=f"http://127.0.0.1:{PORT}", api_key=None, timeout=10)
print(client.http.client.timeout)          # Timeout(timeout=10.0)
for part in client.runs.stream(thread_id="t", assistant_id="a", input={}):
    print(part)                            # never reached; the loop never ends
```

### Error Message and Stack Trace (if applicable)

None. That is the report.

```
client timeout                        server                         outcome
Timeout(connect=5, read=300, ...)     accepts, then stays silent     ReadTimeout after 300 s   (control)
Timeout(connect=5, read=300, ...)     heartbeats, no event            did not return; my watchdog killed the process at 962 s; no exception
Timeout(timeout=10.0)                 heartbeats, no event            did not return; my watchdog killed the process at 181 s; no exception
Timeout(timeout=5)                    real `langgraph dev` server     one metadata event at 0.7 s, then nothing; killed at 60 s; no exception
```

The timeout is not missing, and it is not the default that is wrong: on a server that accepts the
connection and says nothing, the same client raises `ReadTimeout` on schedule. It is only inert
when the connection carries heartbeats.

The last row is the same client against a real `langgraph dev` server running a graph whose node
sleeps. This one is a legitimately long node, which is the point: from the client, a long node and a
stuck one look identical, so the caller needs a way to set its own ceiling. In every run with
heartbeats the process had to be killed; the client never returned or raised on its own.

### Description

* I am calling `client.runs.stream(...)` against a LangGraph server and passing `timeout=`,
  expecting a bound on how long the call can go without progress.
* I expect the call to raise `ReadTimeout` when nothing arrives for the configured interval.
* Instead the call runs forever, because the server keeps the connection alive with SSE comment
  lines.

The heartbeats are intentional — I assume to keep long runs from being cut by proxies — and I am not
asking to change them. The problem is that `timeout=` then has no effect on a stream at all.

The reason is what the read timeout measures. `read` is the maximum gap between two *bytes*.
While a stream is open the server writes a comment-only SSE heartbeat, `: heartbeat`, every few
seconds — a 20-second `curl -N` capture against a local server shows three of them. A comment is
bytes, so every heartbeat resets the clock, and no interval a caller can pass will ever elapse.
Against a stream that never finishes, `timeout=` is silently inert.

Both the sync and async clients decode the stream the same way; the repro above uses the sync one.

One consequence: a run that never finishes (a stuck node, a graph waiting on something that never
arrives, a run the server lost track of) parks the caller forever. Async callers can wrap the call in
`asyncio.timeout(...)`; sync callers have no equivalent, because a thread blocked in a socket read
cannot be interrupted.

This is a design question as much as a bug. **Which layer should carry the bound?** A client-side
opt-in (a "no decoded event for N seconds" deadline, default off, existing behaviour untouched) is
one option; a server-side limit on stream lifetime or idle time is another, and it would also cover
clients that are not the Python SDK. I am aware `AGENTS.md` says the SDKs stay thin and that new
public surface for ergonomics alone is ruled out, so I do not want to assume the client-side answer
is the one you want. I have prepared a client-side opt-in, but I would rather ask which layer you
want before opening anything.

### System Info

```
System Information
------------------
> OS:  Windows
> OS Version:  10.0.22631
> Python Version:  3.11.16 (main, Sep  1 2026, 14:15:24) [MSC v.1944 64 bit (AMD64)]

Package Information
-------------------
> langchain_core: 1.7.1
> langsmith: 0.14.15
> langgraph_sdk: 0.4.10

Other Dependencies
------------------
> anyio: 4.15.1
> httpx: 0.28.1
> orjson: 3.13.0
> pydantic: 2.14.2
```

The last row of the table was measured against `langgraph dev` with langgraph-api 0.17.0 on this
machine.

If the client is the right layer for this, I have an opt-in patch and tests ready (no breaking
change, default keeps today's behaviour) and will open a PR once the issue is assigned.
