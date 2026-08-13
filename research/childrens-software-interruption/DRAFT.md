# Nobody Counts the Ad Breaks

**Sean Campbell** · Working draft · August 2026

**Tags:** `childrens-software`, `interruption`, `dark-patterns`, `attention-economy`, `local-first`, `provenance`, `measurement-gap`, `waydroid`, `f-droid`, `parental-consent`, `coppa`, `loot-boxes`

---

My kids came to me on a Saturday and asked to play a game. A silly one. The kind of thing that is thirty years old in every way that matters — a small loop, a few rules, no reason it should require anything of anyone.

We do not have an emulator on the machine, so we went looking on the web. That is the only detail in this paper that is really about my household, and it is the one that mattered most: the browser was not a preference. It was the only door available.

Every version we found was ad-walled, account-gated, or a malware trap dressed as a game — a play button surrounded by a dozen other buttons that also said play, each one an interstitial wearing the costume of the thing we came for. When we finally got into something that ran, it served an ad every five moves unless we paid for premium.

I was not playing. I was watching. And what I watched, for most of an afternoon, was two kids spending more time dismissing interruptions than playing the game.

---

## The session looked great

Here is the part that has stayed with me. On the other end of that afternoon, in whatever dashboard the studio keeps, our session was a success.

Long time-on-app. High interaction count. Repeat returns to the tab. Every signal that instrument collects went up, and every one of them went up *because* the experience was bad. My kids' frustration and my kids' delight are the same shape at the metrics layer. There is no field in that system that can tell them apart, and no commercial reason to build one.

I have written this argument before in a different room. Assessment systems are built to see output, not learning, and they report the answer as though it were a measurement of understanding. A student who knows something and cannot produce it in the expected format gets counted as not knowing it. The gradebook is not lying, exactly. It is reporting faithfully on a proxy and then letting the proxy stand in for the thing.

Engagement telemetry does the same trick on the same afternoon. Time-on-app is a proxy for enjoyment the way a worksheet is a proxy for understanding: correlated often enough to feel like a measurement, and wrong in a direction that is not random. The kid who is having a wonderful time and the kid who is mashing the close button on an interstitial both register as engaged. The error does not distribute evenly, either. It is largest exactly where the interruption load is heaviest, which is to say largest in the products aimed at the youngest users with the least money.

The proxy is not merely imprecise. It is inverted. A worse experience produces a better number.

---

## What this paper is not

It is not a screen-time argument. I am not going to claim that games are bad for children, that the previous generation had it right, or that the correct amount of any of this is less. My kids were doing something reasonable, and so was I.

It is not an argument that the children are the problem. A nine-year-old clicking the biggest, brightest button on a page did not fail a literacy test. There was no signal to read. The design goal of that page was that no signal be legible, and the design succeeded. Blaming the reader for a document engineered to be unreadable is not analysis, it is just an older person's reflex.

And it is not a call for a new law. The laws are coming anyway, and the record below shows regulators moving faster on this than on most things. This paper is about a narrower and more stubborn problem that regulation has not touched: the fact that the harm has no number attached to it that a parent can look up.

---

## The record already exists

Almost everything I noticed that Saturday has been documented, litigated, or measured by someone more rigorous than me. It is worth walking through what is already established, because the gap only becomes visible once you see how much is not a gap.

**The regulators have named the mechanism and priced it.** In December 2022 the Federal Trade Commission settled with Epic Games for $520 million — $275 million as a civil penalty for children's privacy violations under COPPA, and $245 million in refunds for billing practices the Commission characterised as dark patterns that duped players into purchases. That second number is the important one: it is a United States regulator putting a price on interface design, separately from privacy. In June 2025 the FTC distributed over $126 million of it to nearly a million Fortnite players. In January 2025 it entered a stipulated order against Cognosphere over *Genshin Impact* — $20 million, COPPA again, plus a requirement to block under-16 in-game purchases without parental consent. The same month it finalised amendments to the COPPA Rule. In June 2025 it convened a workshop titled "The Attention Economy: How Big Tech Firms Exploit Children and Hurt Families," and in February 2026 it issued an enforcement policy statement on age-verification technology.

**Consumer bodies have documented the specific moves.** The Norwegian Consumer Council's report *Insert Coin: How the Gaming Industry Exploits Consumers Using Loot Boxes* is the most mechanism-level document in the pile, and the one closest in method to how I try to work. It does not argue that monetisation is distasteful; it names the operations. Virtual currencies that break the link between a purchase and its cost in money. Artificial scarcity — limited packs, limited windows — manufactured to convert deliberation into impulse. Design that targets known cognitive vulnerabilities, in products whose users include millions of minors. It names EA and the publisher of *Raid: Shadow Legends* specifically. More than twenty consumer organisations across eighteen European countries endorsed it and asked their governments for a ban on deceptive design, additional protections for minors, and disclosure that lets a buyer know what they are buying.

**Researchers have run the compliance audits.** Leon Y. Xiao's work is the closest thing in this literature to the discipline I want, because he does not ask whether companies say the right things — he counts whether the mechanism is present. In a content analysis by Xiao and Solip Park, published in *Acta Psychologica* in 2025, ninety of the hundred highest-grossing South Korean iPhone games contained paid loot boxes, and 84.4% of those ninety — seventy-six games — actually disclosed their probabilities under the law that became mandatory in March 2024. An earlier study by Xiao with Laura Henderson and Philip Newall put compliance among the hundred highest-grossing UK iPhone games, operating under industry self-regulation rather than law, at 64.0%.

That pair of numbers is the argument about self-regulation stated as a measurement rather than an opinion. Two cautions on reading it. They come from separate studies of separate markets in separate years, so the gap between them is a comparison and not a controlled contrast — the authors' own title, "Better than industry self-regulation," makes the comparison, but the design does not isolate the law as the cause. And the legally mandated figure is not 100%. Roughly one in seven games under an actively enforced statute still did not disclose, and the study's further finding is that among those that did, accessibility and visual prominence were frequently poor. A disclosure a parent cannot find is not distinguishable, at the moment of decision, from one that does not exist.

**Advocates have filed.** Fairplay — the organisation that used to be the Campaign for a Commercial-Free Childhood, and which is what people mean, dismissively, when they say a mothers' group — files with Georgetown Law's technology clinic drafting. Their comments to the FTC on dark patterns lay out how the specific tactics map onto specific developmental facts: fear-of-missing-out mechanics against immature executive function, endless content against undeveloped stopping ability, in-game currencies with arbitrary denominations against a still-forming grasp of abstract value. More recently they and the National Center on Sexual Exploitation asked the FTC to investigate Roblox, with the virtual-currency system named explicitly in the filing.

**And the census work tells us how much of this children are exposed to.** Common Sense Media's 2025 census covers children zero to eight — the aggregation matters, because this is the youngest band and says nothing about teenagers — drawn from an online survey of 1,578 parents fielded in August 2024 and published the following February, against a prior wave run in early 2020, just before the pandemic.

The headline figure is not the one usually quoted. Total screen media use barely moved: 2 hours 27 minutes a day, against 2 hours 24 minutes in 2020. What moved was the composition. Gaming rose to an average of 38 minutes a day across the whole zero-to-eight band, a 65% increase in five years, with five-to-eight-year-olds going from 40 to 64 minutes and two-to-four-year-olds from 16 to 21.

That is a better fact than the one the screen-time argument wants. The total held steady and gaming took a larger share of it — meaning the exposure to the interruption economy specifically went up by roughly two thirds during a period when children were not, in aggregate, looking at screens more. This is a displacement, not a flood, and it is the reason a paper about ad breaks is not a paper about screen time.

Ofcom's *Children and Parents: Media Use and Attitudes* report, 2026 edition, published in May 2026 from fieldwork run between November 2025 and March 2026, covers ages six months to seventeen along with parents' own accounts of how they monitor and manage.

---

## What none of it tells a parent on a Saturday

Read all of that and you know a great deal. You know the mechanism, its legal price, its compliance rate under two different regulatory regimes, its developmental target, and roughly how many hours a week a child is exposed to the category.

You still do not know whether *this game*, the one your kid is asking for right now, interrupts them every five moves.

That is the whole gap. The regulatory record is retrospective and per-company: it tells you what Epic did in 2022 and what Cognosphere did before 2025. The audit literature is aggregate and top-ranked: it tells you about the hundred highest-grossing titles, which are not the ones a seven-year-old finds. The census work is population-level by construction. The advocacy filings are about platforms, not about titles. Every one of these is good work and none of them resolves to the unit of decision — one app, one child, one afternoon.

The commercial market does resolve to that unit. Ad-load, session interruption, monetisation mix, and publisher ownership are all tracked in fine detail by Sensor Tower, data.ai, Tenjin, GameAnalytics, and their competitors. The data exists, it is good, and it is sold by subscription — to the publishers buying and selling the ad inventory.

So the measurement of the harm sits behind exactly the same account-server-subscription wall as everything else I have complained about, one layer up. A parent cannot buy it, and would not know it existed to buy.

---

## Two things that are already machine-readable

There are two exceptions, and they are the seed of everything that follows in this paper.

F-Droid, the free-software Android repository, carries an **AntiFeatures** field on every application in its catalogue: a comma-separated list, per build, with `Ads` and `Tracking` among the named values. `Tracking` is applied to apps that report activity somewhere without permission or by default. This is a published, versioned, machine-readable statement about behaviour rather than provenance, attached to the app, free to query.

It also comes with a caveat that is more instructive than the field itself. F-Droid's own documentation notes that `Ads` is rarely applied, because almost every application serving advertising does so through proprietary software — AdMob and its peers — and is therefore excluded from the repository upstream. So the absence of an `Ads` flag inside F-Droid does not mean an app was checked and found clean. It means the ad-supported population was filtered out before the flag had anything to say. The flag is honest about what it saw and silent about what it structurally cannot see, which is the correct behaviour and is also exactly the failure mode to watch for.

Exodus Privacy, a French non-profit, covers the complementary population. It performs static analysis on Android packages — no decompilation, just an inventory of which tracking libraries are embedded — and publishes the results in an open reports database with an API. It pulls its packages from Google Play, which is to say from precisely the lane F-Droid excludes. Their standing finding is that at least two thirds of Android applications carry trackers, and that ten or more in a single application is unremarkable.

Between them: one free, queryable source for the free-software lane and one for the commercial lane.

Neither of them measures interruption. Both measure embedded SDKs, which is a proxy — a good one, tightly correlated, and still not the thing. An app with an ad SDK might show one banner at launch or a full-screen interstitial every five moves, and no static analysis distinguishes those. Getting from the proxy to the fact still requires someone to sit down with the running application and count.

Which is what I did on Saturday, by accident, and which nobody has anywhere to record.

---

## The fact

If the thing that is missing is a fact, the first obligation is to say precisely what fact, in terms someone could actually go and produce. A field named `kid_friendly` is not a fact. It is a mood with a schema.

The fact I want is this: **how many times, in ten minutes of ordinary play, does the application stop the child in order to show them something they did not ask for.**

That definition is doing specific work. It counts interruptions rather than advertisements, because a paywall prompt, a rate-us modal, a daily-reward popup and a video ad are the same event from the seat the child is sitting in — the game stopped and something else wants attention. It is per unit of *play time* rather than per session, because sessions are not comparable and because the studio's own telemetry is already denominated in session length, which is the number I do not trust. And it is observed during ordinary play rather than during a scripted test, because the interruption schedule in these products is frequently adaptive, and a clean-room run is exactly the condition under which it behaves.

Three things travel with the count, because without them it is not usable.

**How the interruption ends.** Skippable immediately, skippable after five seconds, unskippable, or — the case that made me want the field in the first place — dismissible only through a close target small enough or misplaced enough that missing it opens the advertisement. That last one is not a worse version of the first. It is a different mechanism: the interruption has been engineered so that the attempt to escape it is itself monetised. A parent who knows "one ad every five minutes" and does not know that has not been told the important part.

**The version it was observed on, and the date.** This is the part that keeps the record honest over time and the part that would be easiest to skip. An interruption count is a measurement of a build. The next release can change it, and in this category will, because ad load is a tuning parameter that product teams adjust continuously against revenue. A number observed on version 3.1 says nothing whatsoever about 3.2. Binding the count to a version and a date is what stops a measurement from silently becoming a superstition.

**Who observed it.** Not for credit. Because a count produced by a parent watching their own child for ten minutes and a count produced by a person running a device farm are different kinds of evidence, and a reader is entitled to know which one they are holding.

---

## Three states and a floor

Every interruption record carries a provenance state, and there are only three.

`measured` means a person watched the application run and counted. `fitted` means the number was derived from something adjacent — the ad SDKs present in the package, the publisher's other titles, the monetisation model declared in the store listing — by a stated rule. `assumed` means nobody has looked.

`assumed` is the default, and it is a value, not an empty cell. This is the part I would defend hardest, because it is the part that everything else rests on. An app with no interruption record and an app measured at zero interruptions are opposite facts, and a catalogue that renders them the same way — a blank space, a missing badge, a quiet omission — has started lying without anyone deciding to lie. "Nobody has checked this" is information. It is, for a parent choosing at nine on a Saturday morning, quite often the *most* actionable information available, because it tells them the thing in front of them is unexamined and their own ten minutes is the only instrument in the room.

When several facts combine into one view, the view is worth its weakest input, propagated by `min()` across the ordering `assumed < fitted < measured`. A catalogue entry that pairs a measured interruption count with an assumed tracker inventory is an assumed entry. Not seventy percent confident. Not two stars out of three. Assumed, because a chain of reasoning does not get stronger than the loosest thing in it, and averaging is the operation by which that fact gets hidden.

And there is one demotion rule that has to be automatic, or the whole scheme rots quietly: **a `measured` record whose observed version does not match the installed version is not `measured`.** It falls back to `fitted` — the old count is still evidence about this publisher's behaviour, which is what `fitted` means — and it does so without anyone remembering to do it. A measurement that does not decay when its subject changes underneath it is worse than no measurement, because it carries the authority of having been checked while describing a build that no longer exists.

---

## Why it is not a score

The obvious next move is the wrong one, and it is worth naming before someone makes it.

The obvious move is to roll the interruption count, the tracker inventory, the age band and the monetisation model into a single number between one and five, put it on a badge, and let parents sort by it. Every instinct in software design points that way. It is also the exact failure this paper opened by describing.

A composite score is a proxy. It would be built by someone choosing weights, and those weights would encode a judgement about how bad an unskippable ad is relative to three trackers, which is not a measurable quantity and is not the same answer for every family. Then the number would be displayed, and it would be sorted on, and within a release or two it would be the thing publishers optimise — at which point it would stop measuring interruption and start measuring compliance with the scoring function, in precisely the way time-on-app stopped measuring enjoyment.

I have written this rule before in a different domain and it holds here without modification: **measurement is not evaluation.** The system reports what was observed. A person decides what it means. Nothing in it should produce a number that competes with a parent's judgement, because the moment it does, the judgement defers to it, and the thing being deferred to is a weighting somebody picked.

So the parent inbox shows the count, its provenance state, its observation date, and how the interruption ends. Four facts, unweighted, uncombined. Whether that is acceptable for this child on this Saturday is not a question the software is entitled to an opinion about.

---

## Where it lives

Three places, and the ordering matters.

In the **application manifest**, as a first-class field beside the existing declarations about network access and data streams — because that is where a claim about behaviour belongs, next to the other claims about behaviour, in the file that gets linted.

In the **catalogue entry**, so it is visible at the moment of browsing rather than only after installation. A fact that arrives after the decision is a receipt, not a gate.

And, at the moment a parent grants or refuses, **copied into the disposition log** as it stood at that instant. This is the one that is easy to leave out and the one I would insist on. The log's job is not to record what is currently true about an application; it is to record what was known to the person who made the decision, at the time they made it. Those diverge immediately — the app updates, someone measures it properly, the count changes. A log that keeps only the current value can confirm the present state but cannot be used to ask whether the reasoning was sound. Corrections land beside the record, never on top of it, and a grant made on an `assumed` record that later measured badly should remain legible as exactly that: a reasonable decision made with thin evidence, not a mistake retroactively made to look like negligence, and not a good call retroactively made to look like foresight.

---

## The gate

None of this is real until something can fail.

The mechanism is a lint that refuses a child-facing catalogue entry carrying no interruption state — not a warning, a failure, in continuous integration, on the pull request. Blank is the one value that is not allowed. `assumed` passes, because admitting nobody has looked is honest and is frequently the truth. Nothing at all does not pass, because that is the state in which the catalogue silently implies more than it knows.

Two further checks earn their place. The version-drift demotion above must be enforced rather than documented, or it is a paragraph in a README that everyone has read and nobody has run. And the lint itself must be broken on purpose to confirm it catches what it claims to: add an entry with a missing state and watch it fail, add one with a stale version and watch it demote. A gate that has never been observed failing is a decoration. The precedent for this already exists one directory over in the store, where a suite of browser games ships a mutation pass whose entire job is to break one mechanism per game and require the tests to notice.

---

## What this cannot see

A coverage claim is a claim about the harness, and the honest version of this one is unflattering.

The two free machine-readable sources cover Android packages. Between them they see the free-software lane and the commercial lane, and their subject in both cases is *embedded libraries*: which advertising and analytics SDKs are compiled into the file. That is a strong signal for whether interruption is possible and no signal at all for how often it happens. An application carrying one ad SDK might show a banner at launch or stop the child every five moves, and no amount of static analysis separates those. Everything above `fitted` requires a human being and a clock.

Which means the measured tier does not scale, and I am not going to pretend otherwise. It scales to as many applications as there are people willing to sit and watch one for ten minutes. That is a real limit, it is not fixable by cleverness, and the correct response to it is `assumed` on everything nobody has done, forever, rather than a synthetic estimate wearing a measured badge.

The larger blind spot is worse and closer to home. All of this machinery gates *installed applications*. The afternoon that produced this paper never involved an installation. It happened in a browser, on the open web, where there is no manifest, no catalogue, no package to analyse, and no version to bind a measurement to. The gate I am describing would have been switched on that Saturday and would have seen nothing, because the failure occurred entirely upstream of the thing it watches.

That is not a reason to abandon it. Getting a working local library onto the machine is what removes the reason to go to the open web looking for a game in the first place, and the honest description of the gate is that it is a supply-side fix: it makes the good path good enough to use, and it says nothing about the bad path. But it does mean the claim has to be stated at that size. This does not protect a child on the web. It reduces the number of afternoons that end up there.

---

## What I did about it, on a Sunday afternoon

I built the thing described above, or the part of it that fits in an afternoon.

It is a catalogue a parent writes and a child chooses from, with a request that
goes to a parent, who grants or refuses with a reason — either way, into a log
that is appended to and never rewritten. A grant checks the file's digest
against what was recorded and installs it, and writes down what happened,
including when that fails. Every entry carries an interruption record with a
provenance state, a measurement demotes itself when the build moves underneath
it, and an entry with nothing recorded does not load at all. There is no score
anywhere in it. Eleven of its mechanisms get broken on purpose in its test
suite, and each one has to make exactly the test that claims to cover it fail,
because a gate nobody has watched fail is a decoration.

Now the part that matters more than any of that.

**The catalogue has four entries and every one of them says `assumed`.** Nobody
has watched a child play any of them. There is no APK on disk with a recorded
digest, so the install path — the part I was most careful about — currently
refuses everything it is asked to do, correctly, on the grounds that it has
nothing verified to install. The game my kids asked for on Saturday is not in
it. If they had come to me on Sunday evening with the same question, this would
have helped them not at all.

So what got built is a filing cabinet. A good one, with locks that work and a
drawer that will not close on an unlabelled folder. It is completely empty.

I want to be plain that this is the honest state of it rather than an
embarrassing one, because the alternative was available and I could see the
shape of it while I worked. I could have populated those four entries from the
tracker inventories, called it `fitted`, and had a catalogue that looked
finished. I could have shipped a badge — green, amber, red — computed from
whatever I had, and it would have demoed beautifully. Both would have produced
something more impressive on a Sunday evening and less true, and the paper you
have just read is an argument about exactly that trade, so making it in the
artifact would have been the loudest possible way to lose the argument.

An empty catalogue that says `assumed` four times is telling the truth. That is
the only claim I am making for it.

## The instrument was in the room the whole time

Here is the thing I did not expect, and it is why the afternoon was worth
spending.

Everything in that app is machinery for *recording* the fact. None of it can
*produce* the fact. There is no code path in it that can reach `measured`, and
I checked — there is a test that fails if one appears. Getting a real number
into that field requires a person to sit with a child for ten minutes and
count, and no amount of engineering shortens that or does it on their behalf.

Which is what I was already doing on Saturday, before any of this existed and
without calling it anything. Not playing. Watching. Noticing that more of the
afternoon went to dismissing interruptions than to the game, which is a
measurement — an aggregate over one session, one child, one build, with no
instrument but attention and no place to put the result.

I have written this before about a different room. A teacher who has watched a
specific student for months knows things about how that student's understanding
surfaces that no rubric captures, and that knowledge is some of the most
accurate assessment data in the building, and it cannot travel. It gets
classified as impressionistic. What it needs is not new technology. It needs
*language*: shared, specific, calibrated, so that what a professional observed
can be written down in terms that hold up to somebody who was not standing
there.

The interruption record is that, for a parent on a Saturday. `count_per_10min`,
how the interruption ends, what build, what date, who watched. Five fields that
turn "that game is awful, it kept stopping" — true, unarguable, and useless to
anybody else — into something a second parent can read, disagree with, or check.

That is a much smaller claim than the one I set out to make. I began this
thinking the gap was a missing dataset, and that the answer was to go and get
it. The regulators have the enforcement record. The consumer bodies have the
mechanism. Xiao has the compliance rates. Common Sense and Ofcom have the
exposure. Sensor Tower has the ad-load, and sells it to the people buying the
inventory. What nobody has is the one number at the unit where the decision
actually gets made, and having spent an afternoon building the place to put that
number, I now think the reason nobody has it is not that it is hard to collect.

It is that it can only be collected by the person who was already going to be in
the room, and until this weekend there was no reason for them to write it down.

I have four rows that say nobody has looked. The first one that says otherwise
is going to take me ten minutes, on a Saturday, doing the thing I was doing
anyway.

---

---

## Sources

*A departure from the house style in the other research drafts, which name sources inline and carry no reference section. Included because this paper's central claim is that a specific fact is unavailable to ordinary people, and that claim is worth nothing if the facts I do cite are not themselves traceable. Drop it if it does not fit the packet.*

*The Provenance column uses this paper's own three states, turned back on the paper's own evidence: `measured` means the primary was read at first hand, `fitted` means the figure was corroborated across independent secondary sources by a stated rule but the primary is still unread, `assumed` means a single source or none. Only the two rows read at first hand earn `measured`; calling a second-hand corroboration `measured` would be the exact conflation the paper is about, committed in its own reference table.*

| Claim | Source | Provenance |
|---|---|---|
| Epic Games settlement: $275M COPPA penalty, $245M dark-pattern refunds, Dec 2022; $126M distributed June 2025 | FTC, gaming industry topic page and press releases | `fitted` — secondary summary, primary order not yet read |
| Cognosphere / *Genshin Impact*: $20M stipulated order, Jan 2025 | FTC | `fitted` — secondary summary |
| COPPA Rule amendments finalised Jan 2025; "Attention Economy" workshop June 2025; age-verification policy statement Feb 2026 | FTC | `fitted` — secondary summary |
| Loot-box dark patterns; 20+ groups across 18 countries endorsing | Norwegian Consumer Council, *Insert Coin*; BEUC | `fitted` — secondary summary, full report not yet read |
| 90/100 top-grossing South Korean iPhone games contain paid loot boxes; 84.4% (76/90) disclosed probabilities under the law mandatory from Mar 2024; disclosures often poorly accessible or prominent | Xiao, L. Y. & Park, S., *Acta Psychologica*, 2025; open access at PMC12583229 | `fitted` — figures corroborated across three independent secondary sources; 84.4% confirmed internally consistent with a 76/90 denominator; full text unread |
| 64.0% disclosure compliance among 100 top-grossing UK iPhone games under industry self-regulation | Xiao, Henderson & Newall, SSRN 3934941 | `fitted` — separate study, separate market, separate year; **not a controlled contrast** with the Korean figure |
| Dark-pattern tactics mapped to developmental stage; Roblox FTC complaint with NCOSE | Fairplay, comments drafted with Georgetown Law tech clinic | `fitted` — secondary summary |
| Total screen media 2:27/day vs 2:24 in 2020; gaming 38 min/day, +65%; 5–8yo 40→64 min, 2–4yo 16→21 min — **aggregation: children aged zero to eight; n=1,578 parents; fielded Aug 2024; prior wave early 2020** | Common Sense Census 2025, *Media Use by Kids Zero to Eight* | `fitted` — corroborated across three independent secondary sources; PDF unread |
| 40% of children have their own tablet by age 2 | Common Sense Census 2025 | `assumed` — single secondary source, wording unconfirmed; **do not use until checked** |
| Children's media use, ages 6 months–17, fieldwork Nov 2025–Mar 2026 | Ofcom, *Children and Parents: Media Use and Attitudes*, pub. 21 May 2026 | `fitted` — secondary summary |
| `AntiFeatures` field with `Ads`/`Tracking`; `Ads` rarely applied because ad-serving apps are excluded upstream | F-Droid documentation, Anti-Features page | `measured` — primary docs read |
| Static tracker analysis, open reports DB + API, packages sourced from Google Play; ≥2/3 of apps carry trackers | Exodus Privacy | `measured` — primary docs read |
| Ad-load / ownership data sold by subscription | Sensor Tower, data.ai, Tenjin, GameAnalytics | `assumed` — inferred from vendor marketing, no pricing sheet obtained |

**Verification debt.** Every row marked `fitted` traces to a corroborated secondary source rather than the primary document. Clearing it means promoting those rows to `measured` — reading the primary — and it must be done before this leaves draft, because a paper whose thesis is traceability cannot rest its own figures on second-hand corroboration.

The two rows doing the most argumentative work — Xiao's compliance percentages and the Common Sense gaming figures — have been raised from a single summary to corroboration across three independent secondary sources each, with publication venue, authorship, sample size and fieldwork dates now pinned. The Xiao figure additionally survives an internal check: 84.4% resolves to exactly 76 of 90, an integer, which a garbled transcription would be unlikely to do. That is better than where this started. It is still not the primary.

**Why it stopped there.** The session this draft was written in routed all outbound traffic through a policy-enforcing egress proxy that permitted GitHub and nothing else. PubMed, Europe PMC, ScienceDirect, the DOI resolver, Crossref, Common Sense Media, the FTC and F-Droid all returned 403 at the proxy. Every primary document cited here is publicly available and free — the Korean study is open access — and none of them was reachable from where this was written.

Labelling those rows `fitted` rather than `measured`: the constraint is environmental, it is not resolved, and a reader deserves to know the difference between a figure checked against its primary and one corroborated only at second hand. Which is, unhelpfully, this paper's entire thesis arriving early and at my own expense.
