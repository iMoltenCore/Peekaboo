# Xcode Tooling Notes

Xcode tooling can automate launch, logging, and debugging flows, especially on simulators.

## Useful commands
- `xcrun simctl launch --wait-for-debugger booted <bundle-id>`
- `xcrun simctl spawn booted log stream --style compact --predicate <predicate>`
- `xcodebuild -workspace <path> -scheme <scheme> -destination <dest> test`

## Tips
- Prefer `--wait-for-debugger` for early breakpoints.
- Use `log stream` predicates to reduce noise.
- Capture the PID from `simctl launch` output for LLDB attach.
