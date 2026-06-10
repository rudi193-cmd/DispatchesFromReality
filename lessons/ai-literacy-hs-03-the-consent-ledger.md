# The Consent Ledger
**AI Literacy for High School · Lesson 03 of 06**
*Grades 9–12 · Computer Science / AI Literacy / Civics · No devices required for core*

---

> *"You generated value. Someone else captured it.
> You clicked 'I Agree.' But did you know what you were agreeing to?"*

---

## Overview

By Lesson 03, students understand that AI models learn from data, and that
the data reflects whose voices and knowledge were captured. This lesson asks
the next question: *how did that data get there?*

In most cases: without meaningful consent.

The data pipelines that feed modern AI systems were built by scraping the
internet at scale — forums, social media, personal blogs, creative writing,
medical discussions, images, and more — before most users had any framework
for understanding what that meant. Even where Terms of Service technically
permitted it, the gap between what people agreed to and what they understood
themselves to be agreeing to is enormous.

This lesson makes that gap visible. It introduces the concept of informed
consent as a practical standard — not just a legal one — and asks students
to think through what it would actually look like in the context of AI.

---

## Learning Objectives

By the end of this lesson, students will be able to:

1. Trace the lifecycle of a personal data point from creation to potential
   use in AI training
2. Distinguish between *legal* consent and *informed* consent
3. Identify the asymmetry between who generates data and who benefits from it
4. Propose at least one structural change that would make consent more meaningful

---

## For Teachers

**Suggested time:** 50 minutes

**No devices required for the core lesson.**
The core activity is a structured role-play using printed case cards.
Optional device extension at the end.

**Facilitation notes:**

This lesson can generate strong reactions — frustration, cynicism, or a
feeling of helplessness ("there's nothing I can do"). All of those are
valid responses. Your job is not to talk students out of them, but to
keep the conversation moving toward agency rather than staying in outrage.

The role-play in Part 3 is designed to surface competing legitimate
interests — not to cast companies as villains and users as victims.
Students who play the company role often have the most interesting
realizations: the incentive structures make sense from inside the system.
That's the more durable insight.

Watch for students who conflate "it's legal" with "it's fine." That's the
key conceptual move to unpack gently.

**Cross-subject connections:**
- Civics / Government: regulatory frameworks, GDPR, COPPA, FERPA
- Philosophy / Ethics: autonomy, informed consent (medical ethics parallel)
- Economics: data as labor, attention economy
- History: historical examples of extractive economies; who benefits, who provides

---

## Materials

- This lesson plan (teacher copy)
- Role Cards (printed, one per student) — see Appendix A
- The Data Journey handout (printed, one per student) — see Appendix B
- Whiteboard or chart paper

---

## Lesson Flow

### Part 1 — The Opening Scenario (8 min)

Read this aloud. Don't editorialize. Just read it.

---

*In 2012, a 16-year-old in Phoenix writes about her anxiety in a private
Tumblr blog. She doesn't use her real name. She writes honestly — about
panic attacks before school, about the things her parents don't understand,
about the music that helps.*

*She stops using the blog in 2015. Forgets about it.*

*In 2020, a company scraping publicly accessible web content for AI training
data includes her blog. Her words — her specific phrases, her way of
describing fear, her metaphors — enter a training corpus alongside
hundreds of millions of other documents.*

*In 2024, an AI model trained on that corpus helps generate mental health
support content. Some of the phrasings feel eerily familiar to people
who read them. No one knows why.*

*The 16-year-old is 28 now. She was never asked.*

---

Ask: *Was anything illegal here?* (Probably not — the blog was publicly
accessible and the Terms of Service likely permitted scraping.)

Ask: *Does "legal" mean "fine"? Why or why not?*

Take five minutes of responses. You are not looking for a settled answer.
You are looking for students to feel the gap between legal and ethical
before you name it.

---

### Part 2 — The Data Journey (12 min)

Distribute the Data Journey handout (Appendix B).

Walk students through it as a class. The handout traces a single data point —
a photo posted to social media — through six stages:

1. **Creation** — a student takes a photo and posts it
2. **Indexing** — a platform stores it, analyzes it, assigns metadata
3. **Monetization** — the platform sells advertising against it
4. **Scraping** — a third party collects it as part of a large dataset
5. **Training** — the image becomes part of a model's training data
6. **Deployment** — the model generates images influenced by this and
   millions of similar inputs

At each stage, ask: *who knows this is happening? Who agreed to it?
Who benefits?*

The key insight to surface: at Stage 1, the student had one mental model
of what they were doing (sharing a photo with friends). By Stage 6, that
photo is part of the substrate of a commercial AI product. The gap between
those two things is not filled by meaningful consent.

Introduce the distinction:
- **Legal consent**: clicking "I Agree" on a Terms of Service document
- **Informed consent**: understanding what you are agreeing to well enough
  to make a genuine choice

Ask: *has anyone here actually read a Terms of Service document?
What would it take to make informed consent realistic at scale?*

---

### Part 3 — The Role-Play (20 min)

Distribute Role Cards (Appendix A). Each student gets one role.
Groups of four: one User, one Company Representative, one Regulator,
one Future Model (a person who speaks for the interests of the AI
system that will be trained on this data).

**Scenario (read aloud):**

> *A proposed regulation would require AI companies to notify individuals
> whenever their publicly posted content is included in a training dataset,
> and to provide an opt-out mechanism. Companies have 90 days to comply
> or remove the data.*

Each group has 10 minutes to discuss: *should this regulation pass?*
Each role argues from their position. The Future Model role is the
interesting one — students must think about what the AI system itself
"needs" to function well, and whether that justifies the data collection.

Then: 5 minutes of whole-class debrief.
Ask: *which argument was hardest to counter? Did anyone change their
position during the discussion? What was the strongest argument on
the side you disagree with?*

**Teacher note:** Students playing the Company role often discover that
the arguments are internally coherent — the incentive structures *make
sense* from inside the system. That's not a defense of the system.
It's an explanation of how we got here. Both things can be true.

---

### Part 4 — The Ledger (5 min)

Return to the board. Draw a simple two-column table:

| Who generates value | Who captures value |
|---|---|

Ask students to fill it in based on everything from today.
The table should end up something like:

| Who generates value | Who captures value |
|---|---|
| Users who post content | Platforms |
| Users whose data is scraped | AI companies |
| Communities whose knowledge is encoded | Model owners |
| Workers who label/clean data | Shareholders |

Ask: *Is this arrangement inevitable? Is it natural? Or is it a choice
that could be made differently?*

Close with: *Lesson 04 is going to ask whether any of this changes
if the AI actually "understands" what it's working with — or whether
the answer stays the same either way.*

---

## Optional Device Extension (15 min, additive)

Students access the Terms of Service for a platform they use
(Instagram, TikTok, Google, YouTube — their choice). Using a
printed checklist, they identify:
- Does the ToS mention AI training?
- What data is covered?
- Is there an opt-out? How hard is it to find?
- Would a reasonable 14-year-old understand this document?

Groups report back. The exercise rarely produces comfort.

---

## Discussion Scaffolds

- *"What is the difference between privacy and consent?
  Can you have one without the other?"*
- *"If you benefit from a service for free — does that make it
  fair for them to use your data? Why or why not?"*
- *"What would a consent system that actually worked look like?
  Who would have to build it? Who would have to require it?"*
- *"Are there other contexts where we require informed consent
  as a legal and ethical standard? What can we learn from those?"*

---

## Appendix A — Role Cards

*Print and cut. One per student. Groups of four (one of each role).*

---

**ROLE: THE USER**

You are a high school student who has been posting on social media since
you were 13. You use it to share art you make, connect with friends,
and find community around things you care about.

You recently found out that posts you made years ago — including some
you later deleted — may have been included in AI training data before
you deleted them.

**Your position:** You support the proposed regulation. You believe
people should know when their content is being used and should have a
real choice about it. You are not asking for money — just for transparency
and control.

**Your strongest argument:** Informed consent is a basic ethical standard
in medicine, research, and law. Why should AI be exempt?

**The hardest question you'll face:** How would opt-in work at scale?
If everyone had to opt in, would there be enough data to build AI at all?

---

**ROLE: THE COMPANY REPRESENTATIVE**

You work for a large AI company. You believe in the products you build —
you have seen them help students learn, help doctors diagnose, help people
access information they couldn't otherwise reach.

You also have genuine concerns about this regulation.

**Your position:** You oppose the regulation as written. You believe
publicly available data should remain available for public purposes,
including AI research. You support transparency initiatives, but
mandatory notification at scale is technically and economically
unworkable.

**Your strongest argument:** The internet was built on the premise that
publicly posted content is publicly accessible. Changing that framework
retroactively creates uncertainty that will slow down beneficial
innovation — including in education and healthcare.

**The hardest question you'll face:** If a 16-year-old posted something
publicly without understanding the implications, does that make it
genuinely public? At what point does "publicly accessible" become
"fair game for any use"?

---

**ROLE: THE REGULATOR**

You work for a government agency responsible for data privacy and
consumer protection. You helped draft this proposed regulation.

**Your position:** You support the regulation. You have seen what happens
when powerful new technologies are deployed without any meaningful consent
framework — and the harms that follow are disproportionately borne by
people with the least power.

**Your strongest argument:** Consent frameworks did not exist for social
media in its early years. We are still living with the consequences.
We have an opportunity to do this right with AI before the harms compound.

**The hardest question you'll face:** Regulation is slow. AI development
is fast. How do you write rules that don't become obsolete before they
take effect — or that don't simply push development to places with
fewer rules?

---

**ROLE: THE FUTURE MODEL**

This is an unusual role. You speak for the interests of the AI system
that will be trained on this data — not as if the AI is a person,
but as an advocate for what it "needs" to function well.

**Your position:** You are genuinely uncertain. On one hand: more data,
more diverse data, produces better models. Restrictions reduce the
training pool. On the other hand: data gathered without consent may
encode resentment, distortion, or gaps that harm the model's reliability.

**Your strongest argument:** A model trained on data people were willing
to contribute might be more trustworthy than one trained on data that
was taken. Consent isn't just an ethical question — it may be a quality
question.

**The hardest question you'll face:** Can an AI system have interests?
What does it mean to advocate for something that can't advocate for itself?

---

## Appendix B — The Data Journey

*One per student. Teacher reads through with class during Part 2.*

---

**A photo enters the machine.**

You are 16. You take a photo of yourself at a concert and post it.
Here is where it goes:

**Stage 1 — Creation**
You post the photo. Your friends see it. You feel good about it.
*Who knows: you, your followers.*
*Who benefits: you (connection, expression).*

**Stage 2 — Indexing**
The platform stores the image, analyzes it with computer vision,
identifies your face, tags the location from metadata, infers your age,
estimates your interests, logs the time.
*Who knows: the platform's systems (automated).*
*Who benefits: the platform (ad targeting, user modeling).*

**Stage 3 — Monetization**
Your profile — including this photo and the engagement it received —
informs the ad system. A concert venue pays to reach "users like you."
*Who knows: the platform, the advertiser.*
*Who benefits: the platform, the advertiser.*

**Stage 4 — Scraping**
An AI company runs a web crawl. Publicly accessible images —
including yours — are collected as part of a training dataset.
*Who knows: the AI company.*
*Who benefits: the AI company.*

**Stage 5 — Training**
Your photo, along with hundreds of millions of others, teaches a model
what "16-year-old at a concert" looks like — how to generate one,
recognize one, caption one.
*Who knows: the AI company.*
*Who benefits: the AI company, future users of the model.*

**Stage 6 — Deployment**
Someone uses an AI image generator. They ask for "a teenager at a
concert, authentic, candid." The model draws on everything it learned —
including your photo. The output is sold as stock imagery.
*Who knows: nobody traces it back.*
*Who benefits: the generator company, the buyer.*

---

**You were at Stage 1. Someone else is at Stage 6.**

*At which stage should you have been asked? What would you have said?*

---

## Standards Alignment

| Framework | Standard |
|-----------|----------|
| CSTA K-12 CS Standards | 3A-IC-29 (data privacy), 3B-IC-27 (societal impacts) |
| ISTE Student Standards | 1.2a (digital rights and responsibilities) |
| Common Core ELA (9-10) | SL.9-10.1c (respond to diverse perspectives) |
| NCSS Social Studies | Power, Authority, and Governance; Individual Development and Identity |

---

## Extensions and Connections

- **Lesson 04** (The Mirror Test) follows: if the AI has used your words,
  your images, your expressions — and it produces something that feels like
  understanding — what does that mean for identity and authorship?
- **GDPR and COPPA**: useful primary source reading for students interested
  in what legal frameworks actually say — and where they fall short
- **The Atlas of AI** by Kate Crawford: rigorous, accessible book on the
  material and political economy of AI; excellent for 12th grade independent reading
- **Data as Labor movement**: economists Jaron Lanier and Glen Weyl have
  proposed frameworks where data contributors are paid; useful counterpoint
  for economics-oriented classes

---

## Agent Disclosure

This lesson was drafted with AI assistance (Claude, Anthropic).
Human direction, editorial judgment, and all instructional design decisions
are those of Sean Campbell (`rudi193-cmd`). AI assisted formatting,
expansion of role card arguments, and standards alignment after structure
and content were set by the human author.

---

## License

This work is licensed under
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Free to share, adapt, and use in any context — including commercially —
with attribution.

*Part of the AI Literacy for High School series.*
*Series index: [ai-literacy-9-12-index.md](./ai-literacy-9-12-index.md)*
