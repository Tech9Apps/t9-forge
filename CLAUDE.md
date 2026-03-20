# claude-code-toolkit

A cross-platform setup plugin for Claude and Cursor.

## What This Is

This is a plugin repository (not a standalone app). It provides:
- a setup agent (`agents/init.md`) that evaluates repositories interactively
- setup entrypoint skills (`/claude-code-toolkit:setup`, `/claude-code-toolkit:init`, aliases)
- template artifacts customized into target projects

## Project Structure

```
.claude-plugin/plugin.json      — Claude plugin manifest
.cursor-plugin/plugin.json      — Cursor plugin manifest
agents/init.md                  — Main interactive setup agent
skills/                         — Entrypoint skills
templates/
  skills/                       — Generated workflow skills
  hooks/                        — Generated Claude hooks
  commands/                     — Generated operator commands
  docs/                         — Generated project docs
  agents/                       — Generated specialist agents
  cursor/                       — Cursor artifacts (AGENTS + rules)
config/rules-schema.json        — Canonical rules schema
config/targets/*.json           — Target capability mappings
tests/test_contracts.py         — Contract/regression checks
```

## Key Conventions

- Templates use `{{PLACEHOLDER}}` syntax for discovered project values.
- Templates include commented examples for common stacks where helpful.
- The setup agent is stack-agnostic and evidence-driven.
- Outputs are interactive/approval-gated; never auto-apply.
- Rules are normalized once, then rendered per target.
- Runtime-backed workflows are capability-gated by discovered tooling and target support flags.

## Template Placeholders

Core command placeholders:
- `{{BUILD_COMMAND}}`
- `{{LINT_COMMAND}}`
- `{{FORMAT_COMMAND}}`
- `{{TYPECHECK_COMMAND}}`
- `{{TYPECHECK_CHAIN}}` (empty or ` && <typecheck command>`)
- `{{TEST_COMMAND}}`
- `{{TEST_ALL_COMMAND}}`
- `{{DEV_SERVER_COMMAND}}`
- `{{VERIFY_COMMAND}}`

Context placeholders:
- `{{PROJECT_NAME}}`
- `{{STACK_SUMMARY}}`
- `{{PR_CONVENTIONS}}`
- `{{CODE_REVIEW_CONVENTIONS}}`
- `{{COMMIT_CONVENTIONS}}`
- `{{COMMIT_TRAILER}}`

Operational placeholders:
- `{{LOG_COMMAND}}`
- `{{CI_STATUS_COMMAND}}`
- `{{DEPLOY_STATUS_COMMAND}}`
- `{{ROLLBACK_STATUS_COMMAND}}`
- `{{NOTIFY_COMMAND}}`
- `{{ADDITIONAL_SERVICES}}`

Rules-render placeholders:
- `{{ARCHITECTURE_RULES}}`
- `{{API_RULES}}`
- `{{DATA_RULES}}`
- `{{TEST_LAYERS}}`
- `{{TESTING_RULES}}`
- `{{WORKFLOW_RULES}}`

## Workflow Coverage

Full workflow set expected in generated templates:

- Planning: `plan`, `plan-verify`, `plan-ceo-review`, `plan-eng-review`, `plan-design-review`
- Quality and release: `review`, `ship`, `qa`, `qa-only`, `qa-design-review`, `browse`, `setup-browser-cookies`
- Documentation and learning: `document-release`, `retro`

Runtime-backed workflows (`browse`, `qa*`, `setup-browser-cookies`, parts of `ship`) must degrade gracefully when capabilities are missing.

## Target Capability Flags

Target definitions in `config/targets/*.json` should include:

- `supportsHooks`
- `supportsBrowserAutomation`
- `supportsCookieImport`
- `supportsGitHubPR`
- `supportsRetrospectives`
- `supportsRuntimeArtifacts`

Renderers should intersect target flags with discovered runtime capabilities (`projectProfile.runtimeCapabilities`) and follow `workflowRules.fallbackPolicy`.

## Agent Phases

1. **Discovery** — inspect stack/tooling/config and confirm findings
2. **Clarification** — ask targeted, stack-derived policy questions
3. **Documentation and Rules** — generate target-specific guidance outputs
4. **Template Customization** — customize approved templates and write outputs

## Editing Guidelines

- Keep the agent interactive and explicit; do not assume.
- Preserve legacy command compatibility in `skills/init/SKILL.md`.
- Keep docs concise and non-generic.
- Maintain capability-gated outputs (skip irrelevant sections).
- If adding placeholders or target capabilities, update this file and tests.
- Validate changes with:
  - `python3 -m unittest tests.test_contracts`
