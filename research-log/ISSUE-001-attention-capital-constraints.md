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

## 議論（Cursor, 2026-06-21）

### 現行式が答える問い

```text
Attention Capacity <= Population × Time × Cognitive Bandwidth
```

これは **注意という資源の潜在総量（Ontological Scarcity）** の上限である。Attention Inflation 棄却（`Attention ≠ ∞`）の根拠。

資本をこの式に第4因子として乗せる案は棄却方向:

- お金は新しい注意時間を生まない（再配分が主）
- `Capacity` と `Captured` の定義が混ざる
- 式の硬さが失われる

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
| GitHub Issue #1 | 本 Log およびドラフト merge 後に close コメント |

---

## 棄却した案

- **案B:** `Attention Captured <= ... × g(Capital)` として第4因子を Capacity 式に追加
- **貧困・偏在を独立章化** し Part II 主線から外す

---

## 次のアクション

- [x] [drafts/ch09-9-2-economic-access-scarcity.md](drafts/ch09-9-2-economic-access-scarcity.md) を Ch 9 に merge（Accepted 更新）
- [x] Ch 7 §7.3 へ Participation Capital 段落（短）
- [x] GitHub Issue #1 に本 Log リンクでコメント
- [x] ADR-0001 に Related Research Log 参照（カタログ追記）
