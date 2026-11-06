# Before It Was in the Minutes

**Sean Campbell** · What the Federal Reserve's own record says, 2023 to 2026 · November 2026

**Tags:** `federal-reserve`, `fomc`, `primary-sources`, `provenance`, `extractive-reading`, `willow`, `exchange-rates`, `market-history`, `systems-thinking`

*A question reaches the podium before the minutes write it down, and the words change before the policy does. Both can be read off the record itself.*

For the broader research map, see [Research Portfolio](../README.md). For the provenance states used here, see [Nobody Counts the Ad Breaks](../childrens-software-interruption/README.md). For the same willow method applied to a 1938 text, see [The Fever Chart in Bursts](../fever-chart-in-bursts/README.md).

---

## Current versions

| Version | Form | Status | Purpose |
|---------|------|--------|---------|
| **v1** | Working draft | [DRAFT.md](DRAFT.md) | Full prose: the rate path, tariffs at the podium before the minutes, the Committee's vocabulary dated, the statement halved at the change of chair, the dollar against its rule of thumb, recoveries after crashes, retirement language in 55 annual reports, and where the reading fails |
| **Packet** | Public summary | This file | Scope, method, evidence, claim boundaries |
| **Stack** | willow stack | [willow/README.md](willow/README.md) | How to rebuild the pile and rerun every reading |

---

## Core question

What does the Federal Reserve's own record, read line by line with every claim cited, say about 2023 to 2026 that the coverage of it blurs?

---

## Thesis

1. **The question comes first.** Tariffs reached the chair's press conference on 7 November 2024, when he declined to discuss the new Administration's policies. The first meeting whose minutes record them is January 2025.
2. **The words change before the policy does.** Artificial intelligence, stablecoins, reserve management purchases and the AI infrastructure "buildout" enter the minutes on dateable meetings; restrictiveness and disinflation leave. Disinflation is last used in April 2026; in September the Committee raised the target range.
3. **The form changes with the chair.** From Chairman Warsh's first meeting in June 2026, the policy text of each statement is roughly half as long.
4. **Rules of thumb have dated exceptions.** In 2025 the dollar fell while American rates rose against foreign rates, which the Fed's own staff noted as unusual. Recoveries after 1973 and 2000 took about fourteen years in real terms.
5. **The reading has limits, and they are findings.** A line cut at its 500th character dated the first tariff mention ten weeks late, silently. Those failures are reported beside the results.

---

## Method

- **One pile, fetched once.** 944 sources fetched on 5 November 2026 and pinned by SHA-256: FOMC statements, minutes, projections and press conference transcripts (2023 to 2026); FRED series; Treasury yield curves; ECB rates; IMF and World Bank country data; the Fama-French library; SEC EDGAR filing indexes for the S&P 500 and the latest 10-K of 55 companies.
- **Read by willow, not summarised.** Every finding is a passage the kernel served with its file and line, or a count read directly from the files. The chain that dates the vocabulary is willow's `dialect` (words used far more than the world uses them) into `first-mention` (each one's first appearance).
- **Lines broken at sentences** before reading, every word kept, because the kernel reads only the first 500 characters of a line.
- **Tag every claim by provenance.** `measured` (read at first hand in the publisher's own file), `fitted` (from a republished copy or corroborated by a stated rule), `assumed` (single source or none).

---

## Evidence base

| Claim | Figure | Source named in the draft | Provenance |
|-------|--------|---------------------------|------------|
| Rate decisions, February 2023 to October 2026 | 31 meetings: 2023 four raises, four holds; 2024 five holds, three cuts; 2025 five holds, three cuts; 2026 five holds, one raise (16 September, to 3-3/4 to 4 percent), one hold | FOMC statements | `measured` |
| Votes against the 28 October 2026 hold | Lisa D. Cook and Beth M. Hammack, preferring a raise | FOMC statement, 28 October 2026 | `measured` |
| First tariff question at a press conference | 7 November 2024, Courtenay Brown of Axios; the chair: "not referring to, to the new Administration's policies at all, nor will I today" | FOMC press conference transcript | `measured` |
| Tariffs at the December 2024 press conference | Eight mentions | FOMC press conference transcript | `measured` |
| First meeting whose minutes record tariffs | January 2025; 166 mentions in 14 sets of minutes through September 2026; 231 in the press conference transcripts | FOMC minutes and transcripts | `measured` |
| First appearance in the minutes | Artificial intelligence May 2024; stablecoins July 2025; reserve management purchases October 2025; buildout January 2026 (25 mentions in four sets of minutes) | FOMC minutes | `measured` |
| Last appearance in the minutes | Restrictiveness December 2025; disinflation April 2026 (19 sets of minutes); disinflation at press conferences, March 2026 | FOMC minutes and transcripts | `measured` |
| Change of chair at the podium | Powell's last press conference 29 April 2026; Chairman Warsh from June 2026; "As before, the policy statement conveys just the facts" (29 July 2026) | FOMC press conference transcripts | `measured` |
| Policy text of each rate statement | 302 to 375 words in 2025 and early 2026; 141 to 183 words from June 2026 | FOMC statements, counted from the release time to the implementation note | `measured` |
| Euro in dollars | 1.0261 (2 January 2025), 1.1770 (30 June 2025), 1.1163 (30 October 2026) | FRED, the Fed's H.10 series | `measured` |
| Yen per dollar | 157.65, 144.17, 157.47 on the same dates | FRED, the Fed's H.10 series | `measured` |
| Broad dollar index | Fell from 129.46 to 119.41 in the first half of 2025; 121.67 at the end of October 2026 | FRED | `measured` |
| The dollar against its rule of thumb | Depreciated "even though U.S. interest rates had risen more than foreign interest rates and prices of risky assets had declined" | FOMC minutes, May 2025 | `measured` |
| Rate checks on dollar-yen | The dollar fell markedly after reports of them | FOMC minutes, January 2026 | `measured` |
| Recoveries after crashes, price and real | 1929 300 and 350 months; 1973 90 and 175; 2000 81 and 171; 2008 65 and 73; 2020 7 and 7; 2022 24 months in price | Shiller's monthly S&P series, as republished by datahub.io | `fitted` |
| Retirement language in 55 latest 10-Ks | Pension wording leads in 38, 401(k) wording in 14, retiree health in 1, none in 6 files | SEC EDGAR, each company's 10-K | `measured` |

---

## Claim boundaries

- A reading of one public record. Not advice, not a forecast, and not a judgement on any decision.
- First and last appearances are within this pile, which begins in 2023. Minutes are dated by the meeting they record, not their release about three weeks later.
- The retirement sort says what each report talks about most, not what each company offers.
- The recovery table uses monthly averages of prices only; daily lows were deeper, and reinvested dividends would shorten every recovery.
- The Shiller series is read from a republished copy, so it is `fitted`, not `measured`.

---

## What comes next

- Read the Shiller series from its own publication and promote the table to `measured`, or say where the copy differs.
- Run the same vocabulary chain on the 10-Ks' risk factors year over year, once the pile holds more than each company's latest report.
- Extend the pile when the FOMC's minutes of 28 October 2026 are released.
