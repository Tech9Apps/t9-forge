# /claude-code-toolkit:setup

Initialize a repository for AI-assisted development across Claude, Cursor, or both.

## Configuration
- context: fork
- agent: init

## Instructions

Run the init agent with target-aware setup behavior.

$ARGUMENTS

If arguments are provided, respect requested target and scope.

Target flags:
- `target claude` — generate Claude outputs
- `target cursor` — generate Cursor outputs
- `target both` — generate both outputs

Scope flags:
- `full setup`
- `docs only`
- `hooks only` (Claude target)
- `skills only`
- `commands only`
- `rules only`
- `update`

Defaults:
- If no target is specified, use `target both`
- If no scope is specified, run full setup

Requirements:
- Follow 4-phase workflow: Discovery, Clarification, Documentation/Rules, Template Customization
- Run project-standards interview before writing rules
- Keep flow interactive; do not write files without explicit approval
- Use stack-derived questions (no fixed stack questionnaire)
