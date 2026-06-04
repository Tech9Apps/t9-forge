#!/usr/bin/env bash
# scaffold-idd.sh — apply the t9-idd scaffold from t9-forge init (Phase 2.6)
# Resolves a t9-idd checkout, then runs idd-setup.sh without clobbering CLAUDE.md.
#
# Usage: bash scaffold-idd.sh [target-directory]
# Env:   T9_IDD_ROOT — path to a local t9-idd clone (optional)

set -euo pipefail

TARGET="$(cd "${1:-.}" && pwd)"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

resolve_idd_root() {
  if [ -n "${T9_IDD_ROOT:-}" ] && [ -f "${T9_IDD_ROOT}/idd-setup.sh" ]; then
    echo "$T9_IDD_ROOT"
    return 0
  fi

  local sibling
  sibling="$(cd "$SCRIPT_DIR/../.." 2>/dev/null && pwd)/t9-idd"
  if [ -f "$sibling/idd-setup.sh" ]; then
    echo "$sibling"
    return 0
  fi

  local dir
  while IFS= read -r dir; do
    if [ -f "$dir/idd-setup.sh" ]; then
      echo "$dir"
      return 0
    fi
  done < <(find "$HOME/.claude/plugins" "$HOME/.claude/plugins/cache" -maxdepth 5 -type d -name 't9-idd' 2>/dev/null || true)

  return 1
}

IDD_ROOT=""
if IDD_ROOT="$(resolve_idd_root)"; then
  echo "Using t9-idd at: $IDD_ROOT"
else
  CACHE="${TMPDIR:-/tmp}/t9-idd-scaffold-$$"
  echo "Cloning t9-idd (shallow) into $CACHE ..."
  git clone --depth 1 https://github.com/Tech9Apps/t9-idd.git "$CACHE"
  IDD_ROOT="$CACHE"
fi

export IDD_SETUP_SKIP_CLAUDE=1
bash "$IDD_ROOT/idd-setup.sh" "$TARGET"
