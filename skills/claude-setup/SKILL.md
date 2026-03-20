# /claude-code-toolkit:claude-setup

Shortcut for setup with Claude-only outputs.

## Configuration
- context: fork
- agent: init

## Instructions

Run the init agent with `target claude`.

If `$ARGUMENTS` is present, append it after the target and preserve scope semantics from `/claude-code-toolkit:setup`.

Examples:
- `target claude full setup`
- `target claude docs only`
- `target claude update`
