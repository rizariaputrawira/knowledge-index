# Knowledge Base Compiler Log

Append-only chronological record of all ingestions, updates, lints, and refactor operations.

> [!TIP] Quick audit — recent entries:
> `grep "^## \[" wiki/log.md | tail -10`

## [2026-09-18] bootstrap | Initialized clean Karpathy LLM Wiki repository structure.
## [2026-09-18] update | Formalized strict versioning invariant and 7-field frontmatter schema across compiler directives and templates; mandatory user prompt if version is absent from source (notes: [[karpathy-template]], [[references/article-template]]).
## [2026-09-18] ingest | no material: raw/README.md
## [2026-09-18] refactor | Implemented 18 improvements from Karpathy spec gap analysis: added check_frontmatter.py + lint_wiki.py scripts; added Query Workflow + Lint Workflow + cross-reference rule to AGENTS.md; unified log format; fixed version fields in karpathy-template + index; added Version header to raw-template; fixed heading violations in llm-wiki-pattern + new-page template; added best-practices §§5–7 (ingest modes, web clipper, image handling); expanded index.md to 7 domains; added log.md grep tip; added Dataview + Marp plugins; configured raw/assets attachment path; wrote raw/README.md; updated .gitignore for pycache.
## [2026-09-18] refactor | Applied ponytail audit simplifications across scripts: replaced frozen dataclass with NamedTuple in check_evidence.py, removed redundant strip_fences and manual dedup loops, inlined label formatting, pruned duplicate is_empty_value entries and dead path prefixes, deleted unused stem(), and optimized slug resolution to O(1) in lint_wiki.py (notes: [[admin-index]]).
