# /explain-system

Explore a codebase and write a verified system design document explaining WHY the system is designed the way it is.

## Instructions

### 1. Problem Discovery

Read foundation files (README, CLAUDE.md, docs/, dependency files, config files) and answer:

1. **What does it solve?** — Core problem in one sentence
2. **Who uses it?** — End users, internal teams, API consumers, other systems
3. **Why does it exist?** — What would users do without it?
4. **What's the scope?** — What it deliberately does NOT do

Present the problem statement and wait for user confirmation.

### 2. System Exploration (C4-Inspired)

Map the system at three zoom levels:

**Context Level** — actors and external systems:
- User types and access patterns
- External APIs consumed and exposed
- Other internal systems

**Container Level** — deployable units:
- Web app, workers, databases, cache, queues, CDN/storage

**Component Level** — internal structure:
- Trace 2-3 primary flows through internal components
- Major boundaries (modules, engines, contexts, packages)
- Sync vs async boundaries

**Domain Model** — read schema files:
- Core entities and relationships in plain language
- Validations, constraints, foreign keys

**Trade-offs** — for each architectural choice:
- What does this optimize for? (speed, scale, simplicity, reliability)
- What does it sacrifice?

Present the system map and wait for user confirmation.

### 3. Design Reasoning

For each major architectural choice, examine evidence for WHY it was chosen:
- Code structure and patterns
- Git history (`git log --grep`)
- Inline comments and existing ADRs (check `docs/adr/`, `docs/decisions/`)

Present each decision as: Context → Decision → Trade-offs → Consequences.

Tag confidence: VERIFIED (from code/docs), INFERRED (from patterns), UNCERTAIN (needs user input).

Wait for user confirmation.

### 4. Verification

Extract every factual claim from Phases 1-3. Verify each against source code.

Present claims table sorted: UNCERTAIN first, then INFERRED, then VERIFIED.

**Gate:** All UNCERTAIN claims must be resolved or marked "[Not confirmed from code]" before writing.

Wait for user confirmation.

### 5. Write the Document

Generate `docs/SYSTEM_DESIGN.md` (100-200 lines):

1. The Problem — what, who, alternatives, scope
2. Core Concepts — domain model in plain language
3. System Overview — C4 levels
4. Architectural Decisions — with confidence tags
5. Trade-off Map — summary table
6. Data Flows — step-by-step with file:line references
7. Constraints and Security

**Writing rules:** explain WHY not WHAT, include file:line references, no undefined jargon, tag INFERRED claims.

Present full document for review. Only write after approval.

$ARGUMENTS
