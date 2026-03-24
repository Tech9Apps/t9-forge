# claude-code-toolkit

A cross-platform setup toolkit for Claude and Cursor. It evaluates your repository, asks stack-relevant standards questions, and generates consistent project artifacts (rules, docs, skills, hooks, commands, agents) tailored to your stack.

## Installation

### As a Claude project plugin

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

### For local development/testing

```bash
claude --plugin-dir /path/to/claude-code-toolkit
```

## Usage

Primary entrypoints:

```text
/claude-code-toolkit:setup
/claude-code-toolkit:init
```

Alias entrypoints:

```text
/claude-code-toolkit:claude-setup
/claude-code-toolkit:cursor-setup
/claude-code-toolkit:project-setup
```

## Scoped Runs

`/claude-code-toolkit:init` remains fully supported with legacy scopes:

```text
/claude-code-toolkit:init just CLAUDE.md
/claude-code-toolkit:init full setup
/claude-code-toolkit:init hooks only
/claude-code-toolkit:init skills only
/claude-code-toolkit:init commands only
/claude-code-toolkit:init docs only
/claude-code-toolkit:init rules only
/claude-code-toolkit:init update
```

Target-aware examples:

```text
/claude-code-toolkit:setup target cursor rules only
/claude-code-toolkit:init target claude full setup
/claude-code-toolkit:init target both update
```

Notes:
- `just CLAUDE.md` maps to `target claude docs only`
- if no target is provided, `target both` is used

## What It Does

The init agent runs a 4-phase interactive flow:

### Phase 1 — Discovery

The agent explores the repository to identify:
- languages/frameworks/tooling from config files
- project structure and entry points
- build/test/lint/format/typecheck commands
- dev server, CI/CD, and deployment clues
- existing AI tool configuration
- available testing layers (unit/integration/e2e)

### Phase 2 — Clarification

The agent asks targeted questions based on discovery:
- project purpose and domain constraints
- architecture/runtime/API/data contract preferences
- testing policy and verification requirements
- workflow and review strictness

It does not use fixed stack questionnaires; questions are derived from the detected stack.

### Phase 3 — Documentation and Rules

Generates or updates:
- **CLAUDE.md** (Claude target)
- **AGENTS.md** + `.cursor/rules/*.mdc` (Cursor target)
- **docs/** files (when relevant, each focused and concise)

For `target both`, one canonical rules model is rendered into both formats.

### Phase 4 — Template Customization

Customizes templates with project-specific commands and conventions, then writes only approved outputs.

**Skills:**
- `/commit`, `/test`, `/verify`, `/code-review`, `/pr`, `/fix-issue`
- `/plan`, `/plan-verify`, `/test-generate`

**Hooks (Claude target):**
- format-on-edit
- lint-on-edit
- validate-bash
- pre-commit
- notify

**Commands:**
- `/healthcheck`, `/logs`, `/serve`
- `/deploy-status`, `/rollback-status`

**Agents (Claude target):**
- security-review

## Target Outputs

For Claude target:
- `CLAUDE.md`
- `.claude/skills/*`
- `.claude/hooks/*`
- `.claude/commands/*`
- `.claude/agents/*`
- `docs/*` when relevant

For Cursor target:
- `AGENTS.md`
- `.cursor/rules/*.mdc`
- `docs/*` when relevant

Note: Cursor target currently focuses on rules/guidance outputs, not `.claude/*` runtime artifacts.

## Full-Parity Workflow Inventory

Generated workflow coverage now includes:

- Planning: `/plan`, `/plan-verify`, `/plan-ceo-review`, `/plan-design-review`
- Quality and release: `/ship`, `/qa`, `/qa-design-review`
- Documentation and learning: `/document-release`, `/retro`

## Runtime Dependency Matrix

Portable workflows (prompt-only) are available across targets:

- `/plan`
- `/plan-verify`
- `/plan-ceo-review`
- `/plan-design-review`
- `/document-release`
- `/retro`

Runtime-backed workflows require discovered capabilities:

- Browser-backed: `/qa`, `/qa-design-review`
  - requires browser automation backend
- Release automation: `/ship`
  - can run local-only; PR automation requires GitHub tooling
  - supports `--dry-run` for assessment-only mode

## Target Capability Mapping

`config/targets/claude.json` and `config/targets/cursor.json` define support flags:

- `supportsHooks`
- `supportsBrowserAutomation`
- `supportsGitHubPR`
- `supportsRetrospectives`
- `supportsRuntimeArtifacts`

The setup agent intersects target support with discovered runtime capabilities before generating behavior.

## Fallback Policy

When required capabilities are missing, generated guidance uses one of:

- `skip` — omit unsupported runtime behavior
- `report-only` — run analysis/audit without execution fixes
- `ask-user` — prompt before downgrading behavior

Default recommendation is `report-only` for browser/QA workflows when runtime is unavailable.

## Design Principles

- **Interactive, not automatic** — always ask before writing
- **Stack-aware and dynamic** — derive questions from repository evidence
- **Concise, high-signal outputs** — skip irrelevant sections
- **No generic stubs** — create files only when they provide value
- **Deterministic safety behavior** — hooks are fast and mandatory-only

## Testing This Plugin

Run contract checks:

```bash
python3 -m unittest tests.test_contracts
```

## Contributing

1. Templates use `{{PLACEHOLDER}}` syntax for discovered project values
2. Keep templates stack-agnostic with concrete examples in comments
3. Preserve interactive approval checkpoints in agent instructions
4. Validate changes with contract tests and local plugin runs
# claude-code-toolkit

Cross-platform repository setup toolkit for Claude and Cursor.

It inspects the active repository, asks project-specific standards questions, and generates consistent project artifacts (rules, docs, skills, hooks, commands, agents) for team-wide usage.

## Installation

### As a project plugin

Add to `.claude/plugins.json`:

```json
{
  "plugins": [
    {
      "path": "/path/to/claude-code-toolkit"
    }
  ]
}
```

### Local development

```bash
claude --plugin-dir /path/to/claude-code-toolkit
```

## Skills

Setup entrypoints:
- `/claude-code-toolkit:setup` (canonical)
- `/claude-code-toolkit:init` (legacy, still supported)
- `/claude-code-toolkit:claude-setup` (alias)
- `/claude-code-toolkit:cursor-setup` (alias)
- `/claude-code-toolkit:project-setup` (alias)

## Setup Arguments

Targets:
- `target claude`
- `target cursor`
- `target both` (default)

Scopes:
- `full setup` (default)
- `docs only`
- `hooks only`
- `skills only`
- `commands only`
- `rules only`
- `update`

Examples:
```text
/claude-code-toolkit:setup
/claude-code-toolkit:setup target cursor rules only
/claude-code-toolkit:claude-setup docs only
/claude-code-toolkit:init target both update
```

## Legacy `:init` Scoped Runs

`/claude-code-toolkit:init` remains fully supported. Equivalent scoped examples:

```text
/claude-code-toolkit:init full setup
/claude-code-toolkit:init hooks only
/claude-code-toolkit:init skills only
/claude-code-toolkit:init commands only
/claude-code-toolkit:init docs only
/claude-code-toolkit:init rules only
/claude-code-toolkit:init update
/claude-code-toolkit:init target claude full setup
/claude-code-toolkit:init target cursor rules only
/claude-code-toolkit:init just CLAUDE.md
```

Notes:
- `just CLAUDE.md` maps to `target claude docs only`.
- If no target is provided, `target both` is used.

## What Gets Generated

For Claude target:
- `CLAUDE.md`
- `.claude/skills/*`
- `.claude/hooks/*`
- `.claude/commands/*`
- `.claude/agents/*`
- `docs/*` when relevant

For Cursor target:
- `AGENTS.md`
- `.cursor/rules/*.mdc`
- `docs/*` when relevant
- Note: Cursor target focuses on rules and guidance outputs. Claude-specific runtime artifacts (`.claude/hooks`, `.claude/commands`, `.claude/agents`) are not generated for Cursor.

For both target:
- same standards are rendered into both formats.

## Workflow

1. Discovery
2. Clarification (including project standards interview)
3. Documentation and rules rendering
4. Template customization and approval

The agent never writes files without approval.

## SDLC Additions

Generated skill set includes:
- `/plan`
- `/plan-verify` (mandatory planning quality gate)
- `/test-generate`

Generated command set includes:
- `/healthcheck`
- `/logs`
- `/serve`
- `/deploy-status`
- `/rollback-status`

## Testing This Plugin

Run contract checks:

```bash
python3 -m unittest tests.test_contracts
```

## Design Constraints

- DRY and explicit over clever
- capability-gated output (skip irrelevant sections)
- no generic stubs
- deterministic safety hooks only
