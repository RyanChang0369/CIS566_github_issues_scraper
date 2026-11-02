# feat(langgraph): add Runtime.on_exit for cleanup that runs however a run ends

Adds `Runtime.on_exit(cb)` to register cleanup that runs however the run ends: success, error, cancel, interrupt, or stream closed early. Today "after" hooks don't run on those paths, so resources like QuickJS interpreter slots leak (open-swe#4703 has a workaround). Draft, for discussion.

```python
def node(state, runtime: Runtime):
    slot = open_interpreter()
    runtime.on_exit(slot.close)  # or get_runtime().on_exit(...)
```

There's no new cleanup machinery here. The Pregel loop already has an internal exit stack that unwinds on every exit path, and this just exposes it. Callbacks go onto the root loop's stack, so they run LIFO after every node has stopped and the final checkpoint is saved. Subgraphs register on the root run.

Open questions:
- Should callbacks get the exit reason? QuickJS wants to keep a slot on interrupt and free it on error.
- Should a callback error on a successful run be raised, or only logged?