# chore(deps): bump mem0ai from 2.0.4 to 2.0.18 in the security-updates group across 1 directory

Bumps the security-updates group with 1 update in the / directory: [mem0ai](https://github.com/mem0ai/mem0).

Updates `mem0ai` from 2.0.4 to 2.0.18
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/mem0ai/mem0/releases">mem0ai's releases</a>.</em></p>
<blockquote>
<h2>Mem0 Python SDK (v2.0.18)</h2>
<p><strong>Bug Fixes:</strong></p>
<ul>
<li><strong>Core:</strong> Percent-escape <code>%</code>, <code>&amp;</code>, and <code>=</code> in <code>user_id</code>, <code>agent_id</code>, and <code>run_id</code> when building the session scope key for the recent-conversation buffer, so the key stays unambiguous for ids containing those characters. Ordinary ids keep their existing key; an id already containing <code>%</code>, <code>&amp;</code>, or <code>=</code> maps to a new key, so its buffer starts empty once and refills on the next <code>add()</code>. Stored memories are unaffected. Reported by <a href="https://github.com/OfficialAbhinavSingh"><code>@​OfficialAbhinavSingh</code></a> (<a href="https://redirect.github.com/mem0ai/mem0/pull/6892">#6892</a>)</li>
<li><strong>Vector Stores:</strong> Raise <code>ValueError</code> when a PGVector <code>in</code>/<code>nin</code> filter value is not a list. A string value was previously iterated character by character into the generated <code>= ANY(...)</code> array (so <code>{&quot;user_id&quot;: {&quot;in&quot;: &quot;alice&quot;}}</code> matched <code>a</code>, <code>l</code>, <code>i</code>, <code>c</code>, <code>e</code>), and a non-iterable value raised a bare <code>TypeError</code> from deep inside filter building (<a href="https://redirect.github.com/mem0ai/mem0/pull/6879">#6879</a>)</li>
<li><strong>Vector Stores:</strong> Reject <code>index_accuracy=0</code> in the Oracle AI Vector Search config. The range check sat behind a truthiness test, so <code>0</code> skipped validation entirely and was passed through to <code>WITH TARGET ACCURACY 0</code> instead of raising (<a href="https://redirect.github.com/mem0ai/mem0/pull/6848">#6848</a>)</li>
<li><strong>Vector Stores:</strong> Close the Oracle connection or pool that Mem0 opened when initialization fails. A client version check, a database version check, or a <code>create_col()</code> error previously propagated with the connection still open, leaking it for the life of the process. A caller-supplied <code>client</code> is left untouched (<a href="https://redirect.github.com/mem0ai/mem0/pull/6839">#6839</a>)</li>
</ul>
<h2>Mem0 Python SDK (v2.0.17)</h2>
<p><strong>New Features:</strong></p>
<ul>
<li><strong>Client:</strong> Add <code>agent_custom_instructions</code> to <code>project.update()</code>/<code>update_project()</code> (sync and async) and to the <code>ProjectUpdateOptions</code> and <code>AddMemoryOptions</code> typed models. It sets a second extraction instruction set that applies only to agent-scoped memories: an add passing <code>agent_id</code> without <code>user_id</code> uses it, one passing both splits by attribution, and while it is unset <code>custom_instructions</code> continues to apply to every memory (<a href="https://redirect.github.com/mem0ai/mem0/pull/6809">#6809</a>)</li>
</ul>
<h2>Mem0 Python SDK (v2.0.16)</h2>
<p><strong>New Features:</strong></p>
<ul>
<li><strong>Client:</strong> Add <code>reference_date</code>, <code>latest_only</code>, and <code>keyword_search</code> to <code>SearchMemoryOptions</code>, and <code>latest_only</code> to <code>GetAllMemoryOptions</code>, keeping the Python client's typed options in sync with the Platform API and the CLIs (<a href="https://redirect.github.com/mem0ai/mem0/pull/6696">#6696</a>)</li>
</ul>
<p><strong>Bug Fixes:</strong></p>
<ul>
<li><strong>Core:</strong> Stop <code>add()</code> metadata from setting a memory's identity scope. <code>_build_filters_and_metadata()</code> now strips <code>user_id</code>, <code>agent_id</code>, <code>run_id</code>, and <code>actor_id</code> from caller-supplied <code>metadata</code> before building the creation template, so metadata can no longer place a memory into a scope that was never passed through the entity params (<a href="https://redirect.github.com/mem0ai/mem0/pull/6656">#6656</a>)</li>
<li><strong>Vector Stores:</strong> Validate Upstash filter keys and values in <code>search()</code>, <code>keyword_search()</code>, and <code>list()</code>. Filter keys must match a safe identifier pattern, values must be <code>str</code>/<code>int</code>/<code>float</code>/<code>bool</code>, and string values containing a double quote or backslash are now rejected instead of being interpolated unescaped into the generated query string (<a href="https://redirect.github.com/mem0ai/mem0/pull/5981">#5981</a>)</li>
<li><strong>Embeddings:</strong> <code>FastEmbedEmbedding.embed()</code> now converts its result with <code>.tolist()</code> before returning, so callers get a plain <code>List[float]</code> instead of a numpy array (<a href="https://redirect.github.com/mem0ai/mem0/pull/6770">#6770</a>)</li>
<li><strong>Embeddings:</strong> <code>HuggingFaceEmbedding</code> now passes <code>api_key</code> to the OpenAI-compatible client when <code>huggingface_base_url</code> is set. The configured key was previously dropped, so the client fell back to <code>OPENAI_API_KEY</code> from the environment or raised <code>OpenAIError</code> at construction when that was unset (<a href="https://redirect.github.com/mem0ai/mem0/pull/6770">#6770</a>)</li>
<li><strong>Embeddings:</strong> Replace Ollama's interactive <code>pip install</code> prompt on import with a plain <code>ImportError</code>. Importing <code>mem0.embeddings.ollama</code> without the <code>ollama</code> package previously blocked on stdin and then called <code>sys.exit(1)</code>, killing the host process instead of raising (<a href="https://redirect.github.com/mem0ai/mem0/pull/6770">#6770</a>)</li>
<li><strong>Core:</strong> <code>remove_code_blocks()</code> now returns an empty string for <code>None</code> input instead of raising <code>AttributeError</code> (<a href="https://redirect.github.com/mem0ai/mem0/pull/6770">#6770</a>)</li>
<li><strong>Core:</strong> <code>parse_vision_messages()</code> now chains the original exception (<code>raise ... from e</code>) when an image download fails, so the root cause is preserved in the traceback (<a href="https://redirect.github.com/mem0ai/mem0/pull/6770">#6770</a>)</li>
<li><strong>Core:</strong> <code>process_telemetry_filters(None)</code> now returns <code>([], {})</code>, matching the two-value tuple every caller unpacks, instead of <code>{}</code> (<a href="https://redirect.github.com/mem0ai/mem0/pull/6770">#6770</a>)</li>
<li><strong>Core:</strong> <code>LlmFactory.create()</code> no longer mutates the caller's config dict in place via <code>.update(kwargs)</code>; the merge now builds a new dict (<a href="https://redirect.github.com/mem0ai/mem0/pull/6770">#6770</a>)</li>
<li><strong>Rerankers:</strong> The Cohere, HuggingFace, SentenceTransformer, and Zero Entropy rerankers' failure-fallback path no longer mutates the caller's document dicts in place when stamping <code>rerank_score</code>; it now falls back on copies (<a href="https://redirect.github.com/mem0ai/mem0/pull/6770">#6770</a>)</li>
<li><strong>Vector Stores:</strong> Remove <code>logging.basicConfig()</code> calls from the MongoDB and Vertex AI Vector Search providers, so selecting either provider no longer reconfigures the host application's root logger as a side effect (<a href="https://redirect.github.com/mem0ai/mem0/pull/6770">#6770</a>)</li>
</ul>
<h2>Mem0 Python SDK (v2.0.15)</h2>
<p><strong>Bug Fixes:</strong></p>
<ul>
<li><strong>Core:</strong> <code>delete_all()</code> now paginates through the vector store in batches of 1000 instead of listing once, so accounts with more memories than a single page (most vector stores default to ~100) had the remainder silently left behind (<a href="https://redirect.github.com/mem0ai/mem0/pull/6636">#6636</a>)</li>
<li><strong>Vector Stores:</strong> Cap Supabase <code>search()</code>/<code>list()</code> <code>top_k</code> at the <code>vecs</code> query limit of 1000 instead of erroring, and fix a <code>col_info()</code> crash by reading collection attributes directly instead of calling the removed <code>describe()</code> method (<a href="https://redirect.github.com/mem0ai/mem0/pull/6695">#6695</a>)</li>
<li><strong>Vector Stores:</strong> Set <code>size</code> on Elasticsearch KNN search queries, so results respect <code>top_k</code> instead of being capped at Elasticsearch's default of 10 hits (<a href="https://redirect.github.com/mem0ai/mem0/pull/5910">#5910</a>)</li>
</ul>
<p><strong>Changes:</strong></p>
<ul>
<li><strong>Rerankers:</strong> <code>LLMReranker</code>'s default model is now <code>gpt-5-mini</code> (was <code>gpt-4o-mini</code>) (<a href="https://redirect.github.com/mem0ai/mem0/pull/6703">#6703</a>)</li>
</ul>
<h2>Mem0 Python SDK (v2.0.14)</h2>
<p><strong>New Features:</strong></p>
<ul>
<li><strong>Vector Stores:</strong> Add an Oracle AI Vector Search provider (<code>oracledb</code>) with connection pooling, <code>HNSW</code>/<code>IVF</code> indexes, JSON metadata filtering, and six selectable distance metrics (<a href="https://redirect.github.com/mem0ai/mem0/pull/5358">#5358</a>)</li>
</ul>
<p><strong>Bug Fixes:</strong></p>
<ul>
<li><strong>Vector Stores:</strong> Translate a <code>&quot;*&quot;</code> filter value in OpenSearch into an <code>exists</code> query for every key, not just identity keys. It was previously ignored or matched literally against the string <code>&quot;*&quot;</code>, so a wildcard filter returned nothing (<a href="https://redirect.github.com/mem0ai/mem0/pull/6522">#6522</a>)</li>
<li><strong>Vector Stores:</strong> Re-raise errors from OpenSearch <code>search()</code> instead of returning <code>[]</code>, so a transport, auth, or index misconfiguration surfaces instead of looking like zero matches. <code>keyword_search()</code> still degrades on failure, since it is a best-effort BM25 signal (<a href="https://redirect.github.com/mem0ai/mem0/pull/6519">#6519</a>)</li>
<li><strong>Vector Stores:</strong> Guard the <code>text</code> field in Milvus <code>update()</code> behind the <code>_has_bm25_schema</code> check, matching <code>insert()</code>, so updating a memory in a collection without the BM25 <code>text</code>/<code>sparse</code> schema no longer fails (<a href="https://redirect.github.com/mem0ai/mem0/pull/5705">#5705</a>)</li>
</ul>
<h2>Mem0 Python SDK (v2.0.13)</h2>
<p><strong>Bug Fixes:</strong></p>
<ul>
<li><strong>Vector Stores:</strong> Fix <code>reset()</code> silently leaving stale vectors behind on local (on-disk) Qdrant when the old collection directory could not be removed, for example an open file handle on Windows or NFS (<a href="https://redirect.github.com/mem0ai/mem0/pull/6412">#6412</a>)</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/mem0ai/mem0/commit/c427a453a89c5a3fee73cdb2e4c4df6a651e1692"><code>c427a45</code></a> docs(changelog): backfill Python v2.0.18 and TypeScript v3.1.6 SDK entries (#...</li>
<li><a href="https://github.com/mem0ai/mem0/commit/f5b4300449434835108b904d956a6fd294dd3993"><code>f5b4300</code></a> docs: redirect deprecated OSS graph memory page to platform graph memory (<a href="https://redirect.github.com/mem0ai/mem0/issues/6914">#6914</a>)</li>
<li><a href="https://github.com/mem0ai/mem0/commit/71f2ebefa3494da21550fb525216818776cde67f"><code>71f2ebe</code></a> fix(memory): escape delimiters when building the session scope key (<a href="https://redirect.github.com/mem0ai/mem0/issues/6892">#6892</a>)</li>
<li><a href="https://github.com/mem0ai/mem0/commit/35a125585e5e9ec31ee60094a08ae92337cff75a"><code>35a1255</code></a> fix(pgvector): raise ValueError when 'in'/'nin' filter value is not a list (#...</li>
<li><a href="https://github.com/mem0ai/mem0/commit/4debc58a83377b18be81ae1e5969a300736b2fac"><code>4debc58</code></a> fix(security): patch 8 HIGH + 18 MEDIUM Vanta vulnerabilities across 4 pnpm w...</li>
<li><a href="https://github.com/mem0ai/mem0/commit/b42cfdd5c8bd169be994c7ef352c59b6afe5c93f"><code>b42cfdd</code></a> Fix broken links: unblock link check in oracledb.mdx (<a href="https://redirect.github.com/mem0ai/mem0/issues/6849">#6849</a>)</li>
<li><a href="https://github.com/mem0ai/mem0/commit/6fe6140dba68327afb4c0049b1b76de00668b27b"><code>6fe6140</code></a> fix(vector-stores/oracledb): Fix accuracy bug (<a href="https://redirect.github.com/mem0ai/mem0/issues/6848">#6848</a>)</li>
<li><a href="https://github.com/mem0ai/mem0/commit/b05dc2740f9f7696d94ea06c3e04c64aac55997b"><code>b05dc27</code></a> docs(memory): note filters-based scoping for search/get_all on add() (<a href="https://redirect.github.com/mem0ai/mem0/issues/6758">#6758</a>)</li>
<li><a href="https://github.com/mem0ai/mem0/commit/4a0a9a92a641b5da75023eca596a758a4f7ae101"><code>4a0a9a9</code></a> fix(ts-oss, py): release Oracle client on init failure, validate insert batch...</li>
<li><a href="https://github.com/mem0ai/mem0/commit/beea626f0a09c454093643d79fff04494d4fdb9e"><code>beea626</code></a> perf(ts-oss): cut Oracle vector store round trips per review feedback (<a href="https://redirect.github.com/mem0ai/mem0/issues/6835">#6835</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/mem0ai/mem0/compare/v2.0.4...v2.0.18">compare view</a></li>
</ul>
</details>
<br />

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Dependency-only change for an optional extra; behavior shifts come from upstream mem0ai fixes between 2.0.4 and 2.0.18, not from CrewAI code.
> 
> **Overview**
> Raises the **`mem0` optional extra** floor in `lib/crewai/pyproject.toml` from `mem0ai>=2.0.0,<3` to **`>=2.0.18,<3`**, and refreshes **`uv.lock`** so installs resolve **`mem0ai` 2.0.18** (was 2.0.4).
> 
> The lockfile also picks up transitive updates tied to the new mem0 release—notably **`posthog` 5.4.0 → 7.80.3** and an explicit **`httpx`** dependency on `mem0ai`. There are **no CrewAI application or test code changes**; impact is limited to environments that install **`crewai[mem0]`**.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit befe03a3b297e5eb96913fd4718049f003968d37. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->