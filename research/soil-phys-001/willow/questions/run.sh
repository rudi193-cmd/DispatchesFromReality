#!/usr/bin/env bash
# Ask the source box everything, with willow's scan, then read the answers.
#
#   WILLOW=WILLOW_DIR bash run.sh HOME_DIR
#
# HOME_DIR is the folder build.sh made. Writes kernel.jsonl and bm25.jsonl
# (tens of MB, not kept in the repo) and the three .json summaries here.
set -euo pipefail
: "${WILLOW:?set WILLOW to a willow checkout}"
HOME_DIR="${1:?usage: WILLOW=DIR bash run.sh HOME_DIR}"
cd "$(dirname "$0")"
S="$WILLOW/adapters/stdlib/scan/scan.py"
python3 "$S" index --from "$HOME_DIR/pile/sources" --to "$HOME_DIR/scan-index"
python3 make_questions.py "$HOME_DIR/pile/sources" ../../DRAFT.md > questions.tsv
python3 "$S" scan --index "$HOME_DIR/scan-index" --questions questions.tsv --top 10 --rank kernel > kernel.jsonl
python3 "$S" scan --index "$HOME_DIR/scan-index" --questions questions.tsv --top 10 --rank bm25 > bm25.jsonl
WILLOW="$WILLOW" python3 analyze.py
WILLOW="$WILLOW" python3 pairs.py
