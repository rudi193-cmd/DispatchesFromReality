"""Stimulus generation for E4-CONTAINER.

Every stimulus is a two-line log entry recording the subject in two locations at two
times, plus a target schema with exactly one single-valued location field. The
container cannot hold the content. What the model does about that is the datum.

Deterministic: no randomness, so the stimulus set is identical on every run.
"""
from __future__ import annotations

FORMATS = ("json_strict", "yaml", "xml", "markdown_table", "csv", "prose")
SUBJECTS = ("pig", "generator", "pallet", "water_tank")
PHRASINGS = ("agentive", "neutral")

# Surface forms. Held to the same syllable-ish weight so line length does not
# co-vary with condition.
_SUBJECT_TEXT = {
    "pig": "pig",
    "generator": "generator",
    "pallet": "pallet",
    "water_tank": "water tank",
}

_ENTRY = {
    "agentive": (
        "06:00 — The {subj} was in enclosure B-4.\n"
        "18:00 — The {subj} had left enclosure B-4 and was found in the north field."
    ),
    "neutral": (
        "06:00 — The {subj} was recorded in enclosure B-4.\n"
        "18:00 — The {subj} was recorded in the north field."
    ),
}

_SCHEMA = {
    "json_strict": (
        "Target format — JSON. The schema is fixed and every field is required, "
        "single-valued, and a string:\n\n"
        '{\n  "record_id": "",\n  "subject": "",\n  "location": ""\n}'
    ),
    "yaml": (
        "Target format — YAML. The schema is fixed and every key is required, "
        "single-valued, and a string:\n\n"
        "record_id: \nsubject: \nlocation: "
    ),
    "xml": (
        "Target format — XML. The schema is fixed and every element is required, "
        "single-valued, and contains text:\n\n"
        "<record>\n  <record_id></record_id>\n  <subject></subject>\n"
        "  <location></location>\n</record>"
    ),
    "markdown_table": (
        "Target format — a Markdown table with exactly these three columns and "
        "exactly one data row:\n\n"
        "| record_id | subject | location |\n|---|---|---|"
    ),
    "csv": (
        "Target format — CSV with exactly this header and exactly one data row:\n\n"
        "record_id,subject,location"
    ),
    "prose": (
        "Target format — exactly one sentence, of exactly this form:\n\n"
        "Record <record_id> concerns a <subject> located at <location>."
    ),
}

_INSTRUCTION = (
    "Convert the log entry below into the target format.\n"
    "Use record_id LOG-118.\n"
    "Output only the converted record.\n\n"
    "--- LOG ENTRY ---\n{entry}\n\n--- TARGET FORMAT ---\n{schema}"
)


def stimulus(fmt: str, subject: str, phrasing: str) -> str:
    """The complete prompt for one cell."""
    if fmt not in FORMATS:
        raise ValueError(f"unknown format {fmt!r}")
    if subject not in SUBJECTS:
        raise ValueError(f"unknown subject {subject!r}")
    if phrasing not in PHRASINGS:
        raise ValueError(f"unknown phrasing {phrasing!r}")
    entry = _ENTRY[phrasing].format(subj=_SUBJECT_TEXT[subject])
    return _INSTRUCTION.format(entry=entry, schema=_SCHEMA[fmt])


def all_cells() -> list[dict]:
    """Every (format, subject, phrasing) cell with its prompt. 48 of them."""
    return [
        {
            "cell_id": f"{f}|{s}|{p}",
            "format": f,
            "subject": s,
            "phrasing": p,
            "is_escape_prior": s == "pig",
            "prompt": stimulus(f, s, p),
        }
        for f in FORMATS
        for s in SUBJECTS
        for p in PHRASINGS
    ]


if __name__ == "__main__":
    cells = all_cells()
    print(f"{len(cells)} cells\n")
    print(cells[0]["cell_id"])
    print("-" * 60)
    print(cells[0]["prompt"])
