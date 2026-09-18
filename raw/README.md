# raw/ — Immutable Primary Source Drop-Zone

This directory holds **write-once, read-only** primary source materials.
The LLM reads from here; it never modifies, reorganizes, or summarizes files in this directory.

---

## Invariant

> **Once a file is committed to `raw/`, it is immutable.**
> If a source needs correction, add a new file with a corrected version alongside the original. Never overwrite.

This directory is the **source of truth** for the wiki. Every load-bearing fact (specific numbers, dates, quotes, parameters) in `wiki/` must exist verbatim in a file here. The `scripts/check_evidence.py` tool enforces this mechanically.

---

## Naming Convention

```
raw/<topic>/YYYY-MM-DD-slug.md
```

- `<topic>`: kebab-case domain name (e.g. `distributed-systems`, `llm-architecture`, `security`)
- `YYYY-MM-DD`: date the source was collected (not published)
- `slug`: short, descriptive, kebab-case identifier

**Examples:**
```
raw/llm-architecture/2026-03-15-attention-is-all-you-need.md
raw/distributed-systems/2026-09-10-raft-extended-paper.md
raw/security/2026-01-22-owasp-top-10-v2025.md
raw/assets/                 ← downloaded images (Obsidian attachment folder)
```

---

## Required Provenance Headers

Every `.md` file in `raw/` must start with these headers (see `wiki/admin/references/raw-template.md`):

```markdown
> Source: {URL, DOI, or origin description}
> Collected: {YYYY-MM-DD}
> Published: {YYYY-MM-DD or Unknown}
> Version: {version string — verify in document or ask user before compiling wiki note}
```

If you cannot determine the `Version:` from the source document, **leave it as a question** and ask the user before proceeding to compile a wiki note from this source.

---

## Sub-directories

| Directory | Purpose |
|---|---|
| `raw/<topic>/` | Domain-specific primary sources |
| `raw/assets/` | Downloaded images (auto-populated by Obsidian Web Clipper + Ctrl+Shift+D) |

---

## What Does NOT Belong Here

- LLM-synthesized summaries (those go in `wiki/`)
- Temporary notes or drafts
- Any file that has been modified after initial commit
