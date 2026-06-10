# The Illusion of Sovereign AI

**Sean Campbell** · Sociotechnical AI research paper · June 2026

*A structural argument about chokepoints, capital, and what "sovereignty" actually requires.*

This paper is the research thread that led directly into the professional portfolio work in this repository. It connects AI policy language, semiconductor supply chains, capital formation, open-weight distribution, local-first infrastructure, and the practical question that also shaped Willow: **what does it mean to control an AI system rather than merely access one?**

For the broader research map, see [Research Portfolio](../README.md).

---

## Current versions

| Version | Form | Status | Purpose |
|---------|------|--------|---------|
| **v1** | Long-form essay | Working draft | Developed the argument in public-facing prose: sovereign AI claims often confuse model ownership with infrastructure control |
| **v2** | Formal paper | Working draft | Recast the same thesis as a structured research paper with abstract, methodology, evidence base, limitations, and references |

The working drafts live in the Willow sociotechnical research worktree. This public packet summarizes the paper and its evidence boundaries without publishing private database files.

---

## Thesis

Most "sovereign AI" narratives define sovereignty too narrowly. They ask whether a nation, company, or institution trained a model. The more important question is whether that actor controls the stack needed to run the model:

1. Model weights that can be downloaded and retained
2. Hardware the institution owns
3. Inference software the institution controls
4. No API key, license, cloud account, platform policy, or vendor relationship that can revoke access

By that standard, many national AI initiatives are not sovereign in the operational sense. They remain dependent on chokepoints in hardware, capital, talent, distribution, or cloud infrastructure.

---

## Evidence base

The analysis is grounded in a structured SQLite research database, `sociotechnical.db`, built from public sources.

| Table / relation | Scope |
|------------------|-------|
| AI organizations | 30 creators / institutions |
| People | 76 persons of interest |
| Funders | 41 capital sources |
| Funding rounds | 40 investment events |
| Relationship edges | 80 directed edges |
| Observations | 56 analytical notes with source attributions |

Representative edge types:

| Edge type | What it tracks |
|-----------|----------------|
| `infrastructure_dependency` | Hardware and compute dependency chains |
| `strategic_backer` | Capital relationships with strategic influence |
| `spawned_talent` | Organizational lineage through personnel movement |
| `geopolitical_split` | Capital or organizational decoupling under policy pressure |
| `ecosystem_node` | Platform positions that mediate distribution or coordination |

---

## Core argument

| Layer | Chokepoint |
|-------|------------|
| Hardware | AI training depends on NVIDIA GPU design, TSMC fabrication, and ASML EUV lithography |
| Capital | Domestic AI initiatives often rely on foreign or strategically entangled funding |
| Talent | Frontier labs share cross-border personnel pipelines and institutional lineage |
| Distribution | Open-weight models frequently depend on Hugging Face, whose investors include major closed-model incumbents |
| Economics | Training efficiency gains may compress API margins and force a 2027-2028 sector correction |

The paper argues that the post-correction economics of AI may make local-first, open-weight deployment not only philosophically attractive but financially dominant for many institutions.

---

## Connection to Willow

This is the conceptual bridge into the Willow systems work.

Willow is not "sovereign AI" at national scale. It is a local-first operator stack that takes the same problem seriously at practical scale:

| Paper criterion | Willow implementation pattern |
|-----------------|-------------------------------|
| Ownable capability | Local-first workflows; Ollama default; open/local model support |
| Controlled runtime | MCP tools, local shell/task execution, Kart worker boundary |
| Durable state | Postgres KB, SOIL stores, handoffs, ledgers |
| No opaque automation | Ingest gates, source-trail verification, FRANK audit ledger |
| Reduced platform dependence | SAFE apps, portless local data, public/private separation |

The sociotechnical paper asks what AI sovereignty requires structurally. Willow is one practical answer at the scale of a single operator and small local fleet.

---

## What the paper claims

Safe to claim:

- The paper maps dependency chains in the AI ecosystem using a structured relational evidence base.
- The central argument distinguishes rhetorical model sovereignty from operational infrastructure sovereignty.
- The work connects AI policy, semiconductor supply chains, capital structures, talent flows, and local-first deployment.
- The v2 draft formalizes the v1 essay into a research-paper structure with methodology, limitations, and references.

Frame carefully:

- The 2027-2028 correction window is a structured forecast, not a point prediction.
- Revenue and valuation figures are based on public reporting and analyst estimates.
- The database is incomplete by design because private capital structures and internal organizational relationships are not fully observable.

Do not claim:

- Peer-reviewed publication
- Complete coverage of every AI governance issue
- Definitive financial prediction
- Hardware sovereignty for local-first systems that still depend on consumer GPUs or Apple Silicon

---

## Portfolio relevance

This paper matters professionally because it shows the research side of the same systems instinct visible in Willow:

- Build a database before making broad claims.
- Separate rhetoric from operational dependency.
- Track evidence as relationships, not isolated facts.
- State limitations explicitly.
- Connect policy language to implementation realities.

Related portfolio documents:

- [Professional portfolio](../../professional/README.md)
- [Willow systems deep dive](../../professional/willow-systems-portfolio.md)
- [Willow ecosystem inventory](../../professional/willow-ecosystem-inventory.md)
- [Portfolio case studies](../../professional/portfolio-case-studies.md)

