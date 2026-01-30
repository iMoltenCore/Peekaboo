#!/usr/bin/env python3
"""Attach to a PID with LLDB and run commands."""

from __future__ import annotations

import argparse
import sys

import lldb


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Attach to a PID with LLDB")
    parser.add_argument("pid", type=int, help="Process ID to attach")
    parser.add_argument(
        "--breakpoint",
        action="append",
        default=[],
        help="Breakpoint function name (repeatable)",
    )
    parser.add_argument(
        "--command",
        action="append",
        default=[],
        help="LLDB command to run (repeatable)",
    )
    parser.add_argument("--continue", dest="do_continue", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    debugger = lldb.SBDebugger.Create()
    debugger.SetAsync(False)

    target = debugger.CreateTarget(None)
    error = lldb.SBError()
    process = target.AttachToProcessWithID(debugger.GetListener(), args.pid, error)
    if error.Fail():
        print(error.GetCString(), file=sys.stderr)
        return 1

    for name in args.breakpoint:
        target.BreakpointCreateByName(name)

    for command in args.command:
        debugger.HandleCommand(command)

    if args.do_continue:
        process.Continue()

    process.Detach()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
