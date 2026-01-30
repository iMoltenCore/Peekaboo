#!/usr/bin/env bun
// Extract ASCII strings from a binary file.

import { readFileSync } from "node:fs";

function parseArgs() {
  const args = process.argv.slice(2);
  const fileIndex = args.indexOf("--file");
  const minIndex = args.indexOf("--min");
  const file = fileIndex >= 0 ? args[fileIndex + 1] : undefined;
  const min = minIndex >= 0 ? Number(args[minIndex + 1]) : 4;
  if (!file) {
    throw new Error("Missing --file <path>");
  }
  return { file, min };
}

function extractStrings(data: Uint8Array, minLen: number): string[] {
  const strings: string[] = [];
  let current: number[] = [];
  for (const byte of data) {
    if (byte >= 32 && byte <= 126) {
      current.push(byte);
    } else {
      if (current.length >= minLen) {
        strings.push(String.fromCharCode(...current));
      }
      current = [];
    }
  }
  if (current.length >= minLen) {
    strings.push(String.fromCharCode(...current));
  }
  return strings;
}

try {
  const { file, min } = parseArgs();
  const data = readFileSync(file);
  for (const value of extractStrings(data, min)) {
    console.log(value);
  }
} catch (error) {
  console.error((error as Error).message);
  process.exit(1);
}
