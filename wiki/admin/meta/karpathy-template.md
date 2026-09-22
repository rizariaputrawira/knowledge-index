---
title: "Karpathy Pattern Template & Standards"
tags: [meta, template, karpathy, wiki-standards]
version: "meta"
updated: 2026-09-18
sources: []
summary: "Standard Karpathy Pattern rules, frontmatter protocol, and verification checklist for all wiki note creation."
aliases: ["karpathy-template", "karpathy-rules", "wiki-template"]
---

# Karpathy Pattern Template & Standards

Up: [[admin-index]]

Reference this page in agent instructions as `Follow [[karpathy-template]]`.

---

## Style Rules
- **Dense, information-rich markdown.** Zero narrative fluff, conversational filler, or boilerplate intros.
- **NO "Executive Summary" or "Context" placeholder headings.** Dive directly into core technical specifications and definitions.
- **Use `[[wikilinks]]`** for internal cross-references across notes.
- **Favor structured over prose:** use Markdown tables, code blocks, and Mermaid diagrams where applicable.
- **Extract verifiable factual content** from primary sources in `raw/`; never invent numbers, dates, or specifications.

---

## Frontmatter Protocol
Every compiled wiki note must begin with valid YAML frontmatter containing the 7 mandatory fields, with optional bundle descriptor when source bundle differs from topic release:

```yaml
---
title: "Page Title"
tags: [domain, topic, subtopic]
version: "1.2.0"
bundle_version: "2026.03"    # Optional: documentation bundle release if different from version
updated: YYYY-MM-DD
sources: ["raw/topic/source-document.md"]
summary: "One-sentence description of the note's core premise"
aliases: ["alternative-name-1", "alternative-name-2"]
---
```

Followed immediately by the provenance header:
```markdown
> Version: 1.2.0
> Bundle: 2026.03 (optional)
> Raw: [[../../raw/topic/source-document.md]]
> Updated: YYYY-MM-DD
```

### Frontmatter Field Requirements
- `title`: Clean, human-readable title.
- `tags`: Substantive, domain-specific tags.
- `version`: Strict release/version identifier of the subject component (e.g. `1.2.0`, `2026.03`, `meta`). If not confirmed in source, ask the user.
- `bundle_version`: Optional source documentation bundle release when extracted from a newer/differing bundle (e.g. `2026.03`).
- `updated`: Current ISO date (`YYYY-MM-DD`).
- `sources`: Array of relative paths pointing to backing documents under `raw/`.
- `summary`: Crisp, single-sentence summary.
- `aliases`: Alternate names, acronyms, or casing variants for Obsidian search.

---

## Pre-Return Self-Verification Checklist
Before completing any note creation or update, verify:

- [ ] Frontmatter contains all 7 fields (`title`, `tags`, `version`, `updated`, `sources`, `summary`, `aliases`).
- [ ] Explicit version is verified or confirmed by user (never omitted or assumed).
- [ ] Provenance blockquote (`> Version:`, `> Raw:`, `> Updated:`) matches frontmatter fields.
- [ ] Filename uses strict `kebab-case.md` and matches note concept.
- [ ] All cross-references use `[[wikilinks]]`.
- [ ] All tables have column headers and valid formatting.
- [ ] Leaf note is registered in its corresponding domain index and linked upward to `[[index]]`.
- [ ] Ingest/update operation is appended to `[[log]]`.
