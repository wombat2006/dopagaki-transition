# Scripts

Project:
ドパガキは模範生

Reusable tooling for this repository and sibling terminology / research projects.

---

## Setup

```bash
python3 -m pip install -r requirements-dev.txt
```

**System dependency:** MeCab shared library (`libmecab`).

| OS | Command |
|---|---|
| Debian/Ubuntu | `sudo apt install mecab libmecab-dev` |
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

**Design:** Config-driven (`meta/glossary-config.json`). Copy CLI + [`meta/glossary-pipeline/`](../meta/glossary-pipeline/README.md) to other repos for problem/option tracking.

**Governance:** 手段の検討・採択は [meta/glossary-pipeline/OPTIONS.md](../meta/glossary-pipeline/OPTIONS.md) / [DECISIONS.md](../meta/glossary-pipeline/DECISIONS.md). 方向性は [TO-BE-GLOSSARY-PIPELINE.md](../meta/TO-BE-GLOSSARY-PIPELINE.md).

```bash
# Verify fugashi + dictionary
python3 scripts/glossary_extractor.py --check

# Generate meta/glossary-candidates.json
python3 scripts/glossary_extractor.py
```

Output: scored candidates (`adopt` / `hold` / `reject`). Human curation → `GLOSSARY.md`.

**Morphology policy:** No silent fallback. If fugashi or dictionary is missing, exit code `2`.

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
| `scripts/glossary_extractor.py` | Shared extraction engine (importable) |
| `meta/glossary-config.json` | Corpus paths, scoring, manual adopt/reject |
| `meta/glossary-candidates.json` | Generated candidate list (not canonical) |
| `GLOSSARY.md` | Reader-facing curated glossary (canonical for readers) |
