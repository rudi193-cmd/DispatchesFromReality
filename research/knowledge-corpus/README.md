# Adversarially Verified Knowledge Corpus

**Sean Campbell** · Structured knowledge base · August 2026

**Tags:** `knowledge-corpus`, `adversarial-verification`, `nestor`, `jeles`, `cross-domain`, `fact-check`, `public-sources`

*A structured knowledge corpus built from public sources, adversarially verified across three rounds of fact-checking, steel-manning, and contradiction challenges.*

This research packet documents a knowledge corpus spanning foundational science, modern infrastructure, people (contemporary and historical), economics, law, environment, war, education, media, health, and labor. Every entry carries evidence with real source URLs. The corpus was built to hold both sides of contested claims and to surface its own errors through adversarial passes.

For the broader research map, see [Research Portfolio](../README.md). For the systems that store and serve it, see [Willow deep dive](../../professional/willow-systems-portfolio.md).

---

## Current versions

| Version | Form | Status | Purpose |
|---------|------|--------|---------|
| **v1** | Nestor bundle | [nestor.bundle.json](nestor.bundle.json) | Portable, re-importable corpus: 1369 pairs, 546 edges, 2105 evidence entries |
| **Packet** | Public summary | This file | Scope, method, domains, claim boundaries |

---

## Core question

What does a knowledge base look like when it is built to include the good, the bad, and the contested — from public sources only — and then turned on itself through adversarial verification?

---

## Scale

| Measure | Count |
|---------|-------|
| Pairs (claim + explanation) | 1369 |
| Edges (contradicts, refines, supersedes) | 546 |
| Evidence entries (source URLs) | 2105 |
| Distinct origins | 180 |
| Domains | ~30 |
| Adversarial rounds | 3 |

---

## Domains

| Batch | Domains | Pairs |
|-------|---------|-------|
| Core (Way Things Work) | Forces, heat/light/sound, electricity, materials, food/body, weather, measurement, money, transportation, digital communication | ~150 |
| AI research | RAG systems, agent memory, knowledge-graph grounding, distillation/caching, multi-agent coordination | ~77 |
| Modern world infrastructure | Internet, energy grids, food systems, healthcare, cities | ~75 |
| People (contemporary) | AI pioneers, tech power, ethics/safety, scandals, open source, scientists, whistleblowers, infrastructure builders, media shapers, rights/reform | ~137 |
| People (historical) | Scientists, political power, liberation movements, thinkers, artists | ~72 |
| Economics, law, environment, education, war | Five domains, R8 batch | ~98 |
| Media/information, health/medicine, labor/work | Three domains, R9 batch | ~53 |
| Cross-domain wiring (3 rounds) | Power-accountability, ethics-creation, credit-erasure, infrastructure-control, ideas-weaponized, money-power, climate-everything, knowledge-control, systems-control, unintended-consequences | ~100 |
| Adversarial passes (3 rounds) | Fact-check, steel-man, contradiction challenge | ~125 |
| Earlier rounds + websearch + wildcard | Various | ~482 |

---

## Method

1. **Research**: structured JSON pairs with source text (the claim), target text (the detailed explanation with dates, numbers, and named sources), and reason (why it matters).
2. **Evidence**: every pair carries at least one evidence entry with a real source URL.
3. **Cross-domain wiring**: edges connecting claims across domains — contradictions, refinements, and supersedes relationships.
4. **Adversarial verification** (three rounds):
   - **Fact-check**: verify specific numbers, dates, and attributions against primary sources. Correct errors, confirm accurate claims.
   - **Steel-man**: present the strongest version of positions that could be dismissed. Add guardrails and nuance.
   - **Challenge contradictions**: identify where claims across domains collide and document both sides.

---

## Claim boundary

- **All draft, none human-sealed.** A machine proposed these entries and a machine verified them adversarially. Per the standing rule: *you may propose, you may not confirm.* Sealing requires a human in `nestor ui`.
- **Public sources only.** Every evidence entry cites a publicly accessible source (Wikipedia, WHO, ILO, OECD, peer-reviewed journals, government reports).
- **Adversarial, not authoritative.** The adversarial passes correct factual errors and surface contradictions, but they are machine-generated corrections of machine-generated claims. The corpus is more accurate for having been challenged, but it is not peer-reviewed scholarship.

---

## Rebuild from bundle

The bundle is a Nestor-format JSON export. To load it into a fresh Nestor store:

```bash
nestor import research/knowledge-corpus/nestor.bundle.json --apply
```

---

## Dual-write stores

The same research feeds two stores with different verification questions:

| Store | Question it asks | Location |
|-------|------------------|----------|
| **Nestor** | Did a named human check this? | `data/nestor-demo.db` (Nestor repo) |
| **Jeles** | Do enough independent sources back this? | `~/.willow/store/ask_jeles_corpus/store.db` |

The ingestion scripts are `scripts/auto_compose.py` (Nestor) and `scripts/jeles_compose.py` (Jeles), both in the [Nestor repo](https://github.com/rudi193-cmd/nestor).
