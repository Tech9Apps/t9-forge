# /onboard

Systematically explore and document an unfamiliar codebase. Zoom in first, then zoom out, recognize patterns, learn history, externalize understanding.

## Instructions

### 1. Zoom In — Trace One Flow

Pick an entry point and trace ONE request/flow end-to-end. Build your first mental model from concrete code, not abstractions.

**Find the entry point:**
- Check README for getting-started hints
- Check `git log --oneline -20` — recent changes = active code
- Find the "front door": routes file, main entry, or primary controller

**Trace the call chain** through 5-8 files (controller → service → model → DB). At each file, note:
- Naming conventions (snake_case? camelCase? prefix/suffix patterns?)
- File organization (by feature? by type? by layer?)
- How dependencies are referenced (imports, injection, includes)

**Validate with tests** — read tests for this flow. Descriptions reveal edge cases.

**Present:** entry point, files traversed, step-by-step description, conventions spotted, open questions.

Wait for user confirmation before proceeding.

### 2. Zoom Out — Map the Architecture

**Stack detection:** Read dependency files to identify framework, database, background jobs, cache, external services.

**Architectural shape:**
- Monolith with conceptual seams
- Modular monolith (engines, packages, components)
- Microservices (multiple services, API gateways)
- Monorepo (apps, packages, workspace config)

**Data model:** Read schema source of truth. Identify 3-5 core entities and their relationships (validations, constraints, foreign keys).

**C4-depth mapping (when `--deep` or full system doc is requested):**

Map at three zoom levels:
- **Context** — actors, user types, external APIs consumed/exposed, other internal systems
- **Container** — web app, workers, databases, cache, queues, CDN/storage
- **Component** — trace 2-3 primary flows through internal components, sync vs async boundaries

**Trade-off analysis** — for each major architectural choice:
- What does this optimize for? (speed, scale, simplicity, reliability)
- What does it sacrifice?
- Tag confidence: VERIFIED (from code/docs), INFERRED (from patterns), UNCERTAIN (needs user input)

Check for ADRs in `docs/adr/` or `docs/decisions/`.

**Present:** stack + versions, architectural shape, core entities, directory map, external integrations. If deep mode, include C4 map and trade-off analysis.

Wait for user confirmation before proceeding.

### 3. Learn from History

**Hotspot analysis:**
```bash
git log --since="6 months ago" --name-only --pretty=format: | sort | uniq -c | sort -rn | head -20
```

High churn + high line count = abstraction under strain.

**Contributors:**
```bash
git shortlog -sn --since="6 months ago"
```

**Present:** hotspot table, change patterns, key contributors.

Wait for user confirmation before proceeding.

### 4. Document

Generate lightweight docs that help both humans and AI agents:

- `docs/ARCHITECTURE.md` (40-80 lines) — system overview, stack, core entities, directory map, key patterns
- `docs/CODEBASE_MAP.md` (30-60 lines) — module inventory, external integrations, testing landscape
- `docs/SYSTEM_DESIGN.md` (100-200 lines, deep mode only) — problem statement, C4 levels, architectural decisions with confidence tags, trade-off map, data flows with file:line references
- Proposed CLAUDE.md updates (as a diff — do NOT auto-write)

**Writing rules for SYSTEM_DESIGN.md:** explain WHY not WHAT, include file:line references, no undefined jargon, tag INFERRED claims. Gate: all UNCERTAIN claims must be resolved or marked before writing.

Present all docs for review. Only write files after approval.

### 5. Suggest Opportunities

Based on everything discovered, suggest up to 5 project-specific skills or agents. For each: evidence found, what it would do, priority.

Never auto-create — present proposals only.

$ARGUMENTS
