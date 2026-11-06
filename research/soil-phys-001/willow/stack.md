# the soil-phys-001 stack

Three willow boxes over the [SOIL-PHYS-001 packet](../README.md): `boxes/whole`,
over the whole pile (the DispatchesFromReality repo as the markdown and text
add-ons mirror it, and the ledger's sources as text), `boxes/sources`, over the
sources alone, and `boxes/links`, over the raw repo for `xref`. A check of the
ledger runs against `boxes/sources`, so it can never find the ledger quoting
itself. Every step reads and writes nothing. [build.sh](build.sh) makes the
folder; run the stack from that folder, so the relative paths below resolve:

    python3 WILLOW/adapters/stdlib/stack/stack.py --box boxes/whole --stack stack.md

The stack reorders the pools tallest first; this is reading order, not run order.

## does the ledger quote its sources as they wrote
- quotes -- --box boxes/sources --in repo/research/soil-phys-001/DRAFT.md

## do the deciding quotes stand in their sources
# from CHECKS.md; the last is the one willow's study missed, past the 500
# characters the kernel reads of a line, and build.sh now breaks such lines
- misquote -- --box boxes/sources "we assume that the baryon and muon conservation laws are not absolute"
- misquote -- --box boxes/sources "the spin-one quanta of some of the gauge fields acquire mass"
- misquote -- --box boxes/sources "The ground state has huge degeneracy. A symmetry operation takes one ground state to another."
- misquote -- --box boxes/sources "it is not implausible that only a 3+1-dimensional spacetime can contain observers"
- misquote -- --box boxes/sources "I hold Space to be something merely relative, as Time is"
- misquote -- --box boxes/sources "those two States, the one such as it now is, the other supposed to be the quite contrary way, would not at all differ from one another"

## do the short claims have their parts in one place
# claim-check finds where to read, and never reads; it works on a claim of a
# few words, worded as the source words it (willow's demo/soil-phys-001)
- claim-check -- --box boxes/sources "Rule 110 is capable of universal computation"
- claim-check -- --box boxes/sources "gravity is an entropic force"
- claim-check -- --box boxes/sources "the metric is proportional to entanglement"

## does the packet hold together
- pair-drift -- --box {box} --full DRAFT.md.txt.txt --summary README.md.txt.txt
- xref -- --box boxes/links

## what the sources say, asked directly
- fair-merge -- --box boxes/sources "what happens to the ground state when a symmetry is broken"
- fair-merge -- --box boxes/sources "is space absolute or relative"
- first-mention -- --box boxes/sources "vacuum"

## what the boxes need from you
- box-health -- --box {box}
- box-health -- --box boxes/sources

## play
- pile-poetry -- --box boxes/sources --seed "the vault is sean's key" --lines 4
