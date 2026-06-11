# Tabletop Mechanical Engines And Narrative Generation

**Sean Campbell** · Systems-design research · June 2026

**Tags:** `game-design`, `tabletop`, `systems-design`, `probability`, `emergent-narrative`, `mechanics`, `rules-engine`, `gateway-momentum-engine`, `dnd-5e`, `valley-of-vander`, `incentive-design`

*How can a rule system generate strategy, agency, and emergent narrative without collapsing into either arbitrariness or rigidity?*

For the broader research map, see [Research Portfolio](../README.md). For the software-systems thread this design instinct connects to, see [Willow systems deep dive](../../professional/willow-systems-portfolio.md).

---

## Current versions

| Version | Form | Status | Purpose |
|---------|------|--------|---------|
| **v1** | Working essay | [DRAFT.md](DRAFT.md) | Full prose draft: rules as engines, probability, emergent narrative, the same design instinct applied to software |
| **Packet** | Public summary | This file | Scope, method, claim boundaries, portfolio links |

---

## Opening

> A tabletop rule system is a machine. You feed it player decisions and dice, and it returns consequences, story, and a next decision. The interesting question is not "is it fun" — it is "what kind of machine is it, and what does it reliably produce?"

This vector treats game design as systems engineering. Rules are the source code. Probability is the runtime. Player agency is the input. Emergent narrative is the output that no single line of the rules wrote on its own.

It is design research and mechanics prototyping — not a published commercial game line.

---

## Core question

How do you design a rule system that produces strategy, agency, and story — without collapsing into arbitrariness (anything can happen, so nothing matters) or rigidity (the outcome is decided before the dice fall)?

---

## Thesis

A good rule system is a constrained generator. It must:

1. Make outcomes uncertain enough that decisions carry risk
2. Make outcomes structured enough that decisions carry meaning
3. Keep the probability legible enough that players can form real strategy
4. Let consequences chain so that narrative emerges from mechanics, not despite them

The skill is the same skill that good software design needs: choosing the constraints that make the interesting behavior likely and the degenerate behavior rare.

---

## Work represented

| Area | Work |
|------|------|
| **Gateway Momentum Engine** | A tabletop mechanics framework built around momentum and gateway states — designing for strategic narrative generation rather than flat resolution |
| **Custom 5e ecosystems** | Structural campaign work, including the Valley of Vander / Drakonite setting: item registries, factions, and a coherent world economy of rules |
| **Creature and faction design** | Custom stat blocks and factions, including the Felfs — designing mechanical identity, not just flavor |
| **Constrained-board mechanics** | Spatial systems such as an 8×8 grid with fixed corners and fluid interior (the "Stillness" / Baba Yaga design problem in *The Gate*) — rigid frame, chaotic field |
| **Rule-as-character systems** | Named rules with in-world identity (e.g. the "Drebin Rule" in the *Books of Mann* material) — mechanics that double as narrative objects |

---

## Method

The design method mirrors the research method used elsewhere in the portfolio:

1. Decide what behavior the system should reliably produce
2. Identify the smallest set of rules that make that behavior likely
3. Model the probability — what is common, what is rare, what is impossible
4. Playtest against degenerate strategies (the "dominant boring move")
5. Tune constraints until interesting play is the path of least resistance
6. Separate mechanics that carry strategy from flavor that carries story
7. State what the system is balanced for, and what it is not

---

## Why this belongs beside the software research

The Gateway Momentum Engine and Willow are the same instinct in two materials.

| Game-design concern | Software-systems parallel |
|---------------------|---------------------------|
| Probability legibility | Observability — can you see why the system did what it did? |
| Degenerate-strategy testing | Adversarial testing, edge-case hunting, ingest gates |
| Constraint design | API boundaries, schema design, execution sandboxes |
| Emergent narrative | Emergent behavior from composed components |
| Balance | Performance and fairness trade-offs under load |
| Named rules as objects | Named tools, policies, and contracts in a coordination framework |

Both ask: given these constraints and this randomness, what does the system reliably produce — and is that what I wanted?

---

## What this research claims

Safe to claim:

- Tabletop systems can be designed as probability-aware rule engines, not just themed content
- The Gateway Momentum Engine is original mechanics-framework design work
- Custom 5e campaign, creature, and faction design demonstrates structural world-building under a rules constraint
- The same systems instinct — constraints, probability, emergent behavior, balance — transfers directly to software design
- Design discipline includes testing against degenerate strategies, not just happy-path play

Frame carefully:

- This is design research and mechanics prototyping
- "Proprietary" means original/in-house design, not a registered commercial product unless separately documented
- Playtest evidence is enthusiast-scale, not published statistical balancing

Do not claim:

- A published or commercially released game line
- Peer-reviewed or industry-certified design credentials
- That the mechanics are finalized, balanced at scale, or shipped

---

## Portfolio relevance

This vector shows a hiring signal that pure software work does not:

- **Systems design outside code** — rules, incentives, feedback loops, probability
- **Probability literacy** — reasoning about distributions, not just outcomes
- **Adversarial design thinking** — anticipating how a system will be exploited
- **Player-facing complexity** — making a complex system legible to a human at the table
- **Constraint as a tool** — using limits to produce, not just restrict, behavior

Related documents:

- [Research portfolio](../README.md)
- [Professional portfolio](../../professional/README.md)
- [Portfolio case studies](../../professional/portfolio-case-studies.md)
- [Willow systems deep dive](../../professional/willow-systems-portfolio.md)
- [Right to fix and mechanical knowledge](../vintage-mechanical-restoration/README.md)
