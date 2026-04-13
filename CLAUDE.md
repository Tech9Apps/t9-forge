# claude-code-toolkit

A Claude Code plugin that initializes projects for optimal Claude Code usage.

## What This Is

This is a Claude Code plugin — not a standalone application. It provides:
- A sub agent (`agents/init.md`) that interactively evaluates codebases
- A skill (`/claude-code-toolkit:init`) as the user entry point
- Template files that get customized and copied into target projects

## Project Structure

```
.claude-plugin/plugin.json    — Plugin manifest
agents/init.md                — Main interactive agent (4-phase flow)
skills/init/SKILL.md          — Entry point skill
templates/
  skills/                     — Template skills (commit, test, code-review, pr, fix-issue)
  hooks/                      — Template hooks (lint, format, validate, pre-commit, notify)
  commands/                   — Template commands (healthcheck, logs, serve)
  docs/                       — Template doc files (architecture, api, testing)
```

## Key Conventions

- Templates use `{{PLACEHOLDER}}` syntax for values the agent fills in
- Templates include HTML comments (`<!-- -->`) with examples for common stacks
- The agent is framework/language agnostic — it discovers the stack, not assumes it
- All templates are generic; the agent customizes them per-project during Phase 4
- Documentation files should stay under 300 lines each

## Template Placeholders

Common placeholders used across templates:
- `{{LINT_COMMAND}}` — project's lint command
- `{{FORMAT_COMMAND}}` — project's format command
- `{{TEST_COMMAND}}` — project's test command (specific files)
- `{{TEST_ALL_COMMAND}}` — project's full test suite command
- `{{DEV_SERVER_COMMAND}}` — project's dev server command
- `{{BUILD_COMMAND}}` — project's build command
- `{{PROJECT_NAME}}` — project name
- `{{VERIFY_COMMAND}}` — project's full verification chain
- `{{PR_CONVENTIONS}}` — team's PR description conventions
- `{{NOTIFY_COMMAND}}` — OS-appropriate desktop notification command
- `{{SPEC_LOCATION}}` — where design specs are stored (e.g., `docs/specs/`)
- `{{PLAN_LOCATION}}` — where implementation plans are stored (e.g., `docs/plans/`)
- `{{WORKTREE_LOCATION}}` — where git worktrees are created (e.g., `.worktrees/`)

## Agent Phases

1. **Discovery** — explore codebase, find config, understand stack
2. **Clarification** — ask user targeted questions
3. **Documentation** — generate CLAUDE.md and docs/
4. **Template Customization** — fill templates, get approval, write to .claude/

## Editing Guidelines

- Keep the agent interactive — it should never auto-apply without confirmation
- Templates should be stack-agnostic with commented examples
- Don't hardcode language/framework lists — the agent learns organically
- Test changes with `claude --plugin-dir .` against sample projects
