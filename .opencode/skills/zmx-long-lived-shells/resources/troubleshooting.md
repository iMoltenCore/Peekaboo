# ZMX Troubleshooting

## zmx not found

```bash
brew install neurosnap/tap/zmx
```

## Session seems stuck
- Detach with Ctrl+Backslash or run `zmx detach` from another terminal.
- If a session is wedged, kill it and re-create: `zmx kill <name>` then `zmx attach <name> ...`.

## Missing output
- Use `zmx history <name>` to fetch scrollback.
- If a command exits immediately, attach to confirm it is still running.

## Shell environment issues
- Use `bash -lc` to load login shell configuration and allow chained commands.
