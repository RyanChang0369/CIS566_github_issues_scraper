# [BUG] A flow resumed from a checkpoint leaves a loop early: methods that ran after the resume are skipped as already completed

### Description

A flow loops over `work` and `check`, and `work` fails in the first pass. The flow is restored from its latest checkpoint and kicked off again. The resumed run does the first pass and then stops: no error is raised, the remaining passes do not run, and neither does `finish`, the listener of the route that ends the loop.

The checkpointing guide says that restoring "rebuilds that state and continues. Completed tasks are skipped". Here the methods that are skipped did not complete before the failure.


### Steps to Reproduce

1. Define a flow with a cycle: `begin -> work -> @router check`, where `check` returns `"again"` twice, `work` also listens to `"again"`, and `finish` listens to `"done"`.
2. Let `work` fail in its first pass, with `checkpoint=CheckpointConfig(location=..., on_events=["method_execution_finished"])`.
3. Restore the latest checkpoint with `LoopFlow.from_checkpoint(CheckpointConfig(restore_from=...))` and call `kickoff()`.


### Expected behavior

The resumed run repeats the failed pass and goes on: `work` runs for counts 0, 1 and 2, and `finish` runs. So `passes` is `[0, 0, 1, 2]` (the failed attempt, then the three passes), `count` is 3 and `finished` is `True`.


### Screenshots/Code snippets

```python
import glob
import os
import tempfile

from crewai import CheckpointConfig
from crewai.flow.flow import Flow, listen, or_, router, start

passes, failures = [], 1


class LoopFlow(Flow):
    @start()
    def begin(self):
        self.state["count"] = 0

    @listen(or_(begin, "again"))
    def work(self):
        global failures
        passes.append(self.state["count"])
        if failures > 0:
            failures -= 1
            raise RuntimeError("transient failure")

    @router(work)
    def check(self):
        self.state["count"] += 1
        return "again" if self.state["count"] < 3 else "done"

    @listen("done")
    def finish(self):
        self.state["finished"] = True


location = tempfile.mkdtemp()
flow = LoopFlow(checkpoint=CheckpointConfig(location=location, on_events=["method_execution_finished"]))
try:
    flow.kickoff()
except RuntimeError as exc:
    print("first run failed:", exc)

latest = max(glob.glob(f"{location}/**/*.json", recursive=True), key=os.path.getmtime)
restored = LoopFlow.from_checkpoint(CheckpointConfig(restore_from=latest))
restored.kickoff()
print("passes:", passes, "count:", restored.state.get("count"), "finished:", restored.state.get("finished"))
```


### Operating System

Ubuntu 22.04

### Python Version

3.12

### crewAI Version

1.15.34

### crewAI Tools Version

not installed

### Virtual Environment

Venv

### Evidence

```
first run failed: transient failure
passes: [0, 0] count: 1 finished: None
```
The same on 1.15.28 and 1.15.33. The run ends normally, so nothing tells the application that two passes and `finish` were lost.


### Possible Solution

`_execute_single_listener` skips a method if it is in `_completed_methods` while `_is_execution_resuming` is set, and the flag stays set for the whole resumed run. So it cannot tell a method that completed before the resume from one that completed in this run. Here `work` and `check` complete in the resumed run, `check` routes to `"again"`, and `work` is skipped as if the checkpoint had recorded it. Then `check` is skipped too, and the flow ends.

Tracking what ran in the resumed run fixes this flow. With these changes the output is `[0, 0, 1, 2]`, `count` 3 and `finished` `True`:

```python
# in Flow's private attributes
_resumed_run: set[FlowMethodName] = PrivateAttr(default_factory=set)

# in _execute_method, after self._completed_methods.add(method_name)
self._resumed_run.add(method_name)

# in _execute_single_listener
if listener_name in self._completed_methods:
    if self._is_execution_resuming and listener_name not in self._resumed_run:
        self._resumed_run.add(listener_name)
        ...
```

This is not a complete fix for loops: I only tried it on this program, and I did not run the test suite. If `work` fails in a later pass, `check` has completed before the failure, and the run stops as in #8437.


### Additional context

This is related to #8437, but it is not the same case: when this flow fails, the router has not run, so no completed router is skipped on resume. PR #8446 does not fix it. With that PR on 1.15.34, this flow raises `RecursionError: Method 'work' has been called 100 times in this flow execution`, since the skipped methods keep replaying the router's outcome.
