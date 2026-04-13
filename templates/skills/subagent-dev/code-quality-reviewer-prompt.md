# Code Quality Reviewer Prompt Template

Use this template when dispatching a code quality reviewer subagent.

**Purpose:** Verify implementation is well-built — clean, tested, maintainable.

**Only dispatch after spec compliance review passes.**

```
Task tool (general-purpose):
  description: "Review code quality for Task N"
  prompt: |
    You are reviewing the code quality of an implementation.

    ## What Was Implemented

    [From implementer's report]

    ## Task Requirements

    Task N from [PLAN_FILE]

    ## Diff Range

    Base: [BASE_SHA]
    Head: [HEAD_SHA]

    Review the diff with: git diff [BASE_SHA]..[HEAD_SHA]

    ## What to Check

    **Code Quality:**
    - Is the code clean, readable, and maintainable?
    - Are names clear and accurate?
    - Is error handling appropriate?
    - Are there any security concerns?

    **Testing:**
    - Do tests verify real behavior (not mock behavior)?
    - Are edge cases covered?
    - Is test coverage adequate?

    **Design:**
    - Does each file have one clear responsibility?
    - Are units decomposed so they can be understood and tested independently?
    - Is the implementation following the file structure from the plan?
    - Did this change create new files that are already large, or significantly
      grow existing files?

    {{CODE_REVIEW_CONVENTIONS}}

    ## Calibration

    Focus on issues that matter: bugs, security holes, design problems,
    missing tests. Don't flag style preferences or minor naming quibbles.

    ## Output Format

    **Strengths:** [what was done well]

    **Issues:**
    - Critical: [must fix before merge]
    - Important: [should fix]
    - Minor: [nice to fix]

    **Assessment:** Approved | Changes Requested
```
