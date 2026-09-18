# Plan: Ponytail Audit Fixes — Script Shrink
**Plan ID**: `03-20260918-flash-ponytail-script-shrink`
**Tier**: flashplan
**Date**: 2026-09-18
**Source**: ponytail-audit findings 1–10

## Success Criteria
- All 10 ponytail findings addressed
- `python3 scripts/check_evidence.py .` exits 0
- `python3 scripts/check_frontmatter.py .` exits 0
- `python3 scripts/lint_wiki.py .` exits 0
- Net line reduction ≥ 35 lines

---

## Tasks

- [x] **Step 1: Fix check_evidence.py** (findings 1, 4, 5, 6, 7, 8)
  - Files: `scripts/check_evidence.py`
  - (6) `Document` frozen dataclass → `typing.NamedTuple` (frozen=True overhead gone)
  - (7) `Candidate` frozen dataclass → `typing.NamedTuple`
  - (4) Delete `strip_fences()` (152–167); replace its only caller `no_material_paths()` with `"\n".join(parse_document(text).body)`
  - (5) Two `seen = set()` / manual-dedup loops → `list(dict.fromkeys(...))`
  - (8) `label()` inner function → inline `article.relative_to(root) if article.is_relative_to(root) else article`
  - (1) `SKIP_SUBSTRINGS`: remove 4 dead `/`-prefixed variants — keep only `{"admin/", "references/", "meta/", "core-system-rules/"}`
  - Verification: `python3 scripts/check_evidence.py . > evidence/task-1/report.txt 2>&1 && echo EXIT:$?`

- [x] **Step 2: Fix check_frontmatter.py** (findings 1, 2)
  - Files: `scripts/check_frontmatter.py`
  - (2) `is_empty_value`: remove duplicate `'""'` and `"''"` entries — reduce to 4 distinct values
  - (1) `SKIP_SUBSTRINGS`: same dead-slash-prefix removal as step 1
  - Verification: `python3 scripts/check_frontmatter.py . > evidence/task-2/report.txt 2>&1 && echo EXIT:$?`

- [x] **Step 3: Fix lint_wiki.py** (findings 3, 9)
  - Files: `scripts/lint_wiki.py`
  - (9) `SKIP_ADMIN`: remove dead `"/admin/"` — keep only `{"admin/"}`
  - (3) `resolve_slug()`: delete rglob branches; accept `all_notes: dict[str, Path]` parameter; do direct dict lookup + kebab-normalized fallback (O(1) per lookup)
  - Verification: `python3 scripts/lint_wiki.py . > evidence/task-3/report.txt 2>&1 && echo EXIT:$?`

- [x] **Step 4: Final verification + line count delta**
  - Run all three scripts together; count lines before/after
  - Commit all changes with atomic message
