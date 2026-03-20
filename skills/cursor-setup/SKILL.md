# /claude-code-toolkit:cursor-setup

Shortcut for setup with Cursor-only outputs.

## Configuration
- context: fork
- agent: init

## Instructions

Run the init agent with `target cursor`.

If `$ARGUMENTS` is present, append it after the target and preserve scope semantics from `/claude-code-toolkit:setup`.

Examples:
- `target cursor full setup`
- `target cursor rules only`
- `target cursor docs only`
