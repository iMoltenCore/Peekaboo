---
name: "ios-debugging-workflows"
description: "Use when debugging iOS apps or system libraries with LLDB/Xcode, especially for crash triage, runtime inspection, or breakpoint-driven investigation."
compatibility: "opencode"
metadata:
  workflow: "Identify target -> choose attach/launch -> set breakpoints -> inspect state -> capture evidence -> fall back if tools are unavailable"
---

# iOS Debugging Workflows

## Overview
Use LLDB and Xcode tooling to inspect runtime state, verify hypotheses, and capture evidence. Keep investigations reproducible and focus on minimal, targeted steps.

## When to Use
- Crashes, hangs, or unexpected control flow in iOS apps or system libraries.
- Breakpoint-driven inspection of dynamic methods and runtime state.
- Need to automate debugging steps or capture logs consistently.

## Workflow
1. Identify the target (bundle id, PID, device/simulator).
2. Choose attach vs. launch with a debugger.
3. Set breakpoints and minimal logging points.
4. Inspect state (backtraces, variables, ObjC runtime).
5. Capture evidence (logs, screenshots, exports).
6. If tools fail, switch to fallback workflows.

## Tooling Expectations
- Use Python with the `lldb` module for scripted attach, breakpoints, and state capture.
- Use Python with Xcode tooling (`xcrun`, `simctl`, `xcodebuild`) to automate launch/log flows.
- Do not add `lldb` as a dependency; it ships with LLDB.

## Fallbacks (when LLDB/Xcode tooling is blocked)
- Screenshot-based inspection for UI state and visual cues.
- Recognition to extract text or UI element info from captures.
- macOS control via scripts or automation to reproduce steps.

## Scripts
- `scripts/lldb_attach.py`: Attach to a PID and run LLDB commands. Run: `python scripts/lldb_attach.py <pid> --breakpoint objc_msgSend --command "bt"`.
- `scripts/simctl_wait_debugger.py`: Launch a simulator app in wait-for-debugger mode. Run: `python scripts/simctl_wait_debugger.py <bundle-id>`.

## Resources
- `resources/lldb-python-quickstart.md`
- `resources/xcode-tooling-notes.md`
- `resources/fallback-workflows.md`
