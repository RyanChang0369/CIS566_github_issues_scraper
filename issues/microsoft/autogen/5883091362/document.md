# fix(agentchat): persist sources in TextMentionTermination component config

Fixes #8282

### Summary
When using declarative component serialization (`dump_component()` / `load_component()`), `TextMentionTerminationConfig` previously only included `text: str`. Any scoped `sources` configured on the condition (e.g. `sources=["writer"]`) were lost during serialization, causing the restored termination condition to match mentions from any speaker (such as user prompts).

This PR:
1. Adds `sources: List[str] | None = None` to `TextMentionTerminationConfig`.
2. Serializes `sources` in `TextMentionTermination._to_config()`.
3. Passes `sources=config.sources` in `TextMentionTermination._from_config()`.
4. Adds a component round-trip test verifying sources filtering is preserved across serialization.