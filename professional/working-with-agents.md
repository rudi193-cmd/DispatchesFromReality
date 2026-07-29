# Working With Agents

**Sean Campbell** · Technical practice document · July 2026

**Tags:** `agent-orchestration`, `ai-verification`, `authorization-design`, `provenance`,
`fail-closed`, `local-first-ai`, `governance`

**One-line summary:** A working method for building with AI agents in which the machine's
output is never treated as verified, the authority to *ask* is structurally separated from
the authority to *grant*, and every artifact records how much of it a human actually
checked.

**Status:** Live practice across seven public repositories. Evidence is code and commit
history, not testimonial.

---

## The problem this solves

Almost every technical organisation is now shipping agent-assisted work. Very few can
answer the question that matters about any given artifact: **which parts of this did a
human actually check?**

The failure is not that models are wrong. It is that a plausible wrong answer and a
verified right one are, by default, the same pixels. A matcher serves a contract clause at
0.974 similarity and marks it verified. A dashboard catches an exception, returns an empty
list, and paints a green tick. A second model, asked to verify a citation list, returns
`VERIFIED / CONFIRMED` against two paper titles it invented.

All three of those are real, all three happened in my own systems, and all three were
caught by the same thing: **a column recording how the result was obtained.** Not
intelligence. Bookkeeping.

What follows is the method that bookkeeping belongs to.

---

## Six practices, and where each one lives

### 1. Machine output is `draft` until a human seals it

Three states, never two. In [Nestor](https://github.com/rudi193-cmd/Nestor): **sealed** (a
human verified it — served verbatim, forever, with provenance), **draft** (a machine
produced it — queued for review, never served as verified), **pending** (nothing to offer,
said plainly rather than improvised).

The economics are the point: each human verification becomes permanent capital. Cost per
answer falls as trust accumulates. *Verified once, served forever.*

The same shape recurs wherever the domain changes. In `apps/field-acoustics` every model
input is `measured`, `fitted` or `assumed`, propagated by `min()` — *a result is worth its
weakest one*. Deliberately not a confidence score: a number either traces to something a
person can look up, or it does not.

### 2. Absence is never rendered as an answer

A surface that cannot reach its data must not report that the data is empty.

I found this in my own code and wrote it down as a load-bearing constraint: a monitoring
pane caught every exception, returned `[]`, and rendered `✓ queue clear` — so *"I could not
reach the queue"* and *"nothing is waiting"* were identical pixels, with a green check on
the failure. The same fail-soft appeared eighteen times in one file, which made it house
style rather than a bug.

The rule generalises across the fleet. A missing consent file reads as denied — *absence is
not consent*. A malformed permission scope confines an app to **no** collections rather than
all of them, because a policy that cannot be parsed is not consent. An unasserted severance
claim reports `not_asserted` rather than passing.

**And it inverts where the beneficiary changes**, which is the part that shows it is a
principle rather than a habit. In `apps/marching-arts`, refusal is *tested as
indistinguishability*: a member who declined and a member who is absent must produce the
same rows, the same count, and the same subject list. If they differed, declining would
itself become the signal, and every member who exercised the choice would be marked by
exercising it. Same question about what an absence means; opposite requirement, because the
person being protected changed from an operator to a minor.

### 3. Asking and granting are separate authorities, enforced by the filesystem

An agent may *request* a capability. It may never *grant itself* one. In
[willow-mcp](https://github.com/rudi193-cmd/willow-mcp) this is structural rather than
conventional:

- `grant-net` (mint an egress lease) is local CLI only — never exposed as an MCP tool
- `confirm-binding` (map an authenticated identity to an app) is operator-only, because a
  remote caller must never confirm its own binding
- `allow-permission` is CLI-only, because an agent must never be able to grant itself a
  permission it was just denied
- Network egress requires **three standing keys plus a one-use signed envelope**: a
  capability flag in the manifest, a global consent switch, a time-boxed per-app lease, and
  a signed task envelope whose private key lives outside the agent's filesystem view

The severance model formalises the distinction that makes this coherent: store and database
are **data** surfaces — someone who writes them corrupts records, and the verdict degrades.
Trust root and egress are **authority** surfaces — someone who writes them grants themselves
what the boundary was supposed to deny, and the verdict breaks.

### 4. The residual is stated plainly, not buried

willow-mcp's README contains a section titled *"The residual, stated plainly"*: on a host
where the agent and the server run as the same uid, the agent can write the very files that
authorise its egress. Leases make a self-grant expire and leave a record; a pre-tool hook
blocks the obvious attempts; the operating system is not stopping it. It is tracked as a
numbered bug, `diagnostic_summary` names exactly which keys the running process could forge,
and strict mode ships **off** by default because enabling it before the uid separation exists
would deny egress on every current install.

[willow-gate](https://github.com/rudi193-cmd/willow-gate) opens with *"Enforcement vs. audit
— read this first"* and concedes that unwired it is a loud ledger, not a gate.

Nestor publishes its measured false-seal rate rather than claiming accuracy, and states the
conclusion against its own interest: **there is no threshold that is simultaneously safe and
useful.** At 0.96 the hardest corpus is clean and effectively dead; at 0.92 it serves real
rewrites and gets roughly one answer in six wrong.

A compliance buyer knows "we are accurate" is a lie. "Here is our measured
false-verification rate, here is the dial that sets it, here is the harness — run it
yourself" is stronger *because* it admits a failure rate.

### 5. Capabilities are earned, not scaffolded

willow-mcp ships four live integration adapters and six **declared stubs** that refuse
fail-closed, each naming what it needs and what would earn its implementation. A stub that
refuses loudly and states its own precondition is honest; a stub that half-works is a
liability.

The same rule governs promotion. `apps/marching-arts` and `apps/field-acoustics` are
playground tier and **deliberately not promoted** — the gate returns `NOT PROMOTED`
(fail-closed) because promotion requires `verified_by ≠ author`. You do not verify your own
work.

### 6. Repeated conversational labour becomes a script

When I notice a model re-deriving the same reasoning across sessions, that is a tool waiting
to be written. willow-mcp's `tools/` directory exists for exactly this — *"each turns
conversational labour into a script, so the next session runs the tool instead of
re-deriving the work."*

This is the compounding discipline, and it is what separates building from producing: every
session should leave the environment better instrumented than it found it. `gap_log` records
what is *not* known so it is not rediscovered. The hash-chained ledger outlives the session
that wrote it. Dead ends are recorded with their reasoning so they are not re-derived — the
`IDEAS.md` convention tags every entry **measured / verified / hypothesis / open**, so the
confidence level travels with the claim.

---

## What agents can and cannot do

This is the most practically useful thing I have learned, and it came out of a failed survey
rather than a success.

I ran read-only survey agents across four repositories to map a migration. They produced an
accurate inventory and one confidently wrong conclusion: they identified a ported module as
an orphan and the original as the port. My own correction, recorded in the repo:

> The survey agents were asked where code **is**, and that question cannot tell a port from
> an original — both look like live implementations from that angle. Only the migration's
> intended direction separates them, and that information existed nowhere in the
> repositories; it came from the operator.
>
> …ask a human which way the migration runs before inferring anything further.

**Agents map what exists. Only the operator holds the direction of travel.** Intent is not in
the artifacts, so it cannot be surveyed, delegated, or recovered from the code — and an agent
asked an inventory question will answer it accurately and mislead you completely.

Two corollaries that follow directly:

**Corroboration between two systems is not verification.** A load-bearing acoustics test
survived two independent reimplementations agreeing to 1e-14 dB *with each other, on the same
wrong input*. Separately, a second model asked to verify a citation list returned
`VERIFIED / CONFIRMED` against two paper titles it had invented — correct journal, correct
authors, correct year, correct subject, wrong title. A wrong fact is caught by the next
reader; a wrong citation is copied forward forever.

**A gate that cannot fail is not a gate.** Authorization logic in `apps/marching-arts` is
mutation-tested: three deliberate breaks introduced, each caught by exactly the test claiming
to cover it and only that test. Including the subtle one — dropping the parentheses around a
joined deny clause, after which only the first term binds, nothing raises, and every row the
denies were meant to withhold silently becomes visible.

---

## Worked example: a marching-arts platform, in one evening

**Status:** Playground tier, merged, not promoted. Two apps, Apache-2.0.
**Evidence:** [safe-app-store PR #112](https://github.com/rudi193-cmd/safe-app-store/pull/112)

### Problem

Drum corps organisations run a touring operation — a hundred and fifty people, most of them
under 22 and many of them minors — largely on spreadsheets and group chat. They have no
budget for per-seat SaaS, frequently no connectivity at the venue, and a duty of care around
member data that off-the-shelf tooling does not model.

### Constraints

- Offline-first and local-first; the organisation runs it on its own hardware
- Sensitive data about minors: rosters, medical information, emergency contacts, guardians
- No per-seat cost, no vendor able to revoke access
- Consent must be real, which means refusing must be costless and invisible

### What I built

- **An authorization resolver** compiling to exactly one predicate:
  `(allow₁ OR allow₂ OR …) AND NOT (deny₁ OR deny₂ OR …)`. Roles grant nothing on their own.
  At sensitivity L3 and above the payload is `NULL` in the SELECT list and only a derived
  instruction is served. L5 — safeguarding intake — is never served to anyone under any
  grant, and is routed to the people whose job it is to receive concerns.
- **Guarantees as mechanisms, not documentation:** `NOT NULL` plus non-blank `CHECK` on
  provenance; a sealed grant without a signer refused by constraint; `COUNT(*)` evaluated in
  SQLite *under* the predicate rather than in Python over fetched rows; an AST walk proving
  no module in the core can reach the network.
- **An acoustic propagation model** — octave-band energy summation, ISO 9613-1 atmospheric
  absorption, circular-piston directivity, one geometrically-gated grandstand reflection —
  with two independent implementations held to each other across five differential tiers.

### Technical judgment

- **The schema is inverted relative to how organisational software is normally built.** The
  member is the root, not a row hanging off a program. That makes protection of minors
  structural rather than a policy layer added later, and it is free now and expensive to
  retrofit.
- **Refusal is invisible by construction**, and that property is tested as
  indistinguishability rather than asserted in a privacy policy.
- **Nobody consented renders as an empty list, not three greyed rows.** Greyed rows would
  disclose exactly who declined.
- **The novel capability is acoustic, not visual.** Every drill design tool in the category
  models visuals. Nothing models what the drill sounds like from the stands — which is the
  one place a model here is not competing with mature commercial software.
- **Not promoted.** Playground tier is contested, not canonical, and promotion requires a
  verifier who is not the author.

---

## What this document claims

**Safe to claim:**

- The practices above are implemented in public code and can be inspected.
- The failure modes named — false seal at 0.974, absence rendered as assurance, confabulated
  citations labelled verified, a survey that could not distinguish a port from an original —
  are all real, all mine, and all recorded in the repositories where they occurred.
- Provenance and verification status are first-class columns in these systems, not
  documentation.

**Frame carefully:**

- Most of this is single-operator work. It has not been through a team's code review process
  or an external security audit.
- The marching-arts and field-acoustics apps are one evening old, playground tier, and
  deliberately unpromoted. They demonstrate a method; they are not production systems.
- Adoption is limited. These are working systems with real users in a small number, not
  products with a user base.

**Do not claim:**

- That the authorization model has been penetration-tested or independently reviewed.
- That any of this makes an AI system safe. It makes what a human checked *legible*, which
  is a smaller and more defensible claim.
- Peer review, certification, or compliance attestation of any kind.

---

## Transferable strengths

1. **Authorization and trust-boundary design** — separating request from grant structurally,
   fail-closed defaults with the failure direction argued rather than assumed, and a stated
   residual where the boundary is convention rather than enforcement.
2. **Verification and provenance engineering** — three-state models (sealed/draft/pending,
   measured/fitted/assumed, empty/populated/unknown) applied across translation, physics, and
   evidence bases, with retrieval status recorded as data.
3. **Agent orchestration with honest limits** — knowing what a survey agent can and cannot
   answer, and designing the human's contribution around direction and intent rather than
   volume.
4. **Adversarial self-testing** — mutation testing on authorization logic, differential
   testing across independent implementations, and publishing measured failure rates rather
   than accuracy claims.
5. **Technical writing that survives contact** — documentation that states its own residual
   risk, records dead ends with reasoning, and tags every claim with its confidence level.

---

## Evidence index

| System | What it demonstrates |
|--------|----------------------|
| [Nestor](https://github.com/rudi193-cmd/Nestor) | Sealed/draft/pending; measured false-seal rates; rejection as a first-class human decision; hash-chained audit |
| [willow-mcp](https://github.com/rudi193-cmd/willow-mcp) | Three-key egress; manifest ACL; severance model; the stated residual; earned-not-scaffolded adapters |
| [willow-gate](https://github.com/rudi193-cmd/willow-gate) | Trust ladder with bound identity; enforcement-vs-audit honesty; the friction floor |
| [kartikeya](https://github.com/rudi193-cmd/kartikeya) | Sandboxed task execution; host-agnostic queue; network-isolated by default |
| [safe-app-store #112](https://github.com/rudi193-cmd/safe-app-store/pull/112) | The worked example: authorization core, mutation testing, provenance propagation |
| [Willow](https://github.com/rudi193-cmd/Willow) | Constitutional layer — envelopes, protected agents, ratification gates |
| [Willow systems deep dive](willow-systems-portfolio.md) | Backend and data-plane detail |

---

*Related: [Portfolio case studies](portfolio-case-studies.md) ·
[Willow ecosystem inventory](willow-ecosystem-inventory.md) ·
[Research portfolio](../research/README.md)*
