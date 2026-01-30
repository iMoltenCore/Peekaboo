# ZMX Command Reference

## Sessions

- `zmx attach <name> [command...]` - Attach to a session, creating it if needed.
- `zmx run <name> [command...]` - Run a command in a session without attaching.
- `zmx detach` - Detach all clients from the current session (or press Ctrl+Backslash).
- `zmx list` - List active sessions.
- `zmx kill <name>` - Kill a session and all clients.

## Output and Diagnostics

- `zmx history <name>` - Print session scrollback to stdout.
- `zmx version` - Show version information.
- `zmx help` - Show help output.

## Common Patterns

```bash
# Start a server without attaching
zmx run dev-server bash -lc 'npm run dev'

# Attach to inspect logs
zmx attach dev-server

# Get scrollback for a quick log snapshot
zmx history dev-server
```
