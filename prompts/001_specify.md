/speckit.specify
Add a new provider, called Wecode in peekaboo.
Wecode is similar to `OpenAIResponsesProvider` for streamText.
But wecode doesn't support generalText directly,
which should collect all responses from `streamText` instead.

Wecode's endpoint is https://api.wecode.zone/openai.
