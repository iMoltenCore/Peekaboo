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
- Optional base URL override: `WECODE_BASE_URL` (default: `https://api.wecode.zone/openai`)
- Provider string: `wecode/<model>` (example: `wecode/wecode`)

```bash
export WECODE_API_KEY="..."
export PEEKABOO_AI_PROVIDERS="wecode/wecode"
peekaboo agent "hello"
```

## Notes

- Streaming emits `text`, `tool`, `done`, and `error` events.
- Tool calls are surfaced to the agent when the provider emits them.
