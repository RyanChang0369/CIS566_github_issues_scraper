# chore(deps): bump the minor-and-patch group across 1 directory with 8 updates

Bumps the minor-and-patch group with 8 updates in the /libs/langgraph directory:

| Package | From | To |
| --- | --- | --- |
| [langchain-core](https://github.com/langchain-ai/langchain) | `1.6.5` | `1.7.3` |
| [xxhash](https://github.com/ifduyue/python-xxhash) | `4.0.1` | `4.0.2` |
| [pydantic](https://github.com/pydantic/pydantic) | `2.13.5` | `2.14.2` |
| [pytest](https://github.com/pytest-dev/pytest) | `9.1.1` | `9.2.0` |
| [pytest-mock](https://github.com/pytest-dev/pytest-mock) | `3.16.0` | `3.17.0` |
| [uvloop](https://github.com/MagicStack/uvloop) | `0.22.1` | `0.23.0` |
| [ruff](https://github.com/astral-sh/ruff) | `0.16.9` | `0.17.3` |
| [ty](https://github.com/astral-sh/ty) | `0.0.84` | `0.0.95` |


Updates `langchain-core` from 1.6.5 to 1.7.3
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/langchain-ai/langchain/releases">langchain-core's releases</a>.</em></p>
<blockquote>
<h2>langchain-core==1.7.3</h2>
<p>Changes since langchain-core==1.7.2</p>
<p>release(core): 1.7.3 (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41564">#41564</a>)</p>
<h2>langchain-core==1.7.2</h2>
<p>Changes since langchain-core==1.7.1</p>
<p>release(core): 1.7.2 (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41562">#41562</a>)
feat(core): add <code>add_notification_metadata</code> and <code>get_notification_metadata</code> (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41540">#41540</a>)
fix(core): stop <code>merge_content</code> from changing the first message's content (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41502">#41502</a>)</p>
<h2>langchain-core==1.7.1</h2>
<p>Changes since langchain-core==1.7.0</p>
<p>release(core): version 1.7.1 (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41548">#41548</a>)
fix(core): preserve gateway tracing metadata in v3 streams (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41504">#41504</a>)
fix(core): escape node metadata in Mermaid labels (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41512">#41512</a>)
chore(deps): bump the minor-and-patch group across 3 directories with 32 updates (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41465">#41465</a>)
chore(deps-dev): bump setuptools from 83.0.0 to 84.1.0 in /libs/core (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41442">#41442</a>)
chore(deps): bump nbconvert from 7.17.1 to 7.17.2 in /libs/core (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41425">#41425</a>)
chore(infra): relax third-party dependency upper bounds (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41407">#41407</a>)</p>
<h2>langchain-core==1.7.0</h2>
<p>Changes since langchain-core==1.6.13</p>
<p>release(core): 1.7.0 (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41418">#41418</a>)
feat(core): emit <code>tool-call-delta</code> for streamed tool-call args (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41257">#41257</a>)</p>
<h2>Notes</h2>
<ul>
<li>Tool-call args now stream as <code>tool-call-delta</code> slices instead of <code>block-delta</code> snapshots of the args so far. If you read raw stream events and their <code>block-delta</code> args mid-stream, read <code>tool-call-delta</code> instead. <code>.tool_calls.get()</code> and <code>.output</code> are unchanged. To keep snapshots, pin <code>langchain-core&lt;1.7</code>.</li>
<li>Since 1.6.13, iterating <code>ChatModelStream.tool_calls</code> yields each call's new args slice, not a snapshot of the args so far.</li>
</ul>
<h2>langchain-core==1.6.13</h2>
<p>Changes since langchain-core==1.6.12</p>
<p>release(core): 1.6.13 (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41397">#41397</a>)
chore(deps): bump certifi from 2025.11.12 to 2026.10.19 in /libs/core (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41373">#41373</a>)
feat(core,langchain,standard-tests): read <code>tool-call-delta</code> in stream consumers (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41246">#41246</a>)</p>
<h2>langchain-core==1.6.12</h2>
<p>Changes since langchain-core==1.6.11</p>
<p>release(core): 1.6.12 (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41277">#41277</a>)
fix(core): propagate extras on content-block-start events (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41272">#41272</a>)</p>
<h2>langchain-core==1.6.11</h2>
<p>Changes since langchain-core==1.6.10</p>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/langchain-ai/langchain/commit/864754c5e293fba981302408fa3e2cf2f5f2d889"><code>864754c</code></a> release(core): 1.7.3 (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41564">#41564</a>)</li>
<li><a href="https://github.com/langchain-ai/langchain/commit/51a3a6ae019eca3dc7981de89999eac1eb8dac12"><code>51a3a6a</code></a> chore(infra): ask how bug reports were discovered (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41563">#41563</a>)</li>
<li><a href="https://github.com/langchain-ai/langchain/commit/0027e67769e8bea61a2dc1dcc6f1fd7d3b649b63"><code>0027e67</code></a> release(core): 1.7.2 (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41562">#41562</a>)</li>
<li><a href="https://github.com/langchain-ai/langchain/commit/7f46a2e59fabee78e1d4abf626f1faf2e09d6676"><code>7f46a2e</code></a> docs: update OpenWiki (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41524">#41524</a>)</li>
<li><a href="https://github.com/langchain-ai/langchain/commit/7ce3593b63bc5d0f22206d4bf06cf9962d8f11ef"><code>7ce3593</code></a> feat(core): add <code>add_notification_metadata</code> and <code>get_notification_metadata</code> (...</li>
<li><a href="https://github.com/langchain-ai/langchain/commit/5029a0f7dd203921b1015e0f51e8a6d6c34bce94"><code>5029a0f</code></a> chore(model-profiles): refresh model profile data (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41556">#41556</a>)</li>
<li><a href="https://github.com/langchain-ai/langchain/commit/350568952c4b65d1310081d45a2536b6449712f0"><code>3505689</code></a> fix(anthropic): handle null cache-creation token counts (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41553">#41553</a>)</li>
<li><a href="https://github.com/langchain-ai/langchain/commit/8875dc8f5b44e5706df44f5bbee983489e4e63e0"><code>8875dc8</code></a> fix(fireworks): promote reranking out of beta (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41551">#41551</a>)</li>
<li><a href="https://github.com/langchain-ai/langchain/commit/399fd2e433e54cefdbddb3ede1079ddd3f8ca9c4"><code>399fd2e</code></a> fix(core): stop <code>merge_content</code> from changing the first message's content (<a href="https://redirect.github.com/langchain-ai/langchain/issues/4">#4</a>...</li>
<li><a href="https://github.com/langchain-ai/langchain/commit/e633868f9cb417456cde1ec19b585190d84c5c17"><code>e633868</code></a> chore(deps): bump authlib from 1.7.2 to 1.9.1 in /libs/langchain_v1 (<a href="https://redirect.github.com/langchain-ai/langchain/issues/41539">#41539</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/langchain-ai/langchain/compare/langchain-core==1.6.5...langchain-core==1.7.3">compare view</a></li>
</ul>
</details>
<br />

Updates `xxhash` from 4.0.1 to 4.0.2
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/ifduyue/python-xxhash/releases">xxhash's releases</a>.</em></p>
<blockquote>
<h2>v4.0.2</h2>
<ul>
<li>Improve type annotation compatibility with <code>hashlib</code></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/ifduyue/python-xxhash/compare/v4.0.1...v4.0.2">https://github.com/ifduyue/python-xxhash/compare/v4.0.1...v4.0.2</a></p>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/ifduyue/python-xxhash/blob/master/CHANGELOG.rst">xxhash's changelog</a>.</em></p>
<blockquote>
<p>v4.0.2 2026-10-19</p>
<pre><code>
- Improve type annotation compatibility with ``hashlib``
</code></pre>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/ifduyue/python-xxhash/commit/5803a455336a0eeb03e34f893d7526387e9555e5"><code>5803a45</code></a> Release v4.0.2</li>
<li><a href="https://github.com/ifduyue/python-xxhash/commit/f00c0f82094a04482822bb078708564a213201ab"><code>f00c0f8</code></a> Bump version to 4.0.2.dev0</li>
<li><a href="https://github.com/ifduyue/python-xxhash/commit/bb22b43bfc4e777fc3ee58041d47bff7278d23aa"><code>bb22b43</code></a> Remove the unused Protocol import from the type stubs</li>
<li><a href="https://github.com/ifduyue/python-xxhash/commit/aba963e90093f2fa1a33141bcd8f3f6cb2e1d823"><code>aba963e</code></a> Improve type annotation compatibility with <code>hashlib</code></li>
<li><a href="https://github.com/ifduyue/python-xxhash/commit/87db22e2d11fac8c1f55d619fd610394dfd005f5"><code>87db22e</code></a> ci: double the pyright timeout</li>
<li><a href="https://github.com/ifduyue/python-xxhash/commit/384a3a795a1b3aa7d3ff38778bf05d441a049ae2"><code>384a3a7</code></a> ci: test on PyPy 3.12</li>
<li><a href="https://github.com/ifduyue/python-xxhash/commit/d3c139ce57c7a24fa0200de70e236ef68753f028"><code>d3c139c</code></a> ci: test on Python 3.15</li>
<li><a href="https://github.com/ifduyue/python-xxhash/commit/f1a5a209df3ffaf49571d378c47556fda416fcb7"><code>f1a5a20</code></a> chore(ci): update actions</li>
<li><a href="https://github.com/ifduyue/python-xxhash/commit/3e74a9031f360f131075f8b5ace949d6930edfd9"><code>3e74a90</code></a> Add 3.7.3 and 3.8.2 changelog entries</li>
<li><a href="https://github.com/ifduyue/python-xxhash/commit/ad7b40b5021e32ebc3dc96c701848fdfdaf90c40"><code>ad7b40b</code></a> chore(ci): update actions</li>
<li>Additional commits viewable in <a href="https://github.com/ifduyue/python-xxhash/compare/v4.0.1...v4.0.2">compare view</a></li>
</ul>
</details>
<br />

Updates `pydantic` from 2.13.5 to 2.14.2
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/pydantic/pydantic/releases">pydantic's releases</a>.</em></p>
<blockquote>
<h2>v2.14.2 2026-10-29</h2>
<h2>v2.14.2 (2026-10-29)</h2>
<p>This release addresses 2 security issues, <a href="https://github.com/pydantic/pydantic/security/advisories/GHSA-qpmf-fgh3-ff25">https://github.com/pydantic/pydantic/security/advisories/GHSA-qpmf-fgh3-ff25</a> and <a href="https://github.com/pydantic/pydantic/security/advisories/GHSA-3r8g-cqwr-jr29">https://github.com/pydantic/pydantic/security/advisories/GHSA-3r8g-cqwr-jr29</a>.</p>
<h4>Packaging</h4>
<ul>
<li>Bump PyO3 to 0.30.1, jiter to 0.18.0, use <code>PyFrozenDict</code> by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14003">#14003</a></li>
<li>Bump speedate to v0.18.0 by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14007">#14007</a></li>
<li>Publish <code>pydantic-core</code> wheels for PyPy 8.0 (<code>pp80</code> ABI) by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14083">#14083</a></li>
</ul>
<h4>Performance</h4>
<ul>
<li>Avoid Python tuple allocation during model fields validation by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/13955">#13955</a></li>
<li>Lazily call repr of values during nested union serialization by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14082">#14082</a></li>
<li>Skip decorator field checks when no field decorators exist by <a href="https://github.com/alexmojaki"><code>@​alexmojaki</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14111">#14111</a></li>
<li>Avoid heap allocation for small JSON model field buffers by <a href="https://github.com/alexmojaki"><code>@​alexmojaki</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14113">#14113</a></li>
</ul>
<h4>Fixes</h4>
<ul>
<li>
<p>Make JSON validation by iteration consistent with Python approach by <a href="https://github.com/davidhewitt"><code>@​davidhewitt</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/13275">#13275</a>.</p>
<p>JSON validation now handles field lookup and extra data the same way as Python validation. In particular, keys that only match an
unused alias or field name are now treated as extra data, instead of being silently dropped:</p>
<pre lang="python"><code>from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
<p>class Page(BaseModel):<br />
model_config = ConfigDict(extra='forbid', alias_generator=to_camel)</p>
<pre><code>page_size: int = 10
</code></pre>
<p>Page.model_validate_json('{&quot;page_size&quot;: 50}')</p>
<h1>Before: Page(page_size=10)</h1>
<h1>After: ValidationError (extra_forbidden)</h1>
<p></code></pre></p>
<p>See the <a href="https://redirect.github.com/pydantic/pydantic/pull/13275">pull request</a> for the full list of behavior changes.
This change addresses <a href="https://github.com/pydantic/pydantic/security/advisories/GHSA-qpmf-fgh3-ff25">https://github.com/pydantic/pydantic/security/advisories/GHSA-qpmf-fgh3-ff25</a>.</p>
</li>
<li>
<p>Ignore extra data matching a field name in <code>TypedDict</code> and dataclasses with <code>extra=allow</code> by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14090">#14090</a>. Addresses <a href="https://github.com/pydantic/pydantic/security/advisories/GHSA-3r8g-cqwr-jr29">https://github.com/pydantic/pydantic/security/advisories/GHSA-3r8g-cqwr-jr29</a>.</p>
</li>
<li>
<p>Fix unpickling of generic classes defined in separate module by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/13994">#13994</a></p>
</li>
<li>
<p>Support explicit <code>by_alias</code> overriding <code>validate_by_alias</code> in validation JSON schemas by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/13997">#13997</a></p>
</li>
<li>
<p>Fix mypy plugin crash on deferred empty model by <a href="https://github.com/ilevkivskyi"><code>@​ilevkivskyi</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14027">#14027</a></p>
</li>
<li>
<p>Fix infinite recursion when validating an invalid default with <code>PydanticUseDefault</code> by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14028">#14028</a></p>
</li>
<li>
<p>Implement recursion guard for <code>validate_strings()</code> by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14029">#14029</a></p>
</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/pydantic/pydantic/blob/v2.14.2/HISTORY.md">pydantic's changelog</a>.</em></p>
<blockquote>
<h2>v2.14.2 (2026-10-29)</h2>
<p><a href="https://github.com/pydantic/pydantic/releases/tag/v2.14.2">GitHub release</a></p>
<h3>What's Changed</h3>
<h4>Packaging</h4>
<ul>
<li>Bump PyO3 to 0.30.1, jiter to 0.18.0, use <code>PyFrozenDict</code> by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14003">#14003</a></li>
<li>Bump speedate to v0.18.0 by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14007">#14007</a></li>
<li>Publish <code>pydantic-core</code> wheels for PyPy 8.0 (<code>pp80</code> ABI) by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14083">#14083</a></li>
</ul>
<h4>Performance</h4>
<ul>
<li>Avoid Python tuple allocation during model fields validation by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/13955">#13955</a></li>
<li>Lazily call repr of values during nested union serialization by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14082">#14082</a></li>
<li>Skip decorator field checks when no field decorators exist by <a href="https://github.com/alexmojaki"><code>@​alexmojaki</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14111">#14111</a></li>
<li>Avoid heap allocation for small JSON model field buffers by <a href="https://github.com/alexmojaki"><code>@​alexmojaki</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14113">#14113</a></li>
</ul>
<h4>Fixes</h4>
<ul>
<li>
<p>Make JSON validation by iteration consistent with Python approach by <a href="https://github.com/davidhewitt"><code>@​davidhewitt</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/13275">#13275</a>.</p>
<p>JSON validation now handles field lookup and extra data the same way as Python validation. In particular, keys that only match an
unused alias or field name are now treated as extra data, instead of being silently dropped:</p>
<pre lang="python"><code>from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
<p>class Page(BaseModel):<br />
model_config = ConfigDict(extra='forbid', alias_generator=to_camel)</p>
<pre><code>page_size: int = 10
</code></pre>
<p>Page.model_validate_json('{&quot;page_size&quot;: 50}')</p>
<h1>Before: Page(page_size=10)</h1>
<h1>After: ValidationError (extra_forbidden)</h1>
<p></code></pre></p>
<p>See the <a href="https://redirect.github.com/pydantic/pydantic/pull/13275">pull request</a> for the full list of behavior changes.</p>
</li>
<li>
<p>Fix unpickling of generic classes defined in separate module by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/13994">#13994</a></p>
</li>
<li>
<p>Support explicit <code>by_alias</code> overriding <code>validate_by_alias</code> in validation JSON schemas by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/13997">#13997</a></p>
</li>
<li>
<p>Fix mypy plugin crash on deferred empty model by <a href="https://github.com/ilevkivskyi"><code>@​ilevkivskyi</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14027">#14027</a></p>
</li>
<li>
<p>Fix infinite recursion when validating an invalid default with <code>PydanticUseDefault</code> by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14028">#14028</a></p>
</li>
<li>
<p>Implement recursion guard for <code>validate_strings()</code> by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14029">#14029</a></p>
</li>
<li>
<p>Support named tuples in <code>Sequence</code> serialization by <a href="https://github.com/Viicos"><code>@​Viicos</code></a> in <a href="https://redirect.github.com/pydantic/pydantic/pull/14033">#14033</a></p>
</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/pydantic/pydantic/commit/aa540acc29960fb394312cf97d888c99f9686814"><code>aa540ac</code></a> Update changelog for v2.14.2</li>
<li><a href="https://github.com/pydantic/pydantic/commit/6cde12fa3e08201193bac8330c84dbe19cc825c8"><code>6cde12f</code></a> Update changelog for v2.14.2</li>
<li><a href="https://github.com/pydantic/pydantic/commit/2db7c25776c2ede3cccc9eca84024f2245ba1571"><code>2db7c25</code></a> Fix deep copy of self-referential models</li>
<li><a href="https://github.com/pydantic/pydantic/commit/d783154a3922871a49dda2de88856f445a58bc35"><code>d783154</code></a> Update changelog for v2.14.2</li>
<li><a href="https://github.com/pydantic/pydantic/commit/df49b6cff91a7e0d4ae8c001e77b8b9f0eec312b"><code>df49b6c</code></a> Avoid heap allocation for small JSON model field buffers</li>
<li><a href="https://github.com/pydantic/pydantic/commit/cd93e699ad7f38be3ec95712b0e2cba2d037b62f"><code>cd93e69</code></a> Skip decorator field checks when no field decorators exist</li>
<li><a href="https://github.com/pydantic/pydantic/commit/2771e57c39e660471f208908c0b856fb65435165"><code>2771e57</code></a> Make JSON validation by iteration consistent with Python approach</li>
<li><a href="https://github.com/pydantic/pydantic/commit/8102e3f16712dbe3109859de1610d9308ea8027f"><code>8102e3f</code></a> Avoid Python tuple allocation during model fields validation</li>
<li><a href="https://github.com/pydantic/pydantic/commit/dd139b5ddc2fbbb63cb1a178104d35f5076ef550"><code>dd139b5</code></a> Bump <code>pydantic.v1</code> namespace to v1.10.27</li>
<li><a href="https://github.com/pydantic/pydantic/commit/66155f9965ef6ad19b2ddb29546644b321d069c9"><code>66155f9</code></a> Prepare release v2.14.2</li>
<li>Additional commits viewable in <a href="https://github.com/pydantic/pydantic/compare/v2.13.5...v2.14.2">compare view</a></li>
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

Updates `uvloop` from 0.22.1 to 0.23.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/MagicStack/uvloop/releases">uvloop's releases</a>.</em></p>
<blockquote>
<h2>v0.23.0</h2>
<h1>Changes</h1>
<ul>
<li>
<p>Add Python 3.15 and 3.15t wheel builds and CI coverage (<a href="https://redirect.github.com/MagicStack/uvloop/issues/758">#758</a>)
(by <a href="https://github.com/honglei"><code>@​honglei</code></a> <a href="https://github.com/fantix"><code>@​fantix</code></a> in f7c05473)</p>
</li>
<li>
<p>Add support for the <code>eager_start</code> keyword argument in create_task() (<a href="https://redirect.github.com/MagicStack/uvloop/issues/748">#748</a>)
(by <a href="https://github.com/samypr100"><code>@​samypr100</code></a> in 3cbb0956 for <a href="https://redirect.github.com/MagicStack/uvloop/issues/746">#746</a> <a href="https://redirect.github.com/MagicStack/uvloop/issues/718">#718</a>)</p>
</li>
<li>
<p>Add thread name prefix to the default thread pool executor (<a href="https://redirect.github.com/MagicStack/uvloop/issues/636">#636</a>)
(by <a href="https://github.com/inikolaev"><code>@​inikolaev</code></a> <a href="https://github.com/fantix"><code>@​fantix</code></a> in 0582f946 for <a href="https://redirect.github.com/MagicStack/uvloop/issues/562">#562</a>)</p>
</li>
<li>
<p>Add support for special hostname <code>&lt;broadcast&gt;</code> (<a href="https://redirect.github.com/MagicStack/uvloop/issues/592">#592</a>)
(by <a href="https://github.com/jpbede"><code>@​jpbede</code></a> in 3060cebc for <a href="https://redirect.github.com/MagicStack/uvloop/issues/540">#540</a>)</p>
</li>
<li>
<p>Upgrade libuv to v1.52.1 (<a href="https://redirect.github.com/MagicStack/uvloop/issues/753">#753</a>)
(by <a href="https://github.com/fantix"><code>@​fantix</code></a> in e8efea40 for <a href="https://redirect.github.com/MagicStack/uvloop/issues/752">#752</a>)</p>
</li>
<li>
<p>Improve performance by using Python C API to enter/exit context (<a href="https://redirect.github.com/MagicStack/uvloop/issues/627">#627</a>)
(by <a href="https://github.com/tarasko"><code>@​tarasko</code></a> in 837ef22c)</p>
</li>
<li>
<p>Improve performance/latency of Transport.write (<a href="https://redirect.github.com/MagicStack/uvloop/issues/619">#619</a>)
(by <a href="https://github.com/tarasko"><code>@​tarasko</code></a> in 1d9b6e0d)</p>
</li>
<li>
<p>Replace some SSL vectorcall with direct methods (<a href="https://redirect.github.com/MagicStack/uvloop/issues/626">#626</a>)
(by <a href="https://github.com/tarasko"><code>@​tarasko</code></a> in 6a27cbe2)</p>
</li>
<li>
<p>Optimize SSL buffered reads using C values (<a href="https://redirect.github.com/MagicStack/uvloop/issues/629">#629</a>)
(by <a href="https://github.com/tarasko"><code>@​tarasko</code></a> in a308f75f)</p>
</li>
</ul>
<h1>Fixes</h1>
<ul>
<li>
<p>Detach socket on create_connection cancellation to prevent fd double-close (<a href="https://redirect.github.com/MagicStack/uvloop/issues/740">#740</a>)
(by <a href="https://github.com/junjzhang"><code>@​junjzhang</code></a> <a href="https://github.com/fantix"><code>@​fantix</code></a> in dc680eb2 for <a href="https://redirect.github.com/MagicStack/uvloop/issues/645">#645</a> <a href="https://redirect.github.com/MagicStack/uvloop/issues/738">#738</a>)</p>
</li>
<li>
<p>Remove <code>loop._ready_len</code> in favor of <code>len(loop._ready)</code> (<a href="https://redirect.github.com/MagicStack/uvloop/issues/721">#721</a>)
(by <a href="https://github.com/x42005e1f"><code>@​x42005e1f</code></a> in 5910a183 for <a href="https://redirect.github.com/MagicStack/uvloop/issues/720">#720</a>)</p>
</li>
<li>
<p>Prefer inspect.iscoroutinefunction (<a href="https://redirect.github.com/MagicStack/uvloop/issues/705">#705</a>)
(by <a href="https://github.com/MatthieuDartiailh"><code>@​MatthieuDartiailh</code></a> in fd650276 for <a href="https://redirect.github.com/MagicStack/uvloop/issues/703">#703</a>)</p>
</li>
<li>
<p>Fix context tests by explicitly yielding after run_in_executor (<a href="https://redirect.github.com/MagicStack/uvloop/issues/743">#743</a>)
(by <a href="https://github.com/samypr100"><code>@​samypr100</code></a> in 6cd24cbb)</p>
</li>
<li>
<p>Fix test_create_connection_open_con_addr with Python 3.13.9+ (<a href="https://redirect.github.com/MagicStack/uvloop/issues/713">#713</a>)
(by <a href="https://github.com/shadchin"><code>@​shadchin</code></a> in b93141a5 for <a href="https://redirect.github.com/MagicStack/uvloop/issues/701">#701</a>)</p>
</li>
<li>
<p>Skip flaky test_cancel_post_init on asyncio 3.13+ (<a href="https://redirect.github.com/MagicStack/uvloop/issues/714">#714</a>)</p>
</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/MagicStack/uvloop/commit/c5f7debaabe98bba70859aa0120db243775c255c"><code>c5f7deb</code></a> uvloop 0.23.0</li>
<li><a href="https://github.com/MagicStack/uvloop/commit/f7c054738fb773e37e11fd86befc12e9408c7cd9"><code>f7c0547</code></a> Add Python 3.15 to CI and fix test issues (<a href="https://redirect.github.com/MagicStack/uvloop/issues/758">#758</a>)</li>
<li><a href="https://github.com/MagicStack/uvloop/commit/e8efea407c783b0d9ad6993cfe1e3a56d1b1dc2e"><code>e8efea4</code></a> Upgrade libuv to v1.52.1 (<a href="https://redirect.github.com/MagicStack/uvloop/issues/753">#753</a>)</li>
<li><a href="https://github.com/MagicStack/uvloop/commit/3cbb09560ed1753089133a3925b130ec5e151826"><code>3cbb095</code></a> feat: support eager_start kwarg (<a href="https://redirect.github.com/MagicStack/uvloop/issues/748">#748</a>)</li>
<li><a href="https://github.com/MagicStack/uvloop/commit/0582f946aeca3a9e9af08c3abe7f812bdbc6f91d"><code>0582f94</code></a> Add thread name prefix to the default thread pool executor (<a href="https://redirect.github.com/MagicStack/uvloop/issues/636">#636</a>)</li>
<li><a href="https://github.com/MagicStack/uvloop/commit/963a5f3e141446884fb408abb012d4de1238d06b"><code>963a5f3</code></a> Support any number of flags in UVLOOP_OPT_CFLAGS (<a href="https://redirect.github.com/MagicStack/uvloop/issues/630">#630</a>)</li>
<li><a href="https://github.com/MagicStack/uvloop/commit/173e88cfcdae8edc1763dd9915087f5136b568aa"><code>173e88c</code></a> Get rid of wheel as a build dependency (<a href="https://redirect.github.com/MagicStack/uvloop/issues/696">#696</a>)</li>
<li><a href="https://github.com/MagicStack/uvloop/commit/b74c2f1c934382924d4ded8e3d68457be1d27afb"><code>b74c2f1</code></a> Update the example to work with 3.14 (<a href="https://redirect.github.com/MagicStack/uvloop/issues/710">#710</a>)</li>
<li><a href="https://github.com/MagicStack/uvloop/commit/dc680eb20c526d8babacaf4751a12f51431ea246"><code>dc680eb</code></a> Detach socket on create_connection cancellation to prevent fd double-close (#...</li>
<li><a href="https://github.com/MagicStack/uvloop/commit/6cd24cbb84f31c47a0820320705f421e7f0defe0"><code>6cd24cb</code></a> fix: explicit yield after run_in_executor as it was implicitly needed (<a href="https://redirect.github.com/MagicStack/uvloop/issues/743">#743</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/MagicStack/uvloop/compare/v0.22.1...v0.23.0">compare view</a></li>
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
<li><a href="https://github.com/carljm"><code>@​carl...

_Description has been truncated_