# /pr

Create a pull request for the current branch.

## Instructions

### 1. Review Changes

Run `git log --oneline main..HEAD` (or equivalent base branch) to understand all commits. Run `git diff main...HEAD --stat` for a file summary.

### 2. Pre-PR Checks

Run the project's verification chain:

{{VERIFY_COMMAND}}

<!-- Examples:
  Node/TypeScript: npm run typecheck && npm run lint && npm test
  Python: ruff check . && mypy . && pytest
  Rust: cargo clippy && cargo test
  Go: golangci-lint run && go test ./...
-->

Fix any failures before proceeding.

### 3. Draft PR Description

Write a clear PR description:

- **Title**: concise summary of the change
- **What**: what changed and why
- **How**: implementation approach (if non-obvious)
- **Testing**: how the changes were verified
- **Related issues**: link any relevant issues with "Fixes #N" or "Relates to #N"

{{PR_CONVENTIONS}}

<!-- Examples for conventions:
  - Include screenshots for UI changes
  - Tag specific reviewers for specific areas
  - Use PR templates if available
-->

### 4. Confirm with User

Present the PR title and description for approval. Show:
- The list of commits included
- The proposed title and description
- The target branch

### 5. Create PR

After approval, create the PR:

```
gh pr create --title "<title>" --body "<description>"
```

Present the PR URL to the user.
