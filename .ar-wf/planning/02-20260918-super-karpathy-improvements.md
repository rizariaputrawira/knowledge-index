# Plan: Superior Karpathy Wiki — 18 Improvement Gaps
**Plan ID**: `02-20260918-super-karpathy-improvements`  
**Tier**: superplan  
**Date**: 2026-09-18  
**Source**: improvement-audit.md — gap analysis vs Karpathy original LLM Wiki spec  
**Goal**: Close all 18 gaps so our wiki is demonstrably superior to the Karpathy spec on every dimension.

---

## Success Criteria
- `python3 scripts/check_frontmatter.py` passes with exit 0 on all current wiki notes
- `python3 scripts/lint_wiki.py` passes with exit 0
- `python3 scripts/check_evidence.py` still passes with exit 0
- AGENTS.md contains Query Workflow, Lint Workflow, cross-reference rule, unified log format
- `karpathy-template.md` and `index.md` have `version: "meta"` field
- `raw-template.md` has `> Version:` header
- `best-practices.md` documents ingest modes, image handling, web clipper
- `index.md` has 7 domain categories
- `community-plugins.json` includes dataview and marp
- `app.json` has `attachmentFolderPath: raw/assets`
- `raw/README.md` exists
- `.gitignore` excludes `__pycache__`
- Zero violations of style rules in admin templates

---

## Tasks

- [x] **Step 1: New scripts — check_frontmatter.py + lint_wiki.py**
  - Files: `scripts/check_frontmatter.py` (new), `scripts/lint_wiki.py` (new)
  - Action: Write `check_frontmatter.py` (~60 lines) to validate all 7 mandatory frontmatter fields are present and non-empty on every non-admin wiki note. Write `lint_wiki.py` (~80 lines) to detect: orphan notes (no inbound wikilinks from any other note), broken `[[wikilinks]]` (link targets that don't exist as files), and notes mentioned inline but lacking their own page.
  - Verification: `python3 scripts/check_frontmatter.py . > evidence/task-1/report.txt 2>&1 && echo EXIT:$?`; `python3 scripts/lint_wiki.py . >> evidence/task-1/report.txt 2>&1 && echo EXIT:$?`

- [x] **Step 2: AGENTS.md — Query workflow + Lint workflow + cross-ref rule + unified log format**
  - Files: `AGENTS.md`
  - Action: (a) Add `### 3. Query Workflow` section: read index first → drill into pages → synthesize → evaluate if answer should be filed back as a wiki note → if yes follow pipeline. (b) Add `### 4. Lint & Maintenance Workflow` section: periodic health-check steps (run lint_wiki.py, check_evidence.py, review orphans, identify concepts mentioned but missing their own page). (c) Update stage 3 of ingest pipeline to explicitly require updating all related existing pages. (d) Unify the two conflicting log format specs into one canonical format with version.
  - Verification: `grep -n "Query Workflow" AGENTS.md && grep -n "Lint" AGENTS.md && grep -n "related existing pages" AGENTS.md`

- [x] **Step 3: Template consistency fixes — version fields + heading violations**
  - Files: `wiki/admin/meta/karpathy-template.md`, `wiki/index.md`, `wiki/admin/references/raw-template.md`, `wiki/admin/meta/llm-wiki-pattern.md`, `.obsidian/templates/new-page.md`
  - Action: (a) Add `version: "meta"` to frontmatter of `karpathy-template.md` and `index.md`. (b) Add `> Version: {version string — verify in source or ask user}` line to `raw-template.md`. (c) Rename `## Executive Concept` heading to `## Core Concept` in `llm-wiki-pattern.md`. (d) Replace prohibited `## Overview` section in `new-page.md` with spec-compliant stub structure (`## Core Concept`, `## Specifications & Details`, `## Related Notes`).
  - Verification: `grep "version:" wiki/admin/meta/karpathy-template.md && grep "version:" wiki/index.md && grep "Version:" wiki/admin/references/raw-template.md && grep -v "Executive Concept" wiki/admin/meta/llm-wiki-pattern.md | grep "Core Concept" && grep -v "Overview" .obsidian/templates/new-page.md | head -5`

- [x] **Step 4: best-practices.md — ingest modes + image handling + web clipper**
  - Files: `wiki/admin/meta/best-practices.md`
  - Action: Add three new sections: (a) `## 5. Ingest Mode Selection` — incremental (one-at-a-time, recommended) vs batch with tradeoffs. (b) `## 6. Source Capture Workflows` — Obsidian Web Clipper → `raw/<topic>/YYYY-MM-DD-slug.md` flow, naming convention. (c) `## 7. Image Handling` — set attachment folder to `raw/assets/`, bind "Download attachments" hotkey (Ctrl+Shift+D), workflow for LLM to view images separately after clipping.
  - Verification: `grep -n "Ingest Mode" wiki/admin/meta/best-practices.md && grep -n "Web Clipper" wiki/admin/meta/best-practices.md && grep -n "Image Handling" wiki/admin/meta/best-practices.md`

- [x] **Step 5: index.md domain expansion + log.md grep tip**
  - Files: `wiki/index.md`, `wiki/log.md`
  - Action: (a) Add 4 new domain catalog sections to `index.md`: Mathematics & Statistics, Security & Cryptography, DevOps & Infrastructure, Reading Notes. (b) Add a grep tip callout to `wiki/log.md` header: `grep "^## \[" wiki/log.md | tail -5` for recent entry audit.
  - Verification: `grep -c "###" wiki/index.md` (expect 7+); `grep "grep" wiki/log.md`

- [x] **Step 6: Obsidian — Dataview + Marp plugins + image attachment path**
  - Files: `.obsidian/community-plugins.json`, `.obsidian/app.json`
  - Action: (a) Add `"dataview"` and `"marp-slides"` to `community-plugins.json`. (b) Set `"attachmentFolderPath": "raw/assets"` in `app.json`. Note: actual plugin binaries managed by Obsidian on first launch — we register intent here.
  - Verification: `grep dataview .obsidian/community-plugins.json && grep marp .obsidian/community-plugins.json && grep attachmentFolderPath .obsidian/app.json`

- [x] **Step 7: raw/ infrastructure + .gitignore**
  - Files: `raw/README.md` (new), `raw/assets/.gitkeep` (new), `.gitignore`
  - Action: (a) Write `raw/README.md` documenting the write-once invariant, naming convention (`YYYY-MM-DD-slug.md`), directory structure, and the `> Version:` provenance header requirement. (b) Create `raw/assets/.gitkeep`. (c) Add `scripts/__pycache__/` and `**/__pycache__/` to `.gitignore`.
  - Verification: `cat raw/README.md | head -5 && cat raw/assets/.gitkeep && grep pycache .gitignore`

- [x] **Step 8: Final verification gate — all scripts pass, commit everything**
  - Action: Run full verification suite: `check_evidence.py`, `check_frontmatter.py`, `lint_wiki.py`. Confirm zero errors. Commit all changes atomically. Append comprehensive log entry to `wiki/log.md`.
  - Verification: All three scripts exit 0; `git log --oneline -5` shows commits; `tail -5 wiki/log.md` shows new entry.
