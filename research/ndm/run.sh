#!/usr/bin/env bash
# ndm: Newmark displacement methodology, tri-model research (haiku+sonnet+opus)/high
# --sessions 1 → 3 sessions total (1 per model), default
set -euo pipefail
cd "$(dirname "$0")"
SESSIONS="${1:-1}"
tito research \
  --id ndm \
  --task tasks/task.ndm.qmd.md \
  --kb kb \
  --sessions "$SESSIONS" \
  --verbose
