#!/usr/bin/env python3
"""Launch a simulator app in wait-for-debugger mode."""

from __future__ import annotations

import argparse
import subprocess
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch app and wait for debugger")
    parser.add_argument("bundle_id", help="Bundle identifier to launch")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Args passed to app")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cmd = ["xcrun", "simctl", "launch", "--wait-for-debugger", "booted", args.bundle_id]
    cmd.extend(args.args)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr.strip(), file=sys.stderr)
        return result.returncode

    print(result.stdout.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
