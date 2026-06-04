# /t9-forge:init

Initialize this project for Claude Code. Evaluates the codebase, generates CLAUDE.md and docs, and sets up customized skills, hooks, and commands.

## Configuration
- context: fork
- agent: init

## Instructions

Run the init agent to set up this project for Claude Code.

$ARGUMENTS

If arguments are provided, respect the requested scope:
- "just CLAUDE.md" or "docs only" — only generate CLAUDE.md and docs/, skip template customization
- "full setup" or no arguments — run the complete init flow (see below)
- "hooks only" — only set up hooks
- "skills only" — only set up skills
- "commands only" — only set up commands
- "update" — re-evaluate and update existing configuration

Otherwise, run the full flow: Discovery, Clarification, companion plugins (2.5), optional IDD scaffold (2.6), Documentation Generation, Template Customization, and wrap-up.
