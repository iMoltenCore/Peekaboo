---
name: zmx-long-lived-shells
description: Use when a task needs a long-lived shell session, background process persistence, or re-attachable terminal output between tool calls.
compatibility: opencode
metadata:
  workflow: Identify the long-lived process -> choose attach vs run -> verify session -> detach or reattach as needed -> capture history -> kill when done
---

# ZMX Long-Lived Shells

## Overview
Use `zmx` to keep shell processes running between tool calls. Sessions can be re-attached for output, or left running in the background.

## When to Use
- You need a server or watcher to keep running between tool calls.
- You want to re-attach to a session to inspect logs.
- The task requires a long-running command but you do not want to block the current tool call.

## Quick Start

```bash
# Create or attach to a session and run a command
zmx attach dev-server bash -lc 'npm run dev'

# Detach current client (or press Ctrl+Backslash inside the session)
zmx detach

# Re-attach later
zmx attach dev-server

# Run a command in the session without attaching
zmx run dev-server bash -lc 'npm run dev'

# List sessions
zmx list

# Print scrollback
zmx history dev-server

# Kill session when finished
zmx kill dev-server
```

## Workflow
1. Pick a stable, descriptive session name (e.g., `dev-server`, `watcher`, `logs`).
2. Use `zmx attach <name> [command...]` when you need interactive output.
3. Use `zmx run <name> [command...]` to start or send a command without attaching.
4. Detach with `zmx detach` (or Ctrl+Backslash) and re-attach later if needed.
5. Capture scrollback with `zmx history <name>` if you need logs.
6. Clean up with `zmx kill <name>` when done.

## Notes and Pitfalls
- `zmx attach` creates the session if it does not exist.
- `zmx run` is ideal for background processes that should not block a tool call.
- Use `bash -lc` when you need shell features, env loading, or chained commands.
- Always stop sessions you no longer need to avoid stale processes.

## Install

```bash
brew install neurosnap/tap/zmx
```

## Scripts
- `scripts/zmx_session.py`: Thin Python wrapper for common zmx commands. Run: `python scripts/zmx_session.py attach dev-server -- bash -lc 'npm run dev'`.
- `scripts/zmx_session.js`: JS wrapper for the same operations. Run: `node scripts/zmx_session.js attach dev-server -- bash -lc 'npm run dev'`.

## Resources
- `resources/quickstart.md`
- `resources/command-reference.md`
- `resources/troubleshooting.md`
