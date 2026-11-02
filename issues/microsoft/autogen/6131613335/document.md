# fix(autogen-ext): apply configured ChromaDB distance metrics

## Why are these changes needed?

`ChromaDBVectorMemory` stores `distance_metric` as ordinary collection metadata. Chroma does not use that key to configure its index, so new collections silently use squared L2 distance even when AutoGen requests the default cosine metric or inner product. With query `[1, 0]` and documents `[0.5, 0]` and `[1, 0.1]`, the default memory retrieves the second document first, although the first has exactly the same direction as the query.

Use Chroma's `hnsw:space` metadata key when creating the collection. Preserve the existing cosine and L2 score conversions. For inner product, return `1 - distance`, the actual dot product: Chroma's IP distance can be negative, so the previous `1 / (1 + distance)` would divide by zero for query `[1, 0]` and document `[2, 0]` once IP was enabled. The tests also cover negative dot products and a zero score threshold.

The class documentation explains that this applies to newly created collections. Chroma retains an existing collection's metric; this change does not migrate or recreate stored data. Inner-product scores can be negative or greater than one.

## Related issue number

Found while verifying the current implementation with custom embeddings and a local persistent Chroma database. No linked issue.

## Validation

From the repository root, with the corresponding isolated environment active:

```sh
uv run --active --no-project python -m pytest python/packages/autogen-ext/tests/memory/test_chroma_memory.py -q
uv run --active --no-project python -m pytest python/packages/autogen-ext/tests/memory/test_chroma_memory.py -k test_distance_metric -q
```

- Python 3.12.15, minimum supported ChromaDB 1.0.0: complete module, **20 passed**. SentenceTransformers 3.4.0 and Torch 2.5.1 were installed for the existing embedding tests.
- ChromaDB 1.5.9: all **5** new regression cases passed. They use the real persistent database and public memory `add`/`query` calls with deterministic embeddings, then reacquire the collection after `close()`. The same final cases give **4 failures and 1 pass** with the unchanged upstream implementation. Enabling the metric without correcting IP scoring separately reproduced two `ZeroDivisionError` failures.
- Project-pinned Ruff 0.4.8 lint/format and Pyright 1.1.389 on both changed files passed with zero diagnostics.
- An initial full-module run in the 1.5.9 environment exposed two existing test/environment failures: the legacy mock embedding function lacks `name`, and SentenceTransformers was not installed there. Both were reproduced using unchanged upstream source and tests. The complete module passes in the fully provisioned 1.0.0 environment above.
- Additional offline restart validation on ChromaDB 1.0.0 and 1.5.9: cosine, L2, IP and IP with threshold zero passed in **16 separate producer/consumer processes**. Each producer writes two records, closes and exits before a fresh consumer opens the same database and queries without adding data. Collection identity, record count, `hnsw:space`, raw distances and converted scores survive restart. This uses the real public memory API and persistent Chroma storage with only deterministic embedding generation; no live embedding provider was called.
- Full SDK tests, the documentation build and HTTP-server mode were not tested.

AI disclosure: Codex generated this change and the tests and performed local verification and a separate AI code review. This is not a claim of human review.

## Checks

- [x] I've included the relevant API docstring changes.
- [x] I've added tests corresponding to the changes introduced in this PR.
- [ ] I've made sure all auto checks have passed.
