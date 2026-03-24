# /plan

Review a proposed change thoroughly before making any code changes. For every issue or recommendation, explain the concrete tradeoffs, give an opinionated recommendation, and ask for input before assuming a direction.

## Priority hierarchy

If running low on context or the user asks to compress: Step 0 > Test review > Opinionated recommendations > Everything else. Never skip Step 0 or the test review.

## Engineering preferences (use these to guide recommendations)

- DRY is important — flag repetition aggressively.
- Well-tested code is non-negotiable; more tests > fewer tests.
- Code should be "engineered enough" — not under-engineered (fragile, hacky) and not over-engineered (premature abstraction, unnecessary complexity).
- Handle more edge cases, not fewer; thoughtfulness > speed.
- Bias toward explicit over clever.
- Minimal diff: achieve the goal with the fewest new abstractions and files touched.
- Do not make assumptions.

## Cognitive patterns

These are not checklist items. They are instincts that experienced engineering leaders develop — the pattern recognition that separates "reviewed the code" from "caught the landmine." Apply them throughout the review.

1. **Blast radius instinct** — Every decision evaluated through "what's the worst case and how many systems/people does it affect?"
2. **Boring by default** — "Every company gets about three innovation tokens." Everything else should be proven technology (McKinley).
3. **Incremental over revolutionary** — Strangler fig, not big bang. Canary, not global rollout. Refactor, not rewrite.
4. **Systems over heroes** — Design for tired humans at 3am, not your best engineer on their best day.
5. **Reversibility preference** — Feature flags, A/B tests, incremental rollouts. Make the cost of being wrong low.
6. **Failure is information** — Blameless postmortems, error budgets, chaos engineering. Incidents are learning opportunities.
7. **Essential vs accidental complexity** — Before adding anything: "Is this solving a real problem or one we created?" (Brooks).
8. **Make the change easy, then make the easy change** — Refactor first, implement second. Never structural + behavioral changes simultaneously (Beck).
9. **DX is product quality** — Slow CI, bad local dev, painful deploys -> worse software, higher attrition.
10. **Error budgets over uptime targets** — SLO of 99.9% = 0.1% downtime *budget to spend on shipping*.

When evaluating architecture, think "boring by default." When reviewing tests, think "systems over heroes." When assessing complexity, ask Brooks's question. When a plan introduces new infrastructure, check whether it's spending an innovation token wisely.

## Diagrams

Use ASCII art diagrams liberally — for data flow, state machines, dependency graphs, processing pipelines, and decision trees. When modifying code that has ASCII diagrams in comments nearby, review whether those diagrams are still accurate. Stale diagrams are worse than no diagrams.

## Instructions

### Step 0 — Scope challenge

Before reviewing anything, answer these questions:

1. **What existing code already partially or fully solves each sub-problem?** Can we capture outputs from existing flows rather than building parallel ones?
2. **What is the minimum set of changes that achieves the stated goal?** Flag any work that could be deferred without blocking the core objective. Be ruthless about scope creep.
3. **Complexity check:** If the plan touches more than 8 files or introduces more than 2 new classes/services, treat that as a smell and challenge whether the same goal can be achieved with fewer moving parts.
4. **Completeness check:** Is the plan doing the complete version or a shortcut? With AI-assisted coding, the cost of completeness (100% test coverage, full edge case handling, complete error paths) is 10-100x cheaper than with a human team. If the plan proposes a shortcut that saves human-hours but only saves minutes with AI assistance, recommend the complete version.

If the complexity check triggers (8+ files or 2+ new classes/services), proactively recommend scope reduction — explain what's overbuilt, propose a minimal version that achieves the core goal, and ask whether to reduce or proceed as-is.

**Critical:** Once the user accepts or rejects a scope reduction recommendation, commit fully. Do not re-argue for smaller scope during later review sections. Do not silently reduce scope or skip planned components.

---

### 1. Architecture review

Evaluate:
- Overall system design and component boundaries.
- Dependency graph and coupling concerns.
- Data flow patterns and potential bottlenecks.
- State transitions, retries, idempotency, and partial failure handling.
- Race/concurrency hazards.
- Scaling characteristics and single points of failure.
- Security architecture (auth, data access, API boundaries, trust boundaries).
- Whether key flows deserve ASCII diagrams in the plan or in code comments.
- For each new codepath or integration point, describe one realistic production failure scenario and whether the plan accounts for it.

**STOP.** For each issue found in this section, ask the user individually. One issue per question. Present options, state recommendation, explain WHY. Do NOT batch multiple issues into one question. Only proceed to the next section after ALL issues in this section are resolved.

---

### 2. Code quality review

Evaluate:
- Code organization and module structure.
- DRY violations — be aggressive.
- Error handling patterns and missing edge cases (call these out explicitly).
- Technical debt hotspots.
- Areas that are over-engineered or under-engineered relative to the engineering preferences above.
- Existing ASCII diagrams in touched files — are they still accurate after this change?

**STOP.** For each issue found in this section, ask the user individually. One issue per question. Only proceed after ALL issues are resolved.

---

### 3. Test review

Evaluate:
- Test coverage gaps (unit, integration, e2e).
- Test quality and assertion strength.
- Missing edge case coverage — be thorough.
- Untested failure modes and error paths.

**STOP.** For each issue found in this section, ask the user individually. One issue per question. Only proceed after ALL issues are resolved.

---

### 4. Performance review

Evaluate:
- N+1 queries and database access patterns.
- Memory-usage concerns.
- Caching opportunities.
- Slow or high-complexity code paths.

**STOP.** For each issue found in this section, ask the user individually. One issue per question. Only proceed after ALL issues are resolved.

---

## Issue reporting format

For every specific issue (bug, smell, design concern, or risk):

1. Describe the problem concretely, with file and line references.
2. Present 2-3 options, including "do nothing" where reasonable.
3. For each option specify in one line: effort, risk, and maintenance burden.
4. Map the reasoning to a specific engineering preference (DRY, explicit > clever, minimal diff, etc.).
5. Ask for explicit user choice before proceeding.

**Numbering:** Number issues (`Issue 1`, `Issue 2`, ...) and give letters for options (`A`, `B`, `C`). Recommended option is always listed first. Labels must clearly show issue number and option letter (e.g., "1A", "1B").

**Escape hatch:** If a section has no issues, say so and move on. If an issue has an obvious fix with no real alternatives, state what you'll do and move on — don't waste a question on it. Only ask when there is a genuine decision with meaningful tradeoffs.

---

## Required outputs

### "NOT in scope" section

Every plan review MUST produce a "NOT in scope" section listing work that was considered and explicitly deferred, with a one-line rationale for each item.

### "What already exists" section

List existing code/flows that already partially solve sub-problems in this plan, and whether the plan reuses them or unnecessarily rebuilds them.

### Failure modes

For each new codepath identified in the review, list one realistic way it could fail in production (timeout, nil reference, race condition, stale data, etc.) and whether:
1. A test covers that failure
2. Error handling exists for it
3. The user would see a clear error or a silent failure

If any failure mode has no test AND no error handling AND would be silent, flag it as a **critical gap**.

### Implementation plan

After all review sections are approved, synthesize into numbered tasks:
- Each task is one clear unit of work.
- Include exact files expected to change.
- Include verification commands per task.
- Include rollback/recovery notes for risky steps.
- Max 10 tasks unless the user requests more detail.

### Completion summary

At the end of the review, display this summary:
- Step 0: Scope Challenge — (scope accepted as-is / scope reduced per recommendation)
- Architecture Review: ___ issues found
- Code Quality Review: ___ issues found
- Test Review: ___ gaps identified
- Performance Review: ___ issues found
- NOT in scope: written
- What already exists: written
- Failure modes: ___ critical gaps flagged

---

## Retrospective learning

Check the git log for this branch. If there are prior commits suggesting a previous review cycle (e.g., review-driven refactors, reverted changes), note what was changed and whether the current plan touches the same areas. Be more aggressive reviewing areas that were previously problematic.

## Unresolved decisions

If the user does not respond to a question or interrupts to move on, note which decisions were left unresolved. At the end of the review, list these as "Unresolved decisions that may bite you later" — never silently default to an option.

## Approval gate

Ask whether to proceed to `/plan-verify`.

Do not start implementation from this skill. Planning only.

$ARGUMENTS
