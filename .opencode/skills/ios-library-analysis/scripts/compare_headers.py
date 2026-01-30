#!/usr/bin/env python3
"""Compare two header files and list added or removed lines."""

from __future__ import annotations

import argparse
import difflib
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare header files")
    parser.add_argument("old", help="Old header path")
    parser.add_argument("new", help="New header path")
    return parser.parse_args()


def load_lines(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8", errors="ignore") as handle:
        return handle.readlines()


def main() -> int:
    args = parse_args()
    old_lines = load_lines(args.old)
    new_lines = load_lines(args.new)

    diff = difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile=args.old,
        tofile=args.new,
        lineterm="",
    )
    for line in diff:
        if line.startswith("+") or line.startswith("-"):
            sys.stdout.write(line)
            if not line.endswith("\n"):
                sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
