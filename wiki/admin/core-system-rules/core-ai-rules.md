---
title: "Core AI Rules & Invariants"
tags: [admin, rules, core]
updated: 2026-09-18
sources: []
summary: "Foundational rules of engagement, data preservation, and security invariants for AI agents."
aliases: ["core-ai-rules"]
---

# Core AI Rules & Invariants

Up: [[admin-index]]

---

## 🛡️ Rules of Engagement

### 1. 💾 Data Lifecycle & Preservation
- **Preservation First:** Never permanently delete compiled research, notes, or historical documentation.
- **Archiving Protocol:** Move deprecated or outdated notes to an `archive/` directory using [[references/archive-template]].
- **Markdown Static Naming:** Never append version suffixes to `.md` filenames (e.g., avoid `note-v2.0.md`) as this permanently breaks Obsidian `[[wikilinks]]`. Keep filenames static (`note.md`) and bump the `updated:` field inside YAML frontmatter.
- **Atomic Two-Way Linking:** Whenever authoring or modifying a note, simultaneously ensure its parent domain catalog or [[index]] links to it.

### 2. ⚠️ Credential & Secret Protection
- **Zero Secrets in Wiki:** Never store, commit, or log API keys, tokens, SSH credentials, private certificates, or personally identifiable information (PII).
- **Masking:** If example payloads or logs contain credentials or tokens, redact them strictly (`<TOKEN_REDACTED>`, `user@example.com`).

### 3. ⚙️ Execution & Verification Rigor
- **Evidence-Bound Claims:** Never claim a note is compiled, a test passes, or a file is verified without running the verification command and inspecting output.
- **Tooling Determinism:** When writing helper automation scripts in `scripts/`, use pure Python standard library to ensure portability across Linux, WSL, and CI environments without external package dependencies.
