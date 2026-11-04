#!/usr/bin/env bash
# Build the Fever Chart willow stack in one folder.
#
#   bash build.sh WILLOW_DIR [HOME_DIR] [KEY_DIR]
#
# WILLOW_DIR  a clone of willow-memory/Willow
# HOME_DIR    where the stack lives (default ~/fever-chart)
# KEY_DIR     where the two keys go (default ~/.willow-keys); keep it
#             outside HOME_DIR, so no pile ever holds a key
#
# Makes:
#   HOME_DIR/repo           a clone of rudi193-cmd/DispatchesFromReality
#   HOME_DIR/mirror-md      the repo's Markdown with its markup off (markdown add-on)
#   HOME_DIR/pile/repo      that, with lines over 500 characters broken (text
#                           add-on); each file's .lines map gives the source line
#   HOME_DIR/pile/sources   Brinton 1938, Gutenberg eBook 78065, hash-checked
#   HOME_DIR/pile/notes     your own notes (the watch list is read from the repo)
#   HOME_DIR/boxes/whole    a box over the whole pile
#   HOME_DIR/boxes/sources  a box over the Brinton text only, so a check of
#                           the draft never finds the draft quoting itself
#   HOME_DIR/boxes/links    a box over the raw repo, for xref: the markdown
#                           add-on keeps a link's text, not its target
# Re-running it pulls the repo, rebuilds the mirrors, and leaves the boxes
# and keys alone.
# FEVER_BRANCH=NAME clones a branch other than main.
set -euo pipefail

WILLOW="${1:?usage: bash build.sh WILLOW_DIR [HOME_DIR] [KEY_DIR]}"
HOME_DIR="${2:-$HOME/fever-chart}"
KEY_DIR="${3:-$HOME/.willow-keys}"
SHA=a88099b4f7f92b0ff75fd6c0ba9822f97f48f4cac6c449f131d0d79f01a036d6
TXT="$HOME_DIR/pile/sources/brinton-1938-gutenberg-78065.txt"

[ -f "$WILLOW/kernel.py" ] || { echo "no kernel.py in $WILLOW"; exit 2; }
case "$KEY_DIR/" in "$HOME_DIR"/*) echo "keep KEY_DIR outside $HOME_DIR"; exit 2;; esac

mkdir -p "$HOME_DIR/pile/sources" "$HOME_DIR/pile/notes" "$HOME_DIR/boxes" "$KEY_DIR"

if [ -d "$HOME_DIR/repo/.git" ]; then
  git -C "$HOME_DIR/repo" pull --ff-only
else
  git clone -b "${FEVER_BRANCH:-main}" https://github.com/rudi193-cmd/DispatchesFromReality "$HOME_DIR/repo"
fi

# The repo's Markdown, read as the kernel can read it, by two add-ons:
# markdown takes the markup off, line for line, and text breaks every line
# over 500 characters at spaces, keeping a hidden .lines map back to the
# source line. The kernel keeps only the first 500 characters of a line, and
# this repo writes a whole paragraph on one line.
rm -rf "$HOME_DIR/mirror-md" "$HOME_DIR/pile/repo"
python3 "$WILLOW/adapters/stdlib/markdown/markdown.py" mirror --from "$HOME_DIR/repo" --to "$HOME_DIR/mirror-md"
python3 "$WILLOW/adapters/stdlib/text/text.py" mirror --from "$HOME_DIR/mirror-md" --to "$HOME_DIR/pile/repo"

if [ ! -f "$TXT" ]; then
  curl -sSL -o "$TXT" https://www.gutenberg.org/cache/epub/78065/pg78065.txt
fi
if command -v sha256sum >/dev/null; then got=$(sha256sum "$TXT" | cut -d' ' -f1); else got=$(shasum -a 256 "$TXT" | cut -d' ' -f1); fi
[ "$got" = "$SHA" ] || { echo "Brinton text does not match its hash: $got"; exit 2; }
echo "sources: Brinton text matches its SHA-256"

cp "$HOME_DIR/repo/research/fever-chart-in-bursts/willow/stack.md" "$HOME_DIR/stack.md"

for box in whole sources links; do
  if [ -f "$HOME_DIR/boxes/$box/kernel.json" ]; then
    echo "boxes/$box: already started"
    continue
  fi
  pile="$HOME_DIR/pile"
  [ "$box" = sources ] && pile="$HOME_DIR/pile/sources"
  [ "$box" = links ] && pile="$HOME_DIR/repo"
  python3 "$WILLOW/kernel.py" init --box "$HOME_DIR/boxes/$box" --pile "$pile" --key "$KEY_DIR/fever-$box.key"
done

echo
echo "built. Run the stack from $HOME_DIR:"
echo "  cd $HOME_DIR && python3 $WILLOW/adapters/stdlib/stack/stack.py --box boxes/whole --stack stack.md"
