#!/usr/bin/env python3
"""Search Apple OSS sources for symbol names."""

from __future__ import annotations

import argparse
import os
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search OSS sources for symbols")
    parser.add_argument("root", help="Path to apple-oss-distributions checkout")
    parser.add_argument("symbol", help="Symbol or identifier to search for")
    parser.add_argument(
        "--ext",
        action="append",
        default=[".c", ".h", ".m", ".mm", ".cpp"],
        help="File extension to include (repeatable)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not os.path.isdir(args.root):
        print(f"Root not found: {args.root}", file=sys.stderr)
        return 1

    matches = 0
    for base, _, files in os.walk(args.root):
        for name in files:
            if not any(name.endswith(ext) for ext in args.ext):
                continue
            path = os.path.join(base, name)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as handle:
                    for line_num, line in enumerate(handle, start=1):
                        if args.symbol in line:
                            print(f"{path}:{line_num}: {line.strip()}")
                            matches += 1
            except OSError:
                continue

    if matches == 0:
        print("No matches found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
