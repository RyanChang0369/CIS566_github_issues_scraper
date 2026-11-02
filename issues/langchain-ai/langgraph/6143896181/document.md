# chore(deps): bump the minor-and-patch group across 1 directory with 9 updates

Bumps the minor-and-patch group with 9 updates in the /libs/cli directory:

| Package | From | To |
| --- | --- | --- |
| [langgraph-sdk](https://github.com/langchain-ai/langgraph) | `0.4.6` | `0.4.10` |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | `1.2.3` | `1.2.4` |
| [pytest](https://github.com/pytest-dev/pytest) | `9.1.1` | `9.2.0` |
| [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio) | `1.4.0` | `1.4.1` |
| [pytest-mock](https://github.com/pytest-dev/pytest-mock) | `3.16.0` | `3.17.0` |
| [msgspec](https://github.com/msgspec/msgspec) | `0.21.1` | `0.22.0` |
| [ruff](https://github.com/astral-sh/ruff) | `0.16.9` | `0.17.3` |
| [ty](https://github.com/astral-sh/ty) | `0.0.84` | `0.0.95` |
| [hatch](https://github.com/pypa/hatch) | `1.18.1` | `1.18.2` |


Updates `langgraph-sdk` from 0.4.6 to 0.4.10
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/langchain-ai/langgraph/releases">langgraph-sdk's releases</a>.</em></p>
<blockquote>
<h2>langgraph-sdk==0.4.10</h2>
<p>Changes since sdk==0.4.9</p>
<ul>
<li>release(checkpoint): 4.3.1 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9447">#9447</a>)</li>
<li>release(langgraph): 1.2.18 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9445">#9445</a>)</li>
<li>release(sdk-py): 0.4.10 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9446">#9446</a>)</li>
<li>fix(sdk-py): retry runs.wait with a bodyless GET and raise run errors in sync wait (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9399">#9399</a>)</li>
<li>fix(sdk-py): follow the SSE spec for multi-line data, empty ids and a leading BOM (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9402">#9402</a>)</li>
<li>fix(sdk-py): accept durability, stream_resumable and context in the runs overloads (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9403">#9403</a>)</li>
<li>release(langgraph): 1.2.17 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9418">#9418</a>)</li>
</ul>
<h2>langgraph-sdk==0.4.9</h2>
<p>Changes since sdk==0.4.8</p>
<ul>
<li>release(sdk-py): 0.4.9 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9398">#9398</a>)</li>
<li>feat(sdk-py): add Priority for thread priority settings (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9392">#9392</a>)</li>
<li>chore(deps): remove precautionary third-party upper bounds (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9390">#9390</a>)</li>
<li>chore(deps): bump certifi from 2026.2.25 to 2026.10.19 in /libs/sdk-py (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9370">#9370</a>)</li>
<li>chore(deps-dev): bump dotenv from 17.4.2 to 18.0.4 in /libs/cli/js-examples in the major group (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9154">#9154</a>)</li>
<li>chore(deps-dev): bump the minor-and-patch group in /libs/prebuilt with 6 updates (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9150">#9150</a>)</li>
</ul>
<h2>langgraph-sdk==0.4.8</h2>
<p>Changes since sdk==0.4.7</p>
<ul>
<li>release(langgraph): 1.2.16 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9334">#9334</a>)</li>
<li>release(sdk-py): 0.4.8 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9335">#9335</a>)</li>
<li>fix(sdk-py): surface thread stream errors and stop retrying a rejected stream (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9317">#9317</a>)</li>
<li>release(prebuilt): 1.1.1 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9316">#9316</a>)</li>
</ul>
<h2>langgraph-sdk==0.4.7</h2>
<p>Changes since sdk==0.4.6</p>
<ul>
<li>release(sdk-py): 0.4.7 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9289">#9289</a>)</li>
<li>release(langgraph): 1.2.15 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9283">#9283</a>)</li>
<li>fix(sdk-py): end a thread stream's run only on a root lifecycle event (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9228">#9228</a>)</li>
<li>fix: order delta channel replay by task path (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/8544">#8544</a>)</li>
<li>release(langgraph): 1.2.14 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/9215">#9215</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/langchain-ai/langgraph/commit/13d66e0ebb62d6dde33e2f8e4ee8ffbd5b392ed2"><code>13d66e0</code></a> 0.4.10</li>
<li><a href="https://github.com/langchain-ai/langgraph/commit/4749a168a9116702fe88e74ca9c3813102d16b26"><code>4749a16</code></a> v0.4.x: Forward compatibility with checkpoints without pending_sends</li>
<li><a href="https://github.com/langchain-ai/langgraph/commit/98c369a0cf2bcc00344790f7fe8b751a252f3dfe"><code>98c369a</code></a> 0.4.9</li>
<li><a href="https://github.com/langchain-ai/langgraph/commit/c3544024b926c04206de1fe31373c29a3a593769"><code>c354402</code></a> If FuturesDict callback has been GCed, don't call it</li>
<li><a href="https://github.com/langchain-ai/langgraph/commit/3c7981201e1c3b5eea5fc9da2c1cdc519a09a3bd"><code>3c79812</code></a> docs: remove usage of <code>StateGraph(dict)</code> (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/4967">#4967</a>)</li>
<li><a href="https://github.com/langchain-ai/langgraph/commit/d7c364c5bb71b23047efea822215d739404a557e"><code>d7c364c</code></a> Port step_timeout/GraphBubbleUp fix to v0</li>
<li><a href="https://github.com/langchain-ai/langgraph/commit/c89fe4c45d101ccbdd168c1a8d2b550bd02c4e9c"><code>c89fe4c</code></a> 0.4.8</li>
<li><a href="https://github.com/langchain-ai/langgraph/commit/48fb91deda3b24fa6a04df962c5c6001b4448ce3"><code>48fb91d</code></a> Fix Command(graph=PARENT) when used together w checkpointer=True</li>
<li><a href="https://github.com/langchain-ai/langgraph/commit/89ce6ea2a8c6a2b5ad61b0f4d8e608425132aea6"><code>89ce6ea</code></a> Remove SchemaCoercionMapper</li>
<li><a href="https://github.com/langchain-ai/langgraph/commit/5602c29668a1671fafd8ef737a705cdaa190ea56"><code>5602c29</code></a> prebuilt: release 0.2.2 (<a href="https://redirect.github.com/langchain-ai/langgraph/issues/4851">#4851</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/langchain-ai/langgraph/compare/0.4.6...0.4.10">compare view</a></li>
</ul>
</details>
<br />

Updates `python-dotenv` from 1.2.3 to 1.2.4
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/theskumar/python-dotenv/releases">python-dotenv's releases</a>.</em></p>
<blockquote>
<h2>v1.2.4</h2>
<h3>Fixed</h3>
<ul>
<li><code>dotenv get</code> no longer exits with code 1 for empty string values (<code>KEY=</code>) by [<a href="https://github.com/ShamikOfficial"><code>@​ShamikOfficial</code></a>] in <a href="https://redirect.github.com/theskumar/python-dotenv/issues/700">#700</a></li>
<li>An unquoted empty value followed by an inline comment (e.g. <code>KEY= # comment</code>) is now parsed as an empty string instead of the comment text by [<a href="https://github.com/Noethix55555"><code>@​Noethix55555</code></a>] in <a href="https://redirect.github.com/theskumar/python-dotenv/issues/663">#663</a></li>
<li><code>dotenv run --no-override</code> now expands variable references with the same precedence as <code>load_dotenv(override=False)</code>, so a value like <code>${BASE}/suffix</code> uses the existing <code>BASE</code> from the environment instead of the one from the <code>.env</code> file by [<a href="https://github.com/ROTl24"><code>@​ROTl24</code></a>] in <a href="https://redirect.github.com/theskumar/python-dotenv/issues/698">#698</a></li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/theskumar/python-dotenv/blob/main/CHANGELOG.md">python-dotenv's changelog</a>.</em></p>
<blockquote>
<h2>[1.2.4] - 2026-10-01</h2>
<h3>Fixed</h3>
<ul>
<li><code>dotenv get</code> no longer exits with code 1 for empty string values (<code>KEY=</code>) by [<a href="https://github.com/ShamikOfficial"><code>@​ShamikOfficial</code></a>] in <a href="https://redirect.github.com/theskumar/python-dotenv/issues/700">#700</a></li>
<li>An unquoted empty value followed by an inline comment (e.g. <code>KEY= # comment</code>) is now parsed as an empty string instead of the comment text by [<a href="https://github.com/Noethix55555"><code>@​Noethix55555</code></a>] in <a href="https://redirect.github.com/theskumar/python-dotenv/issues/663">#663</a></li>
<li><code>dotenv run --no-override</code> now expands variable references with the same precedence as <code>load_dotenv(override=False)</code>, so a value like <code>${BASE}/suffix</code> uses the existing <code>BASE</code> from the environment instead of the one from the <code>.env</code> file by [<a href="https://github.com/ROTl24"><code>@​ROTl24</code></a>] in <a href="https://redirect.github.com/theskumar/python-dotenv/issues/698">#698</a></li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/theskumar/python-dotenv/commit/a565c2cc41599c48eabc6b7b7f5b826d43c5a6d7"><code>a565c2c</code></a> Bump version: 1.2.3 → 1.2.4</li>
<li><a href="https://github.com/theskumar/python-dotenv/commit/4a7abd00261e51baba958e15f443c66165042ea2"><code>4a7abd0</code></a> docs: add 1.2.4 release notes (<a href="https://redirect.github.com/theskumar/python-dotenv/issues/663">#663</a>, <a href="https://redirect.github.com/theskumar/python-dotenv/issues/698">#698</a>, <a href="https://redirect.github.com/theskumar/python-dotenv/issues/700">#700</a>)</li>
<li><a href="https://github.com/theskumar/python-dotenv/commit/f215c0274dc4c310e5ca5feb4c6bddade25ece21"><code>f215c02</code></a> fix: dotenv get exits 0 for empty string values (<a href="https://redirect.github.com/theskumar/python-dotenv/issues/700">#700</a>)</li>
<li><a href="https://github.com/theskumar/python-dotenv/commit/58f2d7c112235b347040bb5cb579d4ebc0a0ad91"><code>58f2d7c</code></a> test: make test_run_with_command_flags portable and meaningful (<a href="https://redirect.github.com/theskumar/python-dotenv/issues/709">#709</a>)</li>
<li><a href="https://github.com/theskumar/python-dotenv/commit/e0310e5bb3f2b701b11bbc007ca0c82c1bd56f38"><code>e0310e5</code></a> fix: honor --no-override when expanding variables in dotenv run (<a href="https://redirect.github.com/theskumar/python-dotenv/issues/698">#698</a>)</li>
<li><a href="https://github.com/theskumar/python-dotenv/commit/a00cb2eed0704cd6d2071b2004c37e95ccc86ee5"><code>a00cb2e</code></a> docs: add CHANGELOG entry for <a href="https://redirect.github.com/theskumar/python-dotenv/issues/663">#663</a> (fix <a href="https://redirect.github.com/theskumar/python-dotenv/issues/600">#600</a>)</li>
<li><a href="https://github.com/theskumar/python-dotenv/commit/f5485a61eefa5e686d6d5bdc7aa9ad6b104b1e92"><code>f5485a6</code></a> fix: parse empty unquoted value with inline comment as empty string</li>
<li>See full diff in <a href="https://github.com/theskumar/python-dotenv/compare/v1.2.3...v1.2.4">compare view</a></li>
</ul>
</details>
<br />

Updates `pytest` from 9.1.1 to 9.2.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/pytest-dev/pytest/releases">pytest's releases</a>.</em></p>
<blockquote>
<h2>9.2.0</h2>
<h1>pytest 9.2.0 (2026-10-27)</h1>
<h2>Removals and backward incompatible breaking changes</h2>
<ul>
<li>
<p><a href="https://redirect.github.com/pytest-dev/pytest/issues/14716">#14716</a>: <code>-c</code> now raises a usage error for a path that does not exist, is a directory, or is in a format pytest has no loader for. Such paths were previously either ignored or reported as an unhandled <code>FileNotFoundError</code>.</p>
</li>
<li>
<p><a href="https://redirect.github.com/pytest-dev/pytest/issues/8593">#8593</a>: The <code>indirect</code>, <code>ids</code> and <code>scope</code> arguments of <code>Metafunc.parametrize() &lt;pytest.Metafunc.parametrize&gt;</code> -- and therefore of <code>@pytest.mark.parametrize &lt;pytest.mark.parametrize ref&gt;</code> -- are now keyword-only.</p>
<p>Passing them positionally was a common source of confusing errors, e.g. <code>parametrize(&quot;arg1&quot;, &quot;arg2&quot;, [(1, 2)])</code> made the argvalues land in <code>indirect</code> and failed with <code>indirect fixture '(1, 2)' doesn't exist</code>; such mistakes now fail with an understandable <code>TypeError</code>. The type annotations have always declared these arguments as keyword-only.</p>
</li>
<li>
<p><a href="https://redirect.github.com/pytest-dev/pytest/issues/993">#993</a>: Plugin import failures at startup are now reported and classified instead of escaping as a raw traceback with the accidental exit code <code>1</code>:</p>
<ul>
<li>a plugin that cannot be found -- via <code>-p</code>, <code>pytest_plugins</code> or <code>PYTEST_PLUGINS</code> -- exits with <code>pytest.ExitCode</code> <code>USAGE_ERROR</code> (<code>4</code>), like a <code>conftest.py</code> that fails to import;</li>
<li>a plugin that is found but raises while importing -- including a broken <code>pytest11</code> entry point or a missing plugin dependency -- exits with <code>pytest.ExitCode</code> <code>INTERNAL_ERROR</code> (<code>3</code>), with the traceback preserved.</li>
</ul>
<p><code>pytest.main</code> now returns these codes instead of raising <code>ImportError</code>. Also fixed an <code>IndexError</code> from pytest's own internals when the plugin raised an exception with no arguments.</p>
</li>
</ul>
<h2>Deprecations (removal in next major release)</h2>
<ul>
<li>
<p><a href="https://redirect.github.com/pytest-dev/pytest/issues/14742">#14742</a>: The private <code>_pytest.python.CallSpec2</code> name has been renamed to <code>CallSpec</code>.
The old <code>CallSpec2</code> alias remains available for now and will be removed in pytest 10 or 11.</p>
</li>
<li>
<p><a href="https://redirect.github.com/pytest-dev/pytest/issues/14755">#14755</a>: Schedule <em>yield_fixture</em> decorator for removal in pytest 10 or 11.</p>
</li>
<li>
<p><a href="https://redirect.github.com/pytest-dev/pytest/issues/14774">#14774</a>: Similarly to the deprecation of class-scoped fixtures defined as instance methods in pytest 9.1,
<em>all</em> higher-scoped fixtures (<code>module</code>, <code>package</code>, and <code>session</code>) defined
as instance methods are now deprecated.</p>
<p>They suffer from the same issue the original deprecation only fixed for
class-scoped fixtures, see <code>10819</code> and <code>14011</code>.</p>
</li>
<li>
<p><a href="https://redirect.github.com/pytest-dev/pytest/issues/14808">#14808</a>: Passing a non-string value to a <code>string</code>-typed ini option now emits a <code>pytest.PytestRemovedIn10Warning</code>. This affects <code>[tool.pytest.ini_options]</code> in <code>pyproject.toml</code>. In pytest 10 this will raise a <code>TypeError</code>, matching the behavior of the corresponding TOML config path.</p>
</li>
<li>
<p><a href="https://redirect.github.com/pytest-dev/pytest/issues/7323">#7323</a>: Passing <code>bytes</code> to <code>TerminalReporter.write_line()</code> is now deprecated, pass a <code>str</code> instead.</p>
</li>
</ul>
<h2>New features</h2>
<ul>
<li><a href="https://redirect.github.com/pytest-dev/pytest/issues/14743">#14743</a>: <!-- raw HTML omitted -->Full diff:<!-- raw HTML omitted --> now contains a legend explaining the <!-- raw HTML omitted -->+<!-- raw HTML omitted --> &amp; <!-- raw HTML omitted -->-<!-- raw HTML omitted --> symbols in diff output.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest/issues/2781">#2781</a>: When <code>strict_markers</code> is enabled, marker names used in <code>-m</code> expressions are now validated against registered markers.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest/issues/6881">#6881</a>: Added the <code>parametrize_long_str_id_strategy</code> configuration option to control how long <code>str</code>/<code>bytes</code> parameter values are handled in auto-generated test IDs. Explicit IDs set via <code>ids=[...]</code> or <code>pytest.param(..., id=...)</code> are not affected. Available strategies: <code>short</code> (default, values over 100 chars fall back to <code>argname+index</code>), <code>sha256</code> (SHA-256 hex digest), <code>legacy</code> (keep full value), and <code>disallow</code> (error requesting explicit IDs).</li>
</ul>
<h2>Improvements in existing functionality</h2>
<ul>
<li><a href="https://redirect.github.com/pytest-dev/pytest/issues/10745">#10745</a>: A <code>RecursionError</code> whose recursion origin cannot be located now shows only the
first and last 10 stack frames, matching what pytest already did when locating
the origin failed outright. Previously the full traceback -- often around a
thousand near-identical frames -- was rendered, which was both slow and
unreadable. Pass <code>--full-trace</code> to see every frame.</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/pytest-dev/pytest/commit/ae1d0ff57b8bd4252da9ade7353523ac0ac73281"><code>ae1d0ff</code></a> Prepare release version 9.2.0</li>
<li><a href="https://github.com/pytest-dev/pytest/commit/143ce31dea9b12ff2ab6add04361ee01ab114931"><code>143ce31</code></a> pre-commit: exclude codespell on generated release announcements</li>
<li><a href="https://github.com/pytest-dev/pytest/commit/532dc5fc78f57de5115c5ecc9c6c29257787ada7"><code>532dc5f</code></a> tox: add attrs dependency to regen, needed in reportingdemo.rst</li>
<li><a href="https://github.com/pytest-dev/pytest/commit/a7b2446ee41a7298d3a0bc22c52f3b8bacae1566"><code>a7b2446</code></a> Merge pull request <a href="https://redirect.github.com/pytest-dev/pytest/issues/15245">#15245</a> from pytest-dev/claude/project-thread-9jcf91</li>
<li><a href="https://github.com/pytest-dev/pytest/commit/679d09c6945156746e17e9ec0b1c8309bbde3ad3"><code>679d09c</code></a> [pre-commit.ci] pre-commit autoupdate (<a href="https://redirect.github.com/pytest-dev/pytest/issues/15266">#15266</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest/commit/41d12cdbb4a35a7877768d93d8dc50a9117a8d8c"><code>41d12cd</code></a> docs: clarify typing for yield fixtures</li>
<li><a href="https://github.com/pytest-dev/pytest/commit/b9022ba04a33bfc76b5c9aefb8974755a80bf5ce"><code>b9022ba</code></a> Merge pull request <a href="https://redirect.github.com/pytest-dev/pytest/issues/15182">#15182</a> from 1871698/docs/improve-getting-started-description</li>
<li><a href="https://github.com/pytest-dev/pytest/commit/16f87a7f364a7362fbfbb204c79a47ad567b4fbd"><code>16f87a7</code></a> docs: improve getting-started.rst test execution description</li>
<li><a href="https://github.com/pytest-dev/pytest/commit/082ed70e314ee8e1ab117763d17fe801648f7508"><code>082ed70</code></a> Merge pull request <a href="https://redirect.github.com/pytest-dev/pytest/issues/15255">#15255</a> from pytest-dev/claude/project-thread-eoi3d6</li>
<li><a href="https://github.com/pytest-dev/pytest/commit/ae37a013763e9c4a143245eda1acdc3c27961685"><code>ae37a01</code></a> Merge pull request <a href="https://redirect.github.com/pytest-dev/pytest/issues/15227">#15227</a> from pytest-dev/claude/project-thread-4etye4</li>
<li>Additional commits viewable in <a href="https://github.com/pytest-dev/pytest/compare/9.1.1...9.2.0">compare view</a></li>
</ul>
</details>
<br />

Updates `pytest-asyncio` from 1.4.0 to 1.4.1
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/pytest-dev/pytest-asyncio/releases">pytest-asyncio's releases</a>.</em></p>
<blockquote>
<h2>pytest-asyncio v1.4.1</h2>
<h1><a href="https://github.com/pytest-dev/pytest-asyncio/tree/1.4.1">1.4.1</a> - 2026-10-25</h1>
<h2>Added</h2>
<ul>
<li>Declared support for Python 3.15 (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1588">#1588</a>)</li>
</ul>
<h2>Fixed</h2>
<ul>
<li>Allow <em>AsyncIterable</em> as a return type for asynchronous generator fixtures decorated with <em>pytest_asyncio.fixture</em> (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1090">#1090</a>)</li>
</ul>
<h2>Notes for Downstream Packagers</h2>
<ul>
<li>Source-tree development dependencies now use PEP 735 dependency groups and <code>uv.lock</code>. (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1518">#1518</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/pytest-dev/pytest-asyncio/commit/6af7f5c9a8c77fe5040b9d368b9ed01837c25652"><code>6af7f5c</code></a> chore: Prepare release of v1.4.1.</li>
<li><a href="https://github.com/pytest-dev/pytest-asyncio/commit/32ccf64ec115e42543bddb8cd142b2026b0cab77"><code>32ccf64</code></a> Support 3.15 (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1588">#1588</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest-asyncio/commit/983007120dcc53b14f8f7e9df492cbd1d20a242c"><code>9830071</code></a> Build(deps): Bump certifi from 2026.6.17 to 2026.10.19 (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1590">#1590</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest-asyncio/commit/0238023e439113044a9ed095307884c774ec9e46"><code>0238023</code></a> Build(deps): Bump virtualenv from 21.7.13 to 21.14.13 (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1589">#1589</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest-asyncio/commit/93893ecd9447d105ebd56419bc5162aa2420587e"><code>93893ec</code></a> Build(deps): Bump astral-sh/setup-uv from 10.2.0 to 10.3.0 (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1583">#1583</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest-asyncio/commit/f287e5e0f5425380b24c32b64037dfb2ed3cb937"><code>f287e5e</code></a> Build(deps): Bump actions/download-artifact from 8.0.1 to 8.0.2 (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1581">#1581</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest-asyncio/commit/b71da4fe09265e1ad86d4cbfc452b590ebfc4daa"><code>b71da4f</code></a> Build(deps-dev): Bump hypothesis from 6.168.3 to 6.168.5 (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1582">#1582</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest-asyncio/commit/d8c51d8990a4bbdf8a19ff0cf80d68b95b11dea8"><code>d8c51d8</code></a> Build(deps): Bump actions/upload-artifact from 7.0.1 to 7.0.2 (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1580">#1580</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest-asyncio/commit/b12808bd8d061b583ccdddc53ad6c85198509eed"><code>b12808b</code></a> Build(deps): Bump virtualenv from 21.7.12 to 21.7.13 (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1578">#1578</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest-asyncio/commit/e0601f0ce9532de0b5453a5cfd08f25b258a93f5"><code>e0601f0</code></a> Build(deps-dev): Bump coverage from 7.16.1 to 7.16.2 (<a href="https://redirect.github.com/pytest-dev/pytest-asyncio/issues/1577">#1577</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/pytest-dev/pytest-asyncio/compare/v1.4.0...v1.4.1">compare view</a></li>
</ul>
</details>
<br />

Updates `pytest-mock` from 3.16.0 to 3.17.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/pytest-dev/pytest-mock/releases">pytest-mock's releases</a>.</em></p>
<blockquote>
<h2>v3.17.0</h2>
<p><em>2026-10-17</em></p>
<ul>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/641">#641</a>: Failures of mock assertions such as <code>assert_called_with</code> are again reported only once, instead of two or three times with the original error from the <code>mock</code> module chained before them.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/642">#642</a>: Mock assertion failures no longer show misleading introspection when they are not about the arguments of the last call: <code>assert_called</code>, <code>assert_called_once</code>, <code>assert_not_called</code>, <code>assert_any_call</code>, their <code>await</code> counterparts, and <code>assert_called_once_with</code>/<code>assert_awaited_once_with</code> when the mock was not called (awaited) exactly once. The introspection also no longer reports arguments passed by position versus by keyword as different for autospecced mocks, and no longer shows empty <code>Args:</code>/<code>Kwargs:</code> sections when assertion rewriting is not available.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/643">#643</a>: <code>assert_has_calls</code> and <code>assert_has_awaits</code> failures no longer show pytest introspection, which compared the expected and actual calls position by position and so reported differences between unrelated calls. The mock's own message, listing the expected and actual calls, is still shown.</li>
</ul>
<h2>v3.16.1</h2>
<p><em>2026-10-17</em></p>
<ul>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/617">#617</a>: Fixed <code>assert_has_calls</code> raising <code>ValueError</code> instead of <code>AssertionError</code> (or showing misleading introspection) when the expected calls are plain tuples rather than <code>call(...)</code> objects, such as <code>(args, kwargs)</code> entries of another mock's <code>call_args_list</code>, <code>(args,)</code>, <code>(kwargs,)</code>, <code>(name, args)</code> or <code>(name, kwargs)</code>.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/621">#621</a>: Fixed <code>mocker.stop()</code> sometimes stopping the wrong mock, for example with mocks from <code>mocker.create_autospec</code>.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/621">#621</a>: <code>mocker.stop()</code> now undoes the most recent patch first when the same object is used in several patches.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/623">#623</a>: Fixed misleading introspection in <code>assert_has_awaits</code> failures, and <code>assert_has_calls</code>/<code>assert_has_awaits</code> raising <code>IndexError</code> instead of <code>AssertionError</code> when <code>calls</code> is passed by keyword.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/624">#624</a>: Clear <code>spy_return_iter</code> after a spied synchronous or asynchronous function raises, matching <code>spy_return</code>.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/627">#627</a>: Document <code>async_stub</code> await assertions and the distinction between call and await tracking.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/629">#629</a>: Fixed <code>mocker.resetall()</code> skipping the mocks patched with <code>mocker.patch.multiple()</code>, both the ones it creates and the ones passed explicitly.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/630">#630</a>: <code>mocker.resetall()</code> now also resets <code>spy_return</code> and <code>spy_exception</code> of spies, like it already did for <code>spy_return_list</code> and <code>spy_return_iter</code>, and no longer overwrites attributes with these names on mocks that are not spies.</li>
<li><a href="https://redirect.github.com/pytest-dev/pytest-mock/pull/633">#633</a>: Fixed spies on <code>classmethod</code>, <code>staticmethod</code>, builtins and classes returning a <code>MagicMock</code> instead of calling the spied code after <code>mocker.resetall(side_effect=True)</code>. Resetting a spy's <code>side_effect</code> now goes back to calling the spied code, also clearing any <code>side_effect</code> set on the spy.</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/pytest-dev/pytest-mock/blob/main/CHANGELOG.rst">pytest-mock's changelog</a>.</em></p>
<blockquote>
<h2>3.17.0</h2>
<p><em>2026-10-17</em></p>
<ul>
<li><code>[#641](https://github.com/pytest-dev/pytest-mock/issues/641) &lt;https://github.com/pytest-dev/pytest-mock/pull/641&gt;</code>_: Failures of mock assertions such as <code>assert_called_with</code> are again reported only once, instead of two or three times with the original error from the <code>mock</code> module chained before them.</li>
<li><code>[#642](https://github.com/pytest-dev/pytest-mock/issues/642) &lt;https://github.com/pytest-dev/pytest-mock/pull/642&gt;</code>_: Mock assertion failures no longer show misleading introspection when they are not about the arguments of the last call: <code>assert_called</code>, <code>assert_called_once</code>, <code>assert_not_called</code>, <code>assert_any_call</code>, their <code>await</code> counterparts, and <code>assert_called_once_with</code>/<code>assert_awaited_once_with</code> when the mock was not called (awaited) exactly once. The introspection also no longer reports arguments passed by position versus by keyword as different for autospecced mocks, and no longer shows empty <code>Args:</code>/<code>Kwargs:</code> sections when assertion rewriting is not available.</li>
<li><code>[#643](https://github.com/pytest-dev/pytest-mock/issues/643) &lt;https://github.com/pytest-dev/pytest-mock/pull/643&gt;</code>_: <code>assert_has_calls</code> and <code>assert_has_awaits</code> failures no longer show pytest introspection, which compared the expected and actual calls position by position and so reported differences between unrelated calls. The mock's own message, listing the expected and actual calls, is still shown.</li>
</ul>
<h2>3.16.1</h2>
<p><em>2026-10-17</em></p>
<ul>
<li><code>[#617](https://github.com/pytest-dev/pytest-mock/issues/617) &lt;https://github.com/pytest-dev/pytest-mock/pull/617&gt;</code>_: Fixed <code>assert_has_calls</code> raising <code>ValueError</code> instead of <code>AssertionError</code> (or showing misleading introspection) when the expected calls are plain tuples rather than <code>call(...)</code> objects, such as <code>(args, kwargs)</code> entries of another mock's <code>call_args_list</code>, <code>(args,)</code>, <code>(kwargs,)</code>, <code>(name, args)</code> or <code>(name, kwargs)</code>.</li>
<li><code>[#621](https://github.com/pytest-dev/pytest-mock/issues/621) &lt;https://github.com/pytest-dev/pytest-mock/pull/621&gt;</code>_: Fixed <code>mocker.stop()</code> sometimes stopping the wrong mock, for example with mocks from <code>mocker.create_autospec</code>.</li>
<li><code>[#621](https://github.com/pytest-dev/pytest-mock/issues/621) &lt;https://github.com/pytest-dev/pytest-mock/pull/621&gt;</code>_: <code>mocker.stop()</code> now undoes the most recent patch first when the same object is used in several patches.</li>
<li><code>[#623](https://github.com/pytest-dev/pytest-mock/issues/623) &lt;https://github.com/pytest-dev/pytest-mock/pull/623&gt;</code>_: Fixed misleading introspection in <code>assert_has_awaits</code> failures, and <code>assert_has_calls</code>/<code>assert_has_awaits</code> raising <code>IndexError</code> instead of <code>AssertionError</code> when <code>calls</code> is passed by keyword.</li>
<li><code>[#624](https://github.com/pytest-dev/pytest-mock/issues/624) &lt;https://github.com/pytest-dev/pytest-mock/pull/624&gt;</code>_: Clear <code>spy_return_iter</code> after a spied synchronous or asynchronous function raises, matching <code>spy_return</code>.</li>
<li><code>[#627](https://github.com/pytest-dev/pytest-mock/issues/627) &lt;https://github.com/pytest-dev/pytest-mock/pull/627&gt;</code>_: Document <code>async_stub</code> await assertions and the distinction between call and await tracking.</li>
<li><code>[#629](https://github.com/pytest-dev/pytest-mock/issues/629) &lt;https://github.com/pytest-dev/pytest-mock/pull/629&gt;</code>_: Fixed <code>mocker.resetall()</code> skipping the mocks patched with <code>mocker.patch.multiple()</code>, both the ones it creates and the ones passed explicitly.</li>
<li><code>[#630](https://github.com/pytest-dev/pytest-mock/issues/630) &lt;https://github.com/pytest-dev/pytest-mock/pull/630&gt;</code>_: <code>mocker.resetall()</code> now also resets <code>spy_return</code> and <code>spy_exception</code> of spies, like it already did for <code>spy_return_list</code> and <code>spy_return_iter</code>, and no longer overwrites attributes with these names on mocks that are not spies.</li>
<li><code>[#633](https://github.com/pytest-dev/pytest-mock/issues/633) &lt;https://github.com/pytest-dev/pytest-mock/pull/633&gt;</code>_: Fixed spies on <code>classmethod</code>, <code>staticmethod</code>, builtins and classes returning a <code>MagicMock</code> instead of calling the spied code after <code>mocker.resetall(side_effect=True)</code>. Resetting a spy's <code>side_effect</code> now goes back to calling the spied code, also clearing any <code>side_effect</code> set on the spy.</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/pytest-dev/pytest-mock/commit/5c2f207ca7098dde996f9bedd06e596e39b6246b"><code>5c2f207</code></a> Release 3.17.0</li>
<li><a href="https://github.com/pytest-dev/pytest-mock/commit/96252715fad4a0dfec1997103cc231bc1f133616"><code>9625271</code></a> Bump the minor version for releases that change existing behavior</li>
<li><a href="https://github.com/pytest-dev/pytest-mock/commit/34b87aeeef1d2a85be5ce4fadb0c6bc4a033c40a"><code>34b87ae</code></a> Drop introspection from assert_has_calls and assert_has_awaits (<a href="https://redirect.github.com/pytest-dev/pytest-mock/issues/643">#643</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest-mock/commit/866520f2d339c7649af56ac227ca67ed36b1e92e"><code>866520f</code></a> Only show introspection for failures about the call arguments (<a href="https://redirect.github.com/pytest-dev/pytest-mock/issues/642">#642</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest-mock/commit/5ab41c143c57842456caad0029082e919fa6a95d"><code>5ab41c1</code></a> Do not chain the original mock error to wrapped assertion failures (<a href="https://redirect.github.com/pytest-dev/pytest-mock/issues/641">#641</a>)</li>
<li><a href="https://github.com/pytest-dev/pytest-mock/commit/1916b14db224b893edf18251f26a38487eb0d6a6"><code>1916b14</code></a> Merge pull request <a href="https://redirect.github.com/pytest-dev/pytest-mock/issues/635">#635</a> from nicoddemus/docs-contributing-resetall</li>
<li><a href="https://github.com/pytest-dev/pytest-mock/commit/212fcd903aeb685a3b39875be82fc84ff58ebc56"><code>212fcd9</code></a> Document resetall, the changelog format and running tests with tox</li>
<li><a href="https://github.com/pytest-dev/pytest-mock/commit/9374b2c3e38e3bbc2e04328f7026ae3680f0476f"><code>9374b2c</code></a> Merge pull request <a href="https://redirect.github.com/pytest-dev/pytest-mock/issues/634">#634</a> from pytest-dev/release-3.16.1</li>
<li><a href="https://github.com/pytest-dev/pytest-mock/commit/fab730daf4a4cfc260d8656b0467503131535a00"><code>fab730d</code></a> Release 3.16.1</li>
<li><a href="https://github.com/pytest-dev/pytest-mock/commit/d26d41bb01e99de5c0b59156c667d46985b03470"><code>d26d41b</code></a> Merge pull request <a href="https://redirect.github.com/pytest-dev/pytest-mock/issues/627">#627</a> from xiehuanyi/docs/async-stub-awaits-20261012-r2</li>
<li>Additional commits viewable in <a href="https://github.com/pytest-dev/pytest-mock/compare/v3.16.0...v3.17.0">compare view</a></li>
</ul>
</details>
<br />

Updates `msgspec` from 0.21.1 to 0.22.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/msgspec/msgspec/releases">msgspec's releases</a>.</em></p>
<blockquote>
<h2>Version 0.22.0 (2026-09-29)</h2>
<ul>
<li><strong>BREAKING</strong>: Setting <code>gc=False</code> on a struct type that has a weakref slot,
whether from <code>weakref=True</code> or from a base class, now raises <code>ValueError</code>.
On CPython 3.12 and later the weakref slot is stored in a pre-header in
front of the instance, so releasing an instance of a <code>gc=False</code> type with
that slot corrupted memory, in most builds crashing the interpreter
outright. The combination worked on 3.10 and 3.11, and the restriction
applies there as well, so that the same class definition behaves the same
way on every supported version (<a href="https://redirect.github.com/msgspec/msgspec/issues/1207">#1207</a>).</li>
<li>Add <code>frozendict</code> support on Python 3.15+ (<a href="https://redirect.github.com/msgspec/msgspec/issues/1052">#1052</a>, <a href="https://redirect.github.com/msgspec/msgspec/issues/1105">#1105</a>).</li>
<li>Support passing a callable as <code>decimal_format</code> to <code>msgspec.json.Encoder</code> and
<code>msgspec.msgpack.Encoder</code> for custom <code>Decimal</code> encoding (<a href="https://redirect.github.com/msgspec/msgspec/issues/978">#978</a>).</li>
<li>Support <code>Literal[True]</code> and <code>Literal[False]</code> types (<a href="https://redirect.github.com/msgspec/msgspec/issues/1004">#1004</a>).</li>
<li>Publish CPython 3.15 wheels, including freethreaded builds (<a href="https://redirect.github.com/msgspec/msgspec/issues/1152">#1152</a>).</li>
<li>Publish Linux <code>riscv64</code> wheels (<a href="https://redirect.github.com/msgspec/msgspec/issues/987">#987</a>).</li>
<li>Support the PyEmscripten (Pyodide) platform (<a href="https://redirect.github.com/msgspec/msgspec/issues/1083">#1083</a>).</li>
<li>Fix handling of PEP 695 type parameter syntax (<code>class Foo[T]</code>) and of
<code>types.GenericAlias</code> instances in type annotations (<a href="https://redirect.github.com/msgspec/msgspec/issues/962">#962</a>).</li>
<li>Fix <code>NameError</code> when creating a <code>Struct</code> with an unquoted forward
reference on Python 3.14 (<a href="https://redirect.github.com/msgspec/msgspec/issues/1165">#1165</a>).</li>
<li>Fix a crash on incorrect <code>typing.ClassVar</code> annotations (<a href="https://redirect.github.com/msgspec/msgspec/issues/1097">#1097</a>).</li>
<li>Fix an <code>AttributeError</code> when converting to a <code>Struct</code> type defined in a
namespace without a <code>__name__</code> (<a href="https://redirect.github.com/msgspec/msgspec/issues/1072">#1072</a>).</li>
<li>Fix overriding an inherited field alias back to the field's own name
(<a href="https://redirect.github.com/msgspec/msgspec/issues/1133">#1133</a>).</li>
<li>Raise <code>ValidationError</code> instead of <code>SystemError</code> when <code>convert</code> receives an
out-of-range <code>int</code> for a <code>float</code> target (<a href="https://redirect.github.com/msgspec/msgspec/issues/1162">#1162</a>).</li>
<li>Report <code>raw</code> rather than the misleading <code>any</code> as the expected type when a
non-<code>Raw</code> value is given for a <code>Raw</code> field in <code>convert</code>, and therefore in
<code>yaml.decode</code> and <code>toml.decode</code> (<a href="https://redirect.github.com/msgspec/msgspec/issues/1169">#1169</a>).</li>
<li>Fix an empty expected-type name in validation errors for a required <code>Raw</code>
field in a <code>TypedDict</code>, or a <code>Raw</code> field with a <code>default_factory</code> on a
<code>dataclass</code> or an <code>attrs</code> class (<a href="https://redirect.github.com/msgspec/msgspec/issues/1176">#1176</a>).</li>
<li>Correct the error messages for out-of-range <code>Meta</code> length bounds
(<a href="https://redirect.github.com/msgspec/msgspec/issues/1172">#1172</a>).</li>
<li>Fix a reference leak when decoding msgpack <code>Ext</code> payloads (<a href="https://redirect.github.com/msgspec/msgspec/issues/1109">#1109</a>).</li>
<li>Fix backing type declaration of <code>Ext.code</code> (<a href="https://redirect.github.com/msgspec/msgspec/issues/1135">#1135</a>).</li>
<li>Fix a reference leak in <code>msgspec.to_builtins</code>, and therefore in
<code>yaml.encode</code>, for <code>array_like=True</code> structs (<a href="https://redirect.github.com/msgspec/msgspec/issues/1177">#1177</a>).</li>
<li>Fix reference leaks in <code>typenode_collect_literal</code>, <code>Meta.__rich_repr__</code>,
<code>ms_decode_bigint</code>, and <code>Encoder.__init__</code> (<a href="https://redirect.github.com/msgspec/msgspec/issues/1021">#1021</a>, <a href="https://redirect.github.com/msgspec/msgspec/issues/1022">#1022</a>,
<a href="https://redirect.github.com/msgspec/msgspec/issues/1023">#1023</a>, <a href="https://redirect.github.com/msgspec/msgspec/issues/1040">#1040</a>).</li>
<li>Fix <code>msgspec.inspect.type_info</code> and <code>msgspec.json.schema</code> crashing on mixed-type <code>Literal</code>s such as <code>Literal[1, None]</code> (<a href="https://redirect.github.com/msgspec/msgspec/issues/1080">#1080</a>).</li>
<li>Place <code>null</code> last in the <code>anyOf</code> generated for optional unions in JSON
schemas (<a href="https://redirect.github.com/msgspec/msgspec/issues/1028">#1028</a>).</li>
<li>Fix <code>minItems</code> in the JSON schema for <code>array_like=True</code> structs whose fields
are all optional (<a href="https://redirect.github.com/msgspec/msgspec/issues/1124">#1124</a>).</li>
<li>Use <code>[]</code> or <code>&quot;&quot;</code> rather than a Python <code>set</code> or <code>bytearray</code> object as the
JSON schema <code>default</code> for <code>Struct</code> fields with a <code>set</code> or <code>bytearray</code></li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/msgspec/msgspec/blob/main/docs/changelog.md">msgspec's changelog</a>.</em></p>
<blockquote>
<h2>Version 0.22.0 (2026-09-29)</h2>
<ul>
<li><strong>BREAKING</strong>: Setting <code>gc=False</code> on a struct type that has a weakref slot,
whether from <code>weakref=True</code> or from a base class, now raises <code>ValueError</code>.
On CPython 3.12 and later the weakref slot is stored in a pre-header in
front of the instance, so releasing an instance of a <code>gc=False</code> type with
that slot corrupted memory, in most builds crashing the interpreter
outright. The combination worked on 3.10 and 3.11, and the restriction
applies there as well, so that the same class definition behaves the same
way on every supported version ({pr}<code>1207</code>).</li>
<li><strong>BREAKING</strong>: Encode an object as a dataclass only when its type defines
<code>__dataclass_fields__</code>, as <code>dataclasses.is_dataclass</code> does. Objects that
expose it only through instance attribute access, such as proxies wrapping
a dataclass instance, are now passed to <code>enc_hook</code>, and encoding them raises
<code>TypeError</code> when no <code>enc_hook</code> is given. An <code>enc_hook</code> can return the wrapped
instance, which is then encoded as a dataclass. Objects with a Python-level
<code>__getattr__</code>, such as pydantic models, now reach <code>enc_hook</code> without that
<code>__getattr__</code> being called ({pr}<code>1196</code>).</li>
<li>Add <code>frozendict</code> support on Python 3.15+ ({pr}<code>1052</code>, {pr}<code>1105</code>).</li>
<li>Support passing a callable as <code>decimal_format</code> to <code>msgspec.json.Encoder</code> and
<code>msgspec.msgpack.Encoder</code> for custom <code>Decimal</code> encoding ({pr}<code>978</code>).</li>
<li>Support <code>Literal[True]</code> and <code>Literal[False]</code> types ({pr}<code>1004</code>).</li>
<li>Publish CPython 3.15 wheels, including freethreaded builds ({pr}<code>1152</code>).</li>
<li>Publish Linux <code>riscv64</code> wheels ({pr}<code>987</code>).</li>
<li>Support the PyEmscripten (Pyodide) platform ({pr}<code>1083</code>).</li>
<li>Fix handling of PEP 695 type parameter syntax (<code>class Foo[T]</code>) and of
<code>types.GenericAlias</code> instances in type annotations ({pr}<code>962</code>).</li>
<li>Fix <code>NameError</code> when creating a <code>Struct</code> with an unquoted forward
reference on Python 3.14 ({issue}<code>1165</code>).</li>
<li>Fix a crash on incorrect <code>typing.ClassVar</code> annotations ({pr}<code>1097</code>).</li>
<li>Raise <code>TypeError</code> instead of crashing when a base class of a <code>Struct</code> type is
a C extension type that has not been initialized with <code>PyType_Ready</code> yet
({pr}<code>1199</code>).</li>
<li>Fix an <code>AttributeError</code> when converting to a <code>Struct</code> type defined in a
namespace without a <code>__name__</code> ({pr}<code>1072</code>).</li>
<li>Fix overriding an inherited field alias back to the field's own name
({pr}<code>1133</code>).</li>
<li>Raise <code>ValidationError</code> instead of <code>SystemError</code> when <code>convert</code> receives an
out-of-range <code>int</code> for a <code>float</code> target ({pr}<code>1162</code>).</li>
<li>Report <code>raw</code> rather than the misleading <code>any</code> as the expected type when a
non-<code>Raw</code> value is given for a <code>Raw</code> field in <code>convert</code>, and therefore in
<code>yaml.decode</code> and <code>toml.decode</code> ({pr}<code>1169</code>).</li>
<li>Fix an empty expected-type name in validation errors for a required <code>Raw</code>
field in a <code>TypedDict</code>, or a <code>Raw</code> field with a <code>default_factory</code> on a
<code>dataclass</code> or an <code>attrs</code> class ({pr}<code>1176</code>).</li>
<li>Correct the error messages for out-of-range <code>Meta</code> length bounds
({pr}<code>1172</code>).</li>
<li>Fix a reference leak when decoding msgpack <code>Ext</code> payloads ({pr}<code>1109</code>).</li>
<li>Fix backing type declaration of <code>Ext.code</code> ({pr}<code>1135</code>).</li>
<li>Raise <code>DecodeError</code> instead of <code>TypeError</code> when a decoded msgpack map key is</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/msgspec/msgspec/commit/6d3443f2dae8413a1a56640290c09a6f486f30c2"><code>6d3443f</code></a> Fix a reference leak of a non-Struct base's type dict (<a href="https://redirect.github.com/msgspec/msgspec/issues/1199">#1199</a>)</li>
<li><a href="https://github.com/msgspec/msgspec/commit/2f0b50da9f3ac3d452e9fd49dd94d3f064738eea"><code>2f0b50d</code></a> Correct the reported signatures of several public callables (<a href="https://redirect.github.com/msgspec/msgspec/issues/1197">#1197</a>)</li>
<li><a href="https://github.com/msgspec/msgspec/commit/8a2547129b61b5c5abc01b4d3be5a5819fd6e364"><code>8a25471</code></a> Skip instance <code>__dataclass_fields__</code> lookup for non-dataclass types (<a href="https://redirect.github.com/msgspec/msgspec/issues/1196">#1196</a>)</li>
<li><a href="https://github.com/msgspec/msgspec/commit/793078028aad2a726f0e09dd85eff211e15a92ac"><code>7930780</code></a> Fix reference leak when defining a Struct type (<a href="https://redirect.github.com/msgspec/msgspec/issues/1194">#1194</a>)</li>
<li><a href="https://github.com/msgspec/msgspec/commit/55f5cdd03545acb3a58b3e145f3efd9fd8294998"><code>55f5cdd</code></a> fix(msgpack): raise DecodeError for unhashable map keys (<a href="https://redirect.github.com/msgspec/msgspec/issues/1209">#1209</a>)</li>
<li><a href="https://github.com/msgspec/msgspec/commit/b2d1b7a81a836f73f1a828bfbcc63bf0792ee039"><code>b2d1b7a</code></a> Reject <code>gc=False</code> on struct types with a weakref slot (<a href="https://redirect.github.com/msgspec/msgspec/issues/1207">#1207</a>)</li>
<li><a href="https://github.com/msgspec/msgspec/commit/f2bbec556ac50a8b405e63dc742536f5c95afb51"><code>f2bbec5</code></a> Move the unreleased changes into the 0.22.0 changelog (<a href="https://redirect.github.com/msgspec/msgspec/issues/1211">#1211</a>)</li>
<li><a href="https://github.com/msgspec/msgspec/commit/c23e150a82faad223706ba888bcce5c16b866d39"><code>c23e150</code></a> Fix json schema defaults for set / bytearray default_factory fields (<a href="https://redirect.github.com/msgspec/msgspec/issues/1183">#1183</a>)</li>
<li><a href="https://github.com/msgspec/msgspec/commit/fed9fc3131f19a2e6a1303433de9f5d1f4ff6938"><code>fed9fc3</code></a> Skip recursive type alias test on Windows ARM64 with Python 3.12 (<a href="https://redirect.github.com/msgspec/msgspec/issues/1210">#1210</a>)</li>
<li><a href="https://github.com/msgspec/msgspec/commit/e7552f0f3341eabdbab4ecfc63c1b352ad26b7dc"><code>e7552f0</code></a> Bump msgpack from 1.2.1 to 1.2.2 (<a href="https://redirect.github.com/msgspec/msgspec/issues/1202">#1202</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/msgspec/msgspec/compare/0.21.1...0.22.0">compare view</a></li>
</ul>
</details>
<br />

Updates `ruff` from 0.16.9 to 0.17.3
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/astral-sh/ruff/releases">ruff's releases</a>.</em></p>
<blockquote>
<h2>0.17.3</h2>
<h2>Release Notes</h2>
<p>Released on 2026-10-26.</p>
<h3>Preview features</h3>
<ul>
<li>[<code>suspicious</code>] Add <code>shared-clock-mock</code> (<a href="https://redirect.github.com/astral-sh/ruff/pull/29074">#29074</a>)</li>
</ul>
<h3>Bug fixes</h3>
<ul>
<li>[<code>pyupgrade</code>] Avoid incorrect conversions to f-strings (<code>UP032</code>) (<a href="https://redirect.github.com/astral-sh/ruff/pull/25485">#25485</a>)</li>
</ul>
<h3>Performance</h3>
<ul>
<li>Buffer stdout in <code>ruff format</code> (<a href="https://redirect.github.com/astral-sh/ruff/pull/29631">#29631</a>)</li>
<li>Specialize ASCII identifier lexing (<a href="https://redirect.github.com/astral-sh/ruff/pull/29503">#29503</a>)</li>
<li>Speed up identifier and keyword lexing (<a href="https://redirect.github.com/astral-sh/ruff/pull/29463">#29463</a>)</li>
</ul>
<h3>Documentation</h3>
<ul>
<li>[<code>flake8-bandit</code>] Describe what the rule actually checks for <code>httpx</code> (<code>S113</code>) (<a href="https://redirect.github.com/astral-sh/ruff/pull/27936">#27936</a>)</li>
</ul>
<h3>Contributors</h3>
<ul>
<li><a href="https://github.com/itsvedantkumar"><code>@​itsvedantkumar</code></a></li>
<li><a href="https://github.com/charliermarsh"><code>@​charliermarsh</code></a></li>
<li><a href="https://github.com/anishgirianish"><code>@​anishgirianish</code></a></li>
</ul>
<h2>Install ruff 0.17.3</h2>
<h3>Install prebuilt binaries via shell script</h3>
<pre lang="sh"><code>curl --proto '=https' --tlsv1.2 -LsSf https://releases.astral.sh/github/ruff/releases/download/0.17.3/ruff-installer.sh | sh
</code></pre>
<h3>Install prebuilt binaries via powershell script</h3>
<pre lang="sh"><code>powershell -ExecutionPolicy Bypass -c &quot;irm https://releases.astral.sh/github/ruff/releases/download/0.17.3/ruff-installer.ps1 | iex&quot;
</code></pre>
<h2>Download ruff 0.17.3</h2>
<table>
<thead>
<tr>
<th>File</th>
<th>Platform</th>
<th>Checksum</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://releases.astral.sh/github/ruff/releases/download/0.17.3/ruff-aarch64-apple-darwin.tar.gz">ruff-aarch64-apple-darwin.tar.gz</a></td>
<td>Apple Silicon macOS</td>
<td><a href="https://releases.astral.sh/github/ruff/releases/download/0.17.3/ruff-aarch64-apple-darwin.tar.gz.sha256">checksum</a></td>
</tr>
<tr>
<td><a href="https://releases.astral.sh/github/ruff/releases/download/0.17.3/ruff-x86_64-apple-darwin.tar.gz">ruff-x86_64-apple-darwin.tar.gz</a></td>
<td>Intel macOS</td>
<td><a href="https://releases.astral.sh/github/ruff/releases/download/0.17.3/ruff-x86_64-apple-darwin.tar.gz.sha256">checksum</a></td>
</tr>
<tr>
<td><a href="https://releases.astral.sh/github/ruff/releases/download/0.17.3/ruff-aarch64-pc-windows-msvc.zip">ruff-aarch64-pc-windows-msvc.zip</a></td>
<td>ARM64 Windows</td>
<td><a href="https://releases.astral.sh/github/ruff/releases/download/0.17.3/ruff-aarch64-pc-windows-msvc.zip.sha256">checksum</a></td>
</tr>
</tbody>
</table>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md">ruff's changelog</a>.</em></p>
<blockquote>
<h2>0.17.3</h2>
<p>Released on 2026-10-26.</p>
<h3>Preview features</h3>
<ul>
<li>[<code>suspicious</code>] Add <code>shared-clock-mock</code> (<a href="https://redirect.github.com/astral-sh/ruff/pull/29074">#29074</a>)</li>
</ul>
<h3>Bug fixes</h3>
<ul>
<li>[<code>pyupgrade</code>] Avoid incorrect conversions to f-strings (<code>UP032</code>) (<a href="https://redirect.github.com/astral-sh/ruff/pull/25485">#25485</a>)</li>
</ul>
<h3>Performance</h3>
<ul>
<li>Buffer stdout in <code>ruff format</code> (<a href="https://redirect.github.com/astral-sh/ruff/pull/29631">#29631</a>)</li>
<li>Specialize ASCII identifier lexing (<a href="https://redirect.github.com/astral-sh/ruff/pull/29503">#29503</a>)</li>
<li>Speed up identifier and keyword lexing (<a href="https://redirect.github.com/astral-sh/ruff/pull/29463">#29463</a>)</li>
</ul>
<h3>Documentation</h3>
<ul>
<li>[<code>flake8-bandit</code>] Describe what the rule actually checks for <code>httpx</code> (<code>S113</code>) (<a href="https://redirect.github.com/astral-sh/ruff/pull/27936">#27936</a>)</li>
</ul>
<h3>Contributors</h3>
<ul>
<li><a href="https://github.com/itsvedantkumar"><code>@​itsvedantkumar</code></a></li>
<li><a href="https://github.com/charliermarsh"><code>@​charliermarsh</code></a></li>
<li><a href="https://github.com/anishgirianish"><code>@​anishgirianish</code></a></li>
</ul>
<h2>0.17.2</h2>
<p>Released on 2026-10-22.</p>
<h3>Preview features</h3>
<ul>
<li>[<code>complexity</code>] Add <code>unnecessary-regular-expression-compile</code> (<a href="https://redirect.github.com/astral-sh/ruff/pull/25533">#25533</a>)</li>
</ul>
<h3>Bug fixes</h3>
<ul>
<li>Avoid syntax errors for type variables with starred constraints (<code>UP040</code>, <code>UP046</code>, <code>UP047</code>, <code>RUF053</code>) (<a href="https://redirect.github.com/astral-sh/ruff/pull/28362">#28362</a>)</li>
<li>[<code>pydocstyle</code>] Treat backslash-escaped <code>*args</code> and <code>**kwargs</code> as documented (<code>D417</code>) (<a href="https://redirect.github.com/astral-sh/ruff/pull/29536">#29536</a>)</li>
<li>[<code>pylint</code>] Avoid false positive on starred elements (<code>PLE0643</code>) (<a href="https://redirect.github.com/astral-sh/ruff/pull/29483">#29483</a>)</li>
<li>[<code>pylint</code>] Mark fixes unsafe when deleting comments (<code>PLR5501</code>, <code>PLW0120</code>) (<a href="https://redirect.github.com/astral-sh/ruff/pull/29414">#29414</a>)</li>
<li>[<code>pyupgrade</code>] Mark fix unsafe when deleting comments (<code>UP035</code>) (<a href="https://redirect.github.com/astral-sh/ruff/pull/29413">#29413</a>)</li>
</ul>
<h3>Performance</h3>
<ul>
<li>Avoid intermediate names in lint name resolution (<a href="https://redirect.github.com/astral-sh/ruff/pull/29506">#29506</a>)</li>
<li>Prefilter bidirectional Unicode checks by UTF-8 leading bytes (<a href="https://redirect.github.com/astral-sh/ruff/pull/29561">#29561</a>)</li>
<li>Share postfix parsing and reduce expression copies (<a href="https://redirect.github.com/astral-sh/ruff/pull/29480">#29480</a>)</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/astral-sh/ruff/commit/ba65abf8ba7bfbcc059f7fb9712be5ba9cab6abc"><code>ba65abf</code></a> Bump version to 0.17.3 (<a href="https://redirect.github.com/astral-sh/ruff/issues/29745">#29745</a>)</li>
<li><a href="https://github.com/astral-sh/ruff/commit/fb2f9218793e3b0e979175d43d88dcac791e92d6"><code>fb2f921</code></a> [ty] Fix narrowing of strings and integers compared with enum members (<a href="https://redirect.github.com/astral-sh/ruff/issues/29743">#29743</a>)</li>
<li><a href="https://github.com/astral-sh/ruff/commit/d1812878d5f81af6f5810d193ebc44413d1b21cc"><code>d181287</code></a> [ty] Index nominal union alternatives (<a href="https://redirect.github.com/astral-sh/ruff/issues/29196">#29196</a>)</li>
<li><a href="https://github.com/astral-sh/ruff/commit/07872adbafa7c00f42f1174d8aa3c3e324033009"><code>07872ad</code></a> [ty] Preserve string literals in comparisons with <code>LiteralString</code> (<a href="https://redirect.github.com/astral-sh/ruff/issues/29741">#29741</a>)</li>
<li><a href="https://github.com/astral-sh/ruff/commit/95888b2edfaa34d0159732856b1466cf53b33e64"><code>95888b2</code></a> [ty] Preserve narrowing after guarded match subject captures (<a href="https://redirect.github.com/astral-sh/ruff/issues/29558">#29558</a>)</li>
<li><a href="https://github.com/astral-sh/ruff/commit/3c8166b683805aa89557b0739f5b9918ad58ea6d"><code>3c8166b</code></a> [ty] Fix hang when negating recursive unions of instance types (<a href="https://redirect.github.com/astral-sh/ruff/issues/29652">#29652</a>)</li>
<li><a href="https://github.com/astral-sh/ruff/commit/3fd20e08598ac345b8afd524d3f7086456e4e758"><code>3fd20e0</code></a> [ty] Preserve generic callback specializations during return refinement (<a href="https://redirect.github.com/astral-sh/ruff/issues/29667">#29667</a>)</li>
<li><a href="https://github.com/astral-sh/ruff/commit/2f0a29ece1f1a539c65c0671c04c76bb886219fe"><code>2f0a29e</code></a> [ty] Record predicate truthiness alongside expression inference (<a href="https://redirect.github.com/astral-sh/ruff/issues/29706">#29706</a>)</li>
<li><a href="https://github.com/astral-sh/ruff/commit/60f104a1a2ec4e980198ff54c38ba6fe7045b29f"><code>60f104a</code></a> [ty] Honor <a href="https://github.com/override"><code>@​override</code></a> on overload implementations in stubs (<a href="https://redirect.github.com/astral-sh/ruff/issues/29470">#29470</a>)</li>
<li><a href="https://github.com/astral-sh/ruff/commit/207ec3affeb118fce03a65f9333959157e228312"><code>207ec3a</code></a> [ty] Add diagnostic baseline support (<a href="https://redirect.github.com/astral-sh/ruff/issues/27636">#27636</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/astral-sh/ruff/compare/0.16.9...0.17.3">compare view</a></li>
</ul>
</details>
<br />

Updates `ty` from 0.0.84 to 0.0.95
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/astral-sh/ty/releases">ty's releases</a>.</em></p>
<blockquote>
<h2>0.0.95</h2>
<h2>Release Notes</h2>
<p>Released on 2026-10-29.</p>
<h3>Bug fixes</h3>
<ul>
<li>Accept another unpacked TypeVarTuple as a default (<a href="https://redirect.github.com/astral-sh/ruff/pull/29752">#29752</a>)</li>
<li>Accept keyword arguments for <code>TypeAliasType</code> name and value (<a href="https://redirect.github.com/astral-sh/ruff/pull/29802">#29802</a>)</li>
<li>Detect traversal budget exhaustion in products of lower bounds (<a href="https://redirect.github.com/astral-sh/ruff/pull/29679">#29679</a>)</li>
<li>Fix recursive protocol materialization self-comparison (<a href="https://redirect.github.com/astral-sh/ruff/pull/29809">#29809</a>)</li>
<li>Reject out-of-scope type variables in PEP 695 pack defaults (<a href="https://redirect.github.com/astral-sh/ruff/pull/29805">#29805</a>)</li>
<li>Use a trailing ParamSpec default after a TypeVarTuple (<a href="https://redirect.github.com/astral-sh/ruff/pull/29755">#29755</a>)</li>
</ul>
<h3>LSP server</h3>
<ul>
<li>Parenthesize assignment and generator expressions in argument hint edits (<a href="https://redirect.github.com/astral-sh/ruff/pull/29797">#29797</a>)</li>
<li>Place argument name inlay hints before grouping parentheses (<a href="https://redirect.github.com/astral-sh/ruff/pull/29794">#29794</a>)</li>
<li>Place variable type inlay hints after grouping parentheses (<a href="https://redirect.github.com/astral-sh/ruff/pull/29795">#29795</a>)</li>
</ul>
<h3>Contributors</h3>
<ul>
<li><a href="https://github.com/carljm"><code>@​carljm</code></a></li>
<li><a href="https://github.com/AlexWaygood"><code>@​AlexWaygood</code></a></li>
<li><a href="https://github.com/charliermarsh"><code>@​charliermarsh</code></a></li>
</ul>
<h2>Install ty 0.0.95</h2>
<h3>Install prebuilt binaries via shell script</h3>
<pre lang="sh"><code>curl --proto '=https' --tlsv1.2 -LsSf https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-installer.sh | sh
</code></pre>
<h3>Install prebuilt binaries via powershell script</h3>
<pre lang="sh"><code>powershell -ExecutionPolicy Bypass -c &quot;irm https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-installer.ps1 | iex&quot;
</code></pre>
<h2>Download ty 0.0.95</h2>
<table>
<thead>
<tr>
<th>File</th>
<th>Platform</th>
<th>Checksum</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-aarch64-apple-darwin.tar.gz">ty-aarch64-apple-darwin.tar.gz</a></td>
<td>Apple Silicon macOS</td>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-aarch64-apple-darwin.tar.gz.sha256">checksum</a></td>
</tr>
<tr>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-x86_64-apple-darwin.tar.gz">ty-x86_64-apple-darwin.tar.gz</a></td>
<td>Intel macOS</td>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-x86_64-apple-darwin.tar.gz.sha256">checksum</a></td>
</tr>
<tr>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-aarch64-pc-windows-msvc.zip">ty-aarch64-pc-windows-msvc.zip</a></td>
<td>ARM64 Windows</td>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-aarch64-pc-windows-msvc.zip.sha256">checksum</a></td>
</tr>
<tr>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-i686-pc-windows-msvc.zip">ty-i686-pc-windows-msvc.zip</a></td>
<td>x86 Windows</td>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-i686-pc-windows-msvc.zip.sha256">checksum</a></td>
</tr>
<tr>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-x86_64-pc-windows-msvc.zip">ty-x86_64-pc-windows-msvc.zip</a></td>
<td>x64 Windows</td>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-x86_64-pc-windows-msvc.zip.sha256">checksum</a></td>
</tr>
<tr>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-aarch64-unknown-linux-gnu.tar.gz">ty-aarch64-unknown-linux-gnu.tar.gz</a></td>
<td>ARM64 Linux</td>
<td><a href="https://releases.astral.sh/github/ty/releases/download/0.0.95/ty-aarch64-unknown-linux-gnu.tar.gz.sha256">checksum</a></td>
</tr>
</tbody>
</table>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/astral-sh/ty/blob/main/CHANGELOG.md">ty's changelog</a>.</em></p>
<blockquote>
<h2>0.0.95</h2>
<p>Released on 2026-10-29.</p>
<h3>Bug fixes</h3>
<ul>
<li>Accept another unpacked TypeVarTuple as a default (<a href="https://redirect.github.com/astral-sh/ruff/pull/29752">#29752</a>)</li>
<li>Accept keyword arguments for <code>TypeAliasType</code> name and value (<a href="https://redirect.github.com/astral-sh/ruff/pull/29802">#29802</a>)</li>
<li>Detect traversal budget exhaustion in products of lower bounds (<a href="https://redirect.github.com/astral-sh/ruff/pull/29679">#29679</a>)</li>
<li>Fix recursive protocol materialization self-comparison (<a href="https://redirect.github.com/astral-sh/ruff/pull/29809">#29809</a>)</li>
<li>Reject out-of-scope type variables in PEP 695 pack defaults (<a href="https://redirect.github.com/astral-sh/ruff/pull/29805">#29805</a>)</li>
<li>Use a trailing ParamSpec default after a TypeVarTuple (<a href="https://redirect.github.com/astral-sh/ruff/pull/29755">#29755</a>)</li>
</ul>
<h3>LSP server</h3>
<ul>
<li>Parenthesize assignment and generator expressions in argument hint edits (<a href="https://redirect.github.com/astral-sh/ruff/pull/29797">#29797</a>)</li>
<li>Place argument name inlay hints before grouping parentheses (<a href="https://redirect.github.com/astral-sh/ruff/pull/29794">#29794</a>)</li>
<li>Place variable type inlay hints after grouping parentheses (<a href="https://redirect.github.com/astral-sh/ruff/pull/29795">#29795</a>)</li>
</ul>
<h3>Contributors</h3>
<ul>
<li><a href="https://github.com/carljm"><code>@​carljm</code></a></li>
<li><a href="https://github.com/AlexWaygood"><code>@​AlexWaygood</code></a></li>
<li><a href="https://github.com/charliermarsh"><code>@​charliermarsh</code></a></li>
</ul>
<h2>0.0.94</h2>
<p>Released on 2026-10-28.</p>
<h3>Bug fixes</h3>
<ul>
<li>Correctly handle line continuation when fixing unused ignore comments (<a href="https://redirect.github.com/astral-sh/ruff/pull/29781">#29781</a>)</li>
<li>Fix Linux x86-64 startup on older kernels (<a href="https://redirect.github.com/astral-sh/ty/pull/4853">#4853</a>)</li>
<li>Fix a panic when a comprehension filter depends on a later binding (<a href="https://redirect.github.com/astral-sh/ruff/pull/29786">#29786</a>)</li>
<li>Fix a panic when sorting diagnostic...

_Description has been truncated_