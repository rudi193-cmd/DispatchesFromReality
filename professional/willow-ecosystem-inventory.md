# Willow Ecosystem Inventory

**Sean Campbell** · Evidence map for technical employers · 2026-06-10

**Tags:** `repo-census`, `systems-inventory`, `safe-apps`, `mcp`, `postgres`, `research-substrate`, `portfolio-evidence`

This document maps the local repo and data landscape behind the Willow systems portfolio. It is a curated inventory, not a raw dump. Paths below are summarized for portfolio context; private operator data stays out of public claims.

**Census snapshot:** 27 top-level git repos under `~/github/`, plus 13 git worktrees, nested SAFE app installs, and research folders under `~/Documents/`. Total git roots discovered locally: ~52 (including worktrees and nested repos).

---

## How to read this

| Lane | Meaning |
|------|---------|
| **Owned/core** | Sean-built primary systems — strongest portfolio evidence |
| **Owned/app** | SAFE apps and local-first utilities in the app store monorepo |
| **Contributed/forked** | Upstream projects where Sean integrated, documented, or contributed |
| **Research substrate** | Ingestion, extraction, verification, figures, paper workflow |
| **Benchmark/eval** | LoCoMo, retrieval, agent benchmarks, generated corpora |
| **Third-party** | Dependency or evaluation checkout — context only, not claimed as owned work |

---

## Owned / core systems

| Repo | Remote | Role |
|------|--------|------|
| [willow-2.0](https://github.com/rudi193-cmd/willow-2.0) | `rudi193-cmd/willow-2.0` | Primary platform: Postgres KB, SAP MCP, SAFE gate, SOIL, Grove, Kart, HNS, Fylgja skills, Ollama default |
| [willow-1.9](https://github.com/rudi193-cmd/willow-1.9) | `rudi193-cmd/willow-1.9` | Prior generation; migration path documented in 2.0 |
| [willow-bot](https://github.com/rudi193-cmd/willow-bot) | `rudi193-cmd/willow-bot` | Bot/automation layer on Willow |
| [safe-app-store](https://github.com/rudi193-cmd/safe-app-store) | `rudi193-cmd/safe-app-store` | Public SAFE App Store monorepo — portless local-first apps |
| [safe-app-willow-grove](https://github.com/rudi193-cmd/safe-app-willow-grove) | `rudi193-cmd/safe-app-willow-grove` | Grove messaging bus + terminal dashboard |
| [DispatchesFromReality](https://github.com/rudi193-cmd/DispatchesFromReality) | `rudi193-cmd/DispatchesFromReality` | Education writing, assessment framework, professional portfolio |
| [quiet-corner](https://github.com/rudi193-cmd/quiet-corner) | `rudi193-cmd/quiet-corner` | Related education/docs mirror |
| [community](https://github.com/rudi193-cmd/community) | `rudi193-cmd/community` | Emerging Rule community fork/contributions |
| [sean-data-vault](https://github.com/rudi193-cmd/sean-data-vault) | `rudi193-cmd/sean-data-vault` | Private data vault (not public portfolio content) |
| [hermes-agent](https://github.com/rudi193-cmd/hermes-agent) | `rudi193-cmd/hermes-agent` | Fork/integration of Hermes agent stack |
| [mcp-memory-service](https://github.com/rudi193-cmd/mcp-memory-service) | `rudi193-cmd/mcp-memory-service` | MCP memory service fork/evaluation |
| [python-sdk](https://github.com/rudi193-cmd/python-sdk) | `rudi193-cmd/python-sdk` | MCP Python SDK fork |
| [litellm](https://github.com/rudi193-cmd/litellm) | `rudi193-cmd/litellm` | LiteLLM fork for routing experiments |
| [awesome-claude-skills](https://github.com/rudi193-cmd/awesome-claude-skills) | `rudi193-cmd/awesome-claude-skills` | Skills contribution (PR #885 to ComposioHQ) |
| [claude-deep-review](https://github.com/rudi193-cmd/claude-deep-review) | `rudi193-cmd/claude-deep-review` | Review tooling |
| [smallcode](https://github.com/rudi193-cmd/smallcode) | `rudi193-cmd/smallcode` | Small utilities |

**Private overlay (correctly not in public repos):** `willow-config`, `~/github/.willow` — fleet config, handoffs, agent settings, ledgers.

---

## SAFE App Store ecosystem

19 apps in the local `safe-app-store` / `safe-app-store-public` monorepo:

| App | Status (public README) | Portfolio relevance |
|-----|------------------------|---------------------|
| [ask-jeles](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/ask-jeles) | Public preview | Local-first TUI librarian: KB → web → 29 institutional sources; synthesis, verification, consent capture |
| [source-trail](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/source-trail) | Beta | Citation and claim verification — Ask Jeles companion |
| [ratatosk](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/ratatosk) | Dev | Sovereign Claude Code replacement; MCP + Grove + persona gate |
| [utety-chat](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/utety-chat) | Stable | UTETY faculty persona chat |
| [story-timeline](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/story-timeline) | Beta | Literary knowledge base (local `timeline.db`) |
| [semantic-translator](https://github.com/rudi193-cmd/safe-app-store) | Local | Corpus + ingest logs for translation/semantic work |
| [private-ledger](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/private-ledger) | Beta | Local financial ledger |
| [public-ledger](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/public-ledger) | Beta | Public ledger variant |
| [field-notes](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/field-notes) | Beta | Plain-text observations |
| [law-gazelle](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/law-gazelle) | Coming soon | Legal case management |
| [the-binder](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/the-binder) | Local | JSONL filing and edge proposals |
| [the-squirrel](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/the-squirrel) | Local | Utility app |
| [nasa-archive](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/nasa-archive) | Local | NASA archive browser |
| [llmphysics](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/llmphysics) | Local | Physics/LLM interface |
| [llmphysics-bot](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/llmphysics-bot) | Local | Reddit/Devvit bots for physics community |
| [UTETY-Reddit-Bots](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/UTETY-Reddit-Bots) | Local | Faculty persona bots (Gerald, Hanz, Oakenscroll) |
| [dating-wellbeing](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/dating-wellbeing) | Local | Wellbeing app prototype |
| [vision-board](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/vision-board) | Local | Vision board frontend |
| [bt-controller](https://github.com/rudi193-cmd/safe-app-store/tree/master/apps/bt-controller) | Local | Bluetooth controller utility |

**Architecture pattern:** Each app is portless, manifest-gated (`safe-app-manifest.json`), and stores user data under `~/.willow/store/<app>/` by convention.

---

## Willow 2.0 internal planes

From the public README and local operation:

| Plane | Components | Data stores |
|-------|------------|-------------|
| **Knowledge** | Postgres KB, hybrid search (pgvector + BM25), intake layer, Jeles, Opus, Binder, lifecycle tiers, FRANK ledger | `knowledge` table, `jeles_atoms`, `opus_atoms`, edges |
| **Session state** | SOIL collections, handoffs, stack snapshots, hooks | `store/<agent>/*.db`, `handoffs.db`, ledgers in `~/.willow/` |
| **Execution** | Kart task queue, bwrap sandbox, systemd kart-worker | `tasks` table, `.kart-scripts/` |
| **Messaging** | Grove Postgres bus, Discord bridge, claim coordination | Grove channels DB, `discord_claims.json` |
| **Inference** | Ollama default, HNS node scheduler, tier routing (3b/8b/Claude) | `grove/nodes`, model tags |
| **Governance** | SAFE manifests, GPG signing, boot ceremony, skills gateway | `~/SAFE/Agents/`, `sap/mcp_registry.json` |
| **Tools surface** | SAP MCP (~90+ tools in full profile), IDE integration | `sap/sap_mcp.py`, `willow.md` contract |

---

## Research substrate

### RH / physics corpus (`~/Documents/rh-research`)

| Artifact | Purpose |
|----------|---------|
| `figures/rh7_fisher_panels/rh_dirty_kb_export.jsonl` | Export of 659 KB atoms from project `rh-dirty` (46 source files) |
| `figures/rh7_fisher_panels/DEVLOG.md` | Session log: 7-panel Fisher decomposition, χ²/ν = 0.45 reproduction |
| `figures/rh7_fisher_panels/PHYSICS_NOTES.md` | Physics commentary on τ_exc/τ₀ and information channels |
| `figures/rh7_fisher_panels/rh7_fisher_panels.py` | Figure generation script |
| `sessions/rh7_verification.json` | Extracted tex chunks for verification |
| `sessions/rh7_extraction.json` | Extraction session output |
| `corpus/source/dirty/` | Raw source materials (.tex, .pdf, .zip) |

**Ingest pipeline (willow-2.0):** `sandbox/rh_harness/ingest.py` → chunker (.tex/.md/.txt/.lean/.pdf/.zip) → `willow_shim.py` → Postgres `knowledge` table, project `rh-dirty`.

**Portfolio framing:** Research-system and verification-tooling evidence. Numerical reproduction and figure generation are portfolio claims; unreviewed physics conclusions are not.

### Sociotechnical research (willow worktree)

| Artifact | Purpose |
|----------|---------|
| `worktrees/research-sociotechnical/sociotechnical.db` | Research SQLite |
| `worktrees/research-sociotechnical/operation_paperclip_genealogy.db` | Genealogy research DB |

### Upstream integration worktrees (willow-2.0)

| Worktree | Upstream focus |
|----------|----------------|
| `upstream-emerging-rule-community` | K-12 AI lessons contribution |
| `upstream-mengram` | Mengram memory integration |
| `upstream-sigmap` | SigMap symbol search integration |
| `upstream-awesome-claude-skills` | Skills ecosystem |
| `upstream-openclaw` | OpenClaw agent integration |
| `upstream-kanon`, `upstream-claudeclaw`, `upstream-commcare-nova`, `upstream-nova-plugin` | Additional agent/memory ecosystem evaluation |

---

## Benchmark / evaluation

| Location | Purpose |
|----------|---------|
| `willow-2.0/willow/bench/locomo/` | LoCoMo retrieval benchmark baselines (`baselines.jsonl`) |
| `willow-2.0/store/hanuman/bench/locomo/atoms.db` | Benchmark atoms in SOIL |
| `sigmap/benchmarks/tasks/*.jsonl` | SigMap benchmark task suites (upstream repo) |
| Hybrid KB gold-query spot checks | Retrieval regression testing (documented in fleet KB) |

---

## Contributed / forked (integration evidence)

| Repo | Relationship | Evidence |
|------|--------------|----------|
| [sigmap](https://github.com/manojmallick/sigmap) | Upstream; local worktree `upstream-sigmap` | Symbol search before AI answers — integrated into Willow evaluation |
| [stash](https://github.com/alash3al/stash) | Upstream eval; PR #8 merged, PR #9 Ollama docs | Agent memory; network with Emerging Rule / Felipe Castro Quiles |
| [basic-memory](https://github.com/basicmachines-co/basic-memory) | Evaluated | Memory patterns reference |
| [engram](https://github.com/Gentleman-Programming/engram) | Evaluated | Agent memory reference |
| [courtlistener-mcp](https://github.com/DefendTheDisabled/courtlistener-mcp) | Local checkout | Legal semantic search MCP — complements Jeles institutional sources |
| [bubblewrap](https://github.com/containers/bubblewrap) | Dependency | Kart sandbox isolation |
| [Emerging-Rule/community](https://github.com/Emerging-Rule/community) | Upstream; lessons merged | Scribe lesson, reading list, AI literacy series |

---

## Third-party checkouts (context only)

| Repo | Notes |
|------|-------|
| `rich`, `pyfiglet` | UI/terminal dependencies |
| `ngrok-python` | Tunneling reference |
| `adjoint` | Evaluated, not owned |
| `DontFeedTheAI` | Third-party, not owned |
| NousResearch/hermes-agent (upstream) | Original Hermes; local fork is `rudi193-cmd/hermes-agent` |

---

## Data artifact summary (safe to reference)

| Category | Examples | Portfolio use |
|----------|----------|---------------|
| **Postgres KB** | `knowledge`, `jeles_atoms`, `tasks`, `edges`, `frank_ledger` | Core memory graph — cite counts from fleet_status, not raw data |
| **SOIL SQLite** | `store/hanuman/atoms.db`, `kb.db`, `sessions.db`, `jeles.db`, per-agent collections | Fast structured state; hooks write stack snapshots |
| **Intake JSONL** | `~/.willow/intake/<agent>/YYYY-MM-DD.jsonl` | Unified write path before tier routing |
| **Ledgers** | `~/.willow/ledger_*.jsonl` | Tamper-evident session audit (private) |
| **App corpora** | `semantic-translator/data/corpus.jsonl`, ingest logs | App-level knowledge packaging |
| **Research export** | `rh_dirty_kb_export.jsonl` (659 atoms) | Research substrate proof |
| **Benchmark JSONL** | LoCoMo baselines, SigMap tasks | Evaluation discipline |

**Do not publish:** credentials, private ledger contents, operator handoffs, or raw personal data from `sean-data-vault`.

---

## Public portfolio repos (rudi193-cmd ecosystem)

From fleet KB and GitHub: coherent public line around **local-first AI memory** — [willow-2.0](https://github.com/rudi193-cmd/willow-2.0), [safe-app-store](https://github.com/rudi193-cmd/safe-app-store), plus adjacent projects (stash fork, ctxvault, holon, ShibaClaw, mengram, ogham-mcp, statewave). Landing: [rudi193-cmd.github.io](https://rudi193-cmd.github.io).

---

## Related documents

- [willow-systems-portfolio.md](willow-systems-portfolio.md) — systems-building case studies drawn from this inventory
- [portfolio-case-studies.md](portfolio-case-studies.md) — summary case study entry point
- [README.md](README.md) — how to read the professional packet

*Last updated: 2026-06-10. Local paths summarized; public links preferred for evidence.*
