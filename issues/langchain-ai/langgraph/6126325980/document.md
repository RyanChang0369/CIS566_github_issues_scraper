# feat(cli): log in to LangSmith without an API key

## Why
`langgraph deploy` and the other control-plane commands required a LangSmith API key. The `langsmith` CLI already supports browser login (OAuth device flow) and stores tokens in `~/.langsmith/config.json`; this lets `langgraph` use the same login.

## What
- New `langgraph_cli/langsmith_auth.py`: reads the active profile (`LANGSMITH_CONFIG_FILE` / `LANGSMITH_PROFILE`), discovers OAuth endpoints (falls back to `<root>/oauth/*`), refreshes the access token, and runs the device-code login with client id `langsmith-cli`.
- `HostBackendClient` accepts an `access_token` callable and sends `Authorization: Bearer …` per request (access tokens live 5 minutes, so it refreshes as needed). `X-Api-Key` is unchanged.
- Credential order: `--api-key` / env / `.env` → profile `api_key` → profile OAuth token. The profile `workspace_id` is used as the tenant when `LANGSMITH_TENANT_ID` is unset.
- New `langgraph login` command. When no credentials exist, an interactive command now starts the login flow instead of prompting for an API key; `--no-input` / `--json` still fail fast, with a message pointing to `LANGSMITH_API_KEY` or `langgraph login`.

The control plane accepts these tokens: `host-backend` auth forwards `Authorization` to the platform `/auth`, which validates LangSmith OAuth JWTs and derives the tenant from the token claims.

## Notes
- JS CLI (langgraphjs) needs a matching change.
- Concurrent refreshes from several processes aren't locked (the Python SDK has a file lock); refresh failures tell the user to run `langgraph login`.
- Not tested end-to-end through a real deploy; the device-code request was smoke-tested against `api.smith.langchain.com`, the rest by unit tests (`tests/unit_tests/test_langsmith_auth.py`).

Made by [Open SWE](https://github.com/langchain-ai/open-swe) · [view thread](https://openswe.langchain.dev/agents/0b32ccbe-d881-4525-a435-65b288a407e7) · anthropic:claude-sonnet-5-5 (high)