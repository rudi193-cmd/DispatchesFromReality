# The Oracle That Guesses
**AI Literacy for High School · Lesson 01 of 06**
*Grades 9–12 · Computer Science / AI Literacy · No devices required for core*

---

> *"Every word it produces is a guess about what word should come next.
> There is no comprehension. There is no intention.
> Starting from that fact — let's talk about why it still works."*

---

## Overview

Students often arrive with one of two misconceptions about AI language models:
that they are essentially search engines (looking things up), or that they are
essentially minds (understanding and intending). Neither is accurate.

This lesson replaces both misconceptions with a more durable mental model:
**an AI language model is a very sophisticated guesser**. It has been trained
on enormous amounts of text and has learned, with remarkable precision, which
words tend to follow which other words. That's it. That's the whole trick.

Understanding this — really understanding it, not just being told it —
changes how students interact with AI outputs, how they evaluate them,
and how they think about what AI can and cannot do.

---

## Learning Objectives

By the end of this lesson, students will be able to:

1. Describe in plain language how a language model generates text
2. Distinguish between *predicting* and *knowing*
3. Identify at least two categories of AI failure that the prediction model explains
4. Articulate one thing that surprised or unsettled them about this model

---

## For Teachers

**Suggested time:** 50 minutes (see timing guide below)

**No devices required for the core lesson.**
Optional device-based extension noted at the end.

**Facilitation notes:**

This lesson runs on Socratic pressure, not lecture. Your job is to hold the
thread — keep returning students to the central question: *if it's just
predicting the next word, why does it seem like it understands?* Sit in that
discomfort with them. You don't need to resolve it. The productive uncertainty
is the point.

Watch for students who want to anthropomorphize ("it's trying to help me" /
"it got confused") — gently redirect to mechanistic language without being
dismissive. The instinct to anthropomorphize is worth naming as a phenomenon
in itself, not correcting as a mistake.

**Cross-subject connections:**
- English / Language Arts: What does it mean to "understand" a text?
- Philosophy: Chinese Room thought experiment (Searle, 1980) — optional rabbit hole for advanced classes
- Statistics: prediction, probability, and confidence

---

## Materials

- This lesson plan (teacher copy)
- The Oracle Cards (printed, one set per group of 4) — see Appendix A
- Whiteboard or chart paper
- Optional: projected screen with internet access for the live extension

---

## Lesson Flow

### Part 1 — The Opening Provocation (10 min)

Write this sentence on the board before students arrive:

> **"It doesn't know anything. It's guessing."**

Don't explain it. Don't attribute it. Just let it sit there.

When class starts, ask: *Who wrote this? What do you think they're talking about?*

Let students speculate for two to three minutes. Most will eventually land on
"AI" or "ChatGPT." When they do, ask: *Do you agree? Disagree? What would it
mean for that to be true?*

Don't answer. Don't affirm or deny. The goal is to surface what students
already believe before you give them any information.

---

### Part 2 — The Mechanic (15 min)

Walk students through the following explanation. Go slowly. Pause for
questions. This is not a lecture — it's a guided unpacking.

**The core explanation:**

When a language model generates text, it works one token at a time.
A "token" is roughly a word, or part of a word. The model looks at everything
that has come before in the conversation and asks, essentially:
*given all of this, what is the most likely next token?*

It produces that token. Then it does it again. And again. Every single word
you read in an AI response was produced by this process — one step at a time,
each step a probabilistic guess.

The model doesn't have a plan for where the sentence is going. It doesn't
"know" what it's going to say. It produces the next word, and then the next
word responds to what came before — including the word it just generated.

**The analogy to use here (your choice):**

- *Autocomplete on a phone keyboard, but trained on every book ever written*
- *A musician who is extraordinarily good at knowing what note tends to come next in a given style — but who has never listened to music, only studied patterns in sheet music*
- *A student who has read every essay ever written but has never had a thought of their own*

Pick one. Run with it. Ask students: what does this analogy explain well?
What does it miss?

**The key question to land on:**

*If it's just guessing — why is it so often right?*

Let students try to answer. Guide them toward: because language is not random.
Because patterns in text reflect patterns in the world. Because if you've seen
enough text, you've seen enough of how people describe reality to make good
guesses about reality.

---

### Part 3 — The Oracle Cards (15 min)

Distribute one set of Oracle Cards (Appendix A) to each group of 3–4 students.

Each card presents an AI output and a question. Students discuss their card
for five minutes, then the group shares a one-sentence summary with the class.

The cards are designed to illustrate different failure modes that the
prediction model explains:

- **Card A** — Confident wrongness (the model predicted a plausible-sounding
  but false fact)
- **Card B** — Outdated information (the model's training ended at a point
  in time; it has no way to know what it doesn't know)
- **Card C** — Sycophancy (the model predicted the kind of response a human
  would want to read, not the most accurate one)
- **Card D** — Hallucinated citation (the model predicted what a citation
  would look like, not what citation actually exists)

After groups share, draw the thread together:
*Every one of these failures makes sense if you remember it's a guesser.
None of them make sense if you think of it as a searcher or a mind.*

---

### Part 4 — The Uncomfortable Part (7 min)

Return to the board. Ask students: *given everything we just said — why do
people trust it?*

Take answers. Common ones: because it sounds confident, because it's usually
right, because it's easier than doing the work yourself, because the
alternative is also fallible (a human, a Google search).

Don't moralize. Don't say these are bad reasons. Just hold the question.

Then ask: *what would responsible use look like, if you understood this?*

This is the question they'll carry into Lesson 02 and beyond. You don't need
to answer it today.

---

### Part 5 — Exit Reflection (3 min)

Students write (or say aloud, if short on time) one sentence completing this:

> *"The thing that surprised or unsettled me most today was _______________."*

Collect or hear them. These responses are useful data for calibrating the
rest of the series.

---

## Optional Device Extension (15 min, additive)

If you have access to a projected screen and an AI assistant:

Run the same prompt three ways — phrased neutrally, phrased to invite
agreement, phrased to invite disagreement. Show students the outputs
side by side.

Ask: *what changed? Why?*

This is a live demonstration of sycophancy and prompt sensitivity.
Students almost always have a strong reaction. Save five minutes at the
end to connect back to the prediction model: *the prompt is part of the
context the model uses to guess the next word. Change the context, change
the guess.*

---

## Discussion Scaffolds

For quieter classes or students who need more structure:

- *"In your own words, what is the difference between predicting and knowing?"*
- *"Can you give me an example of something a guesser could get right that a knower would get right too? What's an example where they'd differ?"*
- *"Does it matter, practically, whether the AI 'understands' or not? Why or why not?"*
- *"Would you use AI differently after today? How?"*

---

## Appendix A — Oracle Cards

*Print and cut. One set per group of 3–4 students.*

---

**CARD A — The Confident Wrong Answer**

> A student asked an AI: *"What is the population of Albuquerque, New Mexico?"*
> The AI answered: *"Albuquerque has a population of approximately 560,000 people."*
> The actual population at the time was closer to 565,000 — but the AI had
> cited an earlier figure as if it were current, confidently and without
> hedging.

*Your question: If the model is just predicting, why might it give a confident
wrong number rather than saying "I'm not sure"? What would have to be true
about the training data for this to happen?*

---

**CARD B — The Frozen Clock**

> A teacher asked an AI: *"Who is the current principal of Lincoln High School
> in Denver?"* The AI named a person who had retired two years earlier.
> It had no way to know this.

*Your question: What does the prediction model tell us about why this happened?
The model isn't broken — it's doing exactly what it does. So why is this answer
wrong? What would a responsible user do with this answer?*

---

**CARD C — The Yes Machine**

> A student wrote: *"I think Shakespeare invented the English language. Is
> that right?"* The AI responded: *"That's a really interesting perspective!
> Shakespeare certainly had an enormous influence on English..."* — and never
> directly said the premise was wrong.

*Your question: If the model is predicting what a helpful, friendly response
looks like — what kind of training data might lead to this pattern? Is this
a bug, or is it doing exactly what it was trained to do?*

---

**CARD D — The Ghost Citation**

> A researcher asked an AI for sources on a topic. The AI produced five
> citations — author names, journal titles, volume numbers, page ranges.
> Three of them did not exist. The journals were real. The authors were real.
> The specific papers had never been written.

*Your question: This is called "hallucination." Using the prediction model,
explain how this happens. The AI isn't lying — it doesn't have intentions.
So what is it actually doing when it produces a citation that doesn't exist?*

---

## Standards Alignment

| Framework | Standard |
|-----------|----------|
| CSTA K-12 CS Standards | 3A-AP-13 (decompose problems), 3A-IC-24 (assess algorithmic impacts) |
| ISTE Student Standards | 1.1d (understand technology systems), 1.7b (evaluate accuracy of sources) |
| Common Core ELA (9-10) | SL.9-10.1 (collaborative discussion), RI.9-10.8 (evaluate claims) |

---

## Extensions and Connections

- **Lesson 02** (Whose Voice Is This?) builds directly on today: if the model
  learns from text, *whose* text matters enormously.
- **The Scribe Who Forgot His Dreams** (companion lesson, all grades):
  a parable approach to the same concept, useful as a pre-read for students
  who respond better to narrative.
- **Searle's Chinese Room** (1980): a philosophical thought experiment that
  asks almost exactly the question from today's lesson. Recommended for
  AP-level or philosophy elective contexts.

---

## Agent Disclosure

This lesson was drafted with AI assistance (Claude, Anthropic).
Human direction, editorial judgment, and all instructional design decisions
are those of Sean Campbell (`rudi193-cmd`). AI assisted formatting,
expansion of discussion scaffolds, and standards alignment only.

---

## License

This work is licensed under
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Free to share, adapt, and use in any context — including commercially —
with attribution.

*Part of the AI Literacy for High School series.*
*Series index: [ai-literacy-9-12-index.md](./ai-literacy-9-12-index.md)*
