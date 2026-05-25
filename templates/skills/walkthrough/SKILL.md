---
description: "Trace one feature end-to-end — from trigger to database and back — and produce a guided code walkthrough. Use when the user wants a walkthrough of a specific feature or file."
user-invocable: true
argument-hint: "<feature-name|file-path>"
---

# /walkthrough

Trace one feature end-to-end — from trigger to database and back — and produce a guided code walkthrough.

## Instructions

$ARGUMENTS is required — provide a feature name (e.g., `checkout`, `login`) or a file path as entry point.

### 1. Locate and Scope

**If a file path was given:** read it, identify its role, use as entry point.

**If a feature name was given:** search for:
- Routes/URL patterns matching the feature name
- File names matching (controllers, services, jobs, commands)
- Git log: `git log --all --oneline --grep="<feature-name>"`
- Test files mentioning the feature

Catalog all entry points (there may be multiple triggers: HTTP, background job, cron, webhook, CLI):

| Trigger | Entry Point | File:Line |
|---------|------------|-----------|

Ask the user which entry point to trace.

### 2. Trace the Call Chain

Follow the call chain from entry point through every layer. Record each step:

| Step | Layer | File:Line | Method | Data In | Data Out |
|------|-------|-----------|--------|---------|----------|

**Cap at 10 hops.** If deeper, note "continues beyond trace depth."

Also track:
- **Data transformations** — how data changes shape at each boundary (params → model → DB → response)
- **Side effects** — jobs enqueued, emails sent, webhooks fired, cache ops, events published
- **Error paths** — what goes wrong, where caught, what the user sees
- **Tests** — read tests for this feature to surface edge cases

Summarize findings and wait for user confirmation.

### 3. Write the Walkthrough

**User Journey** — 3-5 sentences from the USER's perspective (no code, no technical terms).

**Step-by-Step Code Trace** — for each step: layer, file:line, 2-3 sentence explanation (WHY, not just what), data in/out.

**Data Transformation Summary:**

| Layer | Data Shape |
|-------|-----------|
| Request | params: `{ ... }` |
| Service | model: `{ ... }` |
| Database | row: `{ ... }` |
| Response | json: `{ ... }` |

**Side Effects** — list all, grouped by type.

**Error Paths** — what goes wrong → where caught → what user sees.

Present the full walkthrough for review.

### 4. Save

Write to `docs/code-walkthrough/<feature-name>.md` (kebab-case). Warn before overwriting existing files. Only write after approval.

$ARGUMENTS
