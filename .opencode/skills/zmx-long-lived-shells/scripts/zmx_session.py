#!/usr/bin/env python3
'''Minimal wrapper around zmx for long-lived sessions.'''

import argparse
import subprocess
import sys


def run_zmx(args):
    cmd = ['zmx'] + args
    try:
        return subprocess.call(cmd)
    except FileNotFoundError:
        print('zmx not found. Install with: brew install neurosnap/tap/zmx', file=sys.stderr)
        return 127


def parse_args():
    parser = argparse.ArgumentParser(description='Wrapper for zmx session commands.')
    subparsers = parser.add_subparsers(dest='command', required=True)

    attach = subparsers.add_parser('attach', help='Attach to a session')
    attach.add_argument('session')
    attach.add_argument('cmd', nargs=argparse.REMAINDER, help='Command to run in session')

    run = subparsers.add_parser('run', help='Run a command in session without attaching')
    run.add_argument('session')
    run.add_argument('cmd', nargs=argparse.REMAINDER, help='Command to run in session')

    subparsers.add_parser('list', help='List sessions')

    history = subparsers.add_parser('history', help='Show session scrollback')
    history.add_argument('session')

    kill = subparsers.add_parser('kill', help='Kill a session')
    kill.add_argument('session')

    subparsers.add_parser('detach', help='Detach all clients from current session')
    subparsers.add_parser('version', help='Show zmx version')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command in ('attach', 'run'):
        return run_zmx([args.command, args.session] + args.cmd)
    if args.command == 'list':
        return run_zmx(['list'])
    if args.command == 'history':
        return run_zmx(['history', args.session])
    if args.command == 'kill':
        return run_zmx(['kill', args.session])
    if args.command == 'detach':
        return run_zmx(['detach'])
    if args.command == 'version':
        return run_zmx(['version'])
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
