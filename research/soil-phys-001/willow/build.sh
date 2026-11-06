#!/usr/bin/env bash
# Build the SOIL-PHYS-001 willow stack in one folder.
#
#   bash build.sh WILLOW_DIR [HOME_DIR] [KEY_DIR]
#
# WILLOW_DIR  a clone of willow-memory/Willow (the pdf reader needs pypdf)
# HOME_DIR    where the stack lives (default ~/soil-phys-001)
# KEY_DIR     where the three keys go (default ~/.willow-keys); keep it
#             outside HOME_DIR, so no pile ever holds a key
#
# Makes:
#   HOME_DIR/repo           a clone of rudi193-cmd/DispatchesFromReality
#   HOME_DIR/keep           the ledger's sources, each fetched by almanac-keep
#                           from the catalog and held to the SHA-256 the
#                           packet logged; the four a script can't fetch are
#                           named, with where to download them by hand
#   HOME_DIR/pile/repo      the repo's Markdown, markup off, lines over 500
#                           characters broken (markdown, then text add-on)
#   HOME_DIR/pile/sources   the sources as text: pdf and web-pages readers,
#                           the Newton Project's TEI with its tags off, every
#                           line over 500 characters broken by the text add-on
#   HOME_DIR/pile/stack     the packet's Almanac catalog and Jeles seed, as passages
#   HOME_DIR/boxes/whole    a box over the whole pile
#   HOME_DIR/boxes/sources  a box over the sources only, so a check of the
#                           ledger never finds the ledger quoting itself
#   HOME_DIR/boxes/links    a box over the raw repo, for xref and the repo checks
#   HOME_DIR/out            what the stack's "made" pool writes (prov, a card, a timeline)
# Re-running it pulls the repo, fetches what's missing, rebuilds the piles,
# and leaves the boxes and keys alone.
# SOIL_BRANCH=NAME clones a branch other than research/soil-phys-001.
set -euo pipefail

WILLOW="${1:?usage: bash build.sh WILLOW_DIR [HOME_DIR] [KEY_DIR]}"
HOME_DIR="${2:-$HOME/soil-phys-001}"
KEY_DIR="${3:-$HOME/.willow-keys}"
W="research/soil-phys-001/willow"

[ -f "$WILLOW/kernel.py" ] || { echo "no kernel.py in $WILLOW"; exit 2; }
case "$KEY_DIR/" in "$HOME_DIR"/*) echo "keep KEY_DIR outside $HOME_DIR"; exit 2;; esac
mkdir -p "$HOME_DIR/keep" "$HOME_DIR/boxes" "$HOME_DIR/out" "$KEY_DIR"

if [ -d "$HOME_DIR/repo/.git" ]; then
  git -C "$HOME_DIR/repo" pull --ff-only
else
  git clone -b "${SOIL_BRANCH:-research/soil-phys-001}" https://github.com/rudi193-cmd/DispatchesFromReality "$HOME_DIR/repo"
fi
CATALOG="$HOME_DIR/repo/$W/stack/catalog/catalog.json"

# Every source the catalog says a script may fetch, kept once.
for id in $(python3 -c 'import json,sys; print(" ".join(e["id"] for e in json.load(open(sys.argv[1]))["entries"]
            if e.get("status") == "live" or any(c.get("permission") == "ok" and "browser" not in (c.get("via") or "")
                                                 for c in e.get("recovery") or [])))' "$CATALOG"); do
  { compgen -G "$HOME_DIR/keep/$id.*" >/dev/null || [ -e "$HOME_DIR/keep/$id" ]; } && continue
  python3 "$WILLOW/adapters/stdlib/almanac-keep/keep.py" --catalog "$CATALOG" --id "$id" --to "$HOME_DIR/keep" >/dev/null \
    || echo "keep: $id: no copy answered"
done

# Each kept file held to the hash the packet logged; the by-hand ones named.
# A web page is regenerated on every request (session codes, tracking), so its
# bytes differ each time; its text is held to the text hash logged beside it.
python3 - "$HOME_DIR/repo/$W/keep" "$HOME_DIR/keep" "$WILLOW" <<'PY'
import hashlib, json, sys
from pathlib import Path
logs, keep = Path(sys.argv[1]), Path(sys.argv[2])
sys.path.insert(0, sys.argv[3])
import kernel
text = {json.loads(x)["file"]: json.loads(x)["text_sha256"]
        for x in (logs / ".text.jsonl").read_text(encoding="utf-8").splitlines()}
want = {}
for name in (".snapshots.jsonl", ".provided.jsonl"):
    for line in (logs / name).read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        want[r["file"]] = (r["sha256"], r.get("how"), r.get("from"))
same = differ = page = live = 0
for f, (sha, how, src) in sorted(want.items()):
    p = keep / f
    if not p.exists():
        print(f"by hand: {f}, from {src}" if how else f"missing: {f}")
    elif hashlib.sha256(p.read_bytes()).hexdigest() == sha:
        same += 1
    elif f in text and hashlib.sha256(kernel.html_text(
            p.read_text(encoding="utf-8", errors="replace")).encode("utf-8")).hexdigest() == text[f]:
        page += 1
    elif f in text:
        live += 1
        print(f"live page: {f}: its text changed too (a counter, a notice); the packet's copy is the record")
    else:
        differ += 1
        print(f"DIFFERENT: {f}: not the bytes the packet logged")
print(f"sources: {same} match their SHA-256; {page} web pages changed, their text the same; "
      f"{live} live pages changed; {differ} differ")
PY

# The repo, as the kernel can read it.
rm -rf "$HOME_DIR/mirror-md" "$HOME_DIR/pile/repo"
python3 "$WILLOW/adapters/stdlib/markdown/markdown.py" mirror --from "$HOME_DIR/repo" --to "$HOME_DIR/mirror-md"
python3 "$WILLOW/adapters/stdlib/text/text.py" mirror --from "$HOME_DIR/mirror-md" --to "$HOME_DIR/pile/repo"

# The sources, as text: each reader, then every line under 500 characters.
rm -rf "$HOME_DIR/stage" "$HOME_DIR/pile/sources"
mkdir -p "$HOME_DIR/stage/pdf" "$HOME_DIR/stage/html" "$HOME_DIR/stage/text"
for f in "$HOME_DIR"/keep/*; do
  case "$f" in
    *.pdf) cp "$f" "$HOME_DIR/stage/pdf/" ;;
    # Wikisource marks each long s as a span, and willow's HTML reader puts a
    # space at every tag (bug #284), so "similar" would read "s imilar": unwrap them
    *.html) sed -E 's#<span class="typographic-long-s"[^>]*>s</span>#s#g' "$f" > "$HOME_DIR/stage/html/$(basename "$f")" ;;
    # an OCR of old type keeps the long s (Dedekind's "Syſtem"): read it as s;
    # a Project Gutenberg text is read between its START and END lines, without
    # the English licence around it (Frege's German would sort as "information")
    *.txt) if grep -q '^\*\*\* START OF THE PROJECT GUTENBERG' "$f"; then
             sed -n '/^\*\*\* START OF THE PROJECT GUTENBERG/,/^\*\*\* END OF THE PROJECT GUTENBERG/p' "$f"
           else cat "$f"; fi | sed 's/ſ/s/g' > "$HOME_DIR/stage/text/$(basename "$f")" ;;
    # a copy almanac-keep saved with no extension (the server didn't name its
    # type): a PDF by its first bytes, otherwise a Newton Project TEI file
    *) if [ "$(head -c 4 "$f")" = "%PDF" ]; then cp "$f" "$HOME_DIR/stage/pdf/$(basename "$f").pdf"; continue; fi
       python3 - "$f" "$HOME_DIR/stage/text/$(basename "$f").txt" <<'PY'
import re, sys
raw = open(sys.argv[1], encoding="utf-8").read()
body = re.split(r"<text\b[^>]*>", raw, maxsplit=1)[-1]
body = re.sub(r"<(p|head|lg|l)\b[^>]*>", "\n\n", body)
paras = [" ".join(x.split()) for x in re.sub(r"<[^>]+>", "", body).split("\n\n")]
open(sys.argv[2], "w", encoding="utf-8").write("\n\n".join(x for x in paras if x) + "\n")
PY
    ;;
  esac
done
python3 "$WILLOW/adapters/deps/pdf/pdf.py" mirror --from "$HOME_DIR/stage/pdf" --to "$HOME_DIR/stage/text/pdf" 2>&1 \
  | grep -v "fontTools is required" || true  # pypdf's note on old fonts, once a page
python3 "$WILLOW/adapters/stdlib/web-pages/web_pages.py" mirror --from "$HOME_DIR/stage/html" --to "$HOME_DIR/stage/text/html"
python3 "$WILLOW/adapters/stdlib/text/text.py" mirror --from "$HOME_DIR/stage/text" --to "$HOME_DIR/pile/sources"

# The packet's Almanac catalog and Jeles seed, as passages (almanac, jeles add-ons).
rm -rf "$HOME_DIR/pile/stack"
python3 "$WILLOW/adapters/stdlib/almanac/almanac.py" mirror --from "$HOME_DIR/repo/$W/stack/catalog" --to "$HOME_DIR/pile/stack/almanac"
python3 "$WILLOW/adapters/stdlib/jeles/jeles.py" mirror --from "$HOME_DIR/repo/$W/stack/nuggets" --to "$HOME_DIR/pile/stack/jeles"

cp "$HOME_DIR/repo/$W/stack.md" "$HOME_DIR/stack.md"

for box in whole sources links; do
  if [ -f "$HOME_DIR/boxes/$box/kernel.json" ]; then
    echo "boxes/$box: already started"
    continue
  fi
  pile="$HOME_DIR/pile"
  [ "$box" = sources ] && pile="$HOME_DIR/pile/sources"
  [ "$box" = links ] && pile="$HOME_DIR/repo"
  python3 "$WILLOW/kernel.py" init --box "$HOME_DIR/boxes/$box" --pile "$pile" --key "$KEY_DIR/soil-$box.key"
done

echo
echo "built. Run the stack from $HOME_DIR:"
echo "  cd $HOME_DIR && python3 $WILLOW/adapters/stdlib/stack/stack.py --box boxes/whole --stack stack.md"
