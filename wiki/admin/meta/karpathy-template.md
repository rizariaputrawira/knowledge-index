---
title: "Karpathy Pattern Template & Standards"
tags: [meta, template, karpathy, wiki-standards]
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
Every compiled wiki note must begin with valid YAML frontmatter containing all 6 mandatory fields:

```yaml
---
title: "Page Title"
tags: [domain, topic, subtopic]
updated: YYYY-MM-DD
sources: ["raw/topic/source-document.md"]
summary: "One-sentence description of the note's core premise"
aliases: ["alternative-name-1", "alternative-name-2"]
---
```

Followed immediately by the provenance header:
```markdown
> Raw: [[../../raw/topic/source-document.md]]
> Updated: YYYY-MM-DD
```

### Frontmatter Field Requirements
- `title`: Clean, human-readable title.
- `tags`: Substantive, domain-specific tags.
- `updated`: Current ISO date (`YYYY-MM-DD`).
- `sources`: Array of relative paths pointing to backing documents under `raw/`.
- `summary`: Crisp, single-sentence summary.
- `aliases`: Alternate names, acronyms, or casing variants for Obsidian search.

---

## Pre-Return Self-Verification Checklist
Before completing any note creation or update, verify:

- [ ] Frontmatter contains all 6 fields (`title`, `tags`, `updated`, `sources`, `summary`, `aliases`).
- [ ] Provenance blockquote (`> Raw:`, `> Updated:`) matches frontmatter sources.
- [ ] Filename uses strict `kebab-case.md` and matches note concept.
- [ ] All cross-references use `[[wikilinks]]`.
- [ ] All tables have column headers and valid formatting.
- [ ] Leaf note is registered in its corresponding domain index and linked upward to `[[index]]`.
- [ ] Ingest/update operation is appended to `[[log]]`.
