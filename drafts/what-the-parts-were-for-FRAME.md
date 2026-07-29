# What the Parts Were For — frame

*Working title (alternates: "A Toolbox Is Not a Shop", "Ninety Minutes"). Frame only —
structure, load-bearing material, and what's still missing. No prose written yet.*

**Working subtitle:** *Sometimes you have to build something you care about to find out
what you've been making.*

---

## The claim

**Sometimes you need to build something fun to bring the pieces together — fun meaning
passionate about, not recreational.**

Not a break from serious work. The thing that *integrates* it. A year of building
components — a local-first stack, an authorization model, an assessment framework, a
rules-engine research packet, a verification ledger — each made in isolation, each
correct on its own terms, none of them ever required to be true at the same time.

A toolbox doesn't tell you what it's for. A job does. And the job has to be one you
actually want the outcome of, because nothing weaker pulls hard enough to make separate
parts prove themselves together.

The evidence: ninety minutes on a drum corps app used more of the last year's work than
three weeks of consolidating it did.

## The arc

1. Never marched, found out too late, couldn't have afforded it anyway
2. What three weeks of maintenance actually was, from the commit record
3. How I build when it's working — and where agents fit
4. Why maintenance broke it: consolidation without application
5. The third state, and the silence I mis-filed — why the parts sat unassembled
6. Ninety minutes, the convergence, and the inversion: start with the kids
7. Close — the corps still haven't answered

---

## I. Too late, and too expensive anyway

**Opening beat: I never marched.** Found out about DCI roughly a year too late — mostly
from peers who came back from a summer changed. Already on the college path by then,
school essentially lined up. And the honest second half, which keeps it from being
self-pity: I doubt I could have afforded it regardless.

Two barriers, and they are exactly the two that software can touch. **Information** — I
didn't know it was available until the window had closed. **Cost** — thousands in tour
fees, travel, and a summer of lost income, which is a documented equity problem in the
activity and not a grievance I'm inventing.

Register check: rueful, measured, done with. Not a wound. The Same Door earns its weight
by refusing to let a real harm become a story, and this gets the same discipline — one
paragraph, stated plainly, then move.

Then the present-day trigger: Drumeo playing in the background while working,
recommendations drift into the current DCI season, and a pitch shelved in November comes
back.

**The tell:** there was *room* for background video. Work that has all of your attention doesn't leave a channel open for
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

## IV. Consolidation without application

The mechanism, not the mood — this is the section that makes the piece useful to
someone else, and the sharper diagnosis is here rather than in "I was tired."

The one contribution no agent can supply is direction. For three weeks I spent all of it
pointing backwards — not choosing what should exist, adjudicating what already did.

But the deeper problem was not that it was backwards. It was that **nothing needed the
parts.** A migration merges components without ever making them do a job together. Three
weeks tidying a toolbox, and a toolbox cannot tell you what it is for.

High output, no application. That's not burnout and it isn't laziness. It is what it
feels like to maintain an inventory nobody is drawing from — including you.

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

That's the section's whole point, and it is a design decision *and* a personal one, in
that order. Org software is normally built admin-first, with the member as a row hanging
off a program. Inverting it makes the person whose data is most sensitive the root of the
schema, and everything else hangs off *them*.

The personal half, stated once and not belaboured: the person at the root of that schema
is the seventeen-year-old who doesn't know yet. §I's kid.

Which means child primacy stops being a policy layer bolted on after the fact and
becomes structural. It was already one of nine platform hard stops in Willow's
constitution; now it's the first table. Corps members are largely under 22 and many are
minors — rosters, medical forms, emergency contacts, guardians. That decision is free
tonight and expensive in six months.

**Why this section is the answer to section IV — and it needs the table, not a claim.**
One evening's build drew on nearly everything the year produced, and each piece had been
made separately for its own unrelated reason:

| Built for | Now doing |
|---|---|
| the sovereignty argument | gyms with no wifi |
| Termux support (Postgres + SQLite, one query) | office desktop, phone on tour |
| agent authorization — manifests, gates, permission groups | staff roles, minors, guardians |
| a constitutional hard stop (child primacy) | the schema's root table |
| the assessment-visibility white paper | judging sheets and captions |
| the tabletop mechanical-engines packet | how a show is scored |
| Nestor's sealed / draft / pending | any human-verified record |
| a year of fleet practice | how it got built in ninety minutes |

None of those were made for this. All of them are true at once here for the first time.
That is the whole argument, and the table carries it better than any sentence I could
write about it.

*Also honest here:* tour is genuinely the ideal local-first case — gyms with no wifi, a
hundred and fifty people, no budget for per-seat SaaS. This isn't a hobby detour from the
architecture. It's the architecture finally aimed at someone who needs it.

**And the cost barrier is addressable, which is the part worth saying plainly.** Apache-2.0
software a corps runs on its own hardware is money not spent on per-seat licensing. That
does not make a summer affordable for a kid, and the essay should not pretend it does. It
is one input to a cost structure, named accurately and not oversold.

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
able to stop me, and then let two unanswered emails stop me for eight months. The machines
had the third state the whole time.

**Alternative, possibly stronger, since it closes the loop to §I:** three absences, one
shape. At seventeen I didn't know it was available and filed that as *not available*. In
November two corps didn't reply and I filed that as *no*. For three weeks a queue that
could not be reached rendered as *clear*. Only one of those was a bug, and it's the only
one I fixed at the time.

---

## What's missing before drafting

1. **What the app actually does** — the concrete feature. Everything above works, but
   §VI stays abstract without one real screen or workflow to name.
2. **Was the migration chosen or imposed?** Changes §IV materially.
3. **Does the app have a repo yet?** Referring to a live URL is stronger than referring
   to an evening.
4. **Where this lives** — `essays/` (personal, arc-driven) or `professional/` (the
   constitutional-design material is portfolio-grade). It can't be both without
   splitting.

## Sources already in hand

Commit records across DispatchesFromReality, Willow, Nestor, willow-mcp, willow-2.0 and
willow-grove, 2026-06-20 → 2026-07-29. READMEs for willow-2.0, willow-mcp, kartikeya,
willow-gate, jeles, willow-1.9. Quotations in §III and §V are the author's own commit
messages and documentation, verbatim.
