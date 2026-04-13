# /brainstorming

Turn ideas into fully formed designs through collaborative dialogue before any implementation begins.

## Instructions

### Hard Gate

Do NOT write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it. This applies to EVERY project regardless of perceived simplicity.

**"This is too simple to need a design"** — Every project goes through this process. A todo list, a single-function utility, a config change — all of them. "Simple" projects are where unexamined assumptions cause the most wasted work. The design can be short (a few sentences for truly simple projects), but you MUST present it and get approval.

### 1. Explore Project Context

Check files, docs, and recent commits to understand the current state.

Before asking detailed questions, assess scope: if the request describes multiple independent subsystems (e.g., "build a platform with chat, file storage, billing, and analytics"), flag this immediately. Don't spend questions refining details of a project that needs to be decomposed first.

If the project is too large for a single spec, help the user decompose into sub-projects: what are the independent pieces, how do they relate, what order should they be built? Then brainstorm the first sub-project through the normal design flow.

### 2. Ask Clarifying Questions

- Ask questions **one at a time** to refine the idea
- Prefer multiple choice questions when possible
- Only one question per message
- Focus on understanding: purpose, constraints, success criteria
- If a topic needs more exploration, break it into multiple questions

### 3. Propose 2–3 Approaches

- Present different approaches with trade-offs
- Lead with your recommended option and explain why
- Be conversational — this is a dialogue, not a report

### 4. Present the Design

Once you believe you understand what's being built, present the design:

- Scale each section to its complexity: a few sentences if straightforward, up to 200–300 words if nuanced
- Ask after each section whether it looks right so far
- Cover: architecture, components, data flow, error handling, testing
- Be ready to go back and clarify if something doesn't make sense

**Design for isolation and clarity:**
- Break the system into smaller units that each have one clear purpose
- Each unit should communicate through well-defined interfaces and be testable independently
- Can someone understand what a unit does without reading its internals? If not, the boundaries need work

**Working in existing codebases:**
- Explore the current structure before proposing changes. Follow existing patterns.
- Where existing code has problems that affect the work, include targeted improvements as part of the design
- Don't propose unrelated refactoring. Stay focused on the current goal.

### 5. Write Design Doc

Save the validated design to a spec file:

```
{{SPEC_LOCATION}}/YYYY-MM-DD-<topic>-design.md
```

<!-- Examples for spec locations:
  Default: docs/specs/
  Alternative: docs/designs/
  Alternative: specs/
-->

Commit the design document to git.

### 6. Spec Self-Review

After writing the spec document, look at it with fresh eyes:

1. **Placeholder scan:** Any "TBD", "TODO", incomplete sections, or vague requirements? Fix them.
2. **Internal consistency:** Do any sections contradict each other? Does the architecture match the feature descriptions?
3. **Scope check:** Is this focused enough for a single implementation plan, or does it need decomposition?
4. **Ambiguity check:** Could any requirement be interpreted two different ways? If so, pick one and make it explicit.

Fix any issues inline. No need to re-review — just fix and move on.

### 7. User Reviews Written Spec

After the self-review, ask the user to review the written spec before proceeding:

> "Spec written and committed to `<path>`. Please review it and let me know if you want to make any changes before we start planning implementation."

Wait for the user's response. If they request changes, make them and re-run the self-review. Only proceed once the user approves.

### 8. Transition to Implementation

After the user approves the spec, suggest next steps:

> "Consider using `/writing-plans` to create a detailed implementation plan from this spec."

Do NOT start implementing directly. The design phase ends with an approved spec.

### Key Principles

- **One question at a time** — Don't overwhelm with multiple questions
- **Multiple choice preferred** — Easier to answer than open-ended when possible
- **YAGNI ruthlessly** — Remove unnecessary features from all designs
- **Explore alternatives** — Always propose 2–3 approaches before settling
- **Incremental validation** — Present design, get approval before moving on
- **Be flexible** — Go back and clarify when something doesn't make sense

### Spec Review (Subagent)

For larger specs, dispatch a spec reviewer subagent using the template in @spec-reviewer-prompt.md to verify the spec is complete, consistent, and ready for planning.
