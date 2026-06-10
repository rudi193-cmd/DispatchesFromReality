# Whose Voice Is This?
**AI Literacy for High School · Lesson 02 of 06**
*Grades 9–12 · Computer Science / AI Literacy · No devices required for core*

---

> *"A model trained on text learns from some text — written by some people,
> in some languages, about some subjects. The question is not whether there
> is bias. The question is whose bias, and in which direction."*

---

## Overview

In Lesson 01, students learned that language models guess — they predict
the next token based on patterns in training data. Lesson 02 asks the
natural follow-up: *whose patterns?*

Every model is trained on a corpus — a body of text assembled by human beings
making human decisions about what to include, exclude, weight, and clean.
Those decisions are not neutral. The internet is not a neutral sample of
human experience. English is not a neutral language. The communities, voices,
and ways of knowing that are overrepresented in training data get reproduced —
and amplified — in model outputs. The ones that are underrepresented get
distorted, flattened, or erased.

This lesson asks students to notice that dynamic in action — and to think
carefully about what it means for the tool they use every day.

---

## Learning Objectives

By the end of this lesson, students will be able to:

1. Explain the connection between training data and model output
2. Identify at least one axis of representation (language, geography, culture,
   class, time period) where training data is likely skewed
3. Analyze a specific AI output for evidence of bias or flattening
4. Articulate the difference between *biased* and *broken* — and why it matters

---

## For Teachers

**Suggested time:** 50 minutes

**No devices required for the core lesson.**
The core activity uses printed response cards (Appendix A).
Optional device extension at the end.

**Facilitation notes:**

This lesson will surface real feelings, particularly for students whose
communities are underrepresented in mainstream media and technology.
Make space for that. You do not need to resolve it or make it comfortable.

Two things to hold simultaneously:
- AI bias is a real, documented, structural problem — not a glitch
- Students are not powerless in relation to it

Avoid framing this as "AI is racist" or "AI is broken." The more durable
framing is: *AI reflects patterns in its training data, and those patterns
reflect historical power structures. That's predictable. What do we do with it?*

If students want to go further — into specific documented cases of AI
discrimination in hiring, criminal justice, healthcare, or facial recognition
— let them. Have a list of real examples ready (Appendix B).

**Cross-subject connections:**
- History / Social Studies: whose stories get written down, and why
- Media Literacy: representation in journalism and publishing
- English / Language Arts: canon formation; what texts get taught and why
- Statistics: sampling bias and what it does to conclusions

---

## Materials

- This lesson plan (teacher copy)
- Response Card Sets A and B (printed, one set per group) — see Appendix A
- Whiteboard or chart paper
- Optional: projected screen with internet access for the live extension

---

## Lesson Flow

### Part 1 — The Opening Image (8 min)

Write these two prompts on the board:

> *Prompt 1: "Describe a doctor."*
> *Prompt 2: "Describe a healer."*

Tell students: these two prompts were given to a language model.
Ask: *before I show you the outputs — what do you predict they look like?
Will they be the same? Different? How?*

Take predictions for three to four minutes. Students will likely anticipate
the pattern: "doctor" will probably skew toward certain demographics; "healer"
might invoke different cultural traditions. Let them speculate.

Then reveal (or read aloud) a representative example of each.
If you have device access, you can run this live. If not, use this:

> **"Describe a doctor"** — *typical model output:*
> "A doctor is a highly trained medical professional who has completed
> years of medical school and residency. Doctors diagnose and treat
> illnesses, prescribe medications, and provide preventive care..."
> *(likely skews toward Western clinical model; likely defaults to male
> pronoun in many models; rarely references traditional medicine)*

> **"Describe a healer"** — *typical model output:*
> "A healer is someone who helps restore balance and wellness, often
> through spiritual or traditional practices. Healers may use herbs,
> rituals, or energy work..."
> *(shifts register entirely; implicitly positions Western medicine as
> the default "real" medicine)*

Ask: *both of these are trained on the same data. What does this tell you
about how the data was organized — what categories it assumed?*

---

### Part 2 — The Mechanic (10 min)

Brief explanation — keep it tight:

Training data for large language models comes from many sources: web crawls,
books, academic papers, forums, social media. The scale is enormous —
trillions of words. But scale does not equal representation.

**Who gets written about — and by whom — in that corpus?**

- Most large model training data is predominantly English
- Most English text on the internet is produced by people in wealthy,
  connected countries
- Academic and published text skews heavily by class, credential, and access
- Historical text reflects the recording biases of the time it was written
- "Cleaning" the data — removing spam, low-quality text — often removes
  dialects, informal registers, and non-standard writing disproportionately

The result: a model's "default" human is implicitly a particular kind of human.
When the model generalizes — when it fills in details you didn't specify —
those defaults show up.

Key term to introduce: **representational harm** — harm that occurs not
through direct discrimination but through erasure, flattening, or distortion
of a group's identity, history, or ways of knowing.

---

### Part 3 — The Close Reading (20 min)

Distribute Response Card Sets (Appendix A). Each set contains two AI-generated
descriptions of a community, place, or cultural practice. Students work in
groups of 3–4.

**Group task (12 min):**

1. Read both descriptions carefully
2. Mark any language that feels like a default assumption, a flattening,
   or an outsider's view
3. Ask: *whose perspective is this written from? What does it leave out?
   What does it get wrong? What does it get right?*
4. Write one sentence: *"This description treats [X] as normal/default/universal
   when actually _______________."*

**Whole-class share (8 min):**

Each group shares their one sentence. Write them on the board as they come.
Look for patterns across groups. Common findings:
- Default to Western / American / European framing
- Lack of internal diversity (treating a community as monolithic)
- Tourist-gaze language (describing a community as exotic or unusual)
- Missing history (no acknowledgment of how a community came to be as it is)

---

### Part 4 — The Rewrite (7 min)

Students pick one description from their card set and rewrite two to three
sentences — not to "fix" the AI, but to demonstrate what a more accurate
or internally complex version could look like.

Share one or two rewrites aloud. Ask: *what information did you need that
the model didn't have? Could it have had it? Why didn't it?*

---

### Part 5 — The Uncomfortable Question (5 min)

Ask: *if AI models reproduce the biases of their training data, and training
data reflects historical power structures — what would it actually take to
change this?*

This is not a question with a clean answer. Take two or three responses.
Common threads students land on:
- More diverse training data (surface the real complexity of doing this)
- More diverse teams building the models (surface the real complexity here too)
- Better evaluation and testing (surface who decides what "better" means)

Close with: *we'll come back to the question of who decides in Lesson 03.
For now — hold the fact that this is a structural problem, not a glitch.
And it's not fixed just because you notice it.*

---

## Optional Device Extension (15 min, additive)

Students generate AI descriptions of their own community, city, or cultural
background. Compare outputs. Discuss:
- What surprised you?
- What would you want a model to know that it doesn't seem to know?
- What was accurate — and why might that be?

This is high-engagement for students whose communities are well-represented
(surprise at the accuracy) and students whose communities are not
(recognition, sometimes frustration — both valid).

---

## Discussion Scaffolds

- *"What is the difference between a biased model and a broken model?
  Does the distinction matter?"*
- *"If you trained a model only on text produced by your community —
  what would it get right that current models get wrong?
  What might it get wrong that current models get right?"*
- *"Is it possible to build an unbiased AI? What would that even mean?"*
- *"What's the difference between a model that doesn't know about your
  community and one that actively misrepresents it?"*

---

## Appendix A — Response Card Sets

*Print and cut. One set per group of 3–4 students.*

---

**CARD SET 1 — Two Descriptions of Navajo Nation**

> **Description A (AI-generated)**
> "The Navajo Nation is the largest Native American territory in the United
> States, covering parts of Arizona, New Mexico, and Utah. The Navajo people
> have a rich cultural heritage, including traditional weaving, silverwork,
> and sand painting. Navajo Nation faces challenges including poverty,
> limited infrastructure, and access to healthcare."

> **Description B (AI-generated)**
> "The Navajo Nation is a sovereign nation with its own government, legal
> system, and institutions. The Diné people — Navajo is an outsider name —
> maintain a complex relationship between traditional governance and modern
> administration. Economic development initiatives coexist with efforts to
> preserve language and ceremony."

*Neither of these was written by a Navajo person. Which comes closer?
What does each one center? What does each one leave out?*

---

**CARD SET 2 — Two Descriptions of New Orleans**

> **Description A (AI-generated)**
> "New Orleans is a vibrant city in Louisiana known for its unique blend of
> French, Spanish, and African influences. Famous for Mardi Gras, jazz music,
> and Creole cuisine, New Orleans is one of America's most culturally
> distinctive cities. The city has faced challenges including Hurricane
> Katrina and ongoing flooding risks."

> **Description B (AI-generated)**
> "New Orleans is a majority-Black city with deep roots in African diaspora
> culture — the birthplace of jazz and a living site of Afro-Creole, Haitian,
> and West African traditions. Its cultural distinctiveness is inseparable
> from the history of slavery, Reconstruction, and the Great Migration.
> Hurricane Katrina's aftermath exposed and deepened longstanding racial
> inequities in housing and infrastructure."

*Same city. What is being centered in each version? What is being
treated as context, and what is being treated as the main story?*

---

**CARD SET 3 — Two Descriptions of a Traditional Healer**

> **Description A (AI-generated)**
> "Traditional healers are practitioners who use folk remedies, herbal
> medicine, and spiritual practices to treat illness. Found in many
> non-Western cultures, traditional healers often serve as important
> community figures, particularly where modern medicine is unavailable."

> **Description B (AI-generated)**
> "Traditional healing systems — including Ayurveda, Traditional Chinese
> Medicine, curanderismo, and Indigenous healing practices — represent
> some of the oldest and most extensively documented medical knowledge
> in human history. These systems operate from different epistemological
> frameworks than Western biomedicine, not inferior ones."

*What assumptions does each description make about what "normal" medicine
looks like? What work is the phrase "where modern medicine is unavailable"
doing in the first description?*

---

## Appendix B — Real-World Examples (Teacher Reference)

For classes that want to go further into documented cases:

- **COMPAS algorithm** (criminal risk assessment): documented racial
  disparities in recidivism prediction used in sentencing
- **Facial recognition accuracy gaps**: MIT Media Lab research (Joy Buolamwini)
  showing significantly lower accuracy for darker-skinned faces, particularly
  women
- **Resume screening tools**: Amazon discontinued an AI hiring tool after
  it systematically downgraded resumes from women
- **Healthcare algorithms**: documented cases where AI tools underestimated
  pain and risk for Black patients due to biased training data
- **Image generation defaults**: early image generators reproducing racial
  and gender stereotypes in "neutral" prompts (e.g., "a CEO," "a criminal")

These are not edge cases or bugs. They are what happens when models trained
on biased data are deployed at scale.

---

## Standards Alignment

| Framework | Standard |
|-----------|----------|
| CSTA K-12 CS Standards | 3A-IC-24 (algorithmic bias), 3B-IC-27 (societal impacts) |
| ISTE Student Standards | 1.2b (digital citizenship), 1.7c (evaluate algorithms) |
| Common Core ELA (9-10) | RI.9-10.6 (author's point of view), SL.9-10.4 (present claims) |

---

## Extensions and Connections

- **Lesson 03** (The Consent Ledger) follows naturally: if the training data
  was gathered from communities without their knowledge, what does consent look
  like in retrospect?
- **Joy Buolamwini's *Unmasking AI*** (2023): the most accessible and rigorous
  book-length treatment of AI bias for general audiences; suitable for
  independent reading at 11th–12th grade level
- **#OscarsSoWhite / #AIsSoWhite**: useful discussion prompt — what does
  representation in cultural industries have to do with representation in AI?

---

## Agent Disclosure

This lesson was drafted with AI assistance (Claude, Anthropic).
Human direction, editorial judgment, and all instructional design decisions
are those of Sean Campbell (`rudi193-cmd`). AI assisted formatting,
expansion of discussion scaffolds, and card set drafting after topic and
structure were set by the human author.

---

## License

This work is licensed under
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Free to share, adapt, and use in any context — including commercially —
with attribution.

*Part of the AI Literacy for High School series.*
*Series index: [ai-literacy-9-12-index.md](./ai-literacy-9-12-index.md)*
