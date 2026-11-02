# Functional API with a cache: a running task can match the cache, so its writes change under it (`IndexError: deque index out of range`)

### Checked other resources

- [x] This is a bug, not a usage question.
- [x] I added a clear and descriptive title that summarizes this issue.
- [x] I used the GitHub search to find a similar question and didn't find it.
- [x] I am sure that this is a bug in LangGraph rather than my code.
- [x] The bug is not resolved by updating to the latest stable version of LangGraph (or the specific integration package).
- [x] This is not related to the langchain-community package.
- [x] I posted a self-contained, minimal, reproducible example. A maintainer can copy it and run it AS IS.

### Related Issues / PRs

- #9304: `dictionary changed size during iteration` in the same code, from a different race. This one remains once that one is fixed, see below.


### Reproduction Steps / Example Code (Python)

```python
import collections
import sys
from importlib.metadata import version

from langgraph.cache.memory import InMemoryCache
from langgraph.func import entrypoint, task
from langgraph.types import CachePolicy

sys.setswitchinterval(5e-6)  # Makes the failure frequent enough to see on any machine.


@task(cache_policy=CachePolicy())
def leaf(i):
    return i


@task(cache_policy=CachePolicy())
def parent(i):
    return [future.result() for future in [leaf(j) for j in range(8)]]


def run():
    @entrypoint(cache=InMemoryCache())  # A cache of its own, so that it starts empty.
    def workflow(n):
        return [future.result() for future in [parent(i) for i in range(4)]]

    for _ in workflow.stream(1):
        pass


outcomes = collections.Counter()
for _ in range(300):
    try:
        run()
        outcomes["ok"] += 1
    except Exception as error:
        outcomes[f"{type(error).__name__}: {str(error)[:60]}"] += 1
print("langgraph", version("langgraph"))
for outcome, count in outcomes.most_common():
    print(count, outcome)
```

### Error Message and Stack Trace (if applicable)

```shell
langgraph 1.2.19
170 RuntimeError: dictionary changed size during iteration
61 RuntimeError: deque mutated during iteration
55 ok
14 IndexError: deque index out of range

  File ".../langgraph/pregel/_loop.py", line 1749, in accept_push
    self.put_writes(task.id, task.writes, cached=True)
  File ".../langgraph/pregel/_loop.py", line 1793, in put_writes
    super().put_writes(task_id, writes, cached=cached)
  File ".../langgraph/pregel/_loop.py", line 557, in put_writes
    self.output_writes(task_id, writes, cached=cached)
  File ".../langgraph/pregel/_loop.py", line 1607, in output_writes
    if writes[0][0] == INTERRUPT:
       ~~~~~~^^^
IndexError: deque index out of range
```

### Description

A functional workflow that runs cached tasks concurrently crashes under the sync API. Every task succeeds, but the run aborts with `RuntimeError: deque mutated during iteration` or `IndexError: deque index out of range`, raised from LangGraph's own bookkeeping, so the application loses the whole run and can do nothing about it.

It happens without any special setup: with the `setswitchinterval` line removed and a 1 ms `time.sleep` in `leaf`, standing for a call to a service, 9 of 300 runs fail with these errors on Ubuntu.

`SyncPregelLoop.accept_push` calls `match_cached_writes` each time a task is pushed, and that method looks at every task in `self.tasks` with a cache key and no writes:

```python
cached = {(t.cache_key.ns, t.cache_key.key): t for t in self.tasks.values() if t.cache_key and not t.writes}
```

A task that is already running also has no writes yet. So when a sibling pushes a task, a running task can match the cache. Its `task.writes` deque is then extended and passed to `put_writes`, which iterates it, while the thread running the task can clear it (`task.writes.clear()` at the start of an attempt in `run_with_retry`) or write to it. That is the mutation in the errors above.

Fixing #9304 does not fix this. With a lock around task registration and cache matching (the change of PR #9515), `dictionary changed size` goes away and these errors stay:

```text
295 ok
2 IndexError: deque index out of range
2 RuntimeError: deque mutated during iteration
1 IndexError: list index out of range
```

Looking up only the task just pushed fixes it. With that lock and this change, all 300 runs are `ok`, and so are all 600 runs of a larger test in which the lock alone failed 27 times:

```python
if pushed := super().accept_push(task, write_idx, call):
    if pushed.cache_key and not pushed.writes and self.cache is not None:
        key = (pushed.cache_key.ns, pushed.cache_key.key)
        for values in self.cache.get((key,)).values():
            pushed.writes.extend(values)
            self.put_writes(pushed.id, pushed.writes, cached=True)
```


### System Info

System Information
------------------
> OS:  Linux (Ubuntu 22.04.5), and Darwin
> Python Version:  3.12.13

Package Information
-------------------
> langgraph: 1.2.19
> langgraph-checkpoint: 4.3.1
> langchain_core: 1.7.3