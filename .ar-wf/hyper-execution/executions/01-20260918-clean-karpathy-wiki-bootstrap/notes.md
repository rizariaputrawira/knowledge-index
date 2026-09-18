# Notes — 01-20260918-clean-karpathy-wiki-bootstrap
_Append-only. Never overwrite. Sections: ## Decisions, ## Issues, ## Learnings, ## Blockers_

## Decisions
- Executing clean-room transplant from first principles instead of copy-and-delete to guarantee zero proprietary data leaks.
- Purging .obsidian/workspace.json and termy Windows binary from vault configuration.
- Single root AGENTS.md as the only instruction file.

## Issues

## Learnings
- Initialized local git configuration with user name and email.
- Created root structure: raw/ (with .gitkeep), wiki/, scripts/, .editorconfig, .gitignore, README.md.
- Authored clean general Karpathy AGENTS.md eliminating all project-specific terminology, hardcoded corporate paths, and Excel/Postman rules. All 6 mandatory frontmatter fields and Grounding Invariant formalized.
- Created wiki/index.md, wiki/log.md, and wiki/admin/admin-index.md with reciprocal navigation links and starter domain sections.
- Transplanted and sanitized 4 canonical templates (article, raw, index, archive) and 4 meta/rules specifications (llm-wiki-pattern, karpathy-template, best-practices, core-ai-rules). Replaced word 'fabricate' with 'invent' to avoid accidental false-positive substring hits on 'bri'. Verified 0 forbidden tokens.
- Hardened scripts/check_evidence.py: exempts wiki/admin/, supports YAML frontmatter sources, supports root-relative (raw/...) and article-relative (../../raw/...) link resolution, strips legacy BRI skips, and returns standard exit code 0 on clean runs and 1 on error. Verified with python3 scripts/check_evidence.py (0 suspects, 0 errors, 0 unreferenced raws).
- Configured clean Obsidian vault: ported app.json, appearance.json, graph.json, core-plugins.json, and templates/new-page.md. Selectively copied 5 plugins (excalidraw, git, kanban, omnisearch, table-editor). Purged termy Windows binary and omitted workspace.json to eliminate phantom locks and UI crashes.
- Completed Task 7 Final Verification Gate: 0 residual project tokens, 0 path leaks, 0 evidence errors, and clean git working tree.

## Blockers
