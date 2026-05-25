---
description: "Initialize this project for Claude Code: evaluate the codebase, generate CLAUDE.md and docs, and set up customized skills, hooks, and commands. Use when starting a new project or refreshing Claude Code configuration."
user-invocable: true
argument-hint: "[full setup|just CLAUDE.md|hooks only|skills only|commands only|update]"
context: fork
agent: init
---

# /t9-forge:init

Initialize this project for Claude Code. Evaluates the codebase, generates CLAUDE.md and docs, and sets up customized skills, hooks, and commands.

## Instructions

Run the init agent to set up this project for Claude Code.

$ARGUMENTS

If arguments are provided, respect the requested scope:
- "just CLAUDE.md" or "docs only" — only generate CLAUDE.md and docs/, skip template customization
- "full setup" or no arguments — run the complete 4-phase flow
- "hooks only" — only set up hooks
- "skills only" — only set up skills
- "commands only" — only set up commands
- "update" — re-evaluate and update existing configuration

Otherwise, run the full 4-phase flow: Discovery, Clarification, Documentation Generation, and Template Customization.
