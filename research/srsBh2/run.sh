#!/usr/bin/env bash
# srsBh2: GMM weight calibration, 2-slot structured prompt, haiku/high, 5 sessions
# Same task as srsB, new ID, haiku model, to test per-slot execute_workflow.
# Run from the server in ~/github/tools/ruflo-tito/tests/real/srsBh2/
set -Eeuo pipefail
cd "$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

TITO_CLAUDE_MODEL=haiku tito research \
  --id srsBh2 \
  --task tasks/task.srs.md \
  --kb kb \
  --sessions 5 \
  --agents 5
