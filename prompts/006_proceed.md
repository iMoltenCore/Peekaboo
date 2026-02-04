/speckit.implement
Current work can run with following command.
`PEEKABOO_NO_REMOTE=1 WECODE_API_KEY="$(cat /tmp/key)" PEEKABOO_AI_PROVIDERS="wecode/gpt-5.2" Apps/CLI/.build/arm64-apple-macosx/debug/peekaboo agent "hello"`
But, I don't want to set `PEEKABOO_NO_REMOTE=1`. Try your best to fix this
issue. You can use xcode, lldb, even print to trace and debug.
You should consider why it is failed at first. And find out the callflow issues.
