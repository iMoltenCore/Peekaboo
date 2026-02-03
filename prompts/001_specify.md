/speckit.specify
Add a new provider, called Wecode in peekaboo.
Wecode is similar to `OpenAIResponsesProvider` for streamText.
But wecode doesn't support generalText directly,
which should collect all responses from `streamText` instead.

### Codebase
Before modification, start a deep scan on current codebase.

### Target
CLI, called peekaboo is the main target.

### Build
You can build it in xcode or using `bunx pnpnm run build:cli`.

### Debug
Try your best to debug. You can use xcode, print, any other methods to debug it.
You can control desktop as well if these tools aren't satisfied.

### Test
For testing, you can use /tmp/key as its api key.

The target binary usually is under `Apps/CLI/.build/arm64-apple-macosx/debug`
after building.

### Repo
You can add codes in submodule with a new branch.
You shouldn't push any codes to remote.

### Verification
You must ensure wecode provider can work with `peekaboo agent "hello"`.
