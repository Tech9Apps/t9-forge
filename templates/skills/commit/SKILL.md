# /commit

Create a well-structured commit for the current changes.

## Instructions

Follow this workflow to create a commit:

### 1. Review Changes

Run `git status` and `git diff --staged` to understand what's being committed. If nothing is staged, run `git diff` to see unstaged changes and ask the user what to stage.

### 2. Pre-commit Checks

Before committing, run the project's checks on changed files:

```
{{LINT_COMMAND}}
{{FORMAT_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npx eslint --fix . && npx prettier --write .
  Python: ruff check --fix . && ruff format .
  Rust: cargo clippy && cargo fmt
  Go: golangci-lint run && gofmt -w .
-->

If checks fail, fix the issues and re-stage before proceeding.

### 3. Draft Commit Message

Write a commit message following conventional commit format:

```
<type>(<scope>): <short summary>

<body — explain why, not what>
```

Types: feat, fix, refactor, test, docs, chore, ci, perf, style, build

{{COMMIT_CONVENTIONS}}

<!-- Examples for conventions:
  - Use imperative mood ("add feature" not "added feature")
  - Keep subject line under 72 characters
  - Reference issue numbers when applicable
-->

{{COMMIT_TRAILER}}

<!-- Examples for trailer conventions:
  - Leave blank to use Claude Code's default behavior
  - "Always include 'Signed-off-by: Name <email>'" for DCO projects
  - Custom trailer requirements per your team's conventions
-->

### 4. Confirm with User

Present the commit message to the user and ask for approval before committing. Show:
- Files that will be committed
- The proposed commit message

Only commit after the user confirms.

### 5. Create Commit

Stage the approved files and create the commit. Do not push unless the user asks.
