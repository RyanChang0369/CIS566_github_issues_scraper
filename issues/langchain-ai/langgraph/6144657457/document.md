# sdk-py: a stream that drops before its first event reconnects without limit

### Description

`StreamController` and `SyncStreamController` reopen the shared SSE after a transport drop, with a budget of `max_reconnect_attempts` (default 5). That budget only counts reconnects that fail to **open**: `_reconnect_shared_stream` returns `True` as soon as the new stream reaches `ready`, so a peer that accepts the connection and then ends it before sending a single event resets the budget on every cycle.

The subscription never terminates. Against a peer that keeps accepting, the client reconnects for as long as the peer allows it, and the caller sees neither events nor an error.

The client-stream path already states the intended rule — #9462 resets its five attempts "once a reconnect yields an event". The v3 controllers reset on a successful open instead, which is why the same peer behaviour is bounded there and unbounded here.

### Reproduction Steps / Example Code (Python)

Real socket, no mocks. The server answers the SSE POST with `200` + `Transfer-Encoding: chunked` and then closes the connection mid-body without a terminating chunk — what a proxy or load balancer does when it kills a connection.

```python
import asyncio
import contextlib
import time

import httpx

from langgraph_sdk.stream.controller import StreamController
from langgraph_sdk.stream.transport.http import ProtocolSseTransport

HEADERS = (
    b"HTTP/1.1 200 OK\r\n"
    b"Content-Type: text/event-stream\r\n"
    b"Transfer-Encoding: chunked\r\n"
    b"\r\n"
)


class DropServer:
    """Answers every request with 200 + chunked, then hangs up without sending an event."""

    def __init__(self) -> None:
        self.connections = 0

    async def handle(self, reader, writer) -> None:
        self.connections += 1
        with contextlib.suppress(Exception):
            await asyncio.wait_for(reader.readuntil(b"\r\n\r\n"), timeout=5)
        try:
            writer.write(HEADERS)
            await writer.drain()
            writer.close()          # FIN mid-body: truncated chunked payload
            with contextlib.suppress(Exception):
                await writer.wait_closed()
        except Exception:
            pass


async def main() -> None:
    state = DropServer()
    server = await asyncio.start_server(state.handle, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]

    client = httpx.AsyncClient(base_url=f"http://127.0.0.1:{port}", timeout=httpx.Timeout(30.0))
    controller = StreamController(transport=ProtocolSseTransport(client=client, thread_id="thread-1"))

    finished = False

    async def consume() -> None:
        nonlocal finished
        async for _ in controller.subscribe(["values"]):
            pass
        finished = True

    task = asyncio.create_task(consume())
    started = time.monotonic()
    await asyncio.sleep(5.0)

    print(f"connections accepted in {time.monotonic() - started:.1f}s: {state.connections}")
    print(f"subscription finished: {finished}")

    task.cancel()
    with contextlib.suppress(BaseException):
        await task
    await controller.close()
    await client.aclose()
    server.close()


if __name__ == "__main__":
    asyncio.run(main())
```

Output on `main` (`e5c961d7`), and with the patch below applied:

| | connections accepted in 5s | subscription finished |
|---|---|---|
| `main` | **518** | `False` |
| patched | **6** | `True` |

(The exact count is just how fast the loop spins on this machine; repeated runs on `main` landed between roughly 410 and 520. The point is that nothing bounds it.)

Two neighbouring cases, same harness, for contrast — neither reconnects on `main`, so they are not part of this report:

- a clean end (proper `0\r\n\r\n` terminator): 1 connection, the subscription finishes normally.
- an immediate TCP reset after the headers: 1 connection, no reconnect.

### Root cause

`_reconnect_shared_stream` treats *a stream that reached `ready`* as a successful attempt, and a stream that reached `ready` then dropped counts for nothing — so a drop after a successful open never advances the budget.

### Expected behavior

A reconnect that delivers no event before dropping should count against the same budget as a reconnect that fails to open, and should back off before retrying, so a peer that accepts and immediately ends connections cannot hold the client in a reconnect loop.

### Notes

When the budget is exhausted today, the subscription ends and subscriber queues receive the end-of-stream sentinel — no error reaches the caller. Whether that should raise instead is a public-API decision, so the patch below leaves it as is.

### Related Issues / PRs

- #9462 — the client-stream path that documents "reset the five attempts once a reconnect yields an event"
- #9499 — an idle stream whose read timeout is held open by heartbeat comments
- #9500 — the client timeout not applying to the in-process transport
