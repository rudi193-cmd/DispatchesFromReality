# The Third State — frame

*Working title. Frame only — structure, load-bearing material, and what's still missing.
No prose written yet.*

**Working subtitle:** *On how I build, what three weeks of maintenance did to it, and
a silence I read as an answer.*

---

## The claim

Every system I've built in the last year enforces one discipline: **absence must never
be rendered as an answer.** A queue that can't be reached must not paint "queue clear."
A model's output is `draft` until a human seals it. A missing consent file reads as
denied, because absence is not consent. Surfaces need three states, not two — empty,
populated, and **unknown**.

I spent months making machines obey that rule, and then read two silences as a no
about my own work, and put an idea down for eight months.

## The arc

1. Background video while grinding through maintenance → an eight-month-old shelved
   pitch surfaces
2. What the maintenance actually was, from the commit record
3. How I build when it's working — and where agents fit
4. Why maintenance broke it, structurally rather than emotionally
5. The third state, and the silence I mis-filed
6. Ninety minutes, and the inversion: start with the kids
7. Close — the corps still haven't answered

---

## I. The open channel

Drumeo playing in the background while working. Recommendations drift into the current
DCI season. A pitch shelved in November comes back.

**The tell, and it opens the essay rather than being buried:** there was *room* for
background video. Work that has all of your attention doesn't leave a channel open for
something else to come in through. The fact that an algorithm could reach me is data
about what the preceding weeks were.

**Second detail worth keeping:** the idea survived eight months of neglect intact
enough to build against in ninety minutes. Most shelved ideas don't. "I put this down
and it was still there" is a better sentence than "I had a new idea."

## II. Three weeks, from the commit log

Don't characterise this — show it. The record is unambiguous and dated.

| Window | What happened |
|---|---|
| Jun 21 – Jul 6 | Sovereignty v3, then **five essays in nine days**: The Same Door, the toaster piece, Somebody Has to Sit Down With You, Nobody Adds It Up, the Applied Governance draft |
| Jul 9 onward | willow-mcp takes 200+ commits in twenty days — 57 on the 9th, 48 on the 21st, 48 on the 23rd |
| Same period | willow-2.0's hundred commits are 26 `docs` and 21 `fix`. Willow is box-scan, remediation-status, handoff, ratify. willow-grove is FLEET_SEAMS, then corrections *of the corrections* |
| Jul 6 → tonight | **Dispatches goes silent.** Two doc fixes and one story |

The essays stopped the week the migration started.

And name what the migration is: willow-2.0 → willow-mcp. A consolidation matrix across
24 repos and 289 clusters with no completion markers on any row. Two live repos each
declaring the other archived. One table created by both with different shapes, where
boot order decides which schema wins and the loser silently no-ops.

My own commit calls it: *"Break 0 — fleet ownership contested — it is the root of every
other break."*

**The line this section has to land:** output was never the problem. The volume was
enormous. It was reconciliation, and you can only be as interested in a reconciliation
as you are in the thing being reconciled.

## III. How I build when it's working

The practice, stated concretely — this is where the agent material lives, and it lives
*inside* the arc rather than as a listicle.

**Everything is built so the next session is cheaper than this one.** `tools/` exists
because each script "turns conversational labor into a script, so the next session runs
the tool instead of re-deriving the work." `gap_log` records what isn't known yet so it
isn't rediscovered. The ledger outlives the session that wrote it. Nestor makes one
human verification into permanent capital — verified once, served forever.

**Asking and granting are separate authorities, and the filesystem enforces it, not
etiquette.** `grant-net` is local CLI only: an agent may request egress and may never
grant it to itself. `confirm-binding` is operator-only — a remote caller must never
confirm its own binding. `allow-permission` is CLI-only, because an agent must never be
able to grant itself a permission it was just denied.

**And the thing agents genuinely cannot do**, in my own words from a commit two days
ago:

> The survey agents were asked where code IS, and that question cannot tell a port from
> an original — both look like live implementations from that angle. Only the
> migration's intended direction separates them, and that information existed nowhere
> in the repositories; it came from the operator.
>
> …ask a human which way the migration runs before inferring anything further.

Agents map what exists. Only I hold the direction of travel. Intent isn't in the
artifacts, so it can't be surveyed or delegated or recovered from the code.

## IV. Why the maintenance broke it

The mechanism, not the mood — this is the section that makes the piece useful to
someone else.

The one contribution no agent can supply is direction. For three weeks I spent all of
it pointing backwards, at reconciling two versions of a thing I'd already built. Not
choosing what should exist — adjudicating what already did.

High output, no direction spent forward. That's not burnout and it isn't laziness. It
is the specific exhaustion of using your only irreplaceable faculty on bookkeeping.

*Still open (see below): was the migration chosen, or did it keep demanding attention
until nothing was left over?* The section reads differently depending, and it should be
answered before drafting.

## V. The third state

November: a pitch sent to two World Class corps — Tempe, Denver.

**No acknowledgment from either.**

Not a no. A rejection resolves; an unanswered thing stays open, and an open thing you
can't act on just sits.

Then the turn, and it uses my own constraint against me:

> **Constraint 1 — never render absence as assurance — is marked load-bearing.**
>
> Grove's human pane catches every exception, returns `[]`, and paints `✓ queue clear`
> — so *"I could not reach the queue"* and *"nothing is waiting"* are the same pixels,
> with a green check on the failure. The fix is a third state: these surfaces have
> empty and populated but no **unknown**.

Nestor: sealed, draft, **pending** — "nothing to offer, said plainly rather than
improvised." willow-mcp: "absence is not consent." Severance: "an unverifiable claim is
not a passing one."

No acknowledgment is `unknown`. I filed it as `empty`. That's why it sat — I thought I
had a result, so there was nothing to retry.

**Do not over-polish this section.** The parallel is strong enough that pushing it
becomes cute. State it, let it sit, move.

## VI. Ninety minutes, and the inversion

Tonight: opened the abandoned pitch and started building it. Apache-2.0, open source, a
give-back to the drum corps community. Broad operational tooling for a corps.

**And then inverted the map — starting with the kids.**

That's the section's whole point and it is a design decision, not a sentiment. Org
software is normally built admin-first, with the member as a row hanging off a program.
Inverting it makes the person whose data is most sensitive the root of the schema, and
everything else hangs off *them*.

Which means child primacy stops being a policy layer bolted on after the fact and
becomes structural. It was already one of nine platform hard stops in Willow's
constitution; now it's the first table. Corps members are largely under 22 and many are
minors — rosters, medical forms, emergency contacts, guardians. That decision is free
tonight and expensive in six months.

**Why this section is the answer to section IV:** it's a decision with a direction,
made in ninety minutes, about something that doesn't exist yet. The opposite of
adjudicating what already does.

*Also honest here:* tour is genuinely the ideal local-first case — gyms with no wifi, a
hundred and fifty people, no budget for per-seat SaaS. This isn't a hobby detour from
the architecture. It's the architecture finally aimed at someone who needs it.

## VII. Close

Constraints on the ending, since this is the part most likely to go wrong:

- **Not triumphant.** Nothing has been solved. Nobody wrote back, the migration is
  still unfinished, and the app is ninety minutes old.
- **The available too-neat ending:** "and so I learned to give myself a third state."
  Don't take it.
- **The truer one:** the corps still haven't answered, and Apache-2.0 means the thing
  will exist whether they ever do. That isn't defiance — it's just what it looks like
  to stop treating a silence as a result.

Candidate final beat: I built the fleet on the principle that no gatekeeper should be
able to stop me, and then let two unanswered emails stop me for eight months. The
machines had the third state the whole time.

---

## What's missing before drafting

1. **What the app actually does** — the concrete feature. Everything above works, but
   §VI stays abstract without one real screen or workflow to name.
2. **The DCI connection.** Marched, taught, staffed, parent, fan from the stands? §I's
   voice depends on it and I won't guess.
3. **Was the migration chosen or imposed?** Changes §IV materially.
4. **Does the app have a repo yet?** Referring to a live URL is stronger than referring
   to an evening.
5. **Where this lives** — `essays/` (personal, arc-driven) or `professional/` (the
   constitutional-design material is portfolio-grade). It can't be both without
   splitting.

## Sources already in hand

Commit records across DispatchesFromReality, Willow, Nestor, willow-mcp, willow-2.0 and
willow-grove, 2026-06-20 → 2026-07-29. READMEs for willow-2.0, willow-mcp, kartikeya,
willow-gate, jeles, willow-1.9. Quotations in §III and §V are the author's own commit
messages and documentation, verbatim.
