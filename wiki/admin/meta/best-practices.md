---
title: "Wiki Synthesis Best Practices"
tags: [meta, rules, best-practices]
updated: 2026-09-18
sources: []
summary: "Synthesis protocols, conflict handling, and lifecycle management for compiling high-signal notes."
aliases: ["best-practices", "synthesis-rules"]
---

# Wiki Synthesis Best Practices

Up: [[admin-index]]

---

## 1. High-Density Knowledge Synthesis
- **Dense Signal:** The wiki is a compiled knowledge layer, not a transcript dump. Reorganize, distill, and tabularize concepts so they can be parsed by human or AI in seconds.
- **Locate Before Write:** Always search the existing wiki (`grep_search` or index inspection) before authoring a new note. If a related concept note already exists, update and enrich it rather than fragmenting the topic into duplicate files.

## 2. Topic Clustering & Naming
- **Atomic Notes:** Follow the one-concept-one-page principle.
- **Kebab-Case Naming:** Use clean, descriptive `kebab-case.md` for all note filenames (e.g., `distributed-consensus.md`, `raft-algorithm.md`). Avoid generic names like `notes.md` or `summary.md`.
- **Domain Prefixes:** If ambiguity exists across domains, use a clear domain prefix (e.g., `net-http2-framing.md`, `db-btree-indexes.md`).

## 3. Provenance & Conflict Management
- **Primary Source Fidelity:** If a source document makes a technical assertion, cite the specific page or section in the note body.
- **Handling Contradictions:** When two reputable sources disagree, do not arbitrarily pick one. Annotate both viewpoints explicitly:
  ```markdown
  > **Status: Disputed**
  > Source A ([title](raw/path1.md)) asserts X, whereas Source B ([title](raw/path2.md)) demonstrates Y under condition Z.
  ```
- **Superseded Concepts:** When a new architecture or standard replaces an older one, mark the older section:
  ```markdown
  > **Status: Outdated** (YYYY-MM-DD)
  > Superseded by [[new-standard]]; retained for legacy compatibility context.
  ```

## 4. Lifecycle & Archiving
- **Active vs Archived:** Active domain folders contain current knowledge. When a concept becomes completely deprecated, move it to `archive/` or use [[references/archive-template]] to preserve historical context without cluttering search results.

---

## Related Notes
- [[llm-wiki-pattern]]: Overview of the Karpathy Wiki Pattern.
- [[karpathy-template]]: Exact formatting rules and self-verification checklist.
- [[core-ai-rules]]: Core safety and data lifecycle invariants.
