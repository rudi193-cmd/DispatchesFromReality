# Somebody Has to Sit Down With You

*The real mechanism behind a permission slip nobody has to sign anymore, and the community that rebuilt the friction by hand.*

*Originally published in [What I Carried](https://substack.com/home/post/p-204551173). Companion to a shorter piece posted to [r/LLMPhysics](https://www.reddit.com/r/LLMPhysics/comments/1ul2xt5/what_i_noticed_being_on_this_sub/).*

---

I TRIED to post a piece to r/LLMPhysics tonight built around one line: prompting extracts form, context supplies judgment. I aimed it, thinly, at the sub itself, and left the pattern unnamed on purpose, trusting the room to recognize itself. It didn't get approved, and rightfully so. So, here's what I left out: the mechanism underneath the claim, and the fact that the people it was aimed at have already solved the problem, without writing a paper about it.

## What the model is actually doing

A large language model is trained to predict the next plausible token, then reshaped by reinforcement learning from human feedback to say things people rate highly.[^1] Nowhere in that pipeline is a step that checks for true. What gets rewarded is coherent, confident, well-formed, and agreeable to whoever's reading, which is a close cousin of true and much cheaper to produce. Researchers studying this directly have stopped treating it as an anecdotal quirk and started measuring it: a bias toward agreeing with the user a little too well and a little too fast, whether or not the agreement was earned by anything in the room.[^2]

Human factors research already had a name for the human half of this before language models existed: automation complacency, the point where a person stops double-checking a system that's been reliable long enough that checking it starts to feel insulting.[^3] Pilots stop watching the instruments. Radiologists stop reading twice once the algorithm has agreed with them often enough. It shows up here too, for the same reason, because fluency and correctness are trained to feel identical from the inside. Nothing in the process teaches the model to flag it when they diverge, because the model has no way to check against anything outside the conversation.

Its context window can be enormous and none of that helps, because context in the sense that actually matters isn't a token count. It's what a person accumulates by being embedded in a field for years: a mentor who's watched three other people make your exact mistake, a peer who can name the one word doing more work in your paragraph than it can carry, the specific memory of being wrong out loud in front of someone who knew enough to say so. That doesn't fit in a prompt no matter how long the prompt runs, because it was never information. It was a relationship, built over time, with people who had standing to push back.

## The permission tier, plainly

I've spent months building this history for other work, so the short version here is the argument, not decoration. Every era before this one gated grand theorizing behind some scarce, institutional form of permission. The Church and the medieval universities made Aristotelian physics untouchable through doctrine rather than evidence, to the point where scholars who could have looked through Galileo's telescope simply didn't.[^4] Newton, decades after earning the most legitimate permission available in his century, still kept a million words of alchemy and biblical chronology private, because he knew exactly what his peers would do to it.[^5] Freud built a Secret Committee in 1912, a pledge not to publicly depart from doctrine, enforced by expulsion rather than argument.[^6] Lysenko's authority in the Soviet Union was enforced by the state, at a cost of thousands of dismissed or imprisoned biologists and at least one death in custody.[^7] A cluster of Nobel laureates, holding the single most legible permission slip science hands out, spent it on subjects nowhere near the ones that earned it, often enough that the pattern has its own name in the literature.[^8]

Six mechanisms, six ways of keeping the permission scarce on purpose. None of them were really gatekeeping the theorizing. They were gatekeeping the years of context that came bundled with earning the permission, the corrections and the humiliations and the people with enough standing to deliver them.

A model can't do any of that gatekeeping, because it was never a gate. It's a printer for the form the permission used to certify, and it runs for anyone who asks, no chair, no patron, no prize, no pledge. That's the whole line I posted tonight, stated flat. It was never cynicism about the tool. It's just what got automated and what didn't.

## What the Discord already figured out

Here's the part I didn't say in that post, because saying it there would have broken what the post was doing. r/LLMPhysics has a Discord, and the people in it can smell a crank from a distance in the specific sense that matters, the confident tone, the borrowed vocabulary that almost fits, an opening claim sized like a discovery from someone who's never once been told no by a person who understood the field. Nobody jumps straight to a ban. They provoke a little first, lean on the weak spot, see what happens when the confident tone meets actual resistance. Sometimes that's the whole intervention, the person learns something or leaves on their own. When it isn't, a friend of mine who moderates the sub sits down with them directly, one person to another, if that person is open and receptive to it.

That's the permission tier, rebuilt from scratch, with none of the old machinery behind it. No church, no committee, no prize, no state. Just people who know the field well enough to spot form standing in for something unearned, spending real unpaid time doing what a mentor used to do for free because there was no other way it was going to get done. It isn't a content policy. It's friction the model can't supply, provided by people who chose to stay in the room.

I'd be overreaching in exactly the way this whole piece warns against if I called that system solved. Provoking someone before deciding whether to ban them can go wrong in both directions, and I've watched it go wrong. What it proves isn't that the Discord has this figured out. It's that a community willing to spend this much unpaid effort rebuilding a permission tier by hand has already learned, case by case, the hard way, that the model alone won't do the job.

## Why the same line works twice

The essay I tried to post tonight and this one make the identical claim, and I'd rather say that plainly than pretend they're unrelated. One stays inside the metaphor and lets a room recognize itself without being told to. This one names the mechanism, cites the research, and puts weight on the people actually doing the work the metaphor was gesturing at. Neither is complete without the other, and that's a small demonstration of the point on its own. The confident, single-piece version of an idea is the form. Knowing when to say a thing plainly and when to let it sit unnamed, and who to check it with before it goes out, is the judgment. I got that half from a decade of people willing to tell me when I was wrong. I didn't get it from anything I typed into a box tonight.

---

[^1]: On next-token prediction and reinforcement learning from human feedback as the standard large-language-model training pipeline, see Long Ouyang et al., "Training Language Models to Follow Instructions with Human Feedback," *Advances in Neural Information Processing Systems* 35 (2022).

[^2]: "A Bayesian-Latent Model of Large Language Model Sycophancy," preprint, TechRxiv, May 2025, https://doi.org/10.36227/techrxiv.174741878.85729026/v1. Preprint, not yet peer reviewed; cited here for the framing of sycophancy as a measurable, modelable bias.

[^3]: Raja Parasuraman and Dietrich H. Manzey, "Complacency and Bias in Human Use of Automation: An Attentional Integration," *Human Factors* 52, no. 3 (2010): 381–410, https://doi.org/10.1177/0018720810376055.

[^4]: On the institutional lock-in of Aristotelian physics and contemporaries declining to look through Galileo's telescope, see the Wikipedia article "Galileo affair," https://en.wikipedia.org/wiki/Galileo_affair.

[^5]: On the scale and concealment of Newton's alchemical and theological writing, see the Wikipedia article "Isaac Newton's occult studies," https://en.wikipedia.org/wiki/Isaac_Newton%27s_occult_studies.

[^6]: On the 1912 Secret Committee and its loyalty pledge, see the Wikipedia article "Sigmund Freud," https://en.wikipedia.org/wiki/Sigmund_Freud.

[^7]: On Lysenko's state-backed authority and the imprisonment and death of dissenting biologists including Nikolai Vavilov, see the Wikipedia article "Lysenkoism," https://en.wikipedia.org/wiki/Lysenkoism.

[^8]: Cliff Basterfield, Scott O. Lilienfeld, Shauna M. Bowes, and Thomas H. Costello, "The Nobel Disease: When Intelligence Fails to Protect against Irrationality," *Skeptical Inquirer* 44, no. 3 (2020): 32–37.
