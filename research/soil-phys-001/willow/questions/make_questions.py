"""Write questions.tsv: every question the sources ask, every pair of the
ledger's ideas in English, German and French, and the ledger's own lines.

    python3 make_questions.py PILE_SOURCES DRAFT.md > questions.tsv

One question a line, `name<TAB>question`, as willow's scan reads them."""
import re, sys, itertools
from pathlib import Path

P, D = Path(sys.argv[1]), Path(sys.argv[2]).read_text(encoding="utf-8")
out = []


def src(p):
    return re.sub(r"(\.(pdf|html|txt))+$", "", p.name)


# the papers' own questions: a sentence of 4 to 40 words ending in "?"
seen = set()
for f in sorted(P.rglob("*.txt")):
    t = " ".join(f.read_text(encoding="utf-8", errors="replace").split())
    for m in re.finditer(r"(?:(?<=[.!?»“\"]\s)|^)([A-ZÄÖÜÉ][^.!?]{15,220}\?)", t):
        q = m.group(1).strip()
        w = re.findall(r"[^\W\d_]{2,}", q)
        if len(w) < 4 or len(w) > 40 or sum(len(x) == 1 for x in q.split()) > len(q.split()) / 3:
            continue
        if q.lower() in seen:
            continue
        seen.add(q.lower())
        out.append((f"own:{src(f)}", q))

# the ledger's ideas, each as English, German, French
C = {"zero": ("Null", "zéro"), "nothing": ("Nichts", "rien"), "empty": ("leer", "vide"), "vacuum": ("Vakuum", "vide"),
     "void": ("Leere", "néant"), "ground state": ("Grundzustand", "état fondamental"), "boundary": ("Grenze", "frontière"),
     "limit": ("Grenzwert", "limite"), "origin": ("Ursprung", "origine"), "unit": ("Einheit", "unité"), "one": ("Eins", "un"),
     "set": ("Menge", "ensemble"), "element": ("Element", "élément"), "number": ("Zahl", "nombre"), "infinite": ("unendlich", "infini"),
     "finite": ("endlich", "fini"), "symmetry": ("Symmetrie", "symétrie"), "broken": ("gebrochen", "brisée"),
     "absolute": ("absolut", "absolu"), "relative": ("relativ", "relatif"), "space": ("Raum", "espace"), "time": ("Zeit", "temps"),
     "dimension": ("Dimension", "dimension"), "singularity": ("Singularität", "singularité"), "horizon": ("Horizont", "horizon"),
     "entropy": ("Entropie", "entropie"), "information": ("Information", "information"), "energy": ("Energie", "énergie"),
     "temperature": ("Temperatur", "température"), "motion": ("Bewegung", "mouvement"), "rest": ("Ruhe", "repos"),
     "measure": ("Maß", "mesure"), "scale": ("Maßstab", "échelle"), "constant": ("Konstante", "constante"), "law": ("Gesetz", "loi"),
     "cause": ("Ursache", "cause"), "reason": ("Grund", "raison"), "chance": ("Zufall", "hasard"),
     "probability": ("Wahrscheinlichkeit", "probabilité"), "observer": ("Beobachter", "observateur"),
     "experience": ("Erfahrung", "expérience"), "field": ("Feld", "champ"), "ether": ("Äther", "éther"), "mass": ("Masse", "masse"),
     "charge": ("Ladung", "charge"), "point": ("Punkt", "point"), "fixed point": ("Fixpunkt", "point fixe"),
     "iteration": ("Iteration", "itération"), "stability": ("Stabilität", "stabilité"), "phase": ("Phase", "phase"),
     "degeneracy": ("Entartung", "dégénérescence"), "conservation": ("Erhaltung", "conservation"),
     "asymmetry": ("Asymmetrie", "asymétrie"), "container": ("Behälter", "contenant"), "distinction": ("Unterscheidung", "distinction"),
     "form": ("Form", "forme"), "order": ("Ordnung", "ordre"), "definition": ("Definition", "définition"),
     "existence": ("Existenz", "existence"), "God": ("Gott", "Dieu"), "world": ("Welt", "monde"), "universe": ("Weltall", "univers"),
     "matter": ("Materie", "matière"), "light": ("Licht", "lumière"), "gravitation": ("Gravitation", "gravitation"),
     "quantum": ("Quanten", "quanta"), "oscillator": ("Oszillator", "oscillateur"), "computation": ("Berechnung", "calcul"),
     "model": ("Modell", "modèle"), "representation": ("Darstellung", "représentation")}
for a, b in itertools.combinations(list(C), 2):
    out += [(f"pair:{a}|{b}|en", f"{a} {b}"), (f"pair:{a}|{b}|de", f"{C[a][0]} {C[b][0]}"),
            (f"pair:{a}|{b}|fr", f"{C[a][1]} {C[b][1]}")]

# the ledger's SOURCE and READING lines, quotes and parentheses taken out
for i, line in enumerate(D.splitlines(), 1):
    m = re.match(r"^(?:\| (\w+) \| (SOURCE|READING) \| |- (SOURCE|READING): )(.*)", line)
    if not m:
        continue
    body = re.sub(r'"[^"]*"|„[^“]*“|\([^)]*\)|\*', "", m.group(4)).split(". ")[0]
    body = " ".join(body.replace("|", "").split())[:200]
    if len(body.split()) >= 3:
        out.append((f"ledger:{i}:{m.group(2) or m.group(3)}", body))

sys.stdout.write("".join(f"{n}\t{q}\n" for n, q in out))
