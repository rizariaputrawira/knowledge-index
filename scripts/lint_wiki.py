#!/usr/bin/env python3
"""Wiki health linter for a Karpathy-style LLM wiki.

Three sweeps:

1. Orphan notes — wiki notes that no other note links to via [[wikilink]].
   index.md, log.md, and domain index files are excluded from the orphan check
   (they are hubs, not leaves).
2. Broken wikilinks — [[wikilinks]] that reference a slug that doesn't
   correspond to any .md file in wiki/.
3. Missing pages — concept slugs mentioned as [[wikilinks]] more than once
   across the wiki but lacking their own .md file (i.e., red links that
   should probably be stubs).

Exit code semantics:
- Returns 0 when 0 broken wikilinks are detected.
  (Orphans and missing pages are reported as warnings, not errors.)
- Returns 1 when broken wikilinks are found (they break Obsidian navigation).

Usage: lint_wiki.py [project-root]
Defaults: project-root is current directory.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]")
SKIP_ORPHAN_STEMS = {"index", "log", "admin-index"}
SKIP_ADMIN = {"admin/", "/admin/"}


def stem(path: Path, wiki_dir: Path) -> str:
    """Return the canonical slug (filename without .md) for a wiki file."""
    return path.stem


def iter_wiki_notes(wiki_dir: Path):
    for path in sorted(wiki_dir.rglob("*.md")):
        rel = path.relative_to(wiki_dir).as_posix()
        if any(sub in rel for sub in SKIP_ADMIN):
            continue
        yield path


def parse_wikilinks(text: str) -> list[str]:
    """Extract all [[wikilink]] slugs from text, stripping fences."""
    # Strip fenced code blocks to avoid matching links in examples
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`[^`\n]*`", " ", text)
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(text)]


def resolve_slug(slug: str, wiki_dir: Path) -> Path | None:
    """Return the .md path for a slug if it exists, else None."""
    # Try direct match (slug = filename stem)
    direct = wiki_dir / f"{slug}.md"
    if direct.is_file():
        return direct
    # Try case-insensitive rglob
    for path in wiki_dir.rglob(f"{slug}.md"):
        return path
    # Try with kebab normalization
    normalized = re.sub(r"\s+", "-", slug.lower())
    for path in wiki_dir.rglob(f"{normalized}.md"):
        return path
    return None


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path.cwd()
    wiki_dir = root / "wiki"
    if not wiki_dir.is_dir():
        print(f"no wiki/ directory under {root}")
        return 1

    # Build slug → path map for all wiki notes
    all_notes: dict[str, Path] = {}
    for path in wiki_dir.rglob("*.md"):
        all_notes[path.stem] = path
        # also index by kebab-normalized name
        normalized = re.sub(r"\s+", "-", path.stem.lower())
        if normalized != path.stem:
            all_notes[normalized] = path

    # Sweep: collect all wikilinks per file and build inbound link map
    outbound: dict[Path, list[str]] = {}
    inbound: dict[str, list[str]] = defaultdict(list)  # slug → list of source files
    mention_count: dict[str, int] = defaultdict(int)   # slug → how many files mention it

    for note in iter_wiki_notes(wiki_dir):
        text = note.read_text(encoding="utf-8")
        links = parse_wikilinks(text)
        outbound[note] = links
        source_label = note.relative_to(wiki_dir).as_posix()
        for slug in links:
            inbound[slug].append(source_label)
            mention_count[slug] += 1

    print("# Wiki health lint\n")

    # --- Sweep 1: Broken wikilinks ---
    print("## Broken wikilinks")
    broken_count = 0
    for note in sorted(iter_wiki_notes(wiki_dir)):
        broken = []
        for slug in outbound.get(note, []):
            target = resolve_slug(slug, wiki_dir)
            if target is None:
                broken.append(slug)
                broken_count += 1
        if broken:
            label = note.relative_to(wiki_dir).as_posix()
            print(f"\n{label}")
            for slug in broken:
                print(f"  - [[{slug}]] → not found")
    if broken_count == 0:
        print("(none)")

    # --- Sweep 2: Orphan notes ---
    print("\n## Orphan notes (no inbound links)")
    orphan_count = 0
    for note in sorted(iter_wiki_notes(wiki_dir)):
        note_stem = note.stem
        if note_stem in SKIP_ORPHAN_STEMS or note_stem.endswith("-index"):
            continue
        if note_stem not in inbound or not inbound[note_stem]:
            label = note.relative_to(wiki_dir).as_posix()
            print(f"  - {label}")
            orphan_count += 1
    if orphan_count == 0:
        print("(none)")
    else:
        print(f"\n⚠ {orphan_count} orphan note(s) — consider adding backlinks or registering in domain index")

    # --- Sweep 3: Red links (mentioned multiple times but no page) ---
    print("\n## Red links (mentioned 2+ times, no page exists)")
    red_count = 0
    for slug, count in sorted(mention_count.items(), key=lambda x: -x[1]):
        if count < 2:
            continue
        target = resolve_slug(slug, wiki_dir)
        if target is None:
            print(f"  - [[{slug}]] — mentioned {count}× but no page exists")
            red_count += 1
    if red_count == 0:
        print("(none)")
    else:
        print(f"\n⚠ {red_count} red link(s) — consider creating stub pages")

    print(f"\n## Summary\n{broken_count} broken wikilink(s), {orphan_count} orphan(s), {red_count} red link(s)")

    # Only broken wikilinks are hard errors (they break Obsidian navigation)
    return 1 if broken_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
