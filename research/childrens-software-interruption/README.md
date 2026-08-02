# Nobody Counts the Ad Breaks

**Sean Campbell** · Children's software and the measurement gap · August 2026

**Tags:** `childrens-software`, `interruption`, `dark-patterns`, `attention-economy`, `provenance`, `measurement-gap`, `local-first`, `parental-consent`, `coppa`, `loot-boxes`, `f-droid`, `waydroid`

*Everything about how children's games manipulate has been documented, litigated and measured — except the one number a parent needs at the moment they decide.*

For the broader research map, see [Research Portfolio](../README.md). For the assessment argument this rests on, see [Assessment Evidence and Expressive Pathways](../../education/assessment-visibility-v1.1/white-paper.md). For the access-as-chokepoint thread, see [Nobody Adds It Up](../../essays/nobody-adds-it-up/README.md).

---

## Current versions

| Version | Form | Status | Purpose |
|---------|------|--------|---------|
| **v1** | Working draft | [DRAFT.md](DRAFT.md) | Full prose: the weekend, the metrics inversion, the existing record, the fact that is missing, the mechanism, and what got built |
| **Packet** | Public summary | This file | Scope, method, claim boundaries, artifact, portfolio links |
| **Artifact** | Shipped code | `apps/playgate` in `safe-app-store` | The mechanism, running and gated in CI |

---

## Opening

> My kids came to me on a Saturday and asked to play a game. A silly one. We do
> not have an emulator on the machine, so we went looking on the web — and that
> is the only detail really about my household, and the one that mattered most:
> the browser was not a preference, it was the only door available.
>
> Every version we found was ad-walled, account-gated, or a malware trap dressed
> as a game. When we finally got into something that ran, it served an ad every
> five moves unless we paid for premium.
>
> I was not playing. I was watching. And what I watched, for most of an
> afternoon, was two kids spending more time dismissing interruptions than
> playing the game.

---

## The angle

On the other end of that afternoon, in whatever dashboard the studio keeps, our
session was a success. Long time-on-app, high interaction count, repeat returns
to the tab. Every signal that instrument collects went up, and every one of them
went up *because* the experience was bad.

That is not a new observation about advertising. It is the same failure I have
already written about in assessment: a system built to see output, reporting a
proxy as though it were a measurement of the thing the proxy stood in for. A
worksheet is a proxy for understanding. Time-on-app is a proxy for enjoyment.
Both are correlated often enough to feel like measurements, and both are wrong
in a direction that is not random.

The difference is that here the proxy is not merely imprecise. **It is inverted.
A worse experience produces a better number.**

---

## Core question

Every party with an interest has measured something. What has none of them
measured, and why is that the one a parent actually needs?

---

## Thesis

The record on children's software is extensive and it stops one level above the
decision.

Regulators have named the mechanism and priced it. Consumer bodies have
documented the specific moves. Researchers have audited compliance under law and
under self-regulation and published the gap. Advocates have mapped the tactics
onto developmental stage. Census work has established exposure.

None of it resolves to **one app, one child, one afternoon.** The regulatory
record is retrospective and per-company. The audit literature is aggregate and
top-ranked. The census work is population-level by construction. The advocacy
filings are about platforms.

The commercial market *does* resolve to that unit — ad-load, session
interruption, monetisation mix and publisher ownership are tracked in fine
detail — and sells it by subscription to the publishers buying the inventory.

So the measurement of the harm sits behind the same account-server-subscription
wall as everything else, one layer up. A parent cannot buy it and would not know
it existed to buy.

The proposal is not a dataset. It is a **field with a provenance state**, and an
honest default of `assumed`.

---

## The mechanism

| Element | What it does |
|---------|--------------|
| The fact | Stops per ten minutes of *ordinary* play — not per session, not ads specifically. A paywall prompt, a rate-us modal and a video ad are the same event from the child's seat. |
| Dismissal | `immediate`, `after_delay`, `unskippable`, `deceptive_close`. The last is not a worse version of the others; it is a different mechanism, in which escaping the interruption is itself monetised. |
| Provenance | `assumed` (nobody looked), `fitted` (derived by a stated rule), `measured` (a person watched and counted). |
| Absence | A missing record is an error, not a default. "Nobody checked" and "measured at zero" are opposite facts. |
| Combination | `min()` across inputs. A view is worth its weakest input — never an average, because averaging is how a strong input hides a weak one. |
| Decay | A `measured` record whose observed build no longer matches the installed build demotes to `fitted`, automatically. Ad load is a tuning parameter; a count for 3.1 says nothing about 3.2. |

**No composite score.** A single displayed number would be built from weights
somebody picked, sorted on, and within two releases optimised against — at which
point it would measure compliance with the scoring function rather than
interruption, exactly as time-on-app stopped measuring enjoyment.

---

## Method

- **Survey what exists first.** Four tiers: regulatory enforcement, consumer-body
  documentation, academic compliance audits, population census. Establish how
  much is *not* a gap before claiming one.
- **Distinguish free machine-readable sources from paid ones.** F-Droid's
  `AntiFeatures` and Exodus Privacy's tracker reports are the two free per-app
  sources; both measure embedded libraries rather than behaviour.
- **State the harness limits alongside every claim.** F-Droid's `Ads` flag is
  rarely applied *because ad-supported apps are excluded upstream*, so its
  absence is not a clean bill.
- **Build the mechanism to find out what it costs.** The artifact was written to
  test whether the field survives contact with a real schema, a real gate and a
  real CI run.

---

## The artifact

`apps/playgate` in `safe-app-store` — merged, in the store's CI matrix, 118
assertions including eleven mutations that break one mechanism each and require
exactly the test claiming to cover it to fail.

It implements the mechanism above: interruption records with provenance,
automatic version-drift demotion, `min()` combination, a catalog that refuses to
load an entry with nothing recorded, an append-only disposition log requiring a
reason to grant as well as to refuse, and a snapshot of the evidence as it stood
at the moment of the decision.

**The catalog has four entries and every one says `assumed`.** Nobody has
watched a child play any of them, a test enforces that no entry claims
otherwise, and there is no code path that can reach `measured`. Populating those
rows from tracker inventories and calling them `fitted` was available and would
have lost this paper's argument inside this paper's own artifact.

---

## What this research claims

Safe to claim:

- The regulatory, consumer-body, academic and census record on children's
  software monetisation is extensive and well-sourced
- None of that record resolves to a per-title, per-child interruption figure
- Commercially, that figure is tracked and sold to the publishers, not to parents
- F-Droid `AntiFeatures` and Exodus Privacy are free, machine-readable, per-app,
  and measure embedded SDKs rather than interruption cadence
- A provenance-stated field is implementable, gateable in CI, and survives
  contact with a real schema
- The `measured` tier cannot be automated and does not scale

Frame carefully:

- The cited figures are corroborated across independent secondary sources, not
  read in the primary — see the DRAFT's Sources table and verification debt
- The Korean 84.4% and UK 64.0% compliance figures come from separate studies of
  separate markets in separate years; the comparison is not a controlled contrast
- The Common Sense figures are aggregated over children aged zero to eight only
- The artifact is prototype-tier: gated, and used by nobody but its author

Do not claim:

- That screen time or gaming is harmful to children — this paper makes no such
  argument and explicitly refuses the framing
- That children clicking the biggest button have failed a literacy test
- That this protects a child on the open web; it gates installed packages only
- Peer review, or that any figure here was verified against a primary document

---

## Connection to the wider portfolio

| Thread | Connection |
|--------|------------|
| [Assessment Visibility](../../education/assessment-visibility-v1.1/white-paper.md) | The parent instrument problem: sustained observation is the most accurate data available and cannot travel without shared language |
| [Nobody Adds It Up](../../essays/nobody-adds-it-up/README.md) | Access as chokepoint — here the measurement of the harm is itself behind the wall |
| [Sociotechnical AI](../sociotechnical-ai-sovereignty/README.md) | Operational control versus mere access |
| [Right to fix](../vintage-mechanical-restoration/README.md) | Inspectability as public capacity |
| [Willow systems](../../professional/willow-systems-portfolio.md) | Provenance as a state, append-only records, corrections beside rather than on top |

The through-line: **a fact either traces to something a person can look up, or it
does not, and blurring that is how a tool starts lying.**

---

## Open decisions

- **Title.** *Nobody Counts the Ad Breaks* deliberately echoes *Nobody Adds It
  Up*. It may read as an essay title on a research packet.
- **The Sources table** departs from the house style of the other research
  drafts, which name sources inline and carry no reference section. Kept because
  a paper arguing a fact is untraceable is in a poor position if its own figures
  are not. Drop or move to this packet if the convention should hold.
- **Verification debt is open.** Two rows do the most argumentative work and
  neither has been read in the primary.
