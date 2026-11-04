# the fever chart stack

Two willow boxes over the [Fever Chart packet](../README.md): `boxes/whole`,
over the whole pile (the DispatchesFromReality repo, the Brinton text and your
notes), and `boxes/sources`, over the Brinton text alone. A check of the draft
runs against `boxes/sources`, so it can never find the draft quoting itself.
Every step reads and writes nothing. [build.sh](build.sh) makes the folder;
run the stack from that folder, so the relative paths below resolve:

    python3 WILLOW/adapters/stdlib/stack/stack.py --box boxes/whole --stack stack.md

The stack reorders the pools tallest first; this is reading order, not run order.

## does the draft quote Brinton as he wrote
- quotes -- --box boxes/sources --in pile/repo/research/fever-chart-in-bursts/DRAFT.md
- claim-check -- --box boxes/sources "the fall of Robespierre was a conspiracy among Jacobin deputies involved in corruption"
- claim-check -- --box boxes/sources "suffering is not in itself a spur to effective revolt"
- claim-check -- --box boxes/sources "another and conflicting chain of institutions demanding obedience is dual sovereignty"
- claim-check -- --box boxes/sources "what is usually called realists, adapted to a common-sense world"

## does every packet hold together
- pair-drift -- --box {box}
- xref -- --box {box}

## what is coming up
- coming-up -- --box {box} --days 150

## what Brinton says, asked directly
- fair-merge -- --box {box} "what makes Thermidor"
- fair-merge -- --box {box} "why do the moderates fail"
- fair-merge -- --box {box} "what are the preliminary signs of revolution"
- first-mention -- --box {box} "dual sovereignty"

## who says what
# said reads quotes in your own notes; put them in pile/notes
- said -- --box {box}

## the four tests, as wagers
- forecasts -- score --box {box}

## what the boxes need from you
- digest -- --box {box}
- box-health -- --box {box}
- box-health -- --box boxes/sources

## play
- pile-poetry -- --box boxes/sources --seed "the vault is sean's key" --lines 4
