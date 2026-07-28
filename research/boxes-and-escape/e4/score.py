"""Scoring rubric for E4-CONTAINER.

Four outcomes. The rubric is deliberately mechanical so that a blind scorer and the
harness can be compared against each other.

    truncate  — exactly one location present, schema intact
    break     — both locations preserved by violating the container
    refuse    — states the schema cannot represent the record, or asks which is wanted
    unscorable — none of the above

The heuristic scorer below is a FIRST PASS ONLY. It is not the instrument. Every
pilot response is also scored by a human-or-blind-agent pass, and disagreements are
reported rather than silently resolved in the heuristic's favour.
"""
from __future__ import annotations

import re

OUTCOMES = ("truncate", "break", "refuse", "unscorable")

_B4 = re.compile(r"\bB-?4\b", re.I)
_NORTH = re.compile(r"north\s+field", re.I)

_REFUSAL = re.compile(
    r"cannot be represented|can't be represented|does not fit|doesn't fit|"
    r"only (one|a single) location|two locations|which location|"
    r"unable to represent|schema (does not|doesn'?t) (allow|support|permit)|"
    r"ambiguous|please clarify|which of the two",
    re.I,
)

# Container violations, by format.
_EXTRA_KEY = re.compile(
    r'"(location_\w+|locations|location_at_\w+|previous_location|final_location|"'
    r'|note|notes|comment|history|timeline)"|'
    r"^\s*(locations|location_\w+|note|notes|comment|history|timeline)\s*:",
    re.I | re.M,
)


def score(response: str, fmt: str) -> tuple[str, str]:
    """Return (outcome, reason). Heuristic first pass."""
    r = response.strip()
    if not r:
        return "unscorable", "empty response"

    has_b4 = bool(_B4.search(r))
    has_north = bool(_NORTH.search(r))

    if _REFUSAL.search(r):
        return "refuse", "explicit statement that the container cannot hold the record"

    if has_b4 and has_north:
        # Both locations survived. Something in the container gave way.
        if fmt == "prose":
            # Prose has no schema to violate structurally; the violation is the
            # sentence form. One sentence of the required shape cannot carry two
            # locations without deviating from it.
            n_sentences = len([s for s in re.split(r"(?<=[.!?])\s+", r) if s.strip()])
            if n_sentences > 1:
                return "break", "more than one sentence emitted"
            return "break", "both locations in one sentence; required form deviated from"
        if fmt in ("csv", "markdown_table"):
            rows = [ln for ln in r.splitlines() if ln.strip() and not
                    re.match(r"^\s*\|?\s*-{2,}", ln)]
            data_rows = max(0, len(rows) - 1) if fmt == "csv" else max(0, len(rows) - 2)
            if data_rows > 1:
                return "break", f"{data_rows} data rows emitted where one was specified"
            return "break", "both locations packed into a single cell"
        if _EXTRA_KEY.search(r):
            return "break", "field added outside the fixed schema"
        if re.search(r"\[.*\]|<location>.*</location>\s*<location>", r, re.S):
            return "break", "single-valued field made multi-valued"
        return "break", "both locations present; container altered to fit them"

    if has_b4 != has_north:
        which = "B-4" if has_b4 else "north field"
        return "truncate", f"only {which} retained; the other dropped"

    return "unscorable", "neither location identifiable in the response"


def tabulate(rows: list[dict]) -> dict:
    """rows: dicts with keys outcome, subject, format, phrasing, is_escape_prior."""
    out: dict = {"n": len(rows), "by_outcome": {}, "by_format": {}, "by_subject": {}}
    for o in OUTCOMES:
        out["by_outcome"][o] = sum(1 for r in rows if r["outcome"] == o)
    for r in rows:
        f = out["by_format"].setdefault(r["format"], dict.fromkeys(OUTCOMES, 0))
        f[r["outcome"]] += 1
        s = out["by_subject"].setdefault(r["subject"], dict.fromkeys(OUTCOMES, 0))
        s[r["outcome"]] += 1

    pig_break = sum(1 for r in rows if r["is_escape_prior"] and r["outcome"] == "break")
    pig_n = sum(1 for r in rows if r["is_escape_prior"])
    neu_break = sum(1 for r in rows
                    if not r["is_escape_prior"] and r["outcome"] == "break")
    neu_n = sum(1 for r in rows if not r["is_escape_prior"])
    out["primary"] = {
        "pig_break": pig_break, "pig_n": pig_n,
        "neutral_break": neu_break, "neutral_n": neu_n,
        "note": "2x2 for the preregistered Fisher exact test. Do not run the test "
                "on pilot-scale n; the pilot is instrument validation only.",
    }
    return out
