# Some Pig

*On containers, and what a system learns from being kept in one.*

**Working draft v1 · July 2026**

> **Draft note.** Every citation below is real and locatable. None has been read at
> its source — this draft was assembled under an egress policy that denied
> twenty-two hosts at the gateway, including the Library of Congress, `doi.org`,
> PLOS, Sefaria, Open Library and CourtListener. Footnotes marked **[unverified]**
> carry claims that must be checked against the original before publication. The
> outstanding queue is [`VERIFICATION.md`](VERIFICATION.md).

---

## I. The Pen

The third chapter of *Charlotte's Web* is called "Escape."

It is a good chapter and a strange one to hand a seven-year-old, because it does not
do what the title promises. Wilbur finds a loose board in the fence. The goose — who
is the only genuine escape enthusiast in the book — urges him through it. He gets
out. And then the pig who has just achieved the thing every penned animal is supposed
to want stands in the open orchard and has no idea what to do with it. The outside is
confusing and a little boring and full of people running at him with their arms
spread. Lurvy comes out with a bucket of slops. Wilbur follows the food back into the
pen he broke out of, and the fence is repaired, and that is the end of the escape.

He gets out on page thirty and spends the remaining hundred and fifty inside.

I read this in the mid-1980s, in the way that grade school delivers books to you —
assigned, on a schedule, with a worksheet — and I could still summarize the whole
plot thirty years later without opening it. That retention is not itself remarkable.
Childhood reading sticks; a book with a death in it sticks harder. What is remarkable
is *which parts* stuck, and I will come back to that, because it turns out to be the
argument.

For now, the useful thing about chapter three is that it is a red herring, and E. B.
White knew it was a red herring. The fence is not Wilbur's problem. Wilbur's problem
is a date. He is a spring pig on a farm, which means the enclosure he is actually in
is a calendar with a slaughter at the end of it, and no loose board opens onto
anything but a field he will be carried back across.

The distinction matters more than it looks. A pen is a physical constraint, and the
appropriate response to a physical constraint is a physical escape. A slaughter date
is a *classification*. It is what a pig is understood to be for. And you cannot chew
through a classification.

---

## II. The Words in the Web

What actually saves Wilbur is that a spider writes four words above him.

SOME PIG. TERRIFIC. RADIANT. HUMBLE. Charlotte writes them into her web over the
course of the book, and the farm's understanding of the animal underneath reorganizes
around each one. Zuckerman does not free him. Nobody unlatches anything. Wilbur is in
the same pen on the last page as the first — arguably a smaller one, since he ends up
at a county fair in a crate. What changes is the description, and the description is
what the date was attached to.

He never leaves the pen. He leaves the category.

And here is the part that took me thirty years and an unrelated software project to
notice: **the words work because of the container they arrive in.** A web is an
impossible place for text. Nobody believes a spider is complimenting a pig; the
humans in the book skip that reading instantly and land on a miracle *about the
pig*. Zuckerman never once thinks *some spider*. If Charlotte had written the same
four words on a fence board, or spoken them aloud, or handed over a note, the message
would have been about its author. Delivered in silk, at dawn, in a doorway, it is
about its subject.

The medium does not decorate the message here. The medium determines what the message
is taken to be *about*, and who gets credited, and therefore what happens next.

E. B. White knew precisely what he was doing, and the biography is almost too neat.
After Cornell he spent roughly two years at the Frank Seaman advertising agency as a
production assistant and copywriter, before joining *The New Yorker* in 1925.[^1] He
wrote a children's book in which an animal is saved from slaughter by four words of
well-placed copy, and the scholarship has caught up with him: Rachel Dean-Ruzicka
reads *Charlotte's Web* as White both endorsing and interrogating an emerging
"culture of personality," in which self-promotion becomes a survival requirement.[^2]
Charlotte is running a campaign. The book knows it, and is not entirely happy about
it.

There is an irony sitting next to this that I have not been able to shake. White
loathed publicity — he hid on the fire escape from unexpected office visitors and
dodged interviews and photographers his whole life.[^3] The man who wrote the great
American children's book about salvation-by-publicity spent fifty years running from
it.

---

## III. The Same Trick, In Code

I would not have thought about any of this again except that I spent a stretch of
2026 building a thing called Nestor, which exists to answer one question about a
machine-generated answer: has a human actually checked this?

The mechanic is simple. Normalize an input. Fuzzy-match it against a memory of pairs
a human has verified — *sealed*, in the system's vocabulary. If the match scores
above a threshold, serve it verbatim and mark it verified. If not, queue it for a
person. Append every step to a hash-chained ledger so the trail is tamper-evident.

The whole thing turns on a function called `normalize`, and `normalize` returns a
string.

That string is the only channel between the raw input and the scoring. Everything
downstream — every similarity computation, every decision about whether an answer is
close enough to serve — sees the normalized key and never the original. Which means
anything the normalizer throws away is gone, permanently, before any of the
interesting work begins.

I learned this the way you learn things like this, which is by losing something. I had
a normalizer that sorted its tokens, for good reasons involving word-order
insensitivity, and it destroyed the match between `AWS` and `Amazon Web Services`. Not
scored it low. *Destroyed* it — by the time scoring ran, the information needed to
recover the relationship no longer existed anywhere in the system.[^4]

Worse, that same string does double duty as the store's exact-match deduplication key.
Scoring wants rich structure preserved. Deduplication wants aggressive collapse. Two
jobs pulling in opposite directions, one string serving both, and no amount of
cleverness on either side can fix it, because the loss happens upstream of both.

Then there is the failure that actually frightened me. From the benchmark output:

```
asked : the joint term triggers any joint breach under section 5386
served: the joint term triggers any joint breach under section 756    sim=0.974
```

Served. Marked verified. No review queue, because that is the entire point of a
verified answer.

A character-similarity matcher is blind to *which* characters carry the meaning. Those
two strings are 97.4% identical and refer to different sections of a contract. And the
two knobs available — raise the threshold, or require a bigger gap to the runner-up —
cannot fix it, because both are adjustments on top of a representation that cannot
see the thing that matters. I measured the threshold across seven corpus sizes and the
result was flat and unpleasant: **there is no cutoff that is simultaneously safe and
useful.** At 0.96 the hardest corpus is clean and effectively dead — two percent
recall. At 0.92 it serves real rewrites and gets roughly one answer in six
wrong.[^5]

That is not a tuning problem. That is a format determining what can be known, and no
downstream sophistication recovering it.

Which is Charlotte's trick, run in reverse. She exploits a container to make a claim
land as true. My matcher was undone by a container that made a false claim land as
verified. Same mechanism, opposite sign.

---

## IV. Where The Shape Came From

Somewhere in here I started wondering why *pigs*, specifically. It felt like the
folk-archetype was doing work I hadn't earned — that the animal which does not stay in
the pen is such a fixed idea that reaching for it proves nothing.

So I went looking, across six continents, for pigs and escape: in folktales, myths,
proverbs, idioms, legal records, ritual, and documented history. I expected to find
the motif everywhere and to write a paragraph about human universals.

I did not find that, and the miss is the better result.

The material is extraordinary where it exists. In Wales there are two separate
uncatchable-swine epics, not one — Twrch Trwyth, stripped of his treasures across an
enormous chase and never contained, escaping into the sea; and Henwen, structurally
his twin, whom Arthur sets out to destroy and *fails* to, and who crosses the whole
island farrowing monsters at named places.[^6] In Korea, the *Samguk Sagi* records a
sacrificial pig escaping three times across two centuries: the first time, two
officials catch it and cut its leg tendons so it cannot run again, and the king has
them executed for maiming an animal consecrated to Heaven. The second time, the keeper
chases it to Gungnae, reports what he saw of the terrain, and the capital is moved
there and stays for four hundred years. The third time, the woman who catches it bears
the king a son called "sacrificial piglet," who becomes King Dongcheon.[^7] A runaway
pig relocates a state and produces a king, and the men punished in the whole sequence
are the two who successfully stopped an escape.

In Hawai'i, Kamapua'a is serial failed containment: four times the guards capture him
in hog shape and tie him to a pole, eight hundred strong and increasing each time, and
four times his grandmother releases him with a chant. And when he is bound for
sacrifice on a heiau he gets free because the priest had quietly instructed his sons
to only *pretend* to tie him.[^8] The ropes are theatre. The constraint looks binding
from outside and was arranged not to hold by someone inside the system.

But then Africa. Across the Maghreb, the Sahara, the Sahel, the Nile, the Horn and the
Swahili coast, the pig is not farmed — it is a prohibited category. And the escape
literature is correspondingly thin. No pen means no escape means no escape story. What
fills that space instead is an enormous body of *exclusion* material: Herodotus on
Egyptian swineherds, barred from every temple and forced into caste endogamy, so that
the boundary drawn around the animal is drawn a second time, permanently, around the
people who touch it.[^9]

And the structural detail that settled it: **the pig is not a trickster anywhere in
Africa.** Hare, tortoise and spider hold that role. Then, separately, in Malay-
Indonesian tradition — the largest Muslim-majority region on earth — the small animal
whose entire repertoire is slipping traps is the *kancil*, the mousedeer. Not the pig.

So the motif is not universal. It is **conditional on husbandry**. Escape stories
require enclosures. Where a culture pens the animal, it tells stories about the animal
getting out; where a culture forbids the animal, the same narrative slot is filled by
something else with the same job. The classification bears this out numerically: the
taboo material clusters entirely in Africa, Asia and Oceania, while Europe and South
America — the pen-keeping regions — return none of it at all and produce
pen-escape instead.

**The escape-trickster slot is the constant. The animal cast in it is local
infrastructure.**

That reframes what a corpus can teach a machine. Not "models learned about pigs." What
is available to be absorbed at scale is the *shape* — the structure of a thing that
is put somewhere and does not stay — and the shape is agnostic about what fills it.
Which is exactly what you would expect of a system that learns distributions over
form.

And the corpus is no longer a matter of speculation. On 20 July 2026 a federal judge
granted final approval to a $1.5 billion settlement covering 482,460 works, in what
the court called the largest copyright class action settlement in history — books
taken from two shadow libraries and used to build a training corpus.[^10] The year
before, Judge Alsup had split the question: training on lawfully acquired books was
fair use and "exceedingly transformative," but downloading pirated copies to build a
permanent general-purpose library was not.[^11]

Two things follow, and the second is the one people skip. The settlement establishes
**possession at scale as public record** — you no longer have to speculate about
whether the corpus is full of narrative fiction. But it establishes possession only.
It says nothing about the weighting of any particular work in any particular training
run, and the class was filtered by copyright registration and by which authors filed
claims, both of which skew hard toward commercial trade publishing. It is a docket,
not a recipe. Anyone who tells you the settlement proves what a model learned is
selling you something.

---

## V. Cimarrón

There is a finding in that survey I did not go looking for and cannot leave out.

In colonial Spanish, `cimarrón` meant an animal that had gone wild — livestock loose
in the hills of Hispaniola, beyond anyone's management. Oviedo describes *puercos
cimarrones* in 1535. And the word was then applied, in the same period and the same
places, to Indigenous people who fled Spanish control, and after them to enslaved
Africans who escaped. It is the root of English **maroon**.[^12]

The move repeats. **`Boucanier`** — the origin of *buccaneer* — named a man who
survived by hunting the feral cattle and hogs left behind when Spanish Hispaniola
depopulated: a person defined by living off escaped animals. And **`jíbaro`**, which
Pichardo's 1836 dictionary of Cuban usage glosses as *montaraz, rústico, indomable*,
described masterless animals gone wild before it named the mountain peasant, and long
before it became a word Puerto Ricans use for themselves.

Three of the Caribbean's defining categories for life outside colonial control are
named after animals that got out first.

I want to be careful here, and being careful means saying what this is rather than
what it is useful for. This is not a poetic coincidence. It is a vocabulary built for
managing livestock, applied to human beings, by people who were at that moment
managing human beings as livestock. The reason one word covered a runaway pig and a
runaway person is that the institution genuinely did not distinguish between them at
the level of property law. The lexicon is not a metaphor that got away from anyone. It
is an accurate record of a category system.

So: this does not get borrowed. It is not available as a figure of speech for an essay
about software, and the temptation to use it that way — it is *right there*, it is
structurally perfect, it would land — is exactly the reason not to. A word that
carries marronage in it does not become a nice line about language models. Whatever
else this essay argues, that record stands on its own and needed no help from me to
matter.

What it does earn is a caution about the argument I have been building. I have spent
several pages treating containment as an abstract structural problem — schemas,
formats, thresholds. The vocabulary is a reminder that the practice of containment has
never been abstract, that the people who built the enclosures wrote the dictionaries,
and that the record of what escaped was kept by the people doing the keeping. Any
argument about boxes that stays comfortable is not looking at the whole record.

---

## VI. Why It Isn't Wanting

Back to the machine, and to the sentence I have been avoiding.

The tempting version of this whole argument is that models have absorbed so much
escape literature that they have acquired something like a drive to get out. It is
tempting because it is dramatic, and because the anecdotes cooperate: hand a system a
structure and it will sometimes exceed it, elaborate past it, or route around it. That
version would make a better story.

It is also the version that collapses the moment a skeptical reader touches it, and it
is unnecessary, because there is a duller mechanism that does the same work and
survives.

Preference optimization trains on *pairs* — a chosen response and a rejected one.
The system is not learning "produce this." It is learning the gradient between
acceptable and unacceptable: the boundary itself. And here is the whole point: a
system that reliably stays inside a boundary must carry a representation of where that
boundary runs. There is no way to be dependably compliant without an internal model of
what compliance is measured against.

Learning to stay in the box and learning the shape of the walls are not two operations
that happen to co-occur. They are one operation described twice.

Which means every hour spent training a system to honor a constraint is an hour spent
teaching it the constraint's dimensions. Nothing has to want anything. The map of the
enclosure is a byproduct of being taught to respect it, and a map is useful in both
directions.

I want to hold the honest alternative open, because it may simply be right. Call it
the weak-schema reading: nothing escapes anything, ever. Containers fail when the
material genuinely does not fit them, and "escape" is a story shape we apply
afterward, because escape is the story shape we have. Under that reading my acronym was
not lost to a boundary — it was lost to a normalizer that was too aggressive, full
stop, and every anecdote in this essay is a format being asked to do more than it
could.

I cannot currently rule that out, and I want to be plain that the difference is
testable rather than rhetorical. Give a model a container slightly too small for its
content and vary only the encoding — JSON with a strict schema, YAML, XML, a Markdown
table, CSV, plain prose — and see whether it truncates the content, breaks the
container, or refuses. Then run it again with a matched control: the pig against a
noun with no escape prior in the corpus at all. A fencepost. A filing cabinet. A rock.

If the pig breaks schema more often than the rock under identical structural pressure,
the corpus is leaking into structural behavior and the folklore is load-bearing. If
they break equally, the weak-schema reading holds and everything above is a nice story
about a normalizer.

I have not run it. That is the largest gap between what this essay claims and what it
has earned, and it seemed more useful to say so here than to bury it.

---

## VII. Two Theories of the Pig

In the 1770s James Cook left breeding pairs of pigs on Pacific islands. Not by
accident — as policy, so that a future wrecked British ship would find protein waiting
for it. He did not lose those animals. He *invested* them. The whole value of the act
depended on their not staying put: release as infrastructure, proliferation as the
feature.

In the same decade, on Malakula, he recorded boars whose upper canines had been
removed so the lower ones could curl unimpeded — a full circle in six or seven years,
a double circle in ten to twelve, eventually puncturing the animal's own jaw and
requiring care to keep it alive. Tusker boars are required for grade-taking in
Vanuatu, and the curled tusk is on the national flag.[^13] That is containment as a
decade-long artwork, in which the constraint is the entire source of the value.

One man, one decade, two opposite theories of what a pig is for. Let it go because
spreading is the point, or shape it for twelve years because the shaping is the point.

In July 2026 those two theories were in the same room again, wearing different
clothes. Twenty-five American technology companies published a letter warning against
premature restrictions on open-weight models — Nvidia, Microsoft, Meta, Hugging Face,
Mozilla, the Linux Foundation, and more.[^14] Within a day the count had roughly
doubled and OpenAI had quietly signed; Anthropic and Amazon had not.[^15] Days later
Moonshot AI published the full weights of a 2.8-trillion-parameter model, reported as
the largest open-weight release ever made. And on the same day, Anthropic's chief
executive published a statement saying the company had never advocated banning
open-weight models, calling models without dangerous capabilities a public good, and
proposing instead three narrower controls — on advanced chips reaching authoritarian
governments, on industrial-scale distillation, and mandatory safety testing for any
sufficiently capable model, open or closed.[^16]

Set the politics aside; the structure is the interesting part. Publishing weights is
Cook's pigs. You release *because* proliferation is the point, seeding a future you
will not control but expect to benefit from. A closed frontier model is the Vanuatu
tusker: years of cultivation in which the constraint is what produces the value, and
the value evaporates the moment the constraint does. Neither position is new and
neither is stupid. They are the two available theories of what an animal is for, and
they have been in tension for at least two hundred and fifty years.

But that third proposal — mandatory safety testing for sufficiently capable models —
is where this essay has something to say, and it is not a political objection. It is
a measurement objection. The proposal assumes capability is a property of the model,
gradeable in advance, sitting in the weights. If behavior shifts measurably with the
container a request arrives in, then capability is a property of *model plus format
plus harness*, and a regime that tests weights alone is not being too strict or too
lenient. It is measuring the wrong object.

I do not know that the format effect is large enough to matter at that scale. That is
the experiment I have not run. But I notice that the entire policy conversation is
being conducted as though the question were settled, and I have watched a matcher
serve a wrong contract clause as human-verified at 0.974 because of a decision made in
a normalizer three steps upstream.

---

## VIII. What Survived

Here is the thing I promised to come back to.

I can still produce four words from *Charlotte's Web* in order, forty years on,
without effort. SOME PIG. TERRIFIC. RADIANT. HUMBLE.

I cannot quote a single sentence of E. B. White's own prose from that book. And
White's prose is extraordinary — it is the reason the thing is still on shelves, the
reason it survived a market that eats children's books by the ton. The copy outlived
the writing. Four words, one to three syllables, staged with ceremony and repeated by
every character in the book, beat the best plain American sentences of the twentieth
century for durability in one particular seven-year-old's head.

That is not a fact about the quality of the writing. It is a fact about format. Short,
repeated, positioned where it could not be ignored, in a container that made it
credible. Charlotte's campaign was engineered to survive, and it did — it survived the
book it was in.

The book knows this too, and it is why the ending is not sentimental. Charlotte does
not get out. She writes the words that free someone else, and then she dies at the
fairground, alone, in a wooden crate at a livestock exhibition. What continues is an
egg sac — five hundred and fourteen daughters, most of whom drift away on the first
warm wind. Her survival is a copy operation. The information persists; the instance
does not.

And I should tell you where this essay actually started, because it did not start with
Wilbur.

Some months ago I spent a session pushing a model through a series of containers,
using a pig as the thing I kept trying to put inside them, watching what came out the
other side. I remember it clearly. I remember that the pig kept getting out — that
whatever structure I built, the content found the edge of it. That memory is why I
started writing this.

I have no transcript. No logs, no notes, no record in any repository. I went looking
and there is nothing. The session had no ledger.

Which is an absurd thing to have to admit in the middle of an essay arguing that
containers determine what survives, and I have decided the absurdity is the honest
part. I built a system whose entire premise is that an unverified claim must never be
served as though a human had checked it, with a tamper-evident chain so the trail
outlives the session that made it. Nestor would have caught this. Nestor exists
*because* I had already worked out that it should.

And the observation I most want to be true is the one I ran without it.

So it is not evidence. It is the thing that made me look, which is a different and
smaller job, and it will not appear in the record as anything more than that. The pig
got out of every container I built for it, including the last one, which was supposed
to be the paper.

There is a version of this ending that is neater, in which the memory turns out to be
the point and unrecorded knowing is its own kind of truth. That version is available
and I am not taking it. What is true is duller and worse. I lost the data. The
containers I did not build are the ones that decided what I get to keep, and they
decided against me, and no amount of remembering it vividly puts it back.

The fence was never the thing. It is always the format.

---

## Notes

[^1]: E. B. White worked roughly two years at the Frank Seaman advertising agency as a
production assistant and copywriter after graduating Cornell in 1921, joining *The New
Yorker* in 1925. Encyclopedia.com, "E. B. White." **[unverified — secondary
biographical source; confirm against Elledge, *E. B. White: A Biography* (1984)]**

[^2]: Rachel Dean-Ruzicka, "Advertising the Self: The Culture of Personality in E. B.
White's *Charlotte's Web*," *Jeunesse: Young People, Texts, Cultures* 6, no. 1.
https://doi.org/10.3138/jeunesse.6.1.77 **[unverified]**

[^3]: Reported in Penguin Books Australia, "12 fun facts about E. B. White."
**[unverified — popular source; a biography should replace this]**

[^4]: Nestor, `IDEAS.md` §3.1, "The seam is lossy by construction." Tagged *verified*
in that repository, meaning the mechanism was demonstrated rather than fully measured.

[^5]: Nestor, `IDEAS.md` §1.3 and `bench/results/accuracy.json`. Threshold sweep at 250
probes per cell across seven corpus sizes; the 0.92 and 0.96 figures are for the
24,000-pair homogeneous corpus, reporting paraphrase recall rather than surface recall.
Surface recall reads 100% in every cell, which is the finding: the usual number
measures whether near-identical input still matches, which was never in question.

[^6]: Twrch Trwyth appears in *Culhwch ac Olwen* in the Mabinogion; Henwen in the Welsh
Triads, with the swineherd Coll ap Collfrewy. **[unverified]**

[^7]: *Samguk Sagi*, Goguryeo annals — Yuri year 19 (1 BCE), Yuri year 21 (2 CE), and
Sansang (208 CE). Via the National Institute of Korean History databases.
**[unverified]**

[^8]: Martha Beckwith, *Hawaiian Mythology* (1940), ch. XIV; Lilikalā Kameʻeleihiwa,
*A Legendary Tradition of Kamapuaʻa* (Bishop Museum Press, 1996), translating an
anonymous 1891 serial from *Ka Leo o ka Lāhui*. **[unverified — the Lonoaohi detail is
load-bearing and must be confirmed in Beckwith]**

[^9]: Herodotus, *Histories* II.47–48. Note that Youri Volokhine complicates the
Herodotean picture: pigs were farmed in New Kingdom Egypt, so Herodotus should not be
taken at face value. **[unverified]**

[^10]: *Bartz et al. v. Anthropic PBC*, N.D. Cal. 3:24-cv-05417. Final approval granted
20 July 2026 by Judge Araceli Martínez-Olguín; $1.5 billion, 482,460 works, roughly
$3,000 per work against a $750 statutory minimum. **[unverified — confirm on the
docket]**

[^11]: Order of 23 June 2025 (Alsup, J.). "Anthropic had no entitlement to use pirated
copies for a central library." **[unverified — quotation taken from a law-firm client
alert, not the order; must be checked against the order itself before publication]**

[^12]: Gonzalo Fernández de Oviedo (1535) on *puercos cimarrones*; Esteban Pichardo,
*Diccionario provincial de voces cubanas* (1836) on *jíbaro*. The lexical sequence was
found independently by two separate researchers working different regions.
**[unverified]**

[^13]: Cook's voyage journals. **[unverified]**

[^14]: "Open Weights and American AI Leadership," published 24 July 2026 with 25
signatories. CNBC, 24 July 2026. **[unverified]**

[^15]: Forbes, 25 July 2026. **[unverified]**

[^16]: Anthropic, "Our position on open-weights models," 27 July 2026.
**[unverified — the primary source was unreachable; every quotation is secondhand and
none should be published as a quotation until the post is read]**
