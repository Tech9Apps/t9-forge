---
description: "Review code for correctness, security, performance, and readability. Use before committing or when the user asks for a code review of recent changes or a specific file/PR."
user-invocable: true
argument-hint: "[file|PR number]"
---

# /code-review

Review code for quality, security, performance, and readability.

## Instructions

### 1. Identify Scope

If $ARGUMENTS specifies files or a PR, review those. Otherwise, review uncommitted changes:

```bash
git diff --name-only
git diff --staged --name-only
```

### 2. Review Checklist

For each changed file, evaluate:

**Correctness**
- Does the logic do what it's supposed to?
- Are edge cases handled?
- Are there potential null/undefined/nil issues?

**Security**
- Any injection vulnerabilities (SQL, XSS, command injection)?
- Secrets or credentials in code?
- Proper input validation at system boundaries?
- Safe handling of user-provided data?

**Performance**
- Unnecessary loops or redundant operations?
- N+1 queries or unbounded data fetching?
- Missing indexes or inefficient data structures?

**Readability**
- Clear naming and intent?
- Appropriate level of abstraction?
- Any code that needs a comment to explain non-obvious logic?

**Project Conventions**
{{CODE_REVIEW_CONVENTIONS}}

<!-- Examples for conventions:
  - Error handling patterns (Result types, try/catch style, error codes)
  - Naming conventions (camelCase, snake_case, etc.)
  - File organization and module structure
  - Import ordering
-->

### 3. Present Findings

Organize findings by severity:
- **Critical** — Must fix (bugs, security issues)
- **Warning** — Should fix (performance, maintainability)
- **Suggestion** — Nice to have (style, minor improvements)

For each finding, include:
- File and line reference
- What the issue is
- Why it matters
- Suggested fix (with code if helpful)

$ARGUMENTS
