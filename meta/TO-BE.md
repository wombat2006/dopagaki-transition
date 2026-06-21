# TO-BE.md

Project:
ドパガキは模範生

Repository:
dopagaki-transition

Status:
Draft

## Immediate Goals

- Dual-audience structure (Reader / Researcher entry points)
- Part I Ch 1 Accepted manuscript
- Part II Ch 4–5, 7.1–7.2, Ch 8 Accepted manuscripts
- Split ADR catalog into individual ADR files
- Split TS catalog into individual TS files

## Planned ADR

- ADR-P001 Surplus Attention Value
- ADR-P002 Meaning Economy
- ADR-P003 Civilizational Transition

## Planned TS

- TS-0007 Meaning Economy
- TS-0008 Religion Layer
- TS-0009 Civilizational Transition
- TS-0010 AI Civilization Model

## Open Questions

- Part IV 宗教層: Attention Scarcity（Ch 9）から接続する宗教学的・配分規範的論じ方の強化
- Attention ≠ ∞（母集団制約）を Meaning Allocation / Religion as Infrastructure へ一貫して接続

## Technical TO-BE

- [TO-BE-GLOSSARY-PIPELINE.md](TO-BE-GLOSSARY-PIPELINE.md) — 用語抽出パイプライン（Phase ロードマップ）
- [glossary-pipeline/](glossary-pipeline/README.md) — **手段案の列記・採択ログ**（governance の portable コピー）
- **Canonical 実装:** [term-prep-platform](https://github.com/wombat2006/term-prep-platform) — MCP・`glossary_extractor.py`・governance 正本。本 repo は **consumer**（corpus・GLOSSARY・`meta/glossary-config.json`）
