# LLDB Python Quickstart

Use the `lldb` module to control debugger sessions from Python. This lets you attach, set breakpoints, and run commands without manual LLDB sessions.

## Minimal example
```python
import lldb

debugger = lldb.SBDebugger.Create()
debugger.SetAsync(False)

target = debugger.CreateTarget(None)
error = lldb.SBError()
process = target.AttachToProcessWithID(debugger.GetListener(), 12345, error)
if error.Fail():
    raise RuntimeError(error.GetCString())

bp = target.BreakpointCreateByName("objc_msgSend")
debugger.HandleCommand("bt")
process.Detach()
```

## Notes
- Use `debugger.HandleCommand` for one-off LLDB commands.
- Prefer named breakpoints when symbols are available.
- Capture evidence (backtrace, register state) before detaching.
