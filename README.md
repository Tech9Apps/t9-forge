# claude-code-toolkit

A Claude Code plugin that interactively initializes projects for Claude Code. It evaluates your codebase, generates a CLAUDE.md file, creates focused documentation, and provides customized skills, hooks, and commands tailored to your project's stack.

## Installation

### As a project plugin

Add to your project's `.claude/plugins.json`:

```json
{
  "plugins": [
    {
      "path": "/path/to/claude-code-toolkit"
    }
  ]
}
```

### For development/testing

```bash
claude --plugin-dir /path/to/claude-code-toolkit
```

## Usage

Run the init skill in any project:

```
/claude-code-toolkit:init
```

### Scoped runs

You can pass arguments to limit the scope:

```
/claude-code-toolkit:init just CLAUDE.md
/claude-code-toolkit:init full setup
/claude-code-toolkit:init hooks only
/claude-code-toolkit:init skills only
/claude-code-toolkit:init commands only
/claude-code-toolkit:init update
```

## What It Does

The init agent runs an interactive flow across five phases:

### Phase 1 — Discovery

The agent explores your codebase to understand:
- Languages, frameworks, and tooling (from config files)
- Project structure and entry points
- Build, test, lint, and format commands
- Dev server configuration
- Existing Claude Code or AI tool configuration
- Git conventions

### Phase 2 — Clarification

The agent asks targeted questions based on what it discovered:
- Project purpose and domain
- Architecture decisions not obvious from code
- Your preferences and conventions

It never assumes — it asks first.

### Phase 2.5 — Companion Plugin Evaluation

The agent evaluates whether your project would benefit from [superpowers](https://github.com/obra/superpowers) — an external Claude Code plugin that adds workflow-discipline skills (brainstorming, TDD, systematic debugging, plan writing, subagent-driven development, git worktrees, verification gates).

If it fits your project, the agent recommends installation and shows you the exact `/plugin` command. Superpowers is **not** bundled into this toolkit — it's maintained upstream and installed as its own plugin.

### Phase 3 — Documentation Generation

Generates or updates:
- **CLAUDE.md** (under 300 lines) — build commands, architecture overview, conventions
- **docs/** files (each under 300 lines) — focused documentation on architecture, API conventions, testing, etc.

All documentation uses `@`-references for cross-linking. Only files with real content are created.

### Phase 4 — Template Customization

Copies and customizes templates into your `.claude/` directory:

**Skills:**
- `/commit` — Guided conventional commit workflow
- `/test` — Run relevant tests based on changes
- `/code-review` — Code quality and security review

**Hooks:**
- Lint on edit — auto-lint after file changes
- Test on edit — auto-run related tests after file changes
- Format on edit — auto-format after file changes
- Validate bash — warn before destructive commands

**Commands:**
- `/healthcheck` — Project health dashboard
- `/logs` — View recent logs
- `/serve` — Start dev server(s)

Each template is customized with your project's actual commands and conventions. The agent presents each one for your approval before writing.

## Design Principles

- **Interactive, not automatic** — the agent always asks before writing
- **Stack agnostic** — works with any language/framework by discovering the stack organically
- **Concise documentation** — CLAUDE.md and docs stay under 300 lines each
- **No stubs** — only creates files with real content
- **Customized, not generic** — every command and convention is specific to your project

## Contributing

1. Templates use `{{PLACEHOLDER}}` syntax for values filled in by the agent
2. Include HTML comments with examples for common stacks
3. Keep templates language/framework agnostic
4. Test with `claude --plugin-dir .` against diverse projects
