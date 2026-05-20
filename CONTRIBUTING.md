# Contributing to t9-forge

t9-forge is a plugin for AI Coding Assistants (e.g. Claude Code) maintained by Tech9. Contributions from Tech9 team members are welcome.

## Before you start

Open a GitHub issue (or post in `#t9-forge` on Slack) describing what you want to change. This lets us align on scope before you write code — especially important for new templates or agent behavior, where there's often a question of whether something belongs in the toolkit at all.

## Local development for Claude Code

Clone the repo and point Claude Code at it:

```
claude --plugin-dir /path/to/t9-forge
```

Then run `/t9-forge:init` in a test project to exercise your change end-to-end. Test against more than one project type if you're touching the agent or shared templates.

## Template authoring

When editing files under `templates/`:

- Use `{{PLACEHOLDER}}` syntax for values the init agent fills in
- Include HTML comments (`<!-- -->`) with examples for common stacks (Node, Python, Go, etc.)
- Keep templates language and framework agnostic — the agent discovers the stack, templates don't assume it
- Documentation files (CLAUDE.md, docs/) should stay under 300 lines

## Submitting changes

Open a PR against `main`. Keep PRs focused — one template or one agent change per PR is easier to review.

## Questions

Ping `#t9-forge` on Slack — design questions, template ideas, or anything else.
