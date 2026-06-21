# ドパガキ・トランジション

## 副題

**ドーパミン経済から意味経済へ**

神経科学・行動心理学・政治経済学・宗教学・AI文明論から見た、高度情報社会の認知適応に関する試論。

---

## 概要

本プロジェクトは、インターネットスラングである「ドパガキ」を出発点として、ドーパミン、探索行動、SNS、Attention Economy、資本論、AI、宗教、文明遷移を横断的に分析する **Research Repository** です。

本論文では、ドパガキを単なる依存症や人格的欠陥としてではなく、**情報過剰環境において探索回路が適応した結果として生じる認知状態**として捉えます。

本リポジトリは論文リポジトリではありません。思考過程、査読、意思決定、理論変遷を含めて保存します。

---

## 知識階層

```text
Constitution   憲法（最高位の規範）
↓
ADR            判例（重要な理論的意思決定）
↓
TS             理論仕様（採択済み決定の再利用可能な定義）
↓
Manuscript     論文本文（読者向け再構成）
↓
Research Log   研究過程（採択前の議論・査読）
```

詳細は [constitution/CONSTITUTION.md](constitution/CONSTITUTION.md) および [meta/META-SPECIFICATION.md](meta/META-SPECIFICATION.md) を参照してください。

---

## 理論軸

```text
Dopagaki
↓
Dopamine
↓
Exploration
↓
Attention
↓
Attention Scarcity
↓
Meaning Allocation
↓
Religion
↓
Civilization
↓
AI Civilization
```

ドパガキは出発点であり、最終目的ではありません。

---

## 現在のフェーズ

| フェーズ | 状態 |
|---|---|
| Research | Completed |
| Architecture | Active |
| Repository Codification | In Progress |

現在の位置づけと次の作業は [meta/AS-IS.md](meta/AS-IS.md) と [meta/TO-BE.md](meta/TO-BE.md) に記録しています。

---

## 採択済み ADR

| ID | タイトル | 状態 |
|---|---|---|
| ADR-0001 | Attention Scarcity | Accepted |
| ADR-0002 | Meaning Allocation | Accepted |
| ADR-0003 | Religion as Attention Allocation System | Accepted |
| ADR-0004 | Dopagaki as Adaptation | Accepted |
| ADR-0005 | User Is Not Product | Accepted |

正典カタログ: [adr/ADR-CATALOG.md](adr/ADR-CATALOG.md)

---

## 採択済み TS

| ID | タイトル | 状態 |
|---|---|---|
| TS-0001 | Dopagaki Definition | Accepted |
| TS-0002 | Dopamine as Exploration | Accepted |
| TS-0003 | Skinner Box SNS Model | Accepted |
| TS-0004 | Attention Capitalism | Accepted |
| TS-0005 | Prediction Market Model | Accepted |
| TS-0006 | Great Inversion | Accepted |

正典カタログ: [ts/TS-CATALOG.md](ts/TS-CATALOG.md)

---

## Manuscript 進捗

正典: [manuscript/MANUSCRIPT-v0.1.md](manuscript/MANUSCRIPT-v0.1.md)

### Part I — Dopagaki and the Exploration Brain

状態: Accepted

- Chapter 1: The Dopagaki Problem
- Chapter 2: Dopamine Is Not Pleasure
- Chapter 3: Exploration in an Information Flood

### Part II — Industrialized Exploration

状態: Accepted（Chapter 7.3 まで）

- Chapter 4: The Industrialization of Exploration
- Chapter 5: The Skinner Box at Planetary Scale
- Chapter 6: Attention Capitalism
- Chapter 7.1: Attention Scarcity
- Chapter 7.2: Prediction Is The Product
- Chapter 7.3: The Great Inversion

### Part III — Meaning Economy

状態: Planned

- Chapter 7.4: Surplus Attention Value
- Chapter 8: Meaning Allocation
- Chapter 9: Meaning Economy

### Part IV — Religion Layer

状態: Planned

- Chapter 10: Religion as Infrastructure
- Chapter 11: Competing Meaning Systems

### Part V — Civilizational Transition

状態: Planned

- Chapter 12: From Industrial Civilization to Attention Civilization
- Chapter 13: AI and the Cost of Information
- Chapter 14: The Future of Meaning

---

## リポジトリ構成

```text
constitution/          憲法（C-0001 〜 C-0008）
adr/                   Architecture Decision Records
ts/                    Theory Specifications
manuscript/            論文本文
meta/                  リポジトリ管理・AS-IS / TO-BE
research-log/          研究過程（採択前の議論）
notes/                 作業メモ（移行中）
docs/                  旧ドキュメント（移行中）

PROJECT-CONTEXT.md     プロジェクト文脈（正典）
```

ルート直下にも `ADR-CATALOG.md`、`TS-CATALOG.md`、`META-SPECIFICATION.md`、`MANUSCRIPT-v0.1.md` が残っています。レイヤディレクトリへの移行作業中です。

---

## はじめに読むファイル

1. [PROJECT-CONTEXT.md](PROJECT-CONTEXT.md) — プロジェクトの起源と理論的転換点
2. [constitution/CONSTITUTION.md](constitution/CONSTITUTION.md) — 憲法と知識階層
3. [meta/META-SPECIFICATION.md](meta/META-SPECIFICATION.md) — 知識管理の仕様
4. [adr/ADR-CATALOG.md](adr/ADR-CATALOG.md) — 採択済み意思決定
5. [ts/TS-CATALOG.md](ts/TS-CATALOG.md) — 理論仕様
6. [manuscript/MANUSCRIPT-v0.1.md](manuscript/MANUSCRIPT-v0.1.md) — 論文構成

---

## コントリビューション

理論的指摘、批判、反証、参考文献提案を歓迎します（[C-0002 Review First](constitution/C-0002-Review-First.md)）。

### Issue

以下の用途で利用してください。

- 誤記修正
- 理論的指摘
- 反証提案
- 参考文献提案
- 新章提案

https://github.com/wombat2006/dopagaki-transition/issues

### Pull Request

以下を歓迎します。

- 誤字脱字修正
- 表現改善
- 参考文献追加
- 図表追加
- 英訳

大規模な理論変更については、先に Issue を作成してください。

https://github.com/wombat2006/dopagaki-transition/pulls

---

## 査読ポリシー

本リポジトリでは以下の状態を使用します。

- Draft
- Proposed
- Review Requested
- Accepted
- Rejected
- Superseded

Accepted となった内容のみ、TS および Manuscript へ正式反映されます。

---

## ライセンス

[CC0 1.0 Universal](LICENSE) — パブリックドメイン相当の放棄。
