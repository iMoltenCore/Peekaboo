#!/usr/bin/env node
'use strict';

const { spawnSync } = require('child_process');

function runZmx(args) {
  const result = spawnSync('zmx', args, { stdio: 'inherit' });
  if (result.error && result.error.code === 'ENOENT') {
    console.error('zmx not found. Install with: brew install neurosnap/tap/zmx');
    return 127;
  }
  if (result.status === null || result.status === undefined) {
    return 1;
  }
  return result.status;
}

function usage() {
  console.error('Usage: zmx_session.js <attach|run|list|history|kill|detach|version> <session?> [-- command...]');
  return 2;
}

const argv = process.argv.slice(2);
const command = argv[0];
const session = argv[1];
const rest = argv.slice(2);

if (!command) {
  process.exit(usage());
}

switch (command) {
  case 'attach':
  case 'run':
    if (!session) {
      process.exit(usage());
    }
    process.exit(runZmx([command, session, ...rest]));
    break;
  case 'list':
    process.exit(runZmx(['list']));
    break;
  case 'history':
  case 'kill':
    if (!session) {
      process.exit(usage());
    }
    process.exit(runZmx([command, session]));
    break;
  case 'detach':
  case 'version':
    process.exit(runZmx([command]));
    break;
  default:
    process.exit(usage());
}
