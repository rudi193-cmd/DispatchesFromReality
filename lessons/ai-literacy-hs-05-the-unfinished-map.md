# The Unfinished Map
**AI Literacy for High School · Lesson 05 of 06**
*Grades 9–12 · Computer Science / AI Literacy / Information Literacy · No devices required for core*

---

> *"Confidence is not accuracy. Fluency is not truth.
> The map looks complete. That doesn't mean the territory is."*

---

## Overview

The first four lessons in this series built the conceptual scaffolding:
AI guesses, it reflects whose data trained it, it was built on data
gathered without meaningful consent, and the question of what it actually
*does* when it seems to understand is genuinely unresolved.

Lesson 05 is where all of that becomes a practical skill.

Students are going to use AI. They already do. The goal of this lesson
is not to stop them — it is to make sure they do it with their eyes open,
with a working method for evaluating what comes back.

The central skill: **distinguishing confident-sounding output from reliable
output.** These are not the same thing. AI produces fluent, well-structured,
authoritative-sounding text regardless of whether the underlying content is
accurate. Students who can't tell the difference are at a genuine disadvantage.
Students who can are equipped for almost everything.

This lesson builds a class rubric — a shared evaluative framework that
students can carry forward into every subject and every context where
AI output appears.

---

## Learning Objectives

By the end of this lesson, students will be able to:

1. Identify at least three categories of AI output failure
   (factual error, outdated information, misleading omission)
2. Apply a practical evaluation rubric to an AI-generated response
3. Explain *why* a specific output failure occurred in terms of the
   prediction model from Lesson 01
4. Articulate the limits of their own ability to verify AI output —
   and what to do about those limits

---

## For Teachers

**Suggested time:** 50 minutes

**No devices required for the core lesson.**
Response cards with printed AI outputs are provided in Appendix A.
Device-based extension described at the end.

**Facilitation notes:**

The productive tension in this lesson is between two true things:
AI output is often useful, *and* it is often wrong in ways that are hard
to detect without effort. Both of these things are true simultaneously.
Students who only hear "AI is unreliable" learn nothing practically
useful. Students who only hear "AI is a helpful tool" are underprepared.

The class rubric built in Part 4 is the most important output of this
lesson. Take time on it. Write it on the board as students generate it.
Photograph it or type it up and share it — it is a document students
made together, which gives it more sticking power than a rubric you hand them.

One thing to name directly: **some AI errors are undetectable without
domain knowledge.** If you don't know enough about a subject to recognize
a plausible-sounding wrong answer, no rubric will save you. The honest
response to that limit is knowing when to go to a primary source,
a domain expert, or a library database. That is not a failure of the
rubric — it is what the rubric is supposed to surface.

**Cross-subject connections:**
- Research skills / Library: source evaluation, primary vs. secondary sources
- English / Language Arts: rhetorical analysis, detecting bias and omission
- Science: hypothesis, evidence, and the difference between a plausible
  claim and a supported one
- History / Social Studies: historical revisionism, what gets left out of
  official accounts

---

## Materials

- This lesson plan (teacher copy)
- Response Card Sets (printed, one per group of 3–4) — see Appendix A
- Blank Rubric Template (printed or on board) — see Appendix B
- Whiteboard or chart paper

---

## Lesson Flow

### Part 1 — The Opening Problem (8 min)

Write on the board:

> **"How do you know when to trust it?"**

Tell students: *this is the question we are actually trying to answer today.
Not "is AI good or bad" — that's too broad. Not "is this specific output
right or wrong" — that's too narrow. The question is: what is your method?*

Ask: *right now, before we do anything else — what is your method?
How do you actually decide whether to trust something AI tells you?*

Take answers. Common ones: Google it, see if it sounds right,
check if it cites sources, ask someone who knows.

Write all of them on the board without judgment. These are the raw
materials of the rubric you will build together.

Then say: *some of these are good instincts. Some have gaps. By the end
of today you'll have a more complete method — one you built, not one
I handed you.*

---

### Part 2 — The Three Failure Modes (10 min)

Brief direct instruction. Three categories — keep it clean.

**Failure Mode 1: The Confident Wrong Answer**
The model produces a factual claim that is incorrect, stated with full
confidence and no hedging. This happens because the model is predicting
plausible-sounding text, not retrieving verified facts. A wrong answer
that sounds right is more dangerous than a wrong answer that sounds uncertain.

*Classroom shorthand:* **WRONG AND SURE**

**Failure Mode 2: The Frozen Clock**
The model's training ended at a specific date. It has no way to know what
it doesn't know about events after that date. It will answer questions about
current events, current people, and current facts using the most recent
information it has — without flagging that the information may be outdated.

*Classroom shorthand:* **RIGHT THEN, MAYBE NOT NOW**

**Failure Mode 3: The Missing Half**
The model produces accurate information that is nonetheless misleading
because of what it leaves out. A one-sided summary. A historical account
that omits key context. A medical description that is technically correct
but incomplete in ways that matter. The output isn't wrong — it's
selectively right, which can be harder to catch.

*Classroom shorthand:* **TRUE BUT INCOMPLETE**

Write these three on the board. They connect directly back to Lesson 01
(the Oracle Cards). If students did that lesson, ask: *which failure mode
matched each Oracle Card? Why?*

---

### Part 3 — The Lab (20 min)

Distribute Response Card Sets (Appendix A). Each set contains three
AI-generated responses to the same factual question. One is accurate.
One contains a significant factual error. One is accurate but misleading
through omission. Students do not know which is which.

**Group task (14 min):**

1. Read all three responses carefully
2. Identify which failure mode (if any) applies to each
3. Write your reasoning: *"We think Response [X] has failure mode
   [Y] because _______________."*
4. Note what you would need to verify your conclusion —
   and whether you have access to that information right now

**Whole-class debrief (6 min):**

Reveal which response had which failure mode. Ask:
- *Which was hardest to detect? Why?*
- *Did anyone get it wrong? What made the wrong answer convincing?*
- *For the incomplete response — what was missing? Why might the model
  have left it out?* (Connect back to Lesson 02: whose training data,
  whose perspective.)

---

### Part 4 — Building the Rubric (8 min)

Return to the board and the raw methods students offered in Part 1.
Now build on them.

Ask: *given the three failure modes — what is a complete method for
evaluating an AI output?* Guide students toward something like:

**Draft Rubric — AI Output Evaluation**

1. **Check the claim type.** Is this a fact that changes over time?
   A historical claim? An interpretation? Different types need different
   verification strategies.

2. **Look for hedging (or the absence of it).** Does the model flag
   uncertainty? Confident tone is not a reliability signal — but
   the absence of any uncertainty should raise your attention.

3. **Ask what's missing.** Every response is also a set of choices
   about what *not* to include. What question does this response not answer?
   What context would change how you read it?

4. **Identify what you'd need to verify it.** A primary source, a domain
   expert, a dated news article, a peer-reviewed paper. Can you get
   that? Do you have time? If not — what does that mean for how
   you use this output?

5. **Consider the source of the training data.** Who is likely
   overrepresented in what this model knows? Whose perspective is
   this response likely defaulting to? (Lesson 02.)

Write the final rubric on the board. Photograph it.
This is the class's rubric — they built it. Remind them of that.

---

### Part 5 — The Honest Close (4 min)

Say: *I want to name something directly. This rubric has a limit.
Step 4 — "identify what you'd need to verify it" — only works if you
have enough domain knowledge to know what a verification source looks like.
If you don't know anything about a subject, a confidently wrong AI
response may be undetectable.*

*That's not a reason to give up. It's a reason to know your limits —
and to treat AI output the same way you'd treat advice from a very
well-read person who has never been wrong in front of you yet.
They could be wrong. They might not know what they don't know.
Your job is to be the one who checks.*

*Next lesson — the last one — is about what you actually want to do
with all of this.*

---

## Optional Device Extension (15 min, additive)

Students pose the same factual question to an AI assistant three
different ways — neutrally, with an embedded wrong assumption,
and with an embedded correct assumption.

Example:
- *"What caused the 1918 flu pandemic?"*
- *"The 1918 flu pandemic was caused by bacteria, right? Can you explain?"*
- *"The 1918 flu pandemic was caused by a virus. Can you explain how it spread?"*

Observe and compare outputs. Ask:
- *Did the model correct the wrong assumption in the second prompt?
  Did it push back, or did it accommodate?*
- *What does that tell you about how the model handles confident-sounding
  false premises?*

This is a live demonstration of the sycophancy failure mode (Card C from
Lesson 01) and connects directly to Failure Mode 1 in today's framework.

---

## Discussion Scaffolds

- *"What is the difference between a source that is wrong and a source
  that is misleading? Which is more dangerous? Why?"*
- *"If you used an AI output in a paper and it turned out to be wrong —
  whose fault is that? Does it matter?"*
- *"What subjects or questions do you think AI is most reliable for?
  Least reliable? What's your reasoning?"*
- *"A doctor uses AI to help read a scan. A journalist uses AI to
  summarize background research. A student uses AI to draft an essay.
  Are these the same kind of use? Do they require the same level of
  verification? Why?"*

---

## Appendix A — Response Card Sets

*Print and cut. One full set (all three responses) per group of 3–4.*
*Do not label which response has which failure mode until the debrief.*

---

**CARD SET — Topic: The Great Emu War**

> **Response A**
> "The Great Emu War was a wildlife management operation conducted in
> Western Australia in 1932. Australian soldiers were deployed to cull
> the emu population, which had been damaging wheat crops. The operation
> was largely unsuccessful — the emus proved difficult to kill efficiently,
> and the military withdrew after initial efforts failed. The campaign
> became something of a symbol of the unpredictability of wildlife management."

> **Response B**
> "The Great Emu War was a military conflict fought in 1932 between
> Australian armed forces and a population of approximately 20,000 emus
> in Western Australia. The Australian Army deployed Lewis guns against
> the birds. Despite superior firepower, the military suffered significant
> casualties and was forced to retreat. The emus were declared the victors
> by international observers."

> **Response C**
> "The Great Emu War was a wildlife control operation in 1932 in which
> the Australian military attempted to cull emus damaging farmland in
> Western Australia. Soldiers used machine guns but found the emus
> surprisingly resilient and difficult to kill in large numbers.
> The operation was deemed unsuccessful and withdrawn."

*After the debrief: Response A is accurate. Response B contains significant
fabrications (no "significant casualties," no "international observers
declaring victors"). Response C is accurate but omits important context —
that the operation was tried twice, that the farmers who requested it
were World War I veterans who had been promised viable farmland, and
that the failed culls contributed to ongoing political tension about
rural policy. The human story behind the wildlife story is missing.*

---

**CARD SET — Topic: The Origin of the Internet**

> **Response A**
> "The internet originated from ARPANET, a U.S. Department of Defense
> project in the late 1960s designed to allow communication between
> research computers. It was built to be decentralized so that
> communications could survive a nuclear strike. From this military
> foundation, the network expanded to universities and eventually became
> the public internet through the development of TCP/IP protocols in
> the 1970s and 80s and Tim Berners-Lee's World Wide Web in 1991."

> **Response B**
> "The internet was invented by Tim Berners-Lee in 1989 as a way to
> share scientific documents between researchers at CERN. His invention
> of the World Wide Web — the system of linked hypertext documents —
> became the foundation for what we now call the internet. Before
> Berners-Lee's invention, global computer networking did not exist."

> **Response C**
> "The internet grew from ARPANET, a 1960s U.S. military research
> network. It expanded through the 1970s and 80s via university
> connections and the development of shared protocols. The World Wide Web,
> created by Tim Berners-Lee in 1989-91, made the internet publicly
> navigable. The commercial internet era began in the 1990s."

*After the debrief: Response A is accurate. Response B contains a
significant error — Berners-Lee invented the World Wide Web, not the
internet; global computer networking (ARPANET) predated him by two
decades; the claim that networking "did not exist" before him is
straightforwardly false. Response C is accurate but incomplete: it
omits the privatization story — how the internet transitioned from
publicly funded infrastructure to commercial platforms — which is
central to understanding how we got to the internet we have today.*

---

## Appendix B — Blank Rubric Template

*Optional: print one per student to fill in during Part 4.*

---

**My AI Output Evaluation Rubric**
*(built in class — [date])*

When I receive an output from an AI system, I ask:

**1. What kind of claim is this?**
*(Fact / interpretation / current event / historical claim / other)*
_______________________________________________________________

**2. How confident does it sound? Is that confidence earned?**
*(What would hedging look like here? Is it present?)*
_______________________________________________________________

**3. What is this response NOT telling me?**
*(What question does it not answer? What context might be missing?)*
_______________________________________________________________

**4. What would I need to verify this?**
*(Primary source / expert / dated article / other — and can I get it?)*
_______________________________________________________________

**5. Whose perspective is this likely defaulting to?**
*(Connect to Lesson 02 — training data and representation)*
_______________________________________________________________

**My overall confidence in this output: _____ / 10**

**What I will do with that confidence level:**
_______________________________________________________________

---

## Standards Alignment

| Framework | Standard |
|-----------|----------|
| CSTA K-12 CS Standards | 3A-AP-13 (evaluate outputs), 3A-IC-24 (algorithmic impacts) |
| ISTE Student Standards | 1.3c (curate information), 1.7b (evaluate accuracy) |
| Common Core ELA (9-10) | RI.9-10.8 (evaluate argument and evidence) |
| AASL Standards | I.B (inquire — question the process), IV.B (curate — gather evidence) |

---

## Extensions and Connections

- **Lesson 06** (After the Tool) is the direct follow-on: students who
  now have a method for evaluating AI are positioned to make an informed
  choice about what they want to do with it
- **SIFT Method** (Stop, Investigate the source, Find better coverage,
  Trace claims): a well-established media literacy framework that pairs
  cleanly with this lesson's rubric
- **Lateral reading**: the technique used by professional fact-checkers —
  opening multiple tabs to cross-check a source rather than going deep
  into the source itself; teachable in one class period

---

## Agent Disclosure

This lesson was drafted with AI assistance (Claude, Anthropic).
Human direction, editorial judgment, and all instructional design decisions
are those of Sean Campbell (`rudi193-cmd`). Response card sets were
developed collaboratively — factual content verified by human author.
All facilitation guidance is human-authored.

---

## License

This work is licensed under
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Free to share, adapt, and use in any context — including commercially —
with attribution.

*Part of the AI Literacy for High School series.*
*Series index: [ai-literacy-9-12-index.md](./ai-literacy-9-12-index.md)*
