"""SOIL-PHYS-001 rev 2 as an Almanac catalog (its sources) and a Jeles seed
(its SOURCE lines). Addresses only where certain.

    python make_stack.py OUT [--probe]

--probe asks each address once, as the Almanac's link checker does, and
writes what it answered into the entry's `observed`: when, whether it was
reachable, and its HTTP status. An address that answers 200 is marked
`live` (by this probe, said in `status_source`), so almanac-keep may keep
it; any other answer leaves the entry `cited`, with the answer said."""
import datetime, json, sys, urllib.request, urllib.error
from pathlib import Path

OUT = Path(sys.argv[1])
D = "https://doi.org/"
A = "https://arxiv.org/pdf/"  # the full text: a line is checked against the paper, not its abstract
# id, title, type, publisher/venue, url or None, ledger line(s), what it shows, topics
S = [
 ("vonneumann-1923", "Zur Einführung der transfiniten Zahlen", "paper", "Acta Sci. Math. (Szeged) 1 (1923) 199", None, "0003, 05.02", "0 is the empty set and 1 = {0}: each ordinal is the set of those before it.", ["set-theory"]),
 ("zermelo-1908", "Untersuchungen über die Grundlagen der Mengenlehre I", "paper", "Math. Ann. 65 (1908) 261", D+"10.1007/BF01449999", "0003, 05.02", "Axiom II: there is an improper set, the null set 0, with no elements; Axiom VII: a set holding 0 and, with each a, the set {a}.", ["set-theory"]),
 ("frege-1884", "Die Grundlagen der Arithmetik", "book", "Koebner, Breslau, 1884", None, "05.02", "0 is the number of the concept 'not identical with itself', under which nothing falls; 1 is the number of the concept 'identical with 0'.", ["logic", "set-theory"]),
 ("dedekind-1888", "Was sind und was sollen die Zahlen?", "book", "Vieweg, Braunschweig, 1888", None, "05.02", "The natural numbers as a simply infinite system, its base element written 1.", ["set-theory"]),
 ("spencer-brown-1969", "Laws of Form", "book", "Allen & Unwin, 1969", None, "0004, 05.02", "A calculus built from one primitive act, drawing a distinction.", ["logic"]),
 ("codata-2022", "CODATA recommended values of the fundamental physical constants", "dataset", "NIST", "https://physics.nist.gov/cuu/Constants/", "01.01", "c, h, e and k_B are exact in the 2019 SI; G is measured; alpha is a pure number.", ["constants"]),
 ("planck-1901", "Über das Gesetz der Energieverteilung im Normalspectrum", "paper", "Ann. Phys. 4 (1901) 553", D+"10.1002/andp.19013090310", "01.01", "Planck's radiation law, after his December 1900 report to the German Physical Society.", ["constants", "quantum"]),
 ("dirac-1937", "The Cosmological Constants", "paper", "Nature 139 (1937) 323", D+"10.1038/139323a0", "01.01", "The large-number coincidences between atomic and cosmic ratios.", ["constants", "cosmology"]),
 ("einstein-1915", "Die Feldgleichungen der Gravitation", "paper", "Sitzungsber. Preuss. Akad. Wiss. (1915) 844", None, "01.02, 02.02", "General relativity's field equations.", ["gravity"]),
 ("ehrenfest-1917", "In what way does it become manifest in the fundamental laws of physics that space has three dimensions?", "paper", "Proc. KNAW Amsterdam 20 (1917) 200", None, "01.02", "Stable planetary orbits and atoms occur only in three space dimensions.", ["dimension"]),
 ("tegmark-1997", "On the dimensionality of spacetime", "paper", "Class. Quantum Grav. 14 (1997) L69", A+"gr-qc/9702052", "01.02", "Stability and predictability arguments single out 3 + 1 dimensions.", ["dimension"]),
 ("kaluza-1921", "Zum Unitätsproblem der Physik", "paper", "Sitzungsber. Preuss. Akad. Wiss. (1921) 966", None, "01.02", "A fifth dimension unifying gravity and electromagnetism.", ["dimension"]),
 ("klein-1926", "Quantentheorie und fünfdimensionale Relativitätstheorie", "paper", "Z. Phys. 37 (1926) 895", D+"10.1007/BF01397481", "01.02", "The fifth dimension compact and small.", ["dimension"]),
 ("planck-2018-parameters", "Planck 2018 results. VI. Cosmological parameters", "paper", "Astron. Astrophys. 641 (2020) A6", A+"1807.06209", "02.01", "The measured baryon density, giving a baryon-to-photon ratio near 6 x 10^-10.", ["cosmology", "asymmetry"]),
 ("sakharov-1967", "Violation of CP invariance, C asymmetry, and baryon asymmetry of the universe", "paper", "JETP Lett. 5 (1967) 24; reprinted Sov. Phys. Usp. 34 (1991) 392", D+"10.1070/PU1991v034n05ABEH002497", "02.01", "A baryon asymmetry can arise if baryon number is violated, C and CP are violated, and equilibrium is departed from.", ["asymmetry"]),
 ("leibniz-clarke-1717", "A Collection of Papers which passed between the late Learned Mr. Leibnitz and Dr. Clarke", "book", "London, 1717 (letters of 1715-16)", None, "02.02", "Leibniz: space is relations among things; shifting everything changes nothing real.", ["relationalism"]),
 ("newton-1687", "Philosophiae Naturalis Principia Mathematica: the Scholium to the Definitions (Motte's translation, 1729)", "book", "London, 1687; Motte's English translation, 1729", None, "02.02", "Absolute space and time, against which relative space is a movable measure: the view Leibniz and Mach argue against.", ["relationalism"]),
 ("mach-1883", "Die Mechanik in ihrer Entwickelung", "book", "Brockhaus, Leipzig, 1883", None, "02.02", "Inertia understood relative to the distant masses.", ["relationalism"]),
 ("weyl-1918", "Gravitation und Elektrizität", "paper", "Sitzungsber. Preuss. Akad. Wiss. (1918) 465", None, "02.02", "Gauge invariance, first as a freedom of local scale.", ["gauge"]),
 ("weyl-1929", "Elektron und Gravitation", "paper", "Z. Phys. 56 (1929) 330", D+"10.1007/BF01339504", "02.02", "Gauge invariance as a freedom of local phase.", ["gauge"]),
 ("nambu-1960", "Quasi-particles and gauge invariance in the theory of superconductivity", "paper", "Phys. Rev. 117 (1960) 648", D+"10.1103/PhysRev.117.648", "02.03", "Spontaneous symmetry breaking in superconductivity.", ["symmetry-breaking"]),
 ("nambu-2008", "Spontaneous symmetry breaking in particle physics: a case of cross fertilization (Nobel Lecture)", "lecture", "Nobel Lecture, 8 December 2008 (read by G. Jona-Lasinio)", "https://www.nobelprize.org/uploads/2018/06/nambu_lecture.pdf", "02.03", "Nambu's own account: in spontaneous symmetry breaking the ground state has huge degeneracy, a symmetry operation takes one ground state to another, and only one of them, with its excited states, is realized.", ["symmetry-breaking"]),
 ("goldstone-1961", "Field theories with superconductor solutions", "paper", "Nuovo Cimento 19 (1961) 154", D+"10.1007/BF02812722", "02.03", "A broken continuous symmetry brings a massless boson.", ["symmetry-breaking"]),
 ("anderson-1963", "Plasmons, gauge invariance, and mass", "paper", "Phys. Rev. 130 (1963) 439", D+"10.1103/PhysRev.130.439", "02.03", "In a gauge theory the would-be massless mode gives the gauge field mass.", ["symmetry-breaking"]),
 ("englert-brout-1964", "Broken symmetry and the mass of gauge vector mesons", "paper", "Phys. Rev. Lett. 13 (1964) 321", D+"10.1103/PhysRevLett.13.321", "02.03", "Gauge bosons acquire mass through a broken symmetry.", ["symmetry-breaking"]),
 ("higgs-1964", "Broken symmetries and the masses of gauge bosons", "paper", "Phys. Rev. Lett. 13 (1964) 508", D+"10.1103/PhysRevLett.13.508", "02.03", "The same mechanism, in which the Goldstone theorem fails for gauge fields, and its prediction of incomplete multiplets of scalar and vector bosons.", ["symmetry-breaking"]),
 ("ghk-1964", "Global conservation laws and massless particles", "paper", "Phys. Rev. Lett. 13 (1964) 585", D+"10.1103/PhysRevLett.13.585", "02.03", "The third 1964 account of the mechanism.", ["symmetry-breaking"]),
 ("julia-1918", "Mémoire sur l'itération des fonctions rationnelles", "paper", "J. Math. Pures Appl. 8 (1918) 47", None, "03.01", "The iteration of rational maps of the complex plane.", ["fractals"]),
 ("fatou-1919", "Sur les équations fonctionnelles", "paper", "Bull. Soc. Math. France 47-48 (1919-20)", None, "03.01", "The same iteration, independently.", ["fractals"]),
 ("mandelbrot-1982", "The Fractal Geometry of Nature", "book", "W. H. Freeman, 1982 (after Les objets fractals, 1975)", None, "03.01", "Fractal geometry as a description of natural forms.", ["fractals"]),
 ("feigenbaum-1978", "Quantitative universality for a class of nonlinear transformations", "paper", "J. Stat. Phys. 19 (1978) 25", D+"10.1007/BF01020332", "03.01", "Period doubling shares universal constants, delta about 4.669 and alpha about 2.503.", ["chaos"]),
 ("ajl-2005", "The spectral dimension of the universe is scale dependent", "paper", "Phys. Rev. Lett. 95 (2005) 171301", A+"hep-th/0505113", "03.02", "In causal dynamical triangulations the spectral dimension runs from about 4 to about 2 at short scales.", ["quantum-gravity", "dimension"]),
 ("wilson-1971", "Renormalization group and critical phenomena", "paper", "Phys. Rev. B 4 (1971) 3174 and 3184", D+"10.1103/PhysRevB.4.3174", "03.02", "The renormalization group and its fixed points.", ["scale"]),
 ("wolfram-1983", "Statistical mechanics of cellular automata", "paper", "Rev. Mod. Phys. 55 (1983) 601", D+"10.1103/RevModPhys.55.601", "03.02", "Elementary cellular automata and their classes of behaviour.", ["computation"]),
 ("cook-2004", "Universality in elementary cellular automata", "paper", "Complex Systems 15 (2004) 1", None, "03.02", "Rule 110 is computationally universal.", ["computation"]),
 ("jacobson-1995", "Thermodynamics of spacetime: the Einstein equation of state", "paper", "Phys. Rev. Lett. 75 (1995) 1260", A+"gr-qc/9504004", "04.01", "Einstein's equation follows from dQ = T dS on local horizons with entropy proportional to area.", ["gravity", "thermodynamics"]),
 ("verlinde-2011", "On the origin of gravity and the laws of Newton", "paper", "JHEP 04 (2011) 029", A+"1001.0785", "04.01", "Gravity proposed as an entropic force.", ["gravity", "thermodynamics"]),
 ("ryu-takayanagi-2006", "Holographic derivation of entanglement entropy from AdS/CFT", "paper", "Phys. Rev. Lett. 96 (2006) 181602", A+"hep-th/0603001", "04.02", "In holographic theories, a region's entanglement entropy is a minimal bulk surface's area over 4G.", ["entanglement", "holography"]),
 ("van-raamsdonk-2010", "Building up spacetime with quantum entanglement", "paper", "Gen. Rel. Grav. 42 (2010) 2323", A+"1005.3035", "04.02", "Removing entanglement between two regions pulls the spacetime between them apart.", ["entanglement", "holography"]),
 ("maldacena-susskind-2013", "Cool horizons for entangled black holes", "paper", "Fortschr. Phys. 61 (2013) 781", A+"1306.0533", "04.02", "ER = EPR: the conjecture that entangled pairs are joined by non-traversable wormholes.", ["entanglement", "holography"]),
 ("casimir-1948", "On the attraction between two perfectly conducting plates", "paper", "Proc. KNAW 51 (1948) 793", None, "05.01", "Two uncharged plates attract: an effect of the vacuum's modes.", ["vacuum"]),
 ("planck-1900", "Ueber irreversible Strahlungsvorgänge", "paper", "Ann. Phys. 1 (1900) 69", None, "01.01", "§26, natural units: units of length, mass, time and temperature from his two radiation constants, c and the gravitational constant, meaningful for all times and cultures.", ["constants"]),
 ("nernst-1912", "Thermodynamik und spezifische Wärme", "paper", "Sitzungsber. Preuss. Akad. Wiss. (1912) 134", None, "05.01", "The unattainability principle: no change of matter reaches absolute zero from any temperature, however low.", ["thermodynamics"]),
 ("planck-1913", "The Theory of Heat Radiation", "book", "Blakiston, Philadelphia, 1914 (Masius's translation of the 1913 second edition)", None, "01.01, 05.01", "§140: at absolute zero an oscillator system's energy is Nhν/2, not 0; §164: natural units.", ["vacuum", "constants"]),
 ("weyl-1922", "Space-Time-Matter", "book", "Methuen, London, 1922 (Brose's translation of the fourth edition, 1921)", None, "02.02", "Weyl's own book account of his 1918 theory: the Action invariant under re-calibration by an arbitrary positive function of position.", ["gauge"]),
 ("planck-1911", "Eine neue Strahlungshypothese", "paper", "Verh. Dtsch. Phys. Ges. 13 (1911) 138", None, "05.01", "The second theory: an oscillator's mean energy is the earlier value plus the constant hν/2.", ["vacuum", "thermodynamics"]),
 ("einstein-stern-1913", "Einige Argumente für die Annahme einer molekularen Agitation beim absoluten Nullpunkt", "paper", "Ann. Phys. 40 (1913) 551", D+"10.1002/andp.19133450309", "05.01", "Arguments for a zero-point energy, from the specific heat of hydrogen and a derivation of Planck's law.", ["vacuum", "thermodynamics"]),
 ("nernst-1906", "Über die Berechnung chemischer Gleichgewichte aus thermischen Messungen", "paper", "Nachr. Ges. Wiss. Göttingen (1906) 1", None, "05.01", "The heat theorem, as a hypothesis about maximal work and energy near absolute zero.", ["thermodynamics"]),
 ("penrose-1965", "Gravitational collapse and space-time singularities", "paper", "Phys. Rev. Lett. 14 (1965) 57", D+"10.1103/PhysRevLett.14.57", "05.01", "Under general conditions gravitational collapse ends in a singularity.", ["gravity"]),
 ("shannon-1948", "A mathematical theory of communication", "paper", "Bell Syst. Tech. J. 27 (1948) 379", D+"10.1002/j.1538-7305.1948.tb01338.x", "06.01", "Information as a measurable quantity; the limits of compression.", ["information"]),
 ("solomonoff-1964", "A formal theory of inductive inference, part I", "paper", "Information and Control 7 (1964) 1", D+"10.1016/S0019-9958(64)90223-2", "06.01", "Induction as finding the shortest program that produces the data.", ["information"]),
 ("huh-2024", "The Platonic Representation Hypothesis", "paper", "ICML 2024", A+"2405.07987", "06.01", "Evidence that larger models' representations grow more alike, and the hypothesis that they converge on a shared model of reality.", ["representation"]),
 ("willow-kernel", "Willow kernel.py", "code", "willow-memory/Willow", "https://raw.githubusercontent.com/willow-memory/Willow/275f15d55d6f14ed966b395db923c344ec0382a3/kernel.py", "06.02", "Serves passages with file and line only when they hold half a question's words; an append-only hash chain whose root is the zero hash; the boot row is numbered 0.", ["willow"]),
]
#: copies the person running the ledger downloaded in a browser where a
#: script is refused; kept by hash in keep/.provided.jsonl
PROVIDED = {
 "englert-brout-1964": "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.13.321",
 "higgs-1964": "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.13.508",
 "ghk-1964": "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.13.585",
 "penrose-1965": "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.14.57",
}
#: how a provided copy was had, where not the 1964 papers' "free to read"
PROVIDED_VIA = {"penrose-1965": "APS, downloaded in a browser by the person running the ledger"}
#: addresses that answer 200 with no work behind them
STUBS = {"solomonoff-1964": "a 2.6 KB redirect page (ScienceDirect)"}
#: open copies other than the publisher's, found 2026-11-06 and kept by
#: almanac-keep as recovery copies (asserted: the holder's word, checked by
#: fetching). Where the publisher's own page is live but holds only an
#: abstract, the open copy is a companion entry, ID-open.
OPEN = {
 "sakharov-1967": ("https://ufn.ru/ufn91/ufn91_5/ufn915h.pdf", "Physics-Uspekhi archive", "the 1991 reprint, English"),
 "shannon-1948": ("https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf", "Harvard mathematics", "the 1948 reprint with corrections, both parts"),
 "solomonoff-1964": ("https://world.std.com/~rjs/1964pt1.pdf", "the author's site", "part I"),
 "nernst-1906": ("https://academicweb.nd.edu/~powers/ame.20231/nernst1906.pdf", "Notre Dame course site", "scan of the Göttingen Nachrichten"),
 "newton-1687": ("https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)/Definitions", "Wikisource", "the 1729 English translation, Definitions and Scholium, long s in markup"),
 "mach-1883": ("https://archive.org/stream/sciencemechanic02machgoog/sciencemechanic02machgoog_djvu.txt", "Internet Archive", "the 1893 English translation, OCR text"),
 "leibniz-clarke-1717": ("https://newtonproject.ox.ac.uk/view/texts/xml/THEM00226", "The Newton Project", "Leibniz's first paper only, CC BY-NC-ND"),
 "einstein-1915": ("https://de.wikisource.org/wiki/Die_Feldgleichungen_der_Gravitation", "Wikisource", "German transcription"),
 "kaluza-1921": ("https://arxiv.org/pdf/1803.08616", "arXiv", "English translation"),
 "klein-1926": ("https://edition-open-sources.org/media/sources/10/10/sources10chap8.pdf", "Edition Open Sources", "sourcebook chapter"),
 "casimir-1948": ("https://www.ph.nat.tum.de/fileadmin/w00bya/t75/pdf/Casimir1948.pdf", "TU Munich physics", "reprint, scanned pages"),
 "julia-1918": ("https://www.numdam.org/item/JMPA_1918_8_1__47_0.pdf", "Numdam", "scan of the original"),
 "fatou-1919": ("https://www.numdam.org/item/10.24033/bsmf.998.pdf", "Numdam", "scan of the original"),
 "vonneumann-1923": ("https://acta.bibl.u-szeged.hu/13294/1/math_001_199-208.pdf", "University of Szeged Library (SZTE Egyetemi Kiadványok)", "scan of the journal pages, 10, with an OCR text layer"),
 "planck-1900": ("https://archive.org/download/sim_annalen-der-physik_1900_1_1/sim_annalen-der-physik_1900_1_1_djvu.txt", "Internet Archive (Serials in Microfilm)", "OCR text of the whole issue, Ann. Phys. 1 no. 1 (1900); the paper is pages 69-122, its natural units §26"),
 "planck-1901": ("https://archive.org/download/sim_annalen-der-physik_1901_4_3/sim_annalen-der-physik_1901_4_3_djvu.txt", "Internet Archive (Serials in Microfilm)", "OCR text of the whole issue, Ann. Phys. 4 no. 3 (1901); the paper is pages 553-563"),
 "nernst-1912": ("https://archive.org/download/in.ernet.dli.2015.105015/2015.105015.Der-Koniglich-Preussischen-Akademie-Der-Wissenschaften-januar-Bis-Juni-1912_djvu.txt", "Internet Archive, from the Digital Library of India", "OCR text of the Sitzungsberichte, January to June 1912; the paper is pages 134-140"),
 "zermelo-1908": ("https://zenodo.org/records/1428264/files/article.pdf", "Zenodo, a CC0 deposit (uploader not named; the work is public domain in the US)", "scan of the original, 21 pages, OCR text layer"),
 "frege-1884": ("https://www.gutenberg.org/cache/epub/48312/pg48312.txt", "Project Gutenberg", "German plain-text transcription of the 1884 edition"),
 "dedekind-1888": ("https://archive.org/download/rcin.org.pl.WA35_13030_4797_Was-sind_5138/WA35_13030_4797_Was-sind_djvu.txt", "Internet Archive, from RCIN (the Polish academies' digital repository)", "OCR text of a scan of the 1888 first edition"),
 "planck-1911": ("https://www.roe.ac.uk/~jap/zpe/planck1911_german.pdf", "a staff page at the Royal Observatory Edinburgh", "German, retyped (not a scan), 11 pages"),
 "einstein-stern-1913": ("https://zenodo.org/records/1424262/files/article.pdf", "Zenodo, a CC0 deposit (uploader not named; the work is public domain in the US)", "scan of the original, 10 pages, OCR text layer"),
 "planck-1913": ("https://www.gutenberg.org/files/40030/40030-pdf.pdf", "Project Gutenberg", "the 1914 English translation, typeset from the Internet Archive's scans"),
 "weyl-1922": ("https://www.gutenberg.org/files/43006/43006-pdf.pdf", "Project Gutenberg", "the 1922 English translation, typeset from the University of Toronto's scans"),
 "cook-2004": ("https://content.wolfram.com/sites/13/2023/02/15-1-1.pdf", "Wolfram, for Complex Systems", "the journal article"),
}
PROBES = OUT.parent / "probes.jsonl"


def history() -> list[dict]:
    """Every probe, oldest first, and every publisher fetch almanac-keep made."""
    rows = []
    if PROBES.exists():
        rows += [json.loads(x) for x in PROBES.read_text(encoding="utf-8").splitlines() if x]
    snaps = OUT.parent / "keep" / ".snapshots.jsonl"
    if snaps.exists():
        for x in snaps.read_text(encoding="utf-8").splitlines():
            s = json.loads(x)
            if s.get("copy") == "the publisher's own address":
                rows.append({"id": s["almanac_id"], "url": s["url"], "checked": s["fetched"],
                             "http_status": s.get("status")})
    return sorted(rows, key=lambda p: p["checked"])


#: further copies of a work, each its own entry beside the work's:
#: id -> (the work's id, address, via, what, provided by hand?)
EXTRA = {
 "leibniz-clarke-1717-third": ("leibniz-clarke-1717", "https://newtonproject.ox.ac.uk/view/texts/xml/THEM00230", "The Newton Project", "Leibniz's third paper, TEI transcription, CC BY-NC-ND", False),
 "dedekind-1888-english": ("dedekind-1888", "https://www.gutenberg.org/files/21016/21016-pdf.pdf", "Project Gutenberg", "Beman's English translation (1901), The Nature and Meaning of Numbers, in Essays on the Theory of Numbers", False),
 "goldstone-1961-preprint": ("goldstone-1961", "https://cds.cern.ch/record/343400/files/CM-P00057225.pdf", "CERN Document Server (CERN-TH-118, 1960), downloaded in a browser", "Goldstone's preprint, scanned, 16 pages", True),
}
entries, pairs = [], []
for sid, title, kind, pub, url, lines, shows, topics in S:
    e = {"id": sid, "title": title, "type": kind, "description": shows, "publisher": pub,
         "status": "cited", "status_source": "SOIL-PHYS-001 rev 2, line " + lines,
         "topics": topics}
    if url:
        e["source"] = {"canonical_url": url}
        # every probe is appended to probes.jsonl and none is ever rewritten:
        # `observed` is the latest answer; an entry is live when any answer was
        # 200 (a later 429 or 403 is the holder's rate limit or block, not the
        # page gone), and keep/.snapshots.jsonl's publisher fetches count too
        if "--probe" in sys.argv:
            when = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            req = urllib.request.Request(url, headers={"User-Agent": "willow-almanac-probe"})
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    code = r.status
            except urllib.error.HTTPError as err:
                code = err.code
            except (urllib.error.URLError, OSError):
                code = None
            with open(PROBES, "a", encoding="utf-8") as log:
                log.write(json.dumps({"id": sid, "url": url, "checked": when, "http_status": code}) + "\n")
            print(f"{code or 'no response'}  {sid}", file=sys.stderr)
        seen = [p for p in history() if p["id"] == sid and p["url"] == url]
        if seen:
            last = seen[-1]
            e["observed"] = {"checked": last["checked"], "reachable": last["http_status"] == 200}
            if last["http_status"] is not None:
                e["observed"]["http_status"] = last["http_status"]
            ok = [p for p in seen if p["http_status"] == 200]
            if ok and sid in STUBS:
                e["status_source"] += f"; the publisher answers 200 with {STUBS[sid]}, so not live"
            elif ok:
                e["status"], e["status_since"] = "live", ok[0]["checked"][:10]
                e["status_source"] = "probe by make_stack.py; cited at " + e["status_source"]
    entries.append(e)
    if sid in PROVIDED:
        e["recovery"] = [{"url": PROVIDED[sid], "via": PROVIDED_VIA.get(sid, "APS, free to read, downloaded in a browser"),
                          "authenticity": "asserted", "permission": "ok",
                          "note": "kept by hash in keep/.provided.jsonl; scripts get 403"}]
    if sid in OPEN:
        url2, via, what = OPEN[sid]
        copy = {"url": url2, "via": via, "authenticity": "asserted", "permission": "ok", "note": what}
        if e["status"] == "live":  # the publisher's page answers, with an abstract: a companion
            entries.append({"id": sid + "-open", "title": title + " (open copy)", "type": kind,
                            "description": f"{what}, held by {via}", "publisher": pub,
                            "status": "cited", "status_source": e["status_source"],
                            "topics": topics, "recovery": [copy]})
        else:
            e["recovery"] = [copy]
    q = f"What does {title} ({pub}) show?"
    pair = {"source_text": q, "target_text": shows, "reason": f"SOIL-PHYS-001 rev 2, {lines}: SOURCE"}
    if url:
        pair["evidence_urls"] = [url]
    pairs.append(pair)
by_id = {e["id"]: e for e in entries}
for xid, (of, url2, via, what, by_hand) in EXTRA.items():
    w = by_id[of]
    copy = {"url": url2, "via": via, "authenticity": "asserted", "permission": "ok", "note": what}
    if by_hand:
        copy["note"] += "; kept by hash in keep/.provided.jsonl; scripts get a bot check"
    entries.append({"id": xid, "title": w["title"] + " (" + what.split(",")[0] + ")", "type": w["type"],
                    "description": f"{what}, held by {via}", "publisher": w["publisher"],
                    "status": "cited", "status_source": w["status_source"], "topics": w["topics"],
                    "recovery": [copy]})
(OUT / "catalog").mkdir(parents=True, exist_ok=True)
(OUT / "nuggets").mkdir(parents=True, exist_ok=True)
(OUT / "catalog" / "catalog.json").write_text(json.dumps(
    {"name": "SOIL-PHYS-001 sources", "entries": entries}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
(OUT / "nuggets" / "soil-phys-001.json").write_text(json.dumps(
    {"domain": "SOIL-PHYS-001", "pairs": pairs}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(len(entries), "sources,", sum(1 for e in entries if "source" in e), "with an address;", len(pairs), "nuggets")
