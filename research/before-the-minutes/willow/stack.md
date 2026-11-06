# the before-the-minutes stack

Run from the folder that holds `boxes/` and this repo cloned as `repo/`, with
WILLOW the willow checkout:

    python3 WILLOW/adapters/stdlib/stack/stack.py --box boxes/fed --stack stack.md

The stack reorders the pools tallest first; this is reading order, not run order.

## does the draft quote the Fed as it wrote
- quotes -- --box boxes/fed --in repo/research/before-the-minutes/DRAFT.md
- claim-check -- --box boxes/fed "decided to raise the target range for the federal funds rate by 1/4 percentage point to 3-3/4 to 4 percent"
- claim-check -- --box boxes/fed "Voting against Cook Hammack preferred to raise the target range"

## does the draft say what the packet says
- pair-drift -- --box boxes/packet --full DRAFT.md --summary README.md

## when the Committee's words came and went
- first-mention -- --box {box} "tariffs"
- first-mention -- --box {box} "artificial intelligence"
- first-mention -- --box {box} "stablecoins"
- first-mention -- --box {box} "reserve management purchases"
- first-mention -- --box {box} "buildout"
- first-mention -- --box {box} "restrictiveness"
- first-mention -- --box {box} "disinflation"

## the Committee's own dialect
- dialect -- --box {box} --top 25

## the retirement language of 55 companies
- sort -- --box boxes/filings --categories repo/research/before-the-minutes/willow/retirement.txt
