---
summary: 'Wecode provider setup and streaming behavior in Peekaboo'
read_when:
  - 'configuring Wecode for Peekaboo agent or CLI'
  - 'debugging Wecode streaming behavior'
---

# Wecode provider

Wecode is a streaming-first provider in Tachikoma. Peekaboo aggregates the stream for non-streaming calls so existing flows keep working.

## Configure

- API key: `WECODE_API_KEY`
- Optional base URL override: `WECODE_BASE_URL` (default: `https://api.wecodemaster.com/v1`)
- Provider string: `wecode/<model>` (only `gpt-5.2`; `wecode` is an alias)

```bash
export WECODE_API_KEY="..."
export PEEKABOO_AI_PROVIDERS="wecode/wecode"
peekaboo agent "hello"
```

## Notes

- Wecode uses the OpenAI Responses streaming format over `/openai/responses`.
- Tool calls are surfaced to the agent when the provider emits them.
