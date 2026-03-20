# /claude-code-toolkit:init

Initialize this project using the toolkit's setup flow. This is the legacy entrypoint and remains fully supported.

## Configuration
- context: fork
- agent: init

## Instructions

Run the init agent.

$ARGUMENTS

If arguments are provided, respect requested target/scope:
- `just CLAUDE.md` or `docs only` — generate docs outputs only
- `full setup` or no scope — run complete 4-phase flow
- `hooks only` — set up hooks only (Claude target)
- `skills only` — set up skills only
- `commands only` — set up commands only
- `rules only` — set up rules outputs only
- `update` — re-evaluate and update existing configuration

Target flags:
- `target claude`
- `target cursor`
- `target both` (default)

Legacy mapping:
- `just CLAUDE.md` -> `target claude docs only`
- `full setup` with no target -> `target both full setup`

Otherwise, run full flow: Discovery, Clarification, Documentation and Rules, Template Customization.
