# /fix-issue

Analyze and fix the GitHub issue: $ARGUMENTS.

## Instructions

### 1. Understand the Issue

Use `gh issue view $ARGUMENTS` to read the issue details. Understand:
- What the reported problem is
- Steps to reproduce (if provided)
- Expected vs actual behavior

### 2. Find Relevant Code

Search the codebase for files related to the issue. Use Grep and Glob to locate:
- Code mentioned in the issue
- Related components, tests, and configuration

### 3. Implement the Fix

Make the necessary code changes. Follow existing patterns and conventions.

### 4. Verify

Run the project's verification checks on changed files:

{{VERIFY_COMMAND}}

<!-- Examples:
  Node/TypeScript: npm run typecheck && npm test
  Python: mypy . && pytest
  Rust: cargo check && cargo test
  Go: go vet ./... && go test ./...
-->

If tests don't exist for the affected code, write them.

### 5. Commit and PR

Stage changes and create a commit following conventional commit format:

```
fix(<scope>): <short summary>

Fixes #$ARGUMENTS
```

Then create a pull request:

```
gh pr create --title "<title>" --body "<description referencing the issue>"
```

Present the PR URL to the user.
