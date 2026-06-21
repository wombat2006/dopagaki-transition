# TO-BE: Glossary / Terminology Pipeline

Project:
ドパガキは模範生（**consumer**）

Status:
Draft — Technical（2026-06-21 更新 — platform 切り出し反映）

Related:
[TO-BE.md](TO-BE.md)
[glossary-pipeline/](glossary-pipeline/README.md)
[glossary-config.json](glossary-config.json)
[scripts/glossary_extractor.py](../scripts/glossary_extractor.py)
[scripts/README.md](../scripts/README.md)
[GLOSSARY.md](../GLOSSARY.md)

**Canonical 実装（共有）:** [term-prep-platform](https://github.com/wombat2006/term-prep-platform)  
**Consumer config（本 repo）:** `meta/glossary-config.json` · platform 側 mirror: `projects/dopagaki-transition/glossary-config.json`

---

## 修正・実装の順序（正）

方針決定 → 文書（TO-BE）→ コード。**Phase 番号どおり。飛ばさない。**

```text
[済] D-002 + RL  … MCP 方針確定 → platform に stub（T2.5-1）
[済] 文書         … 本 TO-BE を platform 移行後の現状に同期（2026-06-21）

Phase 0  … 出力・gitignore・config（dopagaki + platform 双方）  ← **済**
Phase 1  … scripts/glossary/ パッケージ化
Phase 2  … registry seed-first
Phase 2.5 … MCP client 連携・provider（platform 側。T2.5-2 以降）
Phase 3  … GLOSSARY 差分提案
Phase 4  … RAG（別 Epic）
```

| 順 | 内容 | 触る場所 | 状態 |
|---|---|---|---|
| 0 | TO-BE・DECISIONS を現状に同期 | dopagaki `meta/` | **済** |
| 1 | Phase 0 — 出力分割・config 拡張 | dopagaki `scripts/` + config；platform に追随 | **済**（platform extractor/config は手動同期） |
| 2 | Phase 1 — Core 分離 | 主に **platform**；dopagaki は薄い CLI または platform 参照 | pending |
| 3 | Phase 2 — registry | 両 repo config + 正典 seed | pending |
| 4 | Phase 2.5 — MCP 本実装 | **platform** `mcp/glossary-knowledge/` | stub のみ済 |
| 5 | dopagaki `mcp/` 削除 | 非 canonical コピー廃止 | **済** |

**原則:** 新規 Python/MCP の開発は **term-prep-platform**。dopagaki は corpus・GLOSSARY・TS/ADR・consumer config。

---

## リポジトリ役割

| 役割 | repo | 内容 |
|---|---|---|
| **Platform** | [term-prep-platform](https://github.com/wombat2006/term-prep-platform) | MCP、`glossary_extractor.py`、governance 正本、複数 PRJ 向け config |
| **Consumer** | dopagaki-transition（本 repo） | 原稿 corpus、`GLOSSARY.md`、TS/ADR、`meta/glossary-config.json` |
| **Deprecated mirror** | ~~dopagaki `mcp/`~~ | 切り出し前のコピー — **削除済**（2026-06-21） |

---

## 設計方針 — 入口は固定、ロジックは別立て

**`scripts/glossary_extractor.py` は当面そのまま使う。** CLI・`--check`・exit code・config パスは **他 PRJ 共通の安定インタフェース** として維持する。

中身のパイプラインは **別モジュールとして切り出し、段階的に育てる**。いまの単一 `.py` に RAG・registry・複合語を詰め込まない。

```text
scripts/glossary_extractor.py     ← 薄い CLI（安定。他 PRJ もこの入口）
        │
        ▼ import
scripts/glossary/                 ← ロジック本体（別立てで改修・バージョンアップ）
    morphology.py                 … fugashi + 外部辞書（必須）
    extract.py                    … corpus → raw terms
    registry.py                   … TS/ADR/GLOSSARY seed（閉世界）
    filter.py                     … 閾値・stop・seed-first
    rank.py                       … スコア・複合語（将来）
    writers.py                    … adopt/hold/reject 出力分割
    rag/                          … RAG 前処理（将来 Epic。今は未実装でよい）
```

| 層 | 方針 |
|---|---|
| **CLI** (`glossary_extractor.py`) | 引数・config 読込・exit code のみ。破壊的変更は避ける |
| **Core** (`scripts/glossary/`) | 抽出・filter・出力形式をここで改修。ユニットテスト対象 |
| **Config** (`meta/glossary-config.json`) | 閾値・corpus・出力パス。PRJ ごとに差し替え |
| **正典** (`GLOSSARY.md`, TS, ADR) | 人間採択。機械出力は提案まで |

**RAG・大規模 corpus は Core の `rag/` サブパッケージとして後付け。** 現 CLI を差し替えない。

---

## AS-IS（2026-06-21 — dopagaki consumer）

| 項目 | 現状 |
|---|---|
| 構成 | 単一 `glossary_extractor.py`（~500 行、CLI+全ロジック同居）— **platform にも同一ファイル** |
| 抽出 | fugashi + unidic-lite、名詞全量 + Markdown シグナル |
| 設定 | `meta/glossary-config.json` — `filter` / `output` / `knowledge_filter` 節（Phase 0 済） |
| 出力 | `meta/glossary-adopt.json` + `meta/glossary-hold.json`（Git 追跡）。reject は `emit_reject: false` で非出力 |
| 正典 | `GLOSSARY.md` Part II 拡充済み（人間採択） |
| MCP | **platform** に stub。本 repo `mcp/` は **削除済** |

### 規模感（Accepted 原稿 7 ファイルのみ）

| 指標 | 値 |
|---|---|
| ファイルサイズ | ~255 KB |
| candidates 総数 | 693 |
| adopt / hold / reject | 23 / 23 / **647** |
| reject 比率 | ~93% |

全 Manuscript + ADR + TS + Research Log を同パイプラインに載せると、**MB 級 JSON・reject 数千件** が Git 管理下に乗る見込み。

### 構造的限界（技術的負債）

| # | 限界 | 影響 |
|---|---|---|
| L1 | 開世界抽出が先、閉世界 seed が後 | ノイズ大量 |
| L2 | reject を Git 追跡 JSON に含める | 肥大化 |
| L3 | 語 surface のみ（span/chunk なし） | RAG 不可 |
| L4 | 複合語未統合 | 「注意」「経済」≠「注意経済」 |
| L5 | スコアリングが catalog 部分一致で過敏 | `TS` `ADR` 等が adopt に混入 |
| L6 | CLI とロジック同居 | 他 PRJ への移植・テストが困難 |

---

## 用途の分離

### 用途 A — 読者向け用語集（GLOSSARY.md）

- 語数 **20–40** 程度
- 一行定義 + 誤解 + TS/ADR リンク
- **人間採択が正典**

### 用途 B — RAG / 専門用語辞典 PRJ

- 用語 ↔ 出典 ↔ chunk 索引
- embedding は別レイヤ
- 生成物は `build/` または DB（Git 外）

**同一 JSON・同一 writer に混ぜない。** 用途 A は `writers.adopt`、用途 B は `writers.rag`（将来）。

---

## 技術的改修一覧

優先度順。**Phase 0–1 は CLI インタフェースを変えずに Core 分離と出力整理のみ。**

### Phase 0 — 出力・リポジトリ衛生（Immediate）

| ID | 改修 | 対象 | 完了条件 | 状態 |
|---|---|---|---|---|
| T0-1 | **reject 非出力** — `filter.emit_reject: false` デフォルト | `filter.py`, config | reject が Git に載らない | `[x]` |
| T0-2 | **出力分割** — adopt / hold / reject を別ファイル | `writers.py`, config | 3 パス設定可能 | `[x]` |
| T0-3 | **`glossary-candidates.json` 廃止** — adopt+hold の slim 版に置換 | config, docs | 単一巨大 JSON なし | `[x]` |
| T0-4 | **`.gitignore`** — `build/glossary/`, `build/rag/` | `.gitignore` | 生成物が commit されない | `[x]` |
| T0-5 | **生成物の正典位置づけ** — docs に「adopt のみ追跡」と明記 | README, scripts/README | 誤コミット防止 | `[x]` |

### Phase 1 — モジュール分離（Immediate〜Mid）

**主 repo:** [term-prep-platform](https://github.com/wombat2006/term-prep-platform)。dopagaki は Phase 1 完了まで mirror を保持。

| ID | 改修 | 対象 | 完了条件 | 状態 |
|---|---|---|---|---|
| T1-1 | **`scripts/glossary/` パッケージ化** — 現 `glossary_extractor.py` から logic を移動 | platform 新 pkg + 薄い CLI | CLI 引数・exit code 不変 | `[ ]` |
| T1-2 | **`morphology.py`** — fugashi + 辞書解決を独立 | glossary/morphology.py | `--check` が pkg 経由で動作 | `[ ]` |
| T1-3 | **`writers.py`** — JSON/JSONL 出力を writer 戦略化 | glossary/writers.py | adopt/hold/reject 切替 | `[ ]` |
| T1-4 | **config スキーマ** — `filter`, `output` 節を schema に反映 | meta/schemas/ | 設定ミスを早期検出 | `[ ]` |

### Phase 2 — 縛り強化（Mid — Glossary 用途）

| ID | 改修 | 対象 | 完了条件 |
|---|---|---|---|
| T2-1 | **`registry.py`** — TS/ADR/GLOSSARY から seed 生成 | meta/glossary-registry.json | 正典語 ID 一覧 |
| T2-2 | **seed-first 抽出** — registry 語の出現を優先集計 | filter.py | 開世界全量より先に seed |
| T2-3 | **`min_morph_freq` / `min_chapters`** — 低頻度語を pre-score 除外 | filter.py, config | hold/adopt 件数が上限内 |
| T2-4 | **`max_candidates_output`** — 出力件数キャップ | filter.py | adopt+hold ≤ N |
| T2-5 | **catalog マッチ修正** — 部分一致による `TS`/`ADR` 誤 adopt 解消 | rank.py | 短語・メタ語が adopt に入らない |
| T2-6 | **複合語マージ** — seed 最長一致で「注意経済」等を統合 | rank.py | 分割候補が減る |
| T2-7 | **英日ペア統合** — `Attention Scarcity` ↔ 注意の有限性 | rank.py | 同一 entry に alias |

### Phase 2.5 — Knowledge Filter MCP（Mid — D-002）

registry + rule filter **の後**、rank **の前**。Phase 0–1 完了後に **client 連携**（T2.5-2 以降）。

**実装 repo:** [term-prep-platform](https://github.com/wombat2006/term-prep-platform)（dopagaki `mcp/` は非 canonical）

| ID | 改修 | 対象 | 完了条件 | 状態 |
|---|---|---|---|---|
| T2.5-1 | **MCP server stub** — `classify_term`, `classify_batch`, NullProvider | platform `mcp/glossary-knowledge/` | Cursor stdio 接続 | `[x]` |
| T2.5-2 | **MCP client** — glossary Core から batch 呼び出し | platform `glossary/knowledge_filter.py` | `enabled: false` で無害 | `[ ]` |
| T2.5-3 | **cache layer** — SQLite、corpus hash 付き | platform MCP | 再実行で API 再呼び出し抑制 | `[ ]` |
| T2.5-4 | **第一 provider** — K-003 or K-006（DECISION 待ち） | platform MCP adapter | general/domain 判定 | `[ ]` |
| T2.5-5 | **判定ログ** — `build/glossary/knowledge-log.jsonl` | platform MCP + writers | C-0003 Traceability | `[ ]` |

仕様: platform [meta/glossary-pipeline/mcp/README.md](https://github.com/wombat2006/term-prep-platform/blob/main/meta/glossary-pipeline/mcp/README.md)。Research Log: [RL-20260621](../research-log/RL-20260621-knowledge-filter-mcp.md)（closed）。

---

### Phase 3 — GLOSSARY 連携（Mid）

| ID | 改修 | 対象 | 完了条件 | 状態 |
|---|---|---|---|---|
| T3-1 | **adopt.json → GLOSSARY 差分提案** | 新 script or subcommand | 人間が反映する材料 | `[ ]` |
| T3-2 | **registry ↔ GLOSSARY 双方向** | registry.py | 用語集更新が seed に伝播 | `[ ]` |

---

### Phase 4 — RAG 前処理（Long — 別 Epic）

| ID | 改修 | 対象 | 完了条件 | 状態 |
|---|---|---|---|---|
| T4-1 | **term ID 安定化** — `term:attention-capacity` | glossary/rag/ids.py | PRJ 横断で同一 ID | `[ ]` |
| T4-2 | **span 抽出** — file + line + 前後文 | glossary/rag/spans.py | 語ごとに出典スニペット | `[ ]` |
| T4-3 | **chunk mapper** — 章/見出し/chunk 単位への逆引き | glossary/rag/chunks.py | RAG chunk と term がリンク | `[ ]` |
| T4-4 | **term-index** — SQLite or JSONL | build/rag/ | 検索可能索引 | `[ ]` |
| T4-5 | **incremental rebuild** — corpus 差分のみ再 index | glossary/rag/ | 全量再生成不要 | `[ ]` |
| T4-6 | **shard 出力** — 章別 JSONL | build/glossary/shards/ | 大 corpus を分割処理 | `[ ]` |

---

## TO-BE: 出力レイアウト

| ファイル | Git | 内容 |
|---|---|---|
| `meta/glossary-registry.json` | ✅ | TS/ADR/GLOSSARY 由来の正典語 |
| `meta/glossary-adopt.json` | ✅ | 採択候補のみ（数十件） |
| `meta/glossary-hold.json` | ⚠️ 任意 | 保留 |
| `build/glossary/reject.jsonl` | ❌ | reject（ローカル/CI artifact） |
| `build/glossary/shards/*.jsonl` | ❌ | 章別 raw（将来） |
| `build/rag/term-index.sqlite` | ❌ | RAG（将来） |

~~`meta/glossary-candidates.json`~~ → **廃止**（T0-3）。

---

## TO-BE: glossary-config 拡張（Phase 0 で dopagaki config に反映予定）

**現状:** `meta/glossary-config.json` に反映済み（Phase 0 完了）。

```json
{
  "morphology": {
    "backend": "fugashi",
    "dictionary": "unidic-lite",
    "required": true
  },
  "filter": {
    "seed_first": true,
    "min_morph_freq": 3,
    "min_chapters": 2,
    "max_candidates_output": 100,
    "emit_reject": false
  },
  "knowledge_filter": {
    "enabled": false,
    "mcp_server": "term-prep-platform/mcp/glossary-knowledge",
    "transport": "stdio",
    "domain": "attention-economics",
    "batch_size": 50
  },
  "output": {
    "registry": "meta/glossary-registry.json",
    "adopt": "meta/glossary-adopt.json",
    "hold": "meta/glossary-hold.json",
    "reject": "build/glossary/reject.jsonl"
  }
}
```

---

## パイプライン TO-BE（Core 内部）

```text
[registry]  TS / ADR / GLOSSARY → seed（閉世界）
     ↓
[extract]   fugashi + 辞書 — corpus → raw（shard 可）
     ↓
[filter]    min_freq, stop, seed-first, valid_term
     ↓
[knowledge] MCP classify_batch（Phase 2.5, platform, optional）
     ↓
[rank]      スコア, 複合語, 英日ペア
     ↓
[writers]   adopt / hold / reject（分離）
     ├─→ GLOSSARY.md（人間）
     └─→ rag/（将来）
```

---

## 実装ロードマップ

| Phase | 内容 | 主 repo | CLI 変更 |
|---|---|---|---|
| **0** | 出力分割・gitignore・config 拡張 | dopagaki + platform 追随 | なし |
| **1** | `scripts/glossary/` 分離 | **platform** | なし |
| **2** | registry + filter 強化 | 両方 config | なし |
| **2.5** | Knowledge Filter MCP client/provider | **platform** | なし |
| **3** | GLOSSARY 差分提案 | dopagaki | `--diff-glossary` 追加可 |
| **4** | RAG subpackage | **platform** | `--rag-index` 追加可 |

**原則:** `python scripts/glossary_extractor.py` は Phase 0–2 まで **引数・exit code 不変**。

---

## Open Questions

1. **registry 正典** — TS のみ vs TS+ADR+GLOSSARY のマージルール
2. **未知語昇格** — 開世界候補を registry に入れる ADR / Research Log フロー
3. **RAG 配置** — 本 repo `build/rag/` vs 専門用語辞典 PRJ
4. **UniDic 標準** — unidic-lite（pip）vs full UniDic（他 PRJ 共通）
5. ~~**Core の配布**~~ — **解決:** [term-prep-platform](https://github.com/wombat2006/term-prep-platform) が canonical。pip 化は platform 側 Open
6. **Knowledge Filter 第一 provider** — K-003 / K-006 / K-008（[RL-20260621](../research-log/RL-20260621-knowledge-filter-mcp.md)）

---

## 判定

| 問い | 答え |
|---|---|
| 実装の canonical repo | **term-prep-platform** |
| dopagaki の役割 | **consumer** — corpus・GLOSSARY・config |
| 今の py を捨てるか | Phase 1 まで dopagaki に残す → 以降 platform 参照 |
| RAG は今やるか | **しない** — Phase 4 |
| 今すぐやる改修 | **Phase 1**（Core 分離 — platform） |
| dopagaki `mcp/` | **削除済** — platform が正本 |
