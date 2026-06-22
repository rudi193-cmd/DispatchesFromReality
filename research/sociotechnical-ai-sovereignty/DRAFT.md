# The Illusion of Sovereign AI

*Sean Campbell · June 2026*

---

Every government has a sovereign AI story right now. France has Mistral — European AI that won't bow to Washington. Germany has Aleph Alpha, GDPR-safe and on-prem. Saudi Arabia announced HUMAIN with reported backing around $100 billion and a direct NVIDIA deal (the partnership is firm; the round number is press, not audited). India bought GPUs and bet on the IIT diaspora. China has DeepSeek and Qwen and tells itself it doesn't need American models. The US has Stargate and half a trillion dollars of announced infrastructure. The posture is always the same: we will not be caught. And they're all describing the wrong thing.

"Sovereign AI" today usually means *we trained a model.* It says almost nothing about who makes the chips, who owns the fabs, who sells the lithography machines, or whose money built the stack. Having a model is not the same as controlling the means to produce it.

I've spent the last year building two research databases on this problem — one tracing Operation Paperclip and the postwar contractor genealogy around Huntsville, one mapping the current AI ecosystem: who funds whom, who spun out of whom, which labs depend on which chokepoints. The same story keeps showing up in both. A small set of physical bottlenecks draws capital toward it. A national-security narrative gets loud enough to quiet awkward questions about where the money and the expertise actually come from. Then comes a reckoning when the scale of the bet doesn't match the scale of the return.

The substrate outlasts the press release — that's the through-line. Von Braun's test infrastructure is still firing engines in Huntsville long after the V-2 program is a museum exhibit. TSMC and ASML will still be chokepoints long after whatever we call the "AI era" gets a Wikipedia summary. The question this essay is really asking is what persists when the current bet reprices, which I think it does, probably 2027–2028, and who ends up able to run AI on their own terms. For the first time in this cycle, there's a plausible answer that isn't a government announcement: the capability you need for real sovereignty is getting small enough to fit on hardware you can buy.

---

## The Map: Chokepoints the Sovereigns Don't Control

Start with the part nobody puts on the slide deck: the hardware. Every model runs on GPUs. NVIDIA designs them but doesn't make them — TSMC does. TSMC needs EUV machines. ASML, one company in the Netherlands, makes those machines. There is no second supplier at the cutting edge. The chain from your chat query to a Dutch export license is about five hops long.

This is the same shape of problem Wernher von Braun solved with rockets, except the substrate moved. In the 1940s the bottleneck was propulsion physics and the engineers who understood it. In the 2020s it's lithography and the fabs that turn designs into silicon. The US didn't build sovereign rockets by inventing every part domestically. It imported expertise under political constraint, built facilities that stayed on the ground, and let the institutional layer compound for seventy years. Leidos — a descendant of that contractor world — did $17.17 billion in FY2025 revenue. Cummings Research Park in Huntsville still reports 26,000 employees across 300-plus companies. The engineers die; the infrastructure doesn't.

In 2023 the US pressured the Netherlands to stop selling EUV to China — one machine type, one country — and that decision constrained Chinese AI more than any model regulation I can name. DeepSeek's response, optimizing on older A100s and squeezing algorithmic efficiency, is the same move Mistral made in Paris when they couldn't tap closed American APIs or buy infinite H100s. Constraint comes first, invention second, and the invention doesn't go away when the budget loosens.

Run the sovereign claims against that map and the pattern is blunt. Mistral trains on NVIDIA H100s. Aleph Alpha runs on NVIDIA. India's national mission is buying NVIDIA clusters. HUMAIN's headline is an NVIDIA partnership. DeepSeek trained on A100s High-Flyer accumulated before the export window closed. Every flag on "sovereign AI" terrain sits on Santa Clara designs and Taiwanese fabs.

### Money

Hardware is visible; capital is where the story gets slippery. In January 2025, Stargate was announced at the White House — up to $500 billion over four years, $100 billion initially committed, framed as American strategic victory. The founding partners named that day were OpenAI, SoftBank, Oracle, and MGX, Abu Dhabi's fund, with Masayoshi Son standing next to the President. G42 shows up later in a separate Stargate UAE cluster in May 2025, not on the January list, though a lot of press conflates them. Most of the money behind "US AI supremacy" is foreign, which isn't a moral verdict — capital doesn't carry a passport — but it is a reminder that sovereignty talk and capital geography diverge.

The entanglements don't stop at Stargate. Alibaba sits on Qwen, led Moonshot's Series A, and holds position in Zhipu — three prongs of the Chinese open-weight world from one corporate entity. Open Philanthropy is Anthropic's largest outside funder at roughly $580 million and also funds METR, which evaluates Anthropic's models for safety, so the evaluator and the evaluated share a wallet. Sequoia formally split its China arm in 2023, but the relationships didn't evaporate because the legal entity changed. Same pattern as the postwar era: the program name changes, the money and talent graphs stay entangled.

### People

Three pipelines feed almost every lab. OpenAI is the university of the era — Anthropic, SSI, and TML all carry its DNA. IIT graduates built American tech (Pichai, Nadella, Srinivas at Perplexity), and India now wants that talent back while the salary gap still points the other way. Yang Zhilin went CMU to Google Brain to Moonshot in Hangzhou — Paperclip in reverse, expertise trained in one jurisdiction deployed in another. Talent follows institutions, and institutions follow capital. "Sovereign AI" initiatives don't reset those graphs; they overlay flags on them.

### Distribution

The quiet chokepoint is Hugging Face. Every major open-weight model — LLaMA, Mistral, Qwen, DeepSeek-R1 — lives there, and Hugging Face's Series D investors included Google, Amazon, NVIDIA, Salesforce, and Intel. The companies most threatened by open weights own equity in the neutral platform that distributes them. That's not neutrality; it's managed neutrality — openness as long as you can see what's open and build a moat around what isn't. If you're serious about sovereignty, you mirror weights locally. Most people don't, because Hugging Face is convenient and the dependency is invisible until it isn't.

---

## The Money: Reading the Bubble

The chokepoints tell you where dependency lives. The financial layer tells you when the story breaks — and by mid-2026 the break looks different than it did when I started mapping this.

The causality isn't subtle. ASML can only build so many EUV systems. TSMC's leading-edge wafer capacity is finite. The fastest datacenter GPUs are allocation fights long before they're architecture debates. When every board is told the future of the company — and the country — rides on not falling behind, those physical limits don't cap spending; they amplify it. Hyperscalers aren't committing $650 billion to software dreams. They're outbidding each other for scarce fab slots, power interconnects, and rack years, mostly because they're afraid someone else will lock them out first. Fear turns a hardware bottleneck into a capex arms race. The bubble isn't a separate story from the map in the previous section. It's what happens when unlimited balance sheets meet silicon you can't wish into existence.

Early in 2025 the frontier labs looked like capital sinks with pretty slide decks. That picture is gone.

| Entity | Latest round (2026) | Valuation | Revenue run-rate |
|--------|---------------------|-----------|------------------|
| OpenAI | $122B committed (Mar 2026) | $852B | ~$24B ARR ($2B/mo) |
| Anthropic | $65B Series H (May 2026) | $965B | ~$47B run-rate |
| SSI | $4B raised | $32B | $0 |
| TML | $2B | undisclosed | $0 |
| xAI | $12B | $50B | limited |
| Perplexity | $0.6B | $9B | limited |

OpenAI and Anthropic alone claim something like $70 billion in combined run-rate — company-reported, annualized, still climbing — so the old argument that AI might never monetize is dead. So is the old argument about a simple revenue gap. Hyperscalers are guiding $650–700 billion in combined capex for 2026, roughly double the ~$300 billion Big Four total for 2025. Google alone moved its 2026 guide toward $180–190 billion. At a naive 5× multiple, that kind of spend wants ~$130 billion in AI-attributed revenue to pencil out, not the ~$51 billion implied by last year's guides. Two labs, narrowly counted, already exceed $130 billion on paper.

That doesn't mean there's no bubble. It means the stress moved. Valuations near a trillion dollars aren't pricing today's revenue. They're pricing a decade of compounded growth that has to survive margin compression, financing cycles, and the efficiency releases already landing in H1 2026. DeepSeek V4 shipped in April. API prices dropped faster than my earlier drafts assumed. Capex and valuation got there first, while efficiency eats premium margins even as the top line still grows.

I've seen this movie in the contractor data. Apollo-scale spending didn't shrink the physics; it built facilities and payrolls that stayed when programs cancelled. The AI version builds data centers and GPU fleets that will keep drawing power when the narrative moves on. The question is who can carry the depreciation.

The mismatch resolves in three ways, and they're already overlapping. On efficiency: DeepSeek V3's final pretraining run cost about $5–6 million and matched GPT-4; R1 matched o1; V4 arrived in 2026. Frontier pretraining still scales up — Epoch puts the largest 2024 runs near $390 million, with billion-dollar runs plausible by 2027 — but the cheap stuff is inference and distilled tiers, not the next GPT-class train. When a million tokens costs pennies instead of dollars, the labs priced on premium API margin feel it first. The export-control irony is real here: blocking H100s pushed High-Flyer to optimize roughly 10,000 A100s bought by 2021, while brute-force labs had no reason to bother. Constraint produced the breakthrough that's now compressing their pricing power.

On capex versus margin, Microsoft, Amazon, Google, and Meta report every quarter against those $650B guides. A few cycles where infrastructure spend outruns AI-attributed margin — not raw revenue — and analysts reprice the sector. The hyperscalers survive; their AI bets get discounted; labs living on cloud partnerships lose leverage. On recession, AI is still a line item most CFOs can freeze, and labs burning billions with thin product surface don't weather a six-month procurement winter. The models remain; some wrappers don't.

Where we are in June 2026 is peak valuation and margin compression at the same time — trillion-dollar private entries while API prices fall. The wall is visible, and the raises haven't stopped. Late 2026 brings follow-on friction for mid-tier labs still priced on 2024 multiples. 2026–2027 is when public earnings reckon with capex. 2027–2028 is consolidation, when labs that bet on infinite API margin absorb or fail.

Who's still standing then? NVIDIA, TSMC, and ASML — the substrate, same as the test stands and primes in the postwar map. OpenAI and Anthropic probably survive on revenue scale that didn't exist last year, though whether $850B–$965B entries earn out is another matter. Mistral, DeepSeek, Hugging Face, and Cohere look positioned: lean, open, or boringly enterprise. Who doesn't: SSI at $32B and zero revenue; Scale AI, which did roughly $870M in 2024 with an estimated ~$2B run-rate for 2025 before Meta took about 49% for $14.3B in June 2025 — a labeling business in a world where models increasingly label their own training data; and Chinese consumer labs that raised on app hype without DeepSeek's efficiency engine.

---

## The Efficiency Convergence

Mistral and DeepSeek are the proof case for the constraint story — not because they're virtuous, but because they couldn't buy their way out. Arthur Mensch, Guillaume Lample, and Timothée Lacroix left DeepMind and Meta's FAIR and started Mistral in Paris in 2023 with European sovereignty rhetoric and no closed US API spigot. They trained Mistral 7B on commodity hardware, matched LLaMA 2 13B at half the parameters, and released the weights. Small and disciplined beat large and expensive — not as philosophy, as arithmetic.

DeepSeek sits inside High-Flyer, a quant fund in Hangzhou, with roughly 10,000 A100s by 2021, before export controls closed the H100 window. When the faster chips arrived they couldn't buy in. Two years later came V3 for about $6 million in reported compute at GPT-4 class, then R1 at o1 class, built from mixture-of-experts, better data curation, and training stability — the tricks you find when you can't run another thousand H100 hours. OpenAI, Google, and Anthropic could always buy more compute. They did, and they didn't have to invent the cheap path.

The ratchet only turns one way. A 7B model in 2026 beats a 7B model in 2024 beats a 7B model in 2022. What required a rack in 2023 runs on a laptop in 2025. That's the new variable in the old story. Postwar rocketry never got small enough to leave the pad. AI is getting small enough to leave the data center.

---

## The Post-Bubble Landscape

When Apollo programs shrank, Huntsville didn't empty out. Test stands, primes, and federal relationships stayed. The rockets changed; the substrate persisted. AI's substrate is silicon, power, and weights, but the selection pressure rhymes: after overbuild comes repricing, and the survivors match cost to what actually outlasts the hype.

That repricing is already audible. API costs are falling — H1 2026 moved faster than I expected when I first wrote this — and a hospital choosing where to run clinical support tools used to face an easy math problem: cloud API is good enough and local is too weak. As the gap closes, the math flips for anyone who cares about privacy, uptime, jurisdiction, or grounding answers in records that never leave the building. GDPR and HIPAA don't care about your sovereignty press conference; they care where the bytes go. Convenience is a real advantage, but it isn't sovereignty.

Institutions that need control — hospitals, regulators, law firms, schools — will eventually have no financial reason to rent what they can run on a box they own. The labs that survive the correction are the ones positioned for that world: open weights, efficient models, local inference. Same cluster the dependency map pointed to all along.

---

## What Sovereignty Actually Requires

A national model on rented H100s is the house on the floodplain: you hold the title, but you don't control the river. Real sovereignty — the kind that survives a repricing, a vendor dispute, an export rule — needs five things you can actually touch.

You need weights you can download and keep, not API access someone can revoke. You need hardware you own, not instances you rent. You need inference software you run — llama.cpp, Ollama, something without a monthly permission slip. You need isolated local data infrastructure: your documents, your patient records, your case files indexed and updated on hardware you control, whether that's local retrieval-augmented generation, on-prem fine-tuning pipelines, or both, so a foundation model anchors to *your* reality instead of the internet's average. And you need no single dependency that can pull the plug on all of the above. ASML's monopoly is fine for ASML; it isn't sovereignty for you.

That stack exists today. Mistral 7B, LLaMA 3 8B, Qwen 2.5 7B, and DeepSeek-R1-Distill are all runnable locally. llama.cpp on Apple Silicon — an M3 Pro with 36GB can run a 13B model in Q4 at roughly 25–45 tokens per second, usable if not frontier-fast — plus consumer NVIDIA cards for more speed. Pair that with a local vector store and retrieval layer, or a small fine-tune on data that never leaves the building, and the model stops being a generic oracle and starts being an instrument grounded in what you actually know. Mirror your downloads; don't assume Hugging Face lasts forever.

The gap to closed API performance closes every few months. By the time the bubble I'm describing fully breaks, a local open model will be close enough for most of what most institutions actually do. Mistral, DeepSeek, the llama.cpp ecosystem, and Hugging Face (with mirroring) are building toward that; RISC-V sits on a ten-year horizon for hardware that might someday not terminate at TSMC. What's selling the illusion is every national GPU cluster still on NVIDIA silicon, and every "sovereign cloud" that's Azure with a European contract wrapper — Delos in Germany, T-Systems, IONOS, OVH, Gaia-X as standards rather than substrate — real compliance gain, not operational independence.

---

## Coda

The Paperclip database and the sociotechnical database aren't separate stories. They're the same story with different nouns: chokepoints, capital flowing toward them, a security narrative loud enough to skip the hard questions, a reckoning when the bet overshoots, and what persists in facilities, relationships, and physics rather than announcements.

You can see it in Saudi money in Stargate, UAE conditions on Chinese components, export controls that accidentally trained the competitor they were meant to block, trillion-dollar valuations while token prices fall, Blue Origin firing engines on Marshall test infrastructure von Braun's world built, Leidos still billing, Cummings still counting heads. The chokepoints remain, as do the capital concentrations, and talent still crosses borders no matter which flag is on the slide.

What's new is the escape hatch. A 7B model on a MacBook. A distilled reasoning model on a Raspberry Pi 5 at roughly 8–10 tokens per second — not full R1, not viral-claim fast, but real enough to use. The capability that used to require a data center and a vendor relationship fits in a room you control. That's the sovereign AI story worth telling, and it doesn't need a press conference.

---

*Built from two research databases: a sociotechnical map of 30 AI organizations, 76 people, 80 dependency edges, and 56 observations; and a postwar contractor genealogy tracing Paperclip through Huntsville. Chokepoint chains, funding relationships, and talent flows are documented and queryable — not inferred from vibes.*
