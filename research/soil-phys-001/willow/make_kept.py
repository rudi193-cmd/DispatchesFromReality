"""KEPT.md from the catalog and keep/: what each kept file is."""
import sys, json, hashlib, pathlib, re
L = pathlib.Path(__file__).resolve().parent
cat = json.load(open(L / "stack/catalog/catalog.json"))["entries"]
FULL, PAGE = "full text", "landing page"
what = {
 "codata-2022": (PAGE, "NIST's constants index; the CODATA values are linked from it"),
 "dirac-1937": (PAGE, "Nature's article page: abstract and preview; the paper is paywalled"),
 "feigenbaum-1978": (PAGE, "Springer's article page: abstract and preview; paywalled. No open copy found"),
 "goldstone-1961": (PAGE, "Springer's article page: abstract and preview; paywalled. The preprint is goldstone-1961-preprint"),
 "klein-1926": (PAGE, "Springer's article page; the open copy is klein-1926-open"),
 "weyl-1929": (PAGE, "Springer's article page: abstract and preview; paywalled. No open copy found"),
 "sakharov-1967": (PAGE, "Physics-Uspekhi's page for the reprint; the open copy is sakharov-1967-open"),
 "sakharov-1967-open": (FULL, "the 1991 Physics-Uspekhi reprint, English, 2 pages, citing JETP Lett. 5 (1967) 24; Physics-Uspekhi's own archive"),
 "klein-1926-open": (FULL, "the 1926 paper as scanned pages (3-14) in Blum and Rickles' sourcebook, Edition Open Sources, CC BY-NC-SA 3.0 DE"),
 "shannon-1948": (FULL, "the 1948 reprint with corrections, both parts, 55 pages; Harvard mathematics"),
 "solomonoff-1964": (FULL, "part I, the author's retypeset copy citing Information and Control 7 (1964) 1, 20 pages; the publisher's address gave a 2.6 KB redirect, set aside"),
 "nernst-1906": (FULL, "scan of the Göttingen Nachrichten, 40 pages, noisy OCR; a Notre Dame course page"),
 "mach-1883": (FULL, "the 1893 English translation (of the 1888 second edition), the Internet Archive's full-text page, noisy OCR"),
 "leibniz-clarke-1717": ("part", "Leibniz's first paper, TEI transcription of the 1717 edition; the Newton Project, CC BY-NC-ND. His third is leibniz-clarke-1717-third"),
 "einstein-1915": (FULL, "Wikisource's German transcription; the scan is in the 1915 Sitzungsberichte on the Internet Archive"),
 "kaluza-1921": (FULL, "an English translation (arXiv:1803.08616), 7 pages; not the German original"),
 "casimir-1948": (FULL, "the KNAW's reprint in 'Gems from a century of science' (2000), scanned, 4 pages; TU Munich physics"),
 "julia-1918": (FULL, "scan of the original, 200 pages; Numdam"),
 "fatou-1919": (FULL, "scan of the original, first memoir, 112 pages; Numdam"),
 "cook-2004": (FULL, "the journal article, 40 pages, hosted by Wolfram for Complex Systems"),
 "willow-kernel": (FULL, "full source, pinned to a commit"),
 "englert-brout-1964": (FULL, "the PRL pages, 3 (the paper with the end of the one before), APS free to read, downloaded in a browser"),
 "higgs-1964": (FULL, "the PRL pages, 2, APS free to read, downloaded in a browser"),
 "nambu-2008": (FULL, "Nambu's Nobel lecture, 7 pages, nobelprize.org (the same bytes as the copy you sent)"),
 "goldstone-1961-preprint": (FULL, "Goldstone's 1960 CERN preprint (CERN-TH-118), scanned, 16 pages; downloaded in a browser"),
 "leibniz-clarke-1717-third": (FULL, "Leibniz's third paper, TEI transcription; the Newton Project, CC BY-NC-ND"),
 "newton-1687": (FULL, "the Definitions and Scholium in Motte's 1729 translation, Wikisource's transcription (the long s kept in markup)"),
 "ghk-1964": (FULL, "the PRL pages, 3 (the paper with the end of the one before), APS free to read, downloaded in a browser"),
}
NONE = {
 "spencer-brown-1969": "a book under copyright: no lawful open copy",
 "mandelbrot-1982": "a book under copyright: no lawful open copy",
 "vonneumann-1923": "the Szeged archive (acta.fyx.hu) doesn't resolve from this environment",
 "wolfram-1983": "APS blocks scripts (403); Wolfram's own publications site doesn't resolve from this environment",
 "weyl-1918": "no open copy found",
 "ehrenfest-1917": "in the KNAW Digital Library, but its record number wasn't found",
 "penrose-1965": "APS: a sign-in for a browser, 403 for scripts; copies found were re-uploads, excluded",
 "wilson-1971": "APS: a sign-in for a browser, 403 for scripts",
 "nambu-1960": "APS: a sign-in for a browser, 403 for scripts",
 "anderson-1963": "APS: a sign-in for a browser, 403 for scripts",
 "planck-1901": "Wiley: a sign-in for a browser, 403 for scripts; a Zenodo upload exists, uploader unknown, not used",
}
rows, full, parts, page, none = [], set(), set(), 0, 0
for e in sorted(cat, key=lambda e: e["id"]):
    i = e["id"]
    files = sorted((L / "keep").glob(i + ".*")) + ([L / "keep" / i] if (L / "keep" / i).exists() else [])
    if files:
        f = files[0]
        h = hashlib.sha256(f.read_bytes()).hexdigest()
        k, w = what.get(i, (FULL, "full text (arXiv PDF)") if f.suffix == ".pdf" else (PAGE, "page"))
        base = re.sub(r"-(open|preprint|third)$", "", i)
        if k == FULL:
            full.add(base)
        elif k == "part":
            parts.add(base)
        rows.append(f"| {i} | {k} | `{f.name}` | {f.stat().st_size:,} | `{h[:16]}…` | {w} |")
    else:
        none += 1
        rows.append(f"| {i} | none | | | | {NONE.get(i, 'no address yet')} |")
part = len(parts - full)
page = sum(1 for r in rows if "| landing page |" in r and r.split(" | ")[0].strip("| ") not in {x for x in full})
works = len({re.sub(r"-(open|preprint|third)$", "", e["id"]) for e in cat})
doc = ["# SOIL-PHYS-001: what is kept", "",
       "Probed and kept 2026-11-06 with Willow's almanac-keep (each file's SHA-256 in full in "
       "`keep/.snapshots.jsonl`) or, where a script is refused, downloaded in a browser by the person "
       "running the ledger (`keep/.provided.jsonl`). Every probe is in `probes.jsonl`. An `-open` entry "
       "is a companion: the publisher's page answers with an abstract, and the open copy is kept beside it.", "",
       f"Of the ledger's {works} works: **{len(full)} held in full** (by the work itself, a reprint, a "
       f"transcription or a translation, each said), {part} in part, {page} only as a landing page, and {none} not held.", "",
       "| Source | Held | File | Bytes | SHA-256 | What it is |", "|---|---|---|---|---|---|"] + rows + ["",
       "## Blocked by this environment, not by the holder", "",
       "- `acta.fyx.hu` (von Neumann, 1923) and `publications.stephenwolfram.com` (Wolfram, 1983) don't resolve here.",
       "- `cds.cern.ch` (Goldstone's preprint) serves a bot check; `jetpletters.ru` (Sakharov's original) resets the connection.",
       "", "Allowed, these could be tried again."]
(L.parent / "KEPT.md").write_text("\n".join(doc) + "\n", encoding="utf-8")
print(doc[4])
