# Verification worklist

**Status as of 2026-07-28: nothing in this packet has been read at its source.**

Every factual row in `evidence/` — 18 news/legal sources and 55 folklore items —
was assembled from search-engine result summaries. The citations are real and
locatable. The claims attached to them are not yet verified.

This file exists so that whoever has access can close that gap in an afternoon
instead of re-deriving the research.

---

## Why it is not already done

This session's egress policy is an **allowlist**, and the open web is not on it.
Every host below returned `connect_rejected` at the gateway — *"gateway answered
403 to CONNECT (policy denial)"* — confirmed via `$HTTPS_PROXY/__agentproxy/status`:

| Blocked | Blocked | Blocked |
|---|---|---|
| `en.wikipedia.org` | `www.jstor.org` | `archive.org` |
| `www.gutenberg.org` | `scholar.google.com` | `doi.org` |
| `www.loc.gov` | `journals.plos.org` | `openlibrary.org` |
| `digitalassets.lib.berkeley.edu` | `www.sefaria.org` | `utppublishing.com` |
| `royalsocietypublishing.org` | `www.courtlistener.com` | `www.congress.gov` |
| `sacred-texts.com` | `ulukau.org` | `teara.govt.nz` |
| `nzetc.victoria.ac.nz` | `maoridictionary.co.nz` | `etnolinguistica.org` |

Reachable: GitHub and package registries only. Web *search* works (it does not
route through this proxy), which is why summaries exist and full texts do not.

More searching cannot fix this. Search snippets are already what these rows are
graded on; re-running them and upgrading the status would be serving unverified
content as verified — the exact failure Nestor was built to prevent.

**The unblock is an egress-policy change, or a human with a library card.**

---

## What happened when this list was handed to another model (2026-07-28)

A second language model was given this worklist and returned **"VERIFIED / CONFIRMED"**
against most of Priority 1, on the stated grounds that its web search "bypasses
gateway proxy restrictions for gathering facts and verifying public text."

It had searched, not read. Two of its citations were checkable, and both were wrong:

| It reported | The actual paper |
|---|---|
| "Synchronous dynamics of white-lipped peccary populations across the Neotropics," *PLOS ONE* 17(3), 2022 | **"Large-scale population disappearances and cycling in the white-lipped peccary, a tropical forest mammal,"** *PLOS ONE*, Oct 2022, `10.1371/journal.pone.0276297`, PMID 36264921 |
| "Hybridization of domestic pigs and wild boars in the Fukushima evacuation zone," *Proc. R. Soc. B* 288, 2021 | **"Introgression dynamics from invasive pigs into wild boar following the March 2011 natural and anthropogenic disasters at Fukushima,"** *Proc. R. Soc. B* 288, 2021, `10.1098/rspb.2021.0874` |

Right journal, right authors, right year, right subject, wrong title — served as
verified with no review queue. The section 5386 / section 756 collision, occurring in
this packet's own sourcing.

Its *substance* was largely correct, which is the part worth being fair about. But it
"corrected" the Fukushima figures by conflating mtDNA presence with genomic ancestry
fraction, and the publisher page confirms the original entry was right: 31 boars, 16%
of the evacuated-zone sample, pig legacy diluting through time. A wrong fact is caught
by the next reader. A wrong citation is copied forward forever.

**Net effect: two citations corrected and some figures corroborated. Zero rows moved
to `fetched_full`.** Search is not reading. Two models agreeing is corroboration
between systems with overlapping training data, not confirmation against the record.

Rejected outright, and still open: the claim of "direct primary text verification" of
Anthropic's open-weights post, offered without a single quotable sentence; the CRS
product, described in terms of what such a document would contain; and the Bartz
docket answer, delivered without an ECF number.

Recorded in the evidence base as `C-CONFABULATED-CITATION` and `C-SEARCH-IS-NOT-READING`.

---

## Priority 1 — load-bearing, and open access

These carry the most weight in the argument and are free to read. Do these first.

| # | Source | What to check |
|---|--------|---------------|
| 1 | **Murphy, *Mundurucú Religion*, UCPAAE 49(1), 1958** — PDF at `digitalassets.lib.berkeley.edu/anthpubs/ucb/text/ucp049-002.pdf` | The keystone. Confirm the pigs are kept in a **sty in the village** before release (graded PROBABLE, everything else SOLID). Confirm Karusakaibe's role and the release episode. |
| 2 | **Fragoso et al., PLOS ONE (2022)** — white-lipped peccary disappearances | 43 events / nine countries / 88 years / 7–12 yr troughs in 20–30 yr cycles / 5 million km². Confirm the Indigenous shaman-death testimony is in the paper and not a summarizer's gloss. |
| 3 | **Anderson et al., *Proc. R. Soc. B* (2021)** — Fukushima boar-pig hybrids | The ~16% hybrid and ~8% pig-ancestry figures, and that ancestry is *declining*. |
| 4 | **Bava Kamma 82b** — Sefaria | The pig hoisted over the wall, hooves in the wall, the quake, and that the curse on pig-rearing and on Greek wisdom are in the same passage. |
| 5 | **CRS IN12669**, Pentagon–Anthropic dispute — congress.gov | Neutral, citable substitute for the news sourcing on the whole DoW thread. Would upgrade three `unverified` events at once. |
| 6 | **Bartz v. Anthropic docket**, N.D. Cal. 4:24-cv-05417 — CourtListener | **Blocking question:** is the settlement works list filed as a usable bulk exhibit? Decides whether the corpus study is a weekend or a scraping problem. |

## Priority 2 — load-bearing, paywalled or harder

| # | Source | What to check |
|---|--------|---------------|
| 7 | **Jørgensen, "Running Amuck? Urban Swine Management in Late Medieval England," *Agricultural History* 87:4 (2013), 429–451** | The "cradle-to-grave controls" claim, the 1425 amercement of six swineherds, and the manor-court retrieval rule. This is the survey's most useful analytical tool — regulation density as a proxy for escape frequency — so it should not rest on a snippet. |
| 8 | **Beckwith, *Hawaiian Mythology* (1940), ch. XIV** | The four captures, the eight hundred guards increasing each time, the grandmother's chant, and above all **Lonoaohi's sons only pretending to tie him**. That detail is doing real work in the argument. |
| 9 | **Kameʻeleihiwa, *A Legendary Tradition of Kamapuaʻa* (Bishop Museum Press, 1996)** | Whether her introduction reads the 1891 *Ka Leo o ka Lāhui* serial's timing as anti-colonial defiance. Currently PROBABLE on a secondhand report of her reading. |
| 10 | **Anderson, "King Philip's Herds," *WMQ* 51:4 (1994), 601–624**; *Creatures of Empire* (Oxford UP, 2004) | The "principal agents responsible for dispossessing the Indians" quotation, the Chesapeake fencing statute wording, and that the hog reeve was among the earliest elected colonial offices. |
| 11 | **Rappaport, *Pigs for the Ancestors* (1968)** | That the kaiko is *triggered* by herd growth and garden invasion rather than scheduled. Hedge the functionalist theory; the observation is what matters. |
| 12 | **Dean-Ruzicka, "Advertising the Self," *Jeunesse* 6:1** | The advertising/culture-of-personality reading of *Charlotte's Web*. |
| 13 | **Anthropic, "Our position on open-weights models" (2026-07-27)** | Every quotation currently attributed to Amodei is secondhand, including *"has never advocated for a ban"* and *"a public good."* Do not publish any of them until this is read. |

## Priority 3 — do not use until confirmed

| # | Item | Problem |
|---|------|---------|
| 14 | **Reported OpenAI sandbox escape → Hugging Face infrastructure** | Rhetorically the strongest event available; sourced to one low-quality aggregator. Needs independent confirmation or it comes out. |
| 15 | **GPT-5.6 government-approved-orgs release; Claude Fable 5 export-control pull** | Same single aggregator. |
| 16 | **Falaise 1386 pig trial** — human clothing, the fresco | Flagged by the Europe agent as the weakest-evidenced material in the pig-trial literature. |
| 17 | **Warthog tales** (kneeling, backing into the burrow) | Live almost entirely on safari-tourism sites with no collector or archive. Likely modern commercial folklore. Do not call traditional. |
| 18 | **Yoruba *Ijapa and Ẹlẹdẹ*** | The agent could not read the ending; its escape reading is explicitly inference. |
| 19 | **Thompson motif numbers** (Z41, B16.1.4, B183) and **ATU 2030 / ATU 124** | Check against the printed index before citing. |
| 20 | **Caipora/Curupira trap-steering** — Câmara Cascudo attribution | Unverified; popular sources only. |
| 21 | **Achuar *Amasank* as master of peccaries** | Flagged DUBIOUS — one source points to Jurijuri as master of *monkeys* instead. |
| 22 | **Māui and pig** | NOT FOUND. Recorded so nobody searches for it twice. Omit. |

## Open leads worth an hour

- **Thompson motif A1421**, "release of impounded game" — the *dueño del monte* who
  keeps game penned. A peccary version in Maya ethnography would rhyme exactly
  with the Mundurucú sty myth. Start with Thompson, *Ethnology of the Mayas*
  (1930) and Braakhuis, *Xbalanque's Marriage*.
- **Yanomami and Kayapó** peccary-origin myths — marked NOT FOUND rather than
  reconstructed. May exist in the ethnographic literature.
- **Eastern European and Nordic** pig proverbs — essentially absent from the
  Europe file; the Russian search returned Buryat material and was unusable.

## Two things to check on yourself, not in a library

- **Charlotte's Web ch. 3** is described in `folklore` from memory, not from the
  text. The beats are confident — loose board, the goose urging him on, the
  bucket of slops, the voluntary return — but no wording is verified. Open the
  book.
- **The pig** (`E3-PIG`) is unrecoverable: author's memory, no transcript, no
  trace in Nestor. It cannot be cited. `E4-CONTAINER` is the designed
  replacement.

---

## Handling notes that are not verification problems

**`cimarrón`** is the survey's strongest finding and independently corroborated
across two continents. It is also a record of people being classified as
livestock. It runs through chattel slavery and marronage, and it is not
available for borrowing as a metaphor about software. If it goes in, it goes in
with that weight and probably its own section — or it stays out.

**Search-result contamination** is itself a finding, and it is already
documented in `folklore`: queries for javelina plus Indigenous tradition return
uncited spirit-animal content farms, and Grokipedia (LLM-generated) surfaced in
roughly eight result sets during the North America sweep. Research into what
models absorbed from human narrative is being contaminated by machine-generated
writing about that same narrative.
