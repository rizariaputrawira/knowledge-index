# Clean Karpathy Wiki Bootstrap Plan

**Plan ID:** `01-20260918-clean-karpathy-wiki-bootstrap`  
**Target Workspace:** `/mnt/d/Users/aria/workspaces/personal/knowledge-index`  
**Source Reference:** `/mnt/d/Users/aria/workspaces/bri/sfd-implementation-project`  
**Status:** READY FOR EXECUTION (Waiting for User Command)  
**Execution Command:** `/ar-hyperexecution .ar-wf/planning/01-20260918-clean-karpathy-wiki-bootstrap.md`  

---

## 🎯 Objective & Architecture

Transform `/mnt/d/Users/aria/workspaces/personal/knowledge-index` into a pristine, standalone, and completely unpolluted **Karpathy LLM Knowledge Wiki**. 

The architecture strictly adheres to Andrej Karpathy's compounding plain-text knowledge system:
1. **`raw/` (Primary Ingestion Tier)**: Immutable, write-once primary documents (PDFs, transcripts, articles, bookmarks) providing empirical grounding.
2. **`wiki/` (Compiled Knowledge Tier)**: Dense, interlinked, structured markdown files synthesized and continuously maintained by AI agents using Obsidian `[[wikilinks]]`.
3. **`AGENTS.md` & `wiki/admin/` (Compiler Rules & Schemas)**: Ingestion directives, frontmatter validation schemas, templates, and operational logs.
4. **Tooling & IDE**: Deterministic, stdlib-only `check_evidence.py` and a sanitized `.obsidian/` workspace free of binary blobs, dead file locks, or foreign project history.

### Zero-Tolerance Sanitization Boundary
The following artifacts from the source repository must be **completely excluded and never copied**:
- ❌ `wiki/sfd-official/`, `wiki/sfm-official/`, `wiki/client-sfm/`, `wiki/client-sfd/`, `wiki/project-management/`
- ❌ `raw/sfd-official/`, `raw/sfm-official/`, `raw/client-sfm/`, `raw/client-sfd/`, `raw/project-management/`
- ❌ `implementation/` (101MB of SAS rules, schemas, UAT test payloads, docs)
- ❌ `.source-code/` (144MB of Java/Groovy codebases)
- ❌ `pseudo-code/` and `.pseudo-code/`
- ❌ `scripts/xls_extract/` (95MB of Node.js mapping scripts, postman collections, `node_modules`, `venv`)
- ❌ `.obsidian/workspace.json`, `.obsidian/plugins/termy/` (hardcoded paths, 40MB Windows binary, stale lockfiles)
- ❌ `wiki/admin/core-system-rules/` (`failures-log.md`, `memory-log.md`, `agent-excel-ingestion.md`) and legacy `log.md`
- ❌ Split-brain `.agents/AGENTS.md`

---

## 📋 Task Checklist

- [x] **Task 1: Workspace Initialization & Core Directory Scaffolding**
  - Initialize git repository in `/mnt/d/Users/aria/workspaces/personal/knowledge-index` (`git init`).
  - Create directory skeleton:
    - `raw/` (with `.gitkeep`)
    - `wiki/`
    - `wiki/admin/`
    - `wiki/admin/references/`
    - `wiki/admin/meta/`
    - `scripts/`
  - Create standard `.gitignore`:
    - Ignore `.obsidian/workspace.json`, `.obsidian/plugins/omnisearch/cache/`, `.DS_Store`, `Thumbs.db`, `.env`, temporary editor files (`~$*.xlsx`, `*.tmp`).
  - Create standard `.editorconfig` (UTF-8, LF line endings, 2-space indentation for yaml/json, trim trailing whitespace).
  - Create root `README.md` introducing the personal Karpathy Knowledge Index, repository layout, and usage workflow.
  - **Verification:** Run `git status` and `find . -maxdepth 3` to verify clean directory layout.

- [x] **Task 2: Authoring the Root General Karpathy `AGENTS.md`**
  - Create a single source of truth `AGENTS.md` in the workspace root, eliminating the split-brain `.agents/AGENTS.md` antipattern.
  - Formulate core directives:
    1. **Identity & Role**: General Knowledge Assistant for curating, synthesizing, and compounding personal knowledge.
    2. **Grounding Invariant**: All factual claims (numbers, dates, direct quotes) must exist verbatim in immutable `raw/` sources.
    3. **4-Stage Ingestion Pipeline**: Fetch (`raw/`) $\rightarrow$ Triage $\rightarrow$ Compile (`wiki/`) $\rightarrow$ Log (`wiki/log.md`).
    4. **Dense Karpathy Formatting**: High-density markdown, structured comparison tables, code blocks, Mermaid diagrams, zero narrative fluff, no "Executive Summary" or "Context" filler headings.
    5. **Frontmatter Standard**: Exactly 6 mandatory fields: `title`, `tags`, `updated` (YYYY-MM-DD), `sources` (paths to `raw/`), `summary`, `aliases`.
    6. **Reciprocal Navigation**: Every compiled leaf note must link upward to its topical domain index, and the domain index must record the note with summary and date.
    7. **Single Log Invariant**: Chronological operations logged strictly to `wiki/log.md` using format `## [YYYY-MM-DD] action | Description`.
  - **Verification:** Check `AGENTS.md` contains 0 mentions of `sfd`, `sfm`, `bri`, `sas`, `boss`, `viya`, `postman`, `excel`, or hardcoded foreign workspace paths.

- [x] **Task 3: Scaffolding Clean Root Indices & Master Logs**
  - Author `wiki/index.md`:
    - Clean top-level navigation hub with starter index sections (e.g. `Computer Science & Systems`, `Engineering & Architecture`, `AI & Machine Learning`, `Reference & Governance`).
    - Link to [[admin-index]] for administration, templates, and patterns.
  - Author `wiki/log.md`:
    - Clean chronological ledger initialized with the bootstrap entry:
      `## [2026-09-18] bootstrap | Initialized clean Karpathy LLM Wiki repository structure.`
  - Author `wiki/admin/admin-index.md`:
    - Structured index linking strictly to active administrative notes:
      - [[core-ai-rules]]
      - [[llm-wiki-pattern]]
      - [[karpathy-template]]
      - [[best-practices]]
      - [[references/article-template]]
      - [[references/raw-template]]
      - [[references/index-template]]
      - [[references/archive-template]]
  - **Verification:** Verify reciprocal wikilinks between `wiki/index.md` and `wiki/admin/admin-index.md`.

- [x] **Task 4: Transplanting & Sanitizing Admin Templates and Meta Specifications**
  - Transplant and sanitize templates from source:
    - `wiki/admin/references/article-template.md`: Update to reconcile frontmatter schema with blockquote provenance (`> Raw:`, `> Sources:`, `> Updated:`).
    - `wiki/admin/references/raw-template.md`: Clean provenance headers (`> Source:`, `> Collected:`, `> Published:`).
    - `wiki/admin/references/index-template.md`: Clean markdown table catalog layout.
    - `wiki/admin/references/archive-template.md`: Clean point-in-time snapshot template.
  - Transplant and sanitize meta specifications:
    - `wiki/admin/meta/llm-wiki-pattern.md`: The canonical 3-layer Karpathy pattern documentation (immutable raw, compiled wiki, agent schema).
    - `wiki/admin/meta/karpathy-template.md`: Cleaned of legacy SAS source path examples and enterprise return tables.
    - `wiki/admin/meta/best-practices.md`: Cleaned of SAS VDMML / Postgres schema references.
    - `wiki/admin/core-system-rules/core-ai-rules.md`: General knowledge preservation, data lifecycle, and redaction rules (purged of CSV/SFM naming rules).
  - **Verification:** Run `grep -rnIE "sfd|sfm|bri|sas|boss|viya|v2026|TechData" wiki/admin/` to confirm zero residual terms.

- [x] **Task 5: Hardening and Porting `scripts/check_evidence.py`**
  - Copy `scripts/check_evidence.py` from `/mnt/d/Users/aria/workspaces/bri/sfd-implementation-project/scripts/check_evidence.py`.
  - Apply 4 critical architectural fixes identified in the adversarial audit:
    1. **Exit Code Semantics**: Update script exit logic so `sys.exit(0)` is returned on zero errors, and `sys.exit(1)` is returned if evidence errors or unreferenced raw files are found (enabling automated CI/CD verification).
    2. **Admin Path Exemption**: Update `SKIP_FILES` or path filtering so files in `wiki/admin/` (templates, meta rules) are recognized as administrative infrastructure and not erroneously flagged for lacking `> Raw:` fields.
    3. **Frontmatter Ingestion**: Add parser support for YAML frontmatter `sources: ["raw/..."]` alongside blockquote `> Raw:` headers to eliminate format-conflict errors.
    4. **Purge Legacy Skips**: Remove hardcoded BRI filenames (`ai-core-index.md`, `ai-brain-index.md`) from `SKIP_FILES`.
  - Make script executable (`chmod +x scripts/check_evidence.py`).
  - **Verification:** Execute `python3 scripts/check_evidence.py .` and verify 0 fidelity suspects, 0 evidence errors, 0 unreferenced raw files, and exit status code 0.

- [x] **Task 6: Obsidian Vault Configuration & Plugin Sanitization**
  - Copy `.obsidian` configurations selectively:
    - Copy `app.json`, `appearance.json`, `graph.json`, `core-plugins.json`.
    - Clean `app.json`: remove hardcoded banking file exclusions (`CLAUDE.md`, `SFD_*.xlsx`, `.planning/`, etc.), keep generic system ignores.
    - Copy `.obsidian/templates/new-page.md`.
  - Copy safe editor plugins from `.obsidian/plugins/`:
    - `obsidian-excalidraw-plugin/`
    - `obsidian-kanban/`
    - `table-editor-obsidian/`
    - `omnisearch/` (strictly exclude any pre-existing cache files)
    - `obsidian-git/`
  - Sanitize plugin registry `.obsidian/community-plugins.json`:
    - Remove `termy` from the enabled plugins list.
  - Strictly **DO NOT COPY**:
    - `.obsidian/workspace.json` (prevents 47 broken file references, excel locks, and missing dock panels).
    - `.obsidian/plugins/termy/` (prevents importing 40MB Windows binary `termy-server-win32-x64.exe` and hardcoded `D:/Users/aria/workspaces/bri/...` paths).
  - **Verification:** Inspect `.obsidian/` to ensure no `workspace.json` exists, no `termy` directory exists, and `community-plugins.json` is valid JSON.

- [x] **Task 7: Final Comprehensive Verification & Integrity Gate**
  - Run **Residual String Scan**:
    ```bash
    grep -rnIE "sfd|sfm|bri|sas|boss|viya" .
    ```
    Confirm zero matches across all committed files.
  - Run **Path Leakage Scan**:
    ```bash
    grep -rnIE "/mnt/d/Users/aria/workspaces/bri" .
    ```
    Confirm zero matches across all committed files.
  - Run **Mechanical Evidence Audit**:
    ```bash
    python3 scripts/check_evidence.py .
    ```
    Confirm 0 errors, 0 suspects, exit code 0.
  - Run **Git Cleanliness Check**:
    ```bash
    git status
    ```
    Confirm all initial assets are tracked and clean.
  - Commit initial pristine state:
    `git add . && git commit -m "feat(wiki): initialize clean Karpathy LLM wiki scaffolding"`

---

## 🛡️ Risk Assessment & Mitigation Matrix

| Risk | Likelihood | Impact | Adversarial Mitigation |
|---|---|---|---|
| **Confidential / Proprietary Data Leak** | High (if bulk copied) | Severe | Clean-room transplant; zero bulk copy of `wiki/`, `raw/`, or `implementation/`; regex scan gate before commit. |
| **Obsidian UI Crash / Modal Errors** | High | Medium | Nuke `workspace.json`; remove `termy` binary plugin; initialize `git init` upfront so `obsidian-git` launches cleanly. |
| **Evidence Checker Rejection on Day 1** | High | High | Patch `check_evidence.py` to exempt `wiki/admin/` templates and support YAML `sources:` frontmatter; use `.gitkeep` instead of `.md` in `raw/`. |
| **Split-Brain Rule Desynchronization** | Medium | Medium | Single root `AGENTS.md`; omit `.agents/AGENTS.md` completely. |
| **Non-Deterministic Wikilink Resolution** | Medium | Medium | Enforce globally unique kebab-case slugs for all compiled articles. |
