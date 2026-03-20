# /context-audit

Audit what's consuming your Claude Code context window and find optimization opportunities.

## Instructions

### 1. List Auto-Loaded Files

Identify all files that are always loaded into Claude Code's context:
- `CLAUDE.md` (always loaded)
- `.claude/settings.json` / `.claude/settings.local.json`
- Memory files (`.claude/memory/`, `.claude/lessons.md`)
- Parent CLAUDE.md files (home directory, parent dirs)

### 2. Measure Each File

Count lines for each file and report:

| File | Lines | Status |
|------|-------|--------|
| CLAUDE.md | ... | OK / WARNING / CRITICAL |

**Thresholds:**
- Over 100 lines → WARNING — suggest trimming or splitting
- Over 200 lines → CRITICAL — needs immediate pruning

### 3. Flag Issues

Check for:
- **Duplicate content** across files → suggest consolidation
- **Stale content** — references to deleted files, old conventions → suggest removal
- **Large knowledge bases** that could be skills instead (loaded on demand, not always)
- **Commented-out or example-heavy sections** → suggest trimming

### 4. Check Skills

- List skills with their line counts
- Flag skills over 200 lines → suggest trimming

### 5. Context Budget Report

```
Context Budget Summary
======================

Auto-loaded files:    X lines
Knowledge bases:      Y lines (always loaded)
Skills:               Z files (loaded on demand)

Recommendations:
- [specific, actionable suggestions]
```

**Common recommendations:**
- Move stable rules to skill files (loaded only when relevant)
- Archive old lessons — keep only recent, actionable ones
- Remove comments and examples from CLAUDE.md — keep it terse
- Split large files into focused, smaller ones

$ARGUMENTS
