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

## 5. Ingest Mode Selection
Two modes — choose based on source type and desired quality control:

| Mode | When to use | Tradeoff |
|---|---|---|
| **Incremental** _(recommended)_ | One source at a time; review LLM output before proceeding | Higher quality steering; slower throughput |
| **Batch** | Multiple sources in one pass with less supervision | Faster; less control; suitable for well-understood domain sources you trust |

Karpathy's preference: incremental. The wiki builds a stronger thesis when you read and guide each synthesis.

---

## 6. Source Capture Workflows

### Web Articles — Obsidian Web Clipper
1. Install the **Obsidian Web Clipper** browser extension.
2. On any article, click the clipper → it converts the page to clean markdown.
3. Save to `raw/<topic>/YYYY-MM-DD-slug.md` with the provenance headers from [[references/raw-template]].
4. Fill in `> Version:` before closing — confirm with the page or ask the user if unclear.

### PDFs & Documents
- Save to `raw/<topic>/YYYY-MM-DD-slug.pdf` (or `.txt` if converted).
- Add a companion `raw/<topic>/YYYY-MM-DD-slug-provenance.md` with provenance headers.

### Transcripts & Podcasts
- Export or transcribe to `raw/<topic>/YYYY-MM-DD-slug.md`.
- Record the episode/show date as `Published:` and recording date as `Collected:`.

---

## 7. Image Handling
Images in clipped articles are useful — LLMs can view them separately to gain additional context after reading the text.

**Setup (one-time in Obsidian):**
1. Open Settings → Files and links → set **Attachment folder path** to `raw/assets`.
2. Open Settings → Hotkeys → search "Download" → bind **"Download attachments for current file"** to `Ctrl+Shift+D`.

**Workflow after clipping an article:**
1. Clip the article to `raw/<topic>/YYYY-MM-DD-slug.md` (images are initially URLs).
2. Open the file in Obsidian and press `Ctrl+Shift+D` — all images download to `raw/assets/`.
3. When ingesting: ask the LLM to read the text first, then view referenced images separately for additional context.

> **Note:** LLMs cannot read markdown with inline images in one pass — the text-then-images workflow works well enough at small scale.

---

## Related Notes
- [[llm-wiki-pattern]]: Overview of the Karpathy Wiki Pattern.
- [[karpathy-template]]: Exact formatting rules and self-verification checklist.
- [[core-ai-rules]]: Core safety and data lifecycle invariants.
