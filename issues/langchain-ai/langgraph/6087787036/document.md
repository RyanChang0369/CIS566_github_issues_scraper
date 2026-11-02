# JsonPlusSerializer: pydantic RootModel state loses its type on checkpoint round trip and breaks interrupt/resume

### Checked other resources

- [x] This is a bug, not a usage question.
- [x] I added a clear and descriptive title that summarizes this issue.
- [x] I used the GitHub search to find a similar question and didn't find it.
- [x] I am sure that this is a bug in LangGraph rather than my code.
- [x] The bug is not resolved by updating to the latest stable version of LangGraph (or the specific integration package).
- [x] This is not related to the langchain-community package.
- [x] I posted a self-contained, minimal, reproducible example. A maintainer can copy it and run it AS IS.

### Related Issues / PRs

#9343 covers aliased fields and #6102 covers generic pydantic models. This report is specifically about `RootModel` subclasses. I searched issues and PRs for `RootModel` and found no existing report.

### Reproduction Steps / Example Code (Python)

```python
from pydantic import RootModel

from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer


class IntList(RootModel[list[int]]):
    pass


serde = JsonPlusSerializer(allowed_msgpack_modules=True)
original = IntList([1, 2, 3])
restored = serde.loads_typed(serde.dumps_typed(original))
print(type(original), type(restored))
# <class '__main__.IntList'> <class 'list'>
```

End-to-end with a persistent checkpointer and an interrupt:

```python
import sqlite3
from typing import TypedDict

from pydantic import RootModel

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class IntList(RootModel[list[int]]):
    pass


class State(TypedDict):
    items: IntList


def prepare(state: State) -> State:
    return {"items": IntList([1, 2])}


def gate(state: State) -> State:
    interrupt("pause")
    return {}


def consume(state: State) -> State:
    return {"items": IntList(state["items"].root + [3])}


graph = StateGraph(State)
graph.add_node("prepare", prepare)
graph.add_node("gate", gate)
graph.add_node("consume", consume)
graph.add_edge(START, "prepare")
graph.add_edge("prepare", "gate")
graph.add_edge("gate", "consume")
graph.add_edge("consume", END)

conn = sqlite3.connect(":memory:", check_same_thread=False, isolation_level=None)
compiled = graph.compile(checkpointer=SqliteSaver(conn))
config = {"configurable": {"thread_id": "root-model"}}

compiled.invoke({"items": IntList([0])}, config)   # stops at the interrupt
compiled.invoke(Command(resume="go"), config)      # fails
```

### Error Message and Stack Trace (if applicable)

```shell
AttributeError: 'list' object has no attribute 'root'
```

### Description

A pydantic v2 `RootModel` stored in graph state does not survive a checkpoint round trip. `JsonPlusSerializer` serializes pydantic v2 models with `obj.model_dump()`, which for a `RootModel` returns the root value itself (a list, string, int, ...). `EXT_PYDANTIC_V2` then rebuilds with `cls(**payload)`, which cannot unpack a non-mapping payload; the exception fallback returns the raw value.

Within a single run this is hidden because the in-memory channel keeps the original object. With a persistent checkpointer, `get_state()` returns the raw list and resuming after `interrupt` passes that list to the next node, so the graph fails with the error above.

Expected behavior: the restored value is the same `RootModel` subclass, and resume works.

Suggested fix, backwards compatible with the existing payload format:

```python
cls = getattr(importlib.import_module(tup[0]), tup[1])
if getattr(cls, "__pydantic_root_model__", False):
    return cls.model_validate(tup[2])
```

This avoids a format change and also fixes existing RootModel payloads. Non-root models keep the current `cls(**payload)` path.

Validation: I reproduced this on released `langgraph-checkpoint==4.3.1` and on `main` at `5c96bce`. I added three regression cases (list, str, nested dict); without the fix two fail, with the fix `tests/test_jsonplus.py` passes 107 tests. End-to-end interrupt/resume succeeds with the fix. Ruff check, format, and import-order checks pass.

AI assistance was used to prepare the repro and the proposed patch; every result above was run locally.

### System Info

- OS: Windows 11
- Python: 3.12.14
- pydantic: 2.14.1
- langgraph-checkpoint: 4.3.1, and main at 5c96bce
- langgraph: 1.2.18

If this direction looks right, could you approve the issue and assign it to me? I have the fix and regression tests ready and will open a PR after assignment.
