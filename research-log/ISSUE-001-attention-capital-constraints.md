# ISSUE-001: Attention が制約される要因の欠如

Status:
Merged

Source:
https://github.com/wombat2006/dopagaki-transition/issues/1

Opened:
2026-06-21

Related:
ADR-0001 Attention Scarcity
TS-0004 Attention Capitalism
Manuscript: [ch09-attention-scarcity.md](../manuscript/part02/ch09-attention-scarcity.md)
Manuscript: [ch07-digital-capital-theory.md](../manuscript/part02/ch07-digital-capital-theory.md) §7.3 Participatory Resource

Draft:
[drafts/ch09-9-2-economic-access-scarcity.md](drafts/ch09-9-2-economic-access-scarcity.md)

---

## Issue 要約

現行定義では Attention の制約要因が **人口・時間・認知帯域幅** の3つのみ。

Issue 提起者の指摘: **資本（お金）** も制約要因として盛り込むべき。

---

## 素案比較

現行式（Layer 1）が答える問い:

```text
Attention Capacity <= Population × Time × Cognitive Bandwidth
```

**注意という資源の潜在総量（Ontological Scarcity）** の上限。Attention Inflation 棄却（`Attention ≠ ∞`）の根拠。

| 案 | 概要 | 棄却 / 採択 |
|---|---|---|
| **A** | ADR-0001 の式は**不変**。資本は Ch 6–7（Capture 競争）の領域。Ch 9 に「Capacity ≠ Capture」の**短い段落のみ**追記 | **棄却** |
| **B** | 資本を第4因子として Capacity 式に追加: `Attention Captured <= Population × Time × Cognitive Bandwidth × g(Capital)` | **棄却** |
| **C** | **二層モデル**。Layer 1（式）は不変。Layer 2（Economic Access Scarcity）として Platform Capital / Participation Capital / Effective Population を Ch 9 に明示 | **採択** |

### 案A を棄却した理由

- Issue の「資本を盛り込む」要求を **Participation Capital**（スマホ・通信料等）まで含めては満たさない
- Platform Capital と Effective Population が Ch 9 に現れず、Issue #1 の議論が **Ch 6–7 に埋もれる**
- 後続（Part III Meaning Allocation）への接続が弱い

### 案B を棄却した理由

- お金は新しい注意時間を**生まない**（有限プールの再配分が主）
- `Capacity`（存在量の上限）と `Captured`（獲得量）の定義が**混ざる**
- `g(Capital)` の関数形が恣意的になり、ADR-0001 の **硬い制約** という性格を損なう

### 案C を採択した理由

- Issue の意図（資本＝獲得競争＋参加コスト）を **Layer 2** として取り込める
- ADR-0001 の Layer 1（判例）を**改変しない**
- Ch 6（Attention Capitalism）→ Ch 7（Participatory Resource）→ Ch 9（Scarcity）の理論線が**一本化**される
- Effective Population により、資本の偏在・貧困層を **Part II の線を維持したまま** Part III / IV へ接続できる

---

## 議論（Cursor, 2026-06-21）

### 採択方針: 案C（二層モデル）

**Layer 1 — Ontological Scarcity（ADR-0001、式は不変）**

潜在容量。物理・人口・認知の硬い制約。

**Layer 2 — Economic Access Scarcity（Ch 9 追記）**

有限プールへの **アクセス** と **獲得競争** の条件。ここに資本が入る。

Layer 2 の資本は2方向に分解:

| 種類 | 主体 | 例 | 制約するもの |
|---|---|---|---|
| **Platform Capital** | 企業・広告主 | 広告費、レコメンド CAPEX、M&A | Capture 競争（誰がプールを取るか） |
| **Participation Capital** | 利用者 | スマホ購入、通信料、端末更新 | 土俵参加（市場に載れるか） |

Participation Capital は Issue 提起者の意図（ユーザがプラットフォームに乗るための投資）に対応する。Ch 7 §7.3 の Participatory Resource（賃金なしで価値創出）と接続:

> 参加には自己負担の資本が要る — 第三の活動形態の非対称性。

### 資本の偏在・貧困層

**文脈からそれない** — ただし第4因子として式に入れるのではなく、**Effective Population** として整理する:

```text
Potential Capacity:  Population × Time × Cognitive Bandwidth
Effective Population <= Population
                     （Participation Capital により間引かれる）
```

- 資本の偏在 → 注意市場に載る人口の分布が歪む
- 貧困層の増加 → Effective Population の縮小または二極化
- 完全除外（0/1）ではなく **程度の問題** として書く（フィーチャーフォン、家族共有端末、公共 Wi‑Fi 等）

一般の所得再分配論・デジタルデバイド横断サーベイには広げない（Part II の線を維持）。

### Part III / IV への接続

- Part III: 誰の Attention を配分対象とするか（Meaning Allocation）
- Part IV: 配分の規範（宗教層）— 誰の時間を神聖視するか

---

## 決定

| 項目 | 内容 |
|---|---|
| ADR-0001 本体 | **不変**（Layer 1 維持） |
| Ch 9 §9.2 | **追記**（Layer 2、Effective Population） |
| Ch 7 §7.3 | 相互参照 1 段落（Participation Capital）— 別途 |
| GLOSSARY | `Effective Population` 追加は将来 |
| GitHub Issue #1 | 素案比較追記後に close（C-0003 準拠） |

### 案C 内の追加決定（議論継続）

| 論点 | 決定 |
|---|---|
| Participation Capital の範囲 | スマホ購入・通信料等、土俵参加の自己負担を含む |
| 貧困・偏在 | 第4因子にせず **Effective Population <= Population** として整理 |
| 除外の程度 | 0/1 ではなく連続（フィーチャーフォン、共有端末、公共 Wi‑Fi 等） |
| 棄却（スコープ外） | 貧困・偏在の **独立章化**、一般の所得再分配論 |

---

## Reopen 履歴

| 日時 | 理由 |
|---|---|
| 2026-06-21 | close コメントが案C の結果のみで、素案比較・棄却理由が欠落（C-0003 Traceability 不充足） |

---

## 次のアクション

- [x] [drafts/ch09-9-2-economic-access-scarcity.md](drafts/ch09-9-2-economic-access-scarcity.md) を Ch 9 に merge（Accepted 更新）
- [x] Ch 7 §7.3 へ Participation Capital 段落（短）
- [x] ADR-0001 に Related Research Log 参照（カタログ追記）
- [x] 素案比較・棄却/採択理由を Research Log に追記（C-0003）
- [x] GitHub Issue #1 に素案比較をコメントして close
