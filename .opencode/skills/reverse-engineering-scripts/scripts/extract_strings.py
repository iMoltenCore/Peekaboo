#!/usr/bin/env python3
"""Extract ASCII strings from a binary file."""

from __future__ import annotations

import argparse
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract ASCII strings")
    parser.add_argument("--file", required=True, help="Path to binary")
    parser.add_argument("--min", type=int, default=4, help="Minimum length")
    return parser.parse_args()


def extract_strings(data: bytes, min_len: int) -> list[str]:
    current: list[str] = []
    strings: list[str] = []
    for byte in data:
        if 32 <= byte <= 126:
            current.append(chr(byte))
        else:
            if len(current) >= min_len:
                strings.append("".join(current))
            current = []
    if len(current) >= min_len:
        strings.append("".join(current))
    return strings


def main() -> int:
    args = parse_args()
    try:
        with open(args.file, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    for value in extract_strings(data, args.min):
        print(value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
