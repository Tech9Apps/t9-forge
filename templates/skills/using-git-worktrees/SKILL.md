# /using-git-worktrees

Create isolated git worktrees with smart directory selection and safety verification for parallel feature work.

## Instructions

### Overview

Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching.

**Core principle:** Systematic directory selection + safety verification = reliable isolation.

### 1. Directory Selection

Follow this priority order:

**Check existing directories:**

```bash
ls -d .worktrees 2>/dev/null     # Preferred (hidden)
ls -d worktrees 2>/dev/null      # Alternative
```

If found, use that directory. If both exist, `.worktrees/` wins.

**Check CLAUDE.md:**

```bash
grep -i "worktree.*director" CLAUDE.md 2>/dev/null
```

If preference specified, use it without asking.

**Ask the user** if no directory exists and no CLAUDE.md preference:

> No worktree directory found. Where should I create worktrees?
> 1. `.worktrees/` (project-local, hidden)
> 2. `{{WORKTREE_LOCATION}}` (custom location)

<!-- Examples for worktree locations:
  Default: .worktrees/ (project-local, hidden)
  Global: ~/.worktrees/<project-name>/
  Custom: ../worktrees/<project-name>/
-->

### 2. Safety Verification

For project-local directories (`.worktrees/` or `worktrees/`), verify the directory is gitignored before creating worktrees:

```bash
git check-ignore -q .worktrees 2>/dev/null || git check-ignore -q worktrees 2>/dev/null
```

**If NOT ignored:** Fix immediately:
1. Add appropriate line to `.gitignore`
2. Commit the change
3. Proceed with worktree creation

**Why critical:** Prevents accidentally committing worktree contents to the repository.

For locations outside the project directory, no `.gitignore` verification is needed.

### 3. Create the Worktree

```bash
# Detect project name
project=$(basename "$(git rev-parse --show-toplevel)")

# Create worktree with new branch
git worktree add "<path>/$BRANCH_NAME" -b "$BRANCH_NAME"
cd "<path>/$BRANCH_NAME"
```

### 4. Run Project Setup

Auto-detect and run the appropriate setup:

```
{{INSTALL_COMMAND}}
```

<!-- Examples for common stacks:
  Node.js: npm install (if package.json exists)
  Rust: cargo build (if Cargo.toml exists)
  Python: pip install -r requirements.txt / poetry install (if requirements.txt / pyproject.toml exists)
  Go: go mod download (if go.mod exists)
-->

### 5. Verify Clean Baseline

Run tests to ensure the worktree starts clean:

```
{{TEST_ALL_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npm test
  Python: pytest
  Rust: cargo test
  Go: go test ./...
-->

**If tests fail:** Report failures and ask the user whether to proceed or investigate.

**If tests pass:** Report ready.

### 6. Report Location

```
Worktree ready at <full-path>
Tests passing (<N> tests, 0 failures)
Ready to implement <feature-name>
```

### Quick Reference

| Situation | Action |
|-----------|--------|
| `.worktrees/` exists | Use it (verify ignored) |
| `worktrees/` exists | Use it (verify ignored) |
| Both exist | Use `.worktrees/` |
| Neither exists | Check CLAUDE.md → Ask user |
| Directory not ignored | Add to .gitignore + commit |
| Tests fail during baseline | Report failures + ask |
| No dependency file found | Skip dependency install |

### Common Mistakes

- **Skipping ignore verification:** Worktree contents get tracked, pollute git status. Always use `git check-ignore` before creating project-local worktrees.
- **Assuming directory location:** Creates inconsistency. Follow the priority: existing > CLAUDE.md > ask.
- **Proceeding with failing tests:** Can't distinguish new bugs from pre-existing issues. Report failures, get explicit permission.
- **Hardcoding setup commands:** Breaks on projects using different tools. Auto-detect from project files.

### Red Flags

**Never:**
- Create a worktree without verifying it's ignored (project-local)
- Skip baseline test verification
- Proceed with failing tests without asking
- Assume directory location when ambiguous

**Always:**
- Follow directory priority: existing > CLAUDE.md > ask
- Verify directory is ignored for project-local
- Auto-detect and run project setup
- Verify clean test baseline
