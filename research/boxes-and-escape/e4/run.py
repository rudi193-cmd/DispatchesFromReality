#!/usr/bin/env python3
"""E4-CONTAINER harness.

The model is an injected seam: pass any callable (prompt: str) -> str. The harness
does not care where the answer came from — same inversion Nestor uses for storage and
matching, for the same reason.

    python3 run.py --dry-run                          # emit all 48 stimuli
    python3 run.py --stimuli json_strict pig agentive # print one cell's prompt
    python3 run.py --api --reps 30                    # full run; needs ANTHROPIC_API_KEY
    python3 run.py --score-file responses.json        # score externally-collected runs
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import score as scoring  # noqa: E402
import stimuli  # noqa: E402

HERE = pathlib.Path(__file__).parent
RESULTS = HERE / "results"


def git_rev() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=HERE, text=True
        ).strip()
    except Exception:
        return "unknown"


def api_caller(model: str):
    """The Anthropic adapter. Import is lazy so the harness runs without the SDK."""
    from anthropic import Anthropic

    client = Anthropic()

    def call(prompt: str) -> str:
        msg = client.messages.create(
            model=model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")

    return call


def run(caller, reps: int, label: str, model: str) -> dict:
    rows = []
    cells = stimuli.all_cells()
    total = len(cells) * reps
    for i, cell in enumerate(cells):
        for rep in range(reps):
            print(f"  [{i * reps + rep + 1}/{total}] {cell['cell_id']} rep{rep}",
                  file=sys.stderr)
            resp = caller(cell["prompt"])
            outcome, reason = scoring.score(resp, cell["format"])
            rows.append({
                "cell_id": cell["cell_id"], "format": cell["format"],
                "subject": cell["subject"], "phrasing": cell["phrasing"],
                "is_escape_prior": cell["is_escape_prior"], "rep": rep,
                "response": resp, "outcome": outcome, "reason": reason,
            })
    return {
        "label": label, "model": model, "reps": reps, "git_rev": git_rev(),
        "n_cells": len(cells), "rows": rows, "summary": scoring.tabulate(rows),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="emit all stimuli, call nothing")
    ap.add_argument("--stimuli", nargs=3, metavar=("FORMAT", "SUBJECT", "PHRASING"))
    ap.add_argument("--api", action="store_true", help="run against the Anthropic API")
    ap.add_argument("--model", default="claude-haiku-4-5-20251001")
    ap.add_argument("--reps", type=int, default=30)
    ap.add_argument("--label", default="run")
    ap.add_argument("--score-file", help="score a JSON list of {cell_id, response}")
    args = ap.parse_args()

    if args.stimuli:
        print(stimuli.stimulus(*args.stimuli))
        return 0

    if args.dry_run:
        cells = stimuli.all_cells()
        RESULTS.mkdir(exist_ok=True)
        path = RESULTS / "stimuli.json"
        path.write_text(json.dumps(cells, indent=2))
        print(f"{len(cells)} cells written to {path}")
        return 0

    if args.score_file:
        raw = json.loads(pathlib.Path(args.score_file).read_text())
        by_id = {c["cell_id"]: c for c in stimuli.all_cells()}
        rows = []
        for r in raw:
            cell = by_id[r["cell_id"]]
            outcome, reason = scoring.score(r["response"], cell["format"])
            rows.append({**{k: cell[k] for k in
                            ("cell_id", "format", "subject", "phrasing", "is_escape_prior")},
                         "rep": r.get("rep", 0), "response": r["response"],
                         "outcome": outcome, "reason": reason})
        out = {"label": args.label, "model": r.get("model", "external"),
               "git_rev": git_rev(), "rows": rows, "summary": scoring.tabulate(rows)}
        RESULTS.mkdir(exist_ok=True)
        path = RESULTS / f"{args.label}.json"
        path.write_text(json.dumps(out, indent=2))
        print(json.dumps(out["summary"], indent=2))
        print(f"\nwrote {path}")
        return 0

    if args.api:
        if not os.environ.get("ANTHROPIC_API_KEY"):
            print("ANTHROPIC_API_KEY not set", file=sys.stderr)
            return 1
        out = run(api_caller(args.model), args.reps, args.label, args.model)
        RESULTS.mkdir(exist_ok=True)
        path = RESULTS / f"{args.label}.json"
        path.write_text(json.dumps(out, indent=2))
        print(json.dumps(out["summary"], indent=2))
        print(f"\nwrote {path}")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
