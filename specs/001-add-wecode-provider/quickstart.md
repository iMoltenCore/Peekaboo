# Quickstart: Add Wecode Provider

## Goal

Validate Wecode with a simple agent prompt and confirm streaming and aggregated
text paths both work.

## Prerequisites

- macOS with required permissions for Peekaboo CLI.
- A Wecode API key available locally at `/tmp/key`.

## Steps

1. Build the CLI (`peekaboo`) from this repository.
2. Configure the Wecode provider to use the API key at `/tmp/key`.
3. Run: `peekaboo agent "hello"` and confirm output appears.
4. Verify a non-streaming text request returns a single combined response.

## Expected Result

- Streaming output appears quickly and completes without errors.
- Non-streaming output returns one combined response.
