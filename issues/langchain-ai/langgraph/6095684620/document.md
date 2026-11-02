# sdk-py: full tool delta buffer raises QueueFull on completion and leaves deltas hanging

### Checked other resources
- [x] This is a bug, not a usage question.
- [x] I searched existing issues and PRs.
- [x] I reproduced this with public client APIs on the current main branch.
- [x] The example below uses a local HTTPX fixture and requires no server or credentials.

### Related Issues / PRs
#8429 concerns the subscription event queue; #9282 concerns the SSE transport queue. This report concerns the independent `ToolCallHandle._deltas` queue. The changes in #8436 and #9296 do not touch this queue.

### Reproduction Steps / Example Code (Python)
With `langgraph-sdk==0.4.10` installed, run the following. It sends valid tool protocol events through `LangGraphClient.threads.stream()` and consumes each handle's deltas after collecting the handles, as the SDK's existing tests do. The fixture yields to the event loop for each event, so the transport and subscription queues do not overflow.

```python
"""Exercise terminal tool events with an exactly full delta buffer via public APIs."""

import asyncio
import json
from importlib.metadata import version

import httpx

from langgraph_sdk.client import LangGraphClient


def tool_event(seq, name, **data):
    return {
        "type": "event",
        "method": "tools",
        "params": {"namespace": [], "data": {"event": name, "tool_call_id": "call-1", **data}},
        "seq": seq,
        "event_id": f"event-{seq}",
    }


class Body(httpx.AsyncByteStream):
    def __init__(self, events):
        self.events = events

    async def __aiter__(self):
        for event in self.events:
            yield f"id: {event['event_id']}\nevent: message\ndata: {json.dumps(event)}\n\n".encode()
            # Give consumers a turn for each event; only the per-tool delta
            # queue fills, not the shared transport or subscription queues.
            await asyncio.sleep(0)


async def run_case(count, terminal):
    def fixture(request):
        body = json.loads(request.content or b"{}")
        if request.url.path.endswith("/commands"):
            return httpx.Response(200, json={"type": "success", "id": body["id"], "result": {"run_id": "r"}})
        if request.url.path.endswith("/stream/events"):
            events = []
            if "tools" in body["channels"]:
                events = [tool_event(0, "tool-started", tool_name="search")]
                events.extend(tool_event(i+1, "tool-output-delta", delta=str(i)) for i in range(count))
                events.append(tool_event(count+1, terminal, output="result", message="tool failed"))
            # End the finite stream naturally; this test concerns a tool
            # event, not run lifecycle or transport shutdown.
            return httpx.Response(200, headers={"content-type": "text/event-stream"}, stream=Body(events))
        raise AssertionError(request.url)

    async with httpx.AsyncClient(transport=httpx.MockTransport(fixture), base_url="https://example.test") as raw:
        async with LangGraphClient(raw).threads.stream(assistant_id="agent") as stream:
            await stream.run.start(input={})
            calls = []
            projection_error = None
            try:
                async for call in stream.tool_calls:
                    calls.append(call)
            except Exception as exc:
                projection_error = type(exc).__name__
            call = calls[0]
            try:
                output = await call.output
            except RuntimeError as exc:
                output = str(exc)
            deltas = []
            try:
                async with asyncio.timeout(2):
                    async for delta in call.deltas:
                        deltas.append(delta)
                terminated = True
            except TimeoutError:
                terminated = False
            print(f"deltas={count}, terminal={terminal}: projection_error={projection_error}, output={output!r}, drained={len(deltas)}, terminated={terminated}")
            return projection_error is None and len(deltas) == count and terminated


async def main():
    print("langgraph-sdk", version("langgraph-sdk"))
    results = []
    for terminal in ("tool-finished", "tool-error"):
        for count in (1023, 1024):
            results.append(await run_case(count, terminal))
    print(f"{sum(results)} passed, {len(results)-sum(results)} failed")
    assert all(results)


if __name__ == "__main__":
    asyncio.run(main())
```

### Actual result
```text
deltas=1023, terminal=tool-finished: projection_error=None, output='result', drained=1023, terminated=True
deltas=1024, terminal=tool-finished: projection_error=QueueFull, output='result', drained=1024, terminated=False
deltas=1023, terminal=tool-error: projection_error=None, output='tool failed', drained=1023, terminated=True
deltas=1024, terminal=tool-error: projection_error=QueueFull, output='tool failed', drained=1024, terminated=False
2 passed, 2 failed
```

Expected: both terminal events complete normally, keep all 1024 buffered deltas available, and let delta iteration finish once they have been consumed. Tool errors should remain available through `call.output`.

### Description and proposed scope
`_finish()` and `_fail()` mark the handle done and resolve `output`, then unconditionally insert the `None` sentinel into its bounded delta queue. With a full queue this raises `asyncio.QueueFull`. The later delta iterator has no sentinel and waits after draining the buffered values.

A narrow fix can use the existing `done` flag to terminate after the buffer drains, while retaining a nonblocking sentinel to wake an already-waiting consumer. This preserves buffered deltas and does not change ordinary delta overflow, shared subscriptions, or transport shutdown behavior.

I have prepared the two-file patch and eight regression cases. On the unmodified base, the success/error full-buffer cases fail with `QueueFull` and six controls pass. With the patch, those eight cases and the complete default SDK suite pass (643 tests; 55 integration tests excluded by the repository's default marker). Package formatting, Ruff, and type checks pass. GNU Make is not installed on this Windows machine, so I ran the equivalent commands from the package's format/lint/test targets with the frozen dependency environment.

Could a maintainer approve this focused fix and assign the issue to @bbbbbbbbbbb114 so I can open the upstream PR under the repository's current issue-link workflow? A reviewable Draft PR is available on my fork: https://github.com/bbbbbbbbbbb114/langgraph/pull/1 (not an upstream PR).

The same four-case public-client reproduction also fails in a separately installed released `langgraph-sdk==0.4.10` environment (two full-buffer failures, two 1023-delta controls passing), and passes in the patched checkout.

### System Info
- Windows, Python 3.14.4
- langgraph-sdk 0.4.10; langchain-core 1.6.5; langchain-protocol 0.0.19
- Source baseline: `ffc3336367e8139668d11e5f0b0e6def57e7c762` (current main when checked)
- Dependencies installed from the committed `uv.lock` with `uv sync --frozen`.

Investigated and tested with Codex assistance.