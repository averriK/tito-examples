#!/usr/bin/env bash
# srsB2: GMM weight calibration, 2-slot structured prompt, sonnet/max, 3 sessions
# Same task as srsB, new ID to test per-slot execute_workflow implementation.
# Run from the server in ~/github/tools/ruflo-tito/tests/real/srsB2/
set -Eeuo pipefail
cd "$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

tito research \
  --id srsB2 \
  --task tasks/task.srs.md \
  --kb kb \
  --sessions 3 \
  --agents 3
