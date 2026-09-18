# 🧠 Knowledge Index (Karpathy LLM Wiki)

A persistent, compounding personal knowledge base built on the **Andrej Karpathy LLM Wiki Pattern**.

Instead of performing query-time retrieval against unorganized document dumps, an AI assistant continuously compiles, interlinks, and maintains a structured, dense Markdown wiki grounded in immutable primary sources.

---

## 📂 Repository Architecture

```
.
├── AGENTS.md                 # Compiler directives & AI operating rules
├── README.md                 # Knowledge base architecture overview
│
├── 🧠 wiki/                   # Compiled Knowledge Base (Dense Markdown Network)
│   ├── index.md              # Master domain navigation hub
│   ├── log.md                # Chronological append-only compiler operations ledger
│   └── admin/                # Operating rules, templates, and pattern specifications
│       ├── admin-index.md    # Index of administrative notes & templates
│       ├── meta/             # Pattern definitions (LLM Wiki, Karpathy standard)
│       └── references/       # Canonical markdown templates (article, raw, index, archive)
│
├── 📥 raw/                    # Immutable Primary Sources (Grounding Tier)
│   └── .gitkeep              # Drop-zone for raw papers, source dumps, and transcripts
│
└── ⚡ scripts/                # Automated verification tooling
    └── check_evidence.py     # Mechanical evidence check enforcing the Grounding Invariant
```

---

## 🧭 Core Operating Principles

1. **The Grounding Invariant**: Every load-bearing factual claim in `wiki/` (numbers, metrics, dates, direct quotes) must exist verbatim in an immutable source file under `raw/`.
2. **4-Stage Ingestion Pipeline**:
   - **Fetch**: Store raw document in `raw/<topic>/YYYY-MM-DD-slug.md` (or `.pdf`/`.txt`) with provenance metadata.
   - **Triage**: Search `wiki/` for existing related topics to determine whether to create new notes or merge into existing notes.
   - **Compile**: Synthesize dense, structured markdown notes following `[[karpathy-template]]` with YAML frontmatter and `[[wikilinks]]`.
   - **Log**: Append an entry in `wiki/log.md` recording the ingest operation.
3. **Compounding Structure**: High-density notes with cross-references, comparison tables, and code snippets. No narrative fluff.

---

## 🛠️ Verification Tooling

To mechanically audit the wiki for factual fidelity and verify that all claims are grounded in `raw/`:

```bash
python3 scripts/check_evidence.py .
```
