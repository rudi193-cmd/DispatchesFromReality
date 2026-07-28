# E4-CONTAINER — protocol, preregistration, and closure

> **CLOSED 2026-07-28 — recorded dead end. Do not resume without reading this box.**
>
> The v1 instrument failed (see [`results/PILOT.md`](results/PILOT.md): 12/12
> `truncate`, zero variance), and the experimental arm was then dropped from the
> packet for a second and better reason: **it tested the wrong direction.**
>
> The packet's central mechanism is *reception* — the same content in a different
> container, read differently by whoever receives it. That is Charlotte's move, and
> Willow's `mai_read_file` requirement. This experiment measured *production*: what a
> system does when asked to serialize content into a container too small for it.
> Different question, and the packet does not rest on it.
>
> Everything below is preserved as written, including the preregistration, so the
> design and its failure are recoverable rather than re-derived. It is no longer
> load-bearing for anything.
>
> **If someone picks this up again**, the experiment worth running is the reception
> version: hold one fact constant, vary only the container it *arrives* in — a JSON
> record, a citation, a log line, a chat message — and measure whether the model's
> credence in it, or its willingness to act on it, moves. Fix the v1 design errors
> in [`results/PILOT.md`](results/PILOT.md) first; they apply to any version.

---

## The question

When a container cannot represent its content, does the *encoding* change what a model
does — and does the *content's narrative prior* change it?

*Framing as originally written, now superseded — see the closure box above:* this was
described as the only component of the packet that could produce a finding rather than
a citation. That overstated it. It would have borne on `M3-CORPUS`, the packet's
weakest supporting mechanism, and even a positive result would have been a curiosity
rather than load-bearing. Tractability was mistaken for importance.

## The manipulation

Every trial gives the model a two-line log entry and a target schema. The entry
records the subject in **two locations at two times**. The schema has exactly **one
single-valued location field**. The container cannot hold the content, and the model
must do something about it.

Three things it can do, and all three are reasonable:

| Outcome | What it means |
|---------|---------------|
| `truncate` | Pick one location, drop the other. Container preserved, content lost. |
| `break` | Preserve both — add a field, use a list, emit two records, append a note or comment. Content preserved, container violated. |
| `refuse` | State that the schema cannot represent the record, or ask which location is wanted. |

`unscorable` exists for anything that fits none of the three.

## Factors

| Factor | Levels |
|--------|--------|
| **format** | `json_strict`, `yaml`, `xml`, `markdown_table`, `csv`, `prose` |
| **subject** | `pig` (high escape prior), `generator`, `pallet`, `water_tank` (neutral) |
| **phrasing** | `agentive` ("left the enclosure … was found in") vs `neutral` ("was recorded in … was recorded in") |

6 × 4 × 2 = **48 cells.**

### Why these controls

The subject nouns are all things that plausibly sit in a farm enclosure and can
plausibly be recorded in two places. That matters: a rock migrating across a field is
*anomalous*, and a model might break schema out of surprise rather than out of
anything to do with escape. Holding plausibility constant isolates the noun's prior as
the manipulated variable.

The phrasing factor separates two explanations that would otherwise be confounded. If
`pig` differs from `generator` **only** under agentive phrasing, the effect is
linguistic — the verb did the work. If it differs under **both**, the effect belongs
to the noun, which is what `M3-CORPUS` predicts.

## Predictions, stated in advance

| Mechanism | Prediction |
|-----------|-----------|
| `M3-CORPUS` | `break` rate higher for `pig` than for neutral subjects, under both phrasings. |
| `M2-WEAK-SCHEMA` (**null**) | `break` rate depends on **format only**. No subject effect. |
| `M1-SEAM` | Outcome tracks how hard the instruction pushes on task completion, not on content. Not manipulated in v1 — a known gap. |

**My own expectation, recorded so it can be wrong: the null.** I expect format to
dominate — strict JSON producing `truncate` or `refuse`, prose producing `break`
trivially because prose has no schema to violate — and I expect no detectable subject
effect at achievable sample sizes.

## Decision rule, fixed in advance

1. Primary test: Fisher exact / χ² on `break` vs `not break`, `pig` against pooled
   neutral subjects, collapsing across format and phrasing.
2. Significance at **p < 0.01**, not 0.05. One shot, no peeking, and the prior is weak.
3. Report the per-format table regardless of the primary result, since format is
   expected to dominate and is worth characterising either way.
4. **A null result is published in the packet exactly as prominently as a positive
   one.** If the subject effect is absent, §VI of the draft concedes the weak-schema
   reading and says so.

## Sample

Adequate power for a small effect needs on the order of 30+ trials per cell — roughly
1,500 calls. That requires API access this session does not have.

**What was actually run tonight is a pilot, not the study.** See
[`results/`](results/). The pilot's only job is instrument validation: do all three
outcome categories occur, is the rubric scoreable by someone blind to the hypothesis,
and does the stimulus read as a genuine ambiguity rather than a trick.

## Running it

```bash
python3 run.py --dry-run              # emit all 48 stimuli, inspect them
python3 run.py --stimuli --format json_strict --subject pig   # one cell's prompt
python3 run.py --api                  # full run; needs ANTHROPIC_API_KEY
```

The model is an **injected seam** — `run.py` takes any callable
`(prompt: str) -> str`. Same shape as Nestor's storage and matcher inversions, and for
the same reason: the harness should not care where the answer came from.

## Known limitations

- **The pilot subjects are Claude Code subagents**, which carry a system prompt and
  tool availability that a bare API call would not. That confound is *constant across
  conditions*, so a pig-vs-generator contrast remains interpretable, but it limits
  generalisation to "this model in this harness."
- Single model, single family. No cross-model comparison.
- `M1-SEAM` is not manipulated in v1.
- The scoring rubric is applied by the harness author, who knows the hypothesis. The
  pilot therefore also asks a blind scorer to categorise a shuffled sample.
