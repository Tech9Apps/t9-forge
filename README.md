# t9-forge

A Claude Code plugin that interactively initializes projects for Claude Code. It evaluates your codebase, generates a CLAUDE.md file, creates focused documentation, and provides customized skills, hooks, and commands tailored to your project's stack.

## Installation

Add the Tech9 marketplace, then install one or both plugins:

```
/plugin marketplace add Tech9Apps/t9-forge
/plugin install t9-forge@tech9-claude
/plugin install t9-idd@tech9-claude
```

The `tech9-claude` marketplace also ships [t9-idd](https://github.com/Tech9Apps/t9-idd) for Intent-Driven Development. During `/t9-forge:init` you can scaffold IDD in-repo, or install `t9-idd` and run `/t9-idd:init` afterward.

### For development/testing

```bash
claude --plugin-dir /path/to/t9-forge
```

## Usage

Run the init skill in any project:

```
/t9-forge:init
```

### Scoped runs

You can pass arguments to limit the scope:

```
/t9-forge:init just CLAUDE.md
/t9-forge:init full setup
/t9-forge:init hooks only
/t9-forge:init skills only
/t9-forge:init commands only
/t9-forge:init update
```

## What It Does

The init agent runs an interactive flow: **1 → 2 → 2.5 → 2.6 (optional IDD) → 3 → 4 → 8**:

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

During clarification, the agent also asks whether you want **Intent-Driven Development (IDD)**. If you choose to scaffold it, Phase 2.6 runs `scripts/scaffold-idd.sh`, which applies the [t9-idd](https://github.com/Tech9Apps/t9-idd) layout (`.idd/`, `prompts/`, IDD commands) without overwriting your `CLAUDE.md`. Tier files still require `/idd-bootstrap` afterward.

### Phase 2.5 — Companion Plugin Evaluation

The agent evaluates whether your project would benefit from [superpowers](https://github.com/obra/superpowers) — an external Claude Code plugin that adds workflow-discipline skills (brainstorming, TDD, systematic debugging, plan writing, subagent-driven development, git worktrees, verification gates).

If it fits your project, the agent recommends installation and shows you the exact `/plugin` command. Superpowers is **not** bundled into this toolkit — it's maintained upstream and installed as its own plugin.

### Phase 2.6 — IDD scaffold (optional)

If you opted in during clarification, the agent runs `scripts/scaffold-idd.sh` to install [t9-idd](https://github.com/Tech9Apps/t9-idd) assets (`.idd/`, `prompts/active|shipped/`, IDD commands) without overwriting an existing `CLAUDE.md`. Platform tier files still need `/idd-bootstrap` afterward; monorepo apps use `scaffold-app.sh` per project.

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

### Phase 8 — Wrap-up

Summarizes what was created, IDD/t9-idd next steps if applicable, and superpowers install reminder.

## Design Principles

- **Interactive, not automatic** — the agent always asks before writing
- **Stack agnostic** — works with any language/framework by discovering the stack organically
- **Concise documentation** — CLAUDE.md and docs stay under 300 lines each
- **No stubs** — only creates files with real content
- **Customized, not generic** — every command and convention is specific to your project

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
