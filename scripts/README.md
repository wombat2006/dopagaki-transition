# Scripts

Project:
ドパガキは模範生（**consumer**）

Reusable tooling for this repository and sibling terminology / research projects.

**Canonical 実装:** [term-prep-platform](https://github.com/wombat2006/term-prep-platform) — 新規開発は platform 側。本 repo の `glossary_extractor.py` は Phase 1 まで mirror。

---

## Setup

```bash
python3 -m pip install -r requirements-dev.txt
```

**System dependency:** MeCab shared library (`libmecab`).

| OS | Command |
|---|---|
| Debian/Ubuntu | `sudo apt install mecab libmecab-dev` |
| AlmaLinux / RHEL | `sudo dnf install mecab`（`mecab-devel` は不要） |
| macOS | `brew install mecab` |

**Dictionary (required, pip):** `unidic-lite` — bundled with `requirements-dev.txt`.

Full UniDic (optional, other projects):

```bash
python3 -m pip install unidic
python3 -m unidic download
# set meta/glossary-config.json → morphology.dictionary: "unidic"
```

---

## glossary_extractor.py

**Purpose:** Extract glossary candidates from Markdown corpora using **fugashi + external dictionary** (mandatory).

**Design:** Config-driven (`meta/glossary-config.json`). Governance（問題・手段案）は [meta/glossary-pipeline/](../meta/glossary-pipeline/README.md)。方向性は [TO-BE-GLOSSARY-PIPELINE.md](../meta/TO-BE-GLOSSARY-PIPELINE.md).

```bash
# Verify fugashi + dictionary
python3 scripts/glossary_extractor.py --check

# Generate adopt + hold (reject omitted when filter.emit_reject is false)
python3 scripts/glossary_extractor.py
```

Output: `meta/glossary-adopt.json` and `meta/glossary-hold.json` (Git-tracked). Reject rows go to `build/glossary/reject.jsonl` only when `filter.emit_reject: true`.

Output: scored candidates (`adopt` / `hold` / `reject`). Human curation → `GLOSSARY.md`.

**Morphology policy:** No silent fallback. If fugashi or dictionary is missing, exit code `2`.

**MCP（Knowledge Filter）:** [term-prep-platform/mcp/glossary-knowledge](https://github.com/wombat2006/term-prep-platform/tree/main/mcp/glossary-knowledge)

---

## check-locale.py

**Purpose:** Validate text files against [meta/locale-policy.json](../meta/locale-policy.json).

```bash
python3 scripts/check-locale.py
```

---

## File roles

| File | Role |
|---|---|
| `scripts/glossary_extractor.py` | Extraction CLI（platform と同期。Phase 1 以降 platform 参照） |
| `meta/glossary-config.json` | Corpus paths, scoring, manual adopt/reject |
| `meta/glossary-candidates.json` | **廃止** — adopt/hold に分割済 |
| `meta/glossary-adopt.json` | 採択候補（Git 追跡） |
| `meta/glossary-hold.json` | 保留候補（Git 追跡） |
| `GLOSSARY.md` | Reader-facing curated glossary (canonical for readers) |
