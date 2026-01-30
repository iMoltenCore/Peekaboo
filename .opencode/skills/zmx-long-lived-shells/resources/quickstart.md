# ZMX Quickstart

## Install

```bash
brew install neurosnap/tap/zmx
```

## Start a long-lived process

```bash
zmx run dev-server bash -lc 'npm run dev'
```

## Attach to the running session

```bash
zmx attach dev-server
```

## Detach and keep it running

```bash
zmx detach
```

## Capture logs

```bash
zmx history dev-server
```

## Clean up

```bash
zmx kill dev-server
```
