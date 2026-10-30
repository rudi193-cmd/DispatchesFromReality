# Fact-check: The Illusion of Sovereign AI (v3)

*Checked 2026-10-29 · seven named-source claims in [DRAFT.md](DRAFT.md)*

Each claim below was checked against an opened source. The verdicts use this
repo's provenance words: **measured** means read at first hand from the primary
source; **fitted** means corroborated by a secondary report that names the
primary one; **assumed** means not checked.

All seven held. Four needed their wording brought back to what the source says,
and DRAFT.md was corrected in the same change as this note. The same claims in
[Nobody Adds It Up](../../essays/nobody-adds-it-up/README.md) and
[Somebody Has to Sit Down With You](../../essays/somebody-has-to-sit-down-with-you/README.md)
were corrected with it.

## What held, and what changed

| Claim | What the source says | Verdict | Wording |
|---|---|---|---|
| Verizon DBIR 2025: third-party involvement in breaches went from 15% to 30% | Verizon's own release (2025-04-23): third-party involvement "doubled to 30%" | measured | Dropped "the largest single-year increase they've measured", which is not on that page |
| Stargate: announced 2025-01-21 at the White House, up to $500 billion over four years, $100 billion right away | Matches. Some press names three founders (OpenAI, SoftBank, Oracle); OpenAI's own announcement adds MGX as an initial equity funder, as the essay does | fitted | Unchanged |
| Change Healthcare: 192.7 million | Change Healthcare's letter to the New Hampshire Attorney General (2025-07-31), as reported by Becker's: about 192.7 million *individuals* | fitted | "patient records" → "the records of 192.7 million people" |
| Sixteen billion credentials in thirty datasets | Cybernews (2025-06-19): 16 billion records in 30 datasets; the source's own author reads them as mostly old credentials gathered over years, not one new breach | fitted | "circulating" → "sit in", with "mostly old leaks" added |
| Meta took about 49% of Scale AI for $14.3 billion (June 2025) | Matches; Scale announced it on 2025-06-12 at a $29 billion valuation | fitted | Unchanged. The essay's Scale revenue figures were not in this source |
| LeCun on Llama 4's benchmark results | Financial Times interview, reported 2026-01-02: the results were "fudged a little bit", with different models used for different benchmarks | fitted | "fudged" → "fudged a little bit" |
| DeepSeek V3 trained for about $5 to $6 million | The V3 report: 2,788,000 H800 GPU hours at an estimated $5,576,000 | fitted | Unchanged. The figure is the final training run only, not research, failed runs or staff |

## Not checked

These stay **assumed** until someone opens their sources:

- HUMAIN's backing of about $100 billion (the essay already calls it press, not audited).
- Epoch's estimate of the largest 2024 training runs near $390 million.
- LMArena's top six within about 100 Elo, and MMLU scores of 93 to 97.
- Scale AI's 2024 revenue of about $870 million.

## Sources

Kept by address, with a SHA-256 where a copy was saved on 2026-10-30. The saved
copies are third-party pages and are not in this repo.

| Source | Address | SHA-256 of the saved copy |
|---|---|---|
| Verizon, 2025 DBIR release | https://www.verizon.com/about/news/2025-data-breach-investigations-report | `4e94d06a8457d47a7ef14891ec55e70f68e95adc2461837ee9ed7f6d90840606` |
| Simon Willison on the DeepSeek V3 report | https://simonwillison.net/2024/Dec/26/deepseek-v3/ | `c3306dae45c585c54d22f2fdf1c70c4bd7963dc4d5e39a3408fd35964d41d04b` |
| The Washington Times on Stargate | https://m.washingtontimes.com/news/2025/jan/21/donald-trump-announces-500-billion-ai-investment-n/ | not saved |
| Becker's Hospital Review on Change Healthcare | https://www.beckershospitalreview.com/healthcare-information-technology/cybersecurity/change-healthcare-data-breach-toll-reaches-192-7-million | not saved (answered 403) |
| Security Affairs on the 16 billion credentials | https://securityaffairs.com/?p=179149 | not saved |
| The Star on Meta and Scale AI | https://www.thestar.com.my/tech/tech-news/2025/06/13/meta-finalizes-investment-in-scale-ai-valuing-startup-at-29-billion | not saved |
| Slashdot on LeCun and Llama 4 | https://tech.slashdot.org/story/26/01/02/1449227/ | not saved |
