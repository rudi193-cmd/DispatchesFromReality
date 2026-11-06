# the soil-phys-001 stack

Three willow boxes over the [SOIL-PHYS-001 packet](../README.md): `boxes/whole`,
over the whole pile (the DispatchesFromReality repo as the markdown and text
add-ons mirror it, and the ledger's sources as text), `boxes/sources`, over the
sources alone, and `boxes/links`, over the raw repo. A check of the ledger runs
against `boxes/sources`, so it can never find the ledger quoting itself.
[build.sh](build.sh) makes the folder; run the stack from that folder, so the
relative paths below resolve:

    python3 WILLOW/adapters/stdlib/stack/stack.py --box boxes/whole --stack stack.md

Most steps only read. The pools marked **on the record** append rows to a
box's record through the kernel (a question asked, a hash taken, a prediction
made); the pool marked **made** writes files into `out/`, nothing else. The
stack reorders the pools tallest first; this is reading order, not run order.

## the ledger against its sources
- quotes -- --box boxes/sources --in repo/research/soil-phys-001/DRAFT.md
- thesis -- --box boxes/sources repo/research/soil-phys-001/DRAFT.md --top 1
- misquote -- --box boxes/sources "we assume that the baryon and muon conservation laws are not absolute"
- misquote -- --box boxes/sources "the spin-one quanta of some of the gauge fields acquire mass"
- misquote -- --box boxes/sources "The ground state has huge degeneracy. A symmetry operation takes one ground state to another."
- misquote -- --box boxes/sources "it is not implausible that only a 3+1-dimensional spacetime can contain observers"
- misquote -- --box boxes/sources "I hold Space to be something merely relative, as Time is"
- misquote -- --box boxes/sources "those two States, the one such as it now is, the other supposed to be the quite contrary way, would not at all differ from one another"
- misquote -- --box boxes/sources "Absolute Space, in its own nature, without relation to anything external, remains always similar and immovable"
- misquote -- --box boxes/sources "Nature was thought to possess the power of preventing the formation of a vacuum"
- quote-check -- --box boxes/sources "the two regions of spacetime pull apart and pinch off from each other"
- quote-check -- --box boxes/sources "The phase of the field is not determined"
# claim-check finds where to read, and never reads; it works on a claim of a
# few words, worded as the source words it (willow's demo/soil-phys-001)
- claim-check -- --box boxes/sources "Rule 110 is capable of universal computation"
- claim-check -- --box boxes/sources "gravity is an entropic force"
- claim-check -- --box boxes/sources "the metric is proportional to entanglement"
- why-not -- --box boxes/sources "Is the spacetime metric proportional to entanglement?"
- why-not -- --box boxes/sources "Where is deletion an appended tombstone?"

## the catalog and the nuggets
# build.sh mirrors the packet's Almanac catalog and Jeles seed into the pile:
# each source's entry, and each SOURCE line as a question and its answer
- fair-merge -- --box {box} "what does Sakharov show"
- ripgrep -- --box {box} "not yet probed"

## the sources, asked directly
- fair-merge -- --box boxes/sources "what happens to the ground state when a symmetry is broken"
- fair-merge -- --box boxes/sources "is space absolute or relative"
- all -- --box boxes/sources --top 3 "spontaneous symmetry breaking"
- launcher -- --box boxes/sources --format lines --limit 3 "absolute space and absolute motion"
- first-mention -- --box boxes/sources "vacuum"
- ripgrep -- --box boxes/sources "Fundamentalhypothese"
# "zero point" is in Casimir, a scan no reader turns into words; Nernst has it in German
- ripgrep -- --box boxes/sources --ignore-case "Nullpunkt"
- accents -- --box boxes/sources "Memoire sur l iteration des fonctions rationnelles"
- stems -- --box boxes/sources --lang german "Feldgleichung der Gravitation"
- typos -- --box boxes/sources "the Goldstone theorm"
- sort -- --box boxes/sources --categories repo/research/soil-phys-001/willow/sections.txt
- log-kit -- --box {box} --words entanglement,symmetry,vacuum --by year
- profile -- --box boxes/sources --top 3 "what happens to the ground state when a symmetry is broken"

## in their own languages, on the record
- words-de -- bite --box boxes/sources "Was sind die Feldgleichungen der Gravitation?"
- words-fr -- bite --box boxes/sources "Qu'est-ce que l'itération des fonctions rationnelles ?"
- plain -- bite --box boxes/sources "what is the zero point energy of an oscillator"
- readings -- bite --box boxes/sources "baryon density"

## the sources kept, on the record
# fixity hashes every source file now and says, next time, which changed
# without an edit; merkle's root seals the record's rows so far
- fixity -- --box boxes/sources
- changed -- --box boxes/sources
- merkle -- root --box boxes/sources

## predictions, on the record
# predict says, before a question's bite, what the box's record says it will
# come to; score grades them once the bites are taken. Ask it outside the
# stack (python3 WILLOW/adapters/stdlib/predict/predict.py ask --box
# boxes/sources "QUESTION"): stack adds --json to a report add-on's step, and
# predict's ask takes none (willow bug #285)
- predict -- score --box boxes/sources

## does the packet hold together
- pair-drift -- --box {box} --full DRAFT.md.txt.txt --summary README.md.txt.txt
- xref -- --box boxes/links
- agents-md-check -- --box boxes/links
- a11y-check -- --box boxes/links
- instruction-files -- --box boxes/links
- reading-level -- --box {box}
- duplicates -- --box {box}

## the repo, read across
- coming-up -- --box {box} --days 30
- digest -- --box {box}
- across -- --box boxes/whole --box boxes/sources digest
- fuzzy-dates -- --box {box}
- amounts -- --box {box}
- contradictions -- --box {box}
- people -- --box {box}
- ids -- --box {box}
- syllabus -- --box {box}
- todo -- --box {box}
- minutes -- --box {box}
- gaps -- --box {box}

## nothing private, nothing risky
- secrets-audit -- --box {box}
- pii-audit -- --box {box}
- risky-code -- --box {box}

## the repo's code, if it ever has dependencies
# a writing repo: these say there's nothing to check, and stand guard for the day there is
- advisories -- --box boxes/links
- outdated -- --box boxes/links
- pins -- --box boxes/links
- typosquat -- --box boxes/links
- install-scripts -- --box boxes/links
- package-contents -- --box boxes/links

## the record
- history -- --box {box}
- again -- --box {box}
- sent-log -- --box {box}
- stale -- --box {box}
- weakest-link -- --box {box}
- assistant-scores -- --box {box}
- on-this-day -- --box {box}
- export -- --box {box} --log
- box-health -- --box {box}
- box-health -- --box boxes/sources

## made, in out/
- prov -- --box boxes/sources --to out/prov.json
- in-toto -- --box boxes/sources --to out/in-toto.json
- folder-card -- --box boxes/sources --to out/card.md
- timeline -- --box boxes/sources --to out/timeline.md "symmetry vacuum"
- badge -- --box boxes/sources --to out/badge.svg
- print -- --box boxes/sources --to out/ground-state.html "what happens to the ground state when a symmetry is broken"
- calendar-out -- --box {box} --to out/calendar.ics --days 30
- cloudevents -- --box boxes/sources --to out/events.jsonl

## play
- pile-poetry -- --box boxes/sources --seed "the vault is sean's key" --lines 4
- surprise -- --box boxes/sources
