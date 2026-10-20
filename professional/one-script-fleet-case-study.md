# Case Study 4 — Honest Systems: The One-Script Fleet

**Sean Campbell** · Technical employer packet · 2026-10

**Tags:** `systems-integration`, `ci-cd`, `test-engineering`, `security-design`, `human-in-the-loop`, `forecasting`, `release-automation`

**One-line summary:** I consolidated a multi-repo agent platform into one shared core ("the one-script") that every game, tool and operator surface imports, so there is one random stream, one tamper-evident record and one human-only seal. Then I proved the move changed no behaviour, drove four interlocking pull requests to green across three organisations, and shipped them through automated releases.

**Status:** Merged and released 2026-10-20 — [willow-bot v1.15.0](https://github.com/willow-memory/willow-bot/releases/tag/v1.15.0) and [willows-grove v0.26.0](https://github.com/willow-memory/willows-grove/releases/tag/v0.26.0). Public repositories. A market-forecast ledger built on the same core is work in progress (see the last section).

**Evidence:** [willow-bot#147](https://github.com/willow-memory/willow-bot/pull/147) · [safe-app-store#226](https://github.com/rudi193-cmd/safe-app-store/pull/226) · [willows-grove#160](https://github.com/willow-memory/willows-grove/pull/160) · [Nestor#324](https://github.com/Die-Namic-Systems/Nestor/pull/324)

**Predecessor:** [Case Study 3 — Willow](portfolio-case-studies.md) (`willow-2.0`, now archived) · [Ecosystem inventory](willow-ecosystem-inventory.md)

---

## Problem

By October 2026 the Willow work had grown into separate repositories across several GitHub organisations: an operator seat (willows-grove), a bot and core library (willow-bot), an app store with tabletop games (safe-app-store), a human-verification ledger (Nestor), and others. Each had grown its own copy of the same few ideas:

- **Three copies of the random stream** that seeds game dice, so "replay this session" depended on which copy a game had used.
- **Two record chains** for game results, so a result could be on one and missing from the other.
- **Three different seal paths** for "a human approved this", one of which was a list of names, the weakest kind of check.
- **Restated rules**: the same three-state answer (populated / empty / unreachable), the same "where is the virtual environment" logic, and the same lookup tables, each written more than once.

Every copy was a place for two versions to disagree quietly. In a system whose whole point is that a person can trust what it says, quiet disagreement is the failure mode.

## Audience / users

- **Primary:** the operator, one person, who has to be able to trust what the system reports and to be the only one who can approve.
- **Secondary:** the agents and tools in the fleet, which all read and write through the same core.

## Constraints

- **Only a person seals.** Code may propose; it must never approve its own work. No machine-held key may stand in for the human's.
- **Nothing breaks on the way.** Games that already ran had to keep producing the same results from the same seeds.
- **Decisions are the operator's.** Each phase was proposed, and the operator chose. Several decisions were reversed partway (see "Judgment calls"). Every decision is recorded with the operator's own words.
- **Frozen records stay frozen.** Earlier experiment results are never edited; new results go beside them.

## What I built

The work ran in phases (F0–F6), each recorded with its decisions:

| Phase | Outcome |
|---|---|
| F1 — one stream | One SHA-256-based random stream (`sha256-stream/v1`) with the standard random-number interface every game already used; the old copies became imports of it |
| F2 — one record | Game sessions write their results as rows on the one hash-chained record; the older parallel chain was retired with a tombstone note rather than deleted |
| F3 — one seal | A story decision moves only on the human's signed answer, checked through the core; a human rejection is itself a signed act, so a "no" is as durable as a "yes" |
| F4 — the randomness, not the games | The games stayed where they were. Their randomness (dice, odds, pools, the day's public seed) moved into the core, and the games import it |
| F5 — one of each rule | One environment rule, one three-state type, and lookup tables as imports instead of copies |
| F6 — readers | The predictions game's twelve questions became a reader that turns a public randomness beacon (drand) into answers on the record |

## How I showed nothing changed

- **Byte-for-byte reproduction:** a 200-run game simulation driven through the new core reproduced the frozen earlier output file exactly.
- **Parity tests:** the new code is held draw-for-draw to the old code it replaced, over many seeds, by tests that keep running.
- **Mutation testing:** for each guard I deliberately broke the code and checked that a test failed. A guard no test can catch hasn't been shown to work. The counts below are the ones I recorded at the time.

| Module | Mutants caught |
|---|---|
| random generator (xorshift) | 6 of 7 (the 7th is an equivalent mutant) |
| dice | 7 of 7 |
| pools | 7 of 7 |
| beacon day functions | 7 of 7 |
| predictions reader | 9 of 9 |
| market ledger | 14 of 14 |

- **Every forbidden act gets a test:** a forecast made after its outcome, a role betting both sides, a record row placed before the seal that should precede it, a forged answer, randomness that isn't the beacon's. Each test attempts the act and checks that it is refused.

## Driving four PRs to green across three organisations

The four pull requests depended on each other. Each repository's CI checked out the others' *default* branches, so no PR could pass until another had merged. There was no merge order that worked. On top of that, my own earlier change had pointed one checkout at a branch name (`master`) that didn't exist in that repository (`main`).

What I did:

1. **Found the circularity from the logs**, rather than retrying jobs.
2. **Changed each sibling checkout to use the same-named branch when one exists**, else the default (`git ls-remote`). Partner PRs now test against each other, and after merge everything falls back to the defaults as before.
3. **Reproduced CI's directory layout locally** (sibling repos checked out *inside* the repo, not beside it). That exposed two real bugs the old layout had hidden: a path assumption in a test, and a function that looked for a dependency only "beside" itself. Both were fixed in code, with a regression test that fails without the fix.
4. **Didn't treat sandbox-only failures as CI failures.** One test failed only because the sandbox's system Python lacked pytest; I recorded that and didn't "fix" it.

Result: all four PRs green and mergeable, merged with merge commits carrying the operator's ratification line, and two automated releases cut and published by release-please.

## Judgment calls

| Decision | Why |
|---|---|
| Reversed "move the games into the core" partway | The operator realised it was the *randomness* they wanted unified, not the games. I undid the move (kept on an unpushed local backup branch) rather than defending finished work |
| A rejection is a signed act | An audit trail that records only approvals can't show what was turned down |
| Kept the frozen records frozen | The new reader got a "successor" note *beside* the old experiment instead of an edit to it |
| Followed the existing code on one spec mismatch | The design spec said one case should read "unreachable". The code deliberately said "escalate", and a test explained why. I kept the code and recorded the difference |
| Didn't call a flaky-looking failure a flake | Every red CI run was traced to a cause: a wrong branch name, a circular checkout, a path assumption, a missing fallback |

## Work in progress: an honest forecast ledger

Apps that promise market gains hide their track records. This ledger uses the same core to make one that can't be faked. Each call ("SPY closes up on Friday, 60%") is recorded and sealed by the human before the market opens, timed by the public drand beacon rather than the computer's clock. The close is read from a price source and written to the record. Every call is then graded by Brier score, the losers included. Paper only: nothing trades, and no edge is claimed. The point is a record that can't lie about whether there is one.

| Status | Detail |
|---|---|
| Built and tested | 42 tests, mutation 14 of 14 |
| Not yet run live | The development sandbox couldn't reach the price source or the beacon, so live use waits on the operator's own machine |

## Claim boundaries

| Claim | Provenance |
|---|---|
| The four PRs merged and the two releases published on 2026-10-20 | `measured`: the linked PR and release pages |
| The suite figures in the PRs (for example 1259 passed, 33 skipped in the core suite) | `measured`: suite runs in the development sandbox on 2026-10-20 |
| The mutation counts | `measured`: mutation scripts run during development and recorded in the commit messages |
| The live beacon and price source behave as the offline test readers do | `assumed`: not run live from the sandbox |
| Fitness for any particular production deployment | Not claimed. This is a one-operator system |

## What it demonstrates

| Area | Signal |
|---|---|
| CI/CD and release engineering | Cross-repo CI made green by root cause, not reruns; release-please automation |
| Test engineering | Parity tests, mutation testing, a test for every forbidden act |
| Security-minded design | A human-only trust root, signed approvals and rejections, a tamper-evident record |
| Systems integration | Copies consolidated into one core without changing behaviour, across three organisations |
| Working with a decision-maker | Proposals, recorded decisions, and course reversals taken without friction |
