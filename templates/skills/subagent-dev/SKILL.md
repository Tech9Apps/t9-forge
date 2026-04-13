# /subagent-dev

Execute an implementation plan by dispatching a fresh subagent per task, with two-stage review after each: spec compliance first, then code quality.

## Instructions

### Overview

Delegate implementation tasks to specialized subagents with isolated context. By precisely crafting their instructions and context, you ensure they stay focused and succeed. Subagents should never inherit your session's context or history — you construct exactly what they need. This preserves your own context for coordination work.

**Core principle:** Fresh subagent per task + two-stage review (spec then quality) = high quality, fast iteration.

### 1. The Process

Each task follows this cycle:

1. **Dispatch implementation subagent** with full task text and context (see @implementer-prompt.md)
2. **Answer any clarifying questions** before work begins
3. **Implementer completes work**, tests, commits, and self-reviews
4. **Dispatch spec compliance reviewer** to verify requirements are met (see @spec-reviewer-prompt.md)
5. If issues found, implementer fixes and spec reviewer re-checks
6. **Dispatch code quality reviewer** for design and implementation assessment (see @code-quality-reviewer-prompt.md)
7. If issues found, implementer fixes and quality reviewer re-checks
8. **Mark task complete** when both reviews pass

After all tasks complete, dispatch a final code reviewer for the entire implementation.

### 2. Review Order Matters

**Spec compliance FIRST, then code quality.** This order is critical:

- There's no point reviewing code quality if the implementation doesn't match the spec
- Spec issues often require significant rework that invalidates quality review
- Code quality review assumes the implementation is functionally correct

**Never** start code quality review before spec compliance passes.

### 3. Model Selection Strategy

Match model capability to task complexity:

| Task Type | Model Choice |
|-----------|-------------|
| Simple, isolated tasks (1–2 files, clear specs) | Faster, cheaper model |
| Multi-file integration work | Standard capability model |
| Architecture and design decisions | Most capable available model |

### 4. Handling Implementer Status

Four possible outcomes require different responses:

**DONE:** Proceed to spec compliance review.

**DONE_WITH_CONCERNS:** Implementation is complete but subagent flagged doubts.
- Address correctness or scope concerns before review
- Note observational concerns and proceed

**NEEDS_CONTEXT:** Missing information was required.
- Provide the gap and re-dispatch

**BLOCKED:** Task cannot be completed.
- Provide additional context, OR
- Escalate to a more capable model, OR
- Break the task smaller, OR
- Escalate to the user
- **Never** retry unchanged

### 5. Dispatching Subagents

**Implementer:** Use the template in @implementer-prompt.md

Key rules for the implementer prompt:
- Paste the FULL task text — don't make subagents read files
- Include scene-setting context: where this fits, dependencies, architecture
- Specify the working directory
- Use `[BRACKETS]` for runtime values you fill in at dispatch time

**Spec Compliance Reviewer:** Use the template in @spec-reviewer-prompt.md

Key rules:
- Include the FULL task requirements
- Include the implementer's report of what they claim they built
- The reviewer MUST verify by reading code, not trusting the report

**Code Quality Reviewer:** Use the template in @code-quality-reviewer-prompt.md

Key rules:
- Only dispatch AFTER spec compliance passes
- Include commit SHAs for the diff range
- Additional checks: file responsibility, decomposition, plan adherence

### 6. Critical Rules

**Never:**
- Skip either review stage
- Ignore open issues from reviewers
- Proceed with unfixed problems
- Start code quality review before spec compliance passes
- Allow implementers to guess when they should ask questions

**Always:**
- Answer subagent questions completely before they proceed
- Re-review after any fixes
- Use fresh subagents (don't reuse session context)
- Dispatch final code review after all tasks complete

### When to Use

- You have an implementation plan with multiple tasks
- Tasks are mostly independent
- You want fast iteration with quality gates

If you don't have a plan yet, consider using `/writing-plans` to create one first.
