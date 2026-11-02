# update_state on the head of a failed run drops a finished sibling's writes

### Checked other resources

- [x] This is a bug, not a usage question.
- [x] I added a clear and descriptive title.
- [x] I used the GitHub search to find a similar question and didn't find it.
- [x] I am sure this is a bug in LangGraph rather than my code.
- [x] The bug is not resolved by updating to the latest stable version.
- [x] This is not related to the langchain-community package.
- [x] I posted a self-contained, minimal, reproducible example.

### Description

`update_state()` on the head checkpoint of a failed (or interrupted) run drops the durable output of already-finished parallel siblings.

Graph: `START -> a`, `START -> b`, both `-> c`. In one superstep `a` succeeds (`a` appends `"a"` to `log`) and `b` raises. `invoke()` propagates the error; `get_state()` still shows `values={'log': ['a']}`, `next=('b',)`. The user recovers with:

```python
graph.update_state(cfg, {"fixed": True, "log": ["manual"]}, as_node="b")
graph.invoke(None, cfg)
```

Expected: `a`'s finished write stays in the state (as it does on a plain retry resume), i.e. `log` ends around `['a', 'manual', 'c']`.

Actual: the head checkpoint is rebuilt from the saved checkpoint's *committed* values only, and `c` runs with `{'log': ['manual'], 'fixed': True}`, final `{'log': ['manual', 'c']}`. `a` is not re-run (`runs={'a': 1, ...}`), so its stored pending write is silently lost with no error.

Comparison reproduced with `InMemorySaver` and `SqliteSaver`, sync and async, and with `interrupt()` instead of a raised exception:

```
[mem-update]  after failure: next=('b',) values={'log': ['a']} runs={'a': 1, 'b': 1}
[mem-update]  recovered via update_state: final={'log': ['manual', 'c'], 'fixed': True} runs={'a': 1, 'b': 1, 'c': 1}
[mem-resume]  recovered via resume:       final={'log': ['a', 'b', 'c']}            runs={'a': 1, 'b': 2, 'c': 1}
[sqlite-update] recovered via update_state: final={'log': ['manual', 'c'], 'fixed': True}
```

Code pointers: `libs/langgraph/langgraph/pregel/main.py:1673` builds the checkpoint from `saved.checkpoint` committed values only; `main.py:2055` (`_store_or_fork_delta_writes`) preserves only delta-channel pending writes; `main.py:2068` passes only the update's tasks to `apply_writes`. A normal resume replays loaded pending writes into tasks instead (`pregel/_loop.py:708-730`).

### Reproduction

```python
# see the script: two parallel nodes, one raises, recover via update_state(as_node=...) then invoke(None)
```

Self-contained script (`final_error_sibling.py`, plus an interrupt variant `sibling_writes_final.py`, an async variant, and a pending-task variant) is available; happy to attach it. No services or API keys.

### Expected behavior

When the addressed checkpoint is the head of the failed run (not a historical fork), recovering via `update_state` should keep the finished siblings' pending writes, matching a plain retry resume.

### Additional context

- Why this is not just fork semantics: merged #6389 deliberately avoids replaying pending writes on **historical** checkpoints (to prevent stale data), but here the update checkpoint *is* the next child of the head and the sibling's write is durable. Delta channels already get fork/head machinery (`_store_or_fork_delta_writes`, `checkpoint_superseded`); plain channels get nothing.
- Suggested direction: when the addressed checkpoint is not superseded, apply the finished tasks' output writes from `saved.pending_writes` alongside the update (mirroring `_reapplies_pending_writes`); keep the current behavior for historical forks.
- Related but distinct: #9076 (open; `update_state` clears `StateSnapshot.interrupts`), #8653 (closed, config-injected checkpointer), #6389 (merged; stale-fork replay rationale).
- Searched open and closed issues/PRs for `update_state` × pending writes / parallel siblings / error recovery: no duplicate.

### System

- langgraph `6f2df05` (main, 2026-10-29)
- Python 3.13, Windows 11

Reported with AI assistance (Claude); the reproduction was executed and verified locally.
