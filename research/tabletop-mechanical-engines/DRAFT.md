# Tabletop Mechanical Engines And Narrative Generation

**Sean Campbell** · Working draft · June 2026

**Tags:** `game-design`, `tabletop`, `systems-design`, `probability`, `emergent-narrative`, `mechanics`, `rules-engine`, `gateway-momentum-engine`

---

A tabletop rule system is a machine.

That is not a metaphor I reach for to sound clever. It is the most accurate description I have. You feed the machine two things — player decisions and randomness — and it returns a third: consequences that nobody at the table fully chose, arranged into something that feels like a story.

The question that has held my attention for years is not *is the game fun.* Fun is real, but it is an output, not a design target you can aim at directly. The question I can actually work on is narrower and more useful: **what kind of machine is this, and what does it reliably produce?**

That is the same question I ask of a carburetor, a database, or an agent framework. It is why this research sits in the same portfolio as the software work. The subject is dice and factions instead of queues and embeddings. The instinct is identical.

---

## The two failure modes

Every rule system is trying to avoid two ways of dying.

The first is **arbitrariness**. If anything can happen, nothing matters. A system with no structure produces noise, not narrative. Players stop making meaningful decisions because no decision changes the distribution of outcomes. You might as well flip a coin and narrate the result.

The second is **rigidity**. If the outcome is decided before the dice fall — by an optimal build, a dominant strategy, or a railroaded plot — then the machine is not generating anything. It is replaying a cassette. Players stop making meaningful decisions because only one decision is correct.

Good design lives in the narrow band between these. Enough uncertainty that choices carry risk. Enough structure that choices carry meaning. The dice should be able to surprise you, but the surprise should be legible in hindsight — *of course that happened, the odds were always there.*

This is a probability problem before it is a creative one.

---

## Rules as source code

When I design mechanics, I treat the ruleset the way I treat a program.

The rules are the source code: the explicit, inspectable logic. Probability is the runtime: the thing that actually executes when the rules meet a real situation. Player agency is the input stream. And the narrative that comes out the other side is emergent behavior — output that no single rule wrote, produced by rules interacting under randomness.

That framing changes how you debug a game. A boring session is not a mysterious failure of "fun." It is a system producing a degenerate output, and degenerate outputs have causes you can find:

- A dominant strategy flattened the decision space
- The probability was illegible, so players could not form real plans
- Consequences did not chain, so mechanics never became story
- The frame was too loose, so outcomes felt arbitrary
- The frame was too tight, so outcomes felt predetermined

You fix a game the way you fix a system: find the rule interaction producing the bad behavior, change one constraint, and test whether the interesting behavior becomes more likely.

---

## The Gateway Momentum Engine

The clearest expression of this thinking is the Gateway Momentum Engine — a mechanics framework I built around momentum and gateway states rather than flat, isolated resolution.

The core design problem it answers is the chaining problem. In a lot of systems, each action resolves in isolation: roll, succeed or fail, move on. Nothing accumulates. The system has no memory, so it cannot build tension, and tension is where narrative comes from.

A momentum-based engine gives the system memory. Outcomes feed forward. A success is not just a success — it shifts the state that the next decision is made inside of. "Gateway" states are thresholds: points where accumulated momentum opens or closes options, where the situation tips from one regime into another.

The design goal is that strategy emerges from managing momentum across a sequence, not from optimizing a single roll. That is what turns a string of mechanical resolutions into a story with a shape: a build-up, a tipping point, a consequence that the players can trace back to their own choices three turns ago.

I frame the engine as proprietary in the sense that it is original, in-house design work — not as a claim that it is a finished, shipped commercial product. It is mechanics-framework research. The point of including it here is the design reasoning, not a sales pitch.

---

## Constraint as a generator

The most counterintuitive lesson in mechanics design is that constraint produces behavior. It does not only restrict; it generates.

One of the clearest cases came from a spatial design problem: an 8×8 board with fixed corners and a fluid interior — a rigid frame around a chaotic field. (In *The Gate*, this is bound up with the "Stillness" problem and the figure of Baba Yaga: how do you make a space that is structurally locked at its boundaries but unpredictable in its middle?)

The naive instinct is that structure kills emergence — that to get interesting play you should remove rules. The opposite is true. The fixed corners are exactly what make the fluid interior meaningful. Without the rigid frame, motion in the interior is just noise. With it, every move is measured against stable reference points, and suddenly position, approach, and timing carry strategic weight.

This is the same lesson schema design teaches in software. A completely free-form data store is not more powerful; it is less. The constraints — types, relations, boundaries — are what make the contents queryable, composable, and meaningful. Structure is not the enemy of emergence. Structure is its precondition.

---

## Worlds as rule economies

Custom campaign work — the Valley of Vander and the Drakonite setting, built on a 5e foundation — is where mechanics meet world-building.

A setting is not just lore. A well-built setting is an economy of rules: what items exist and what they cost in the system's currency of power, what factions want and what mechanical levers they can pull, what is scarce, what is abundant, what is forbidden. An item registry is not a list of treasure. It is a balance sheet. Every item is a small rule, and the set of items defines what strategies the world rewards.

The Felfs — a custom creature and faction — are an example of designing mechanical identity rather than flavor alone. A faction earns its place in the system when it changes how the game is played: when its stat block, abilities, and incentives create decisions that would not exist without it. The design question is never just "what are they like." It is "what does their presence make true at the table that was not true before."

Even named rules can carry double duty. A rule like the *Books of Mann*'s "Drebin Rule" is mechanically a constraint, but it is also a narrative object — a piece of the world that players reference by name. The best mechanics often work this way: they are simultaneously code and lore, doing structural work and story work in the same breath.

---

## The same instinct, two materials

I did not come to software design and game design separately. They are the same activity in different materials.

| Game-design concern | Software-systems parallel |
|---------------------|---------------------------|
| Probability legibility | Observability — can you see why the system did what it did? |
| Testing against degenerate strategies | Adversarial testing, edge cases, ingest gates |
| Constraint design | API boundaries, schema design, sandboxes |
| Emergent narrative | Emergent behavior from composed components |
| Momentum / state chaining | Stateful pipelines, feedback loops, memory |
| Balance | Performance and fairness under load |
| Named rules as objects | Named tools, policies, and contracts |

When I built Willow — a local-first AI coordination framework — I was solving the same problem I solve at the table. Given these components, these constraints, and this much nondeterminism, what does the system reliably produce, and is that what I wanted? A multi-agent framework is a rule system. The agents are players with incentives. The tools are the action economy. The coordination contract is the ruleset. And the failure modes are the same two: arbitrariness (agents do incoherent things) and rigidity (the system can only do one thing).

The discipline that keeps a game from collapsing is the discipline that keeps a distributed system from collapsing. Make the probability legible. Test against the degenerate case. Use constraints to make good behavior the path of least resistance.

---

## Method

The method is consistent across every system I design, physical, tabletop, or software:

1. Decide what behavior the system should reliably produce
2. Find the smallest rule set that makes that behavior likely
3. Model the probability explicitly — common, rare, impossible
4. Hunt the degenerate strategy before the players do
5. Tune constraints until interesting play is the easy path
6. Separate the mechanics that carry strategy from the flavor that carries story
7. State what the system is balanced for — and what it is not

Step 7 is the one most designers skip, and it is the one that matters most for honesty. A system is always balanced *for* something: a player count, a session length, a skill level, a tone. Naming that boundary is the difference between design research and a marketing claim.

---

## What this is and is not

This is design research and mechanics prototyping. It demonstrates systems thinking under a different set of constraints than code: probability, incentives, player psychology, and balance.

It is not a published or commercially released game line. The Gateway Momentum Engine is original design work, not a shipped product. The campaign, creature, and faction material is structural world-building, not a printed supplement. The playtest evidence is enthusiast-scale, not statistically balanced at commercial volume.

What it shows is the thing worth showing: that the instinct to build constrained generators — systems that produce rich, legible, emergent behavior from a small set of well-chosen rules — is the same instinct whether the runtime is a handful of dice or a Postgres-backed agent fleet.

The dice are honest about one thing software tries to hide. The outcome was never certain. Good design is just making the uncertainty *mean* something.

---

*Working draft. Public packet and claim boundaries: [README.md](README.md)*
