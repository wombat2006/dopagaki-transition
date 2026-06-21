# DUAL-AUDIENCE.md

Project:
ドパガキは模範生

Status:
Draft

---

## 目的

本リポジトリは **二つの成立条件** を同時に満たす。

1. **学術研究の場** — 追跡可能、反証可能、版管理された知識体系
2. **読み物** — 論理の階段を辿れる、読んで納得できる叙述

両者は矛盾しない。Manuscript が読み物、Constitution / ADR / TS / Research Log が研究基盤である。

---

## 二層モデル

| 層 | 入口 | 主な読者 | 主な成果物 |
|---|---|---|---|
| 読者層 | [manuscript/README.md](../manuscript/README.md) | 一般読者、論考好き | Accepted Manuscript |
| 研究層 | [research/README.md](../research/README.md) | 査読者、共同研究者 | Constitution, ADR, TS, Research Log |

---

## 設計原則

### Manuscript は発明しない

Manuscript は新理論を発明しない。ADR と TS によって採択された内容を読者向けに再構成する（[META-SPECIFICATION.md](META-SPECIFICATION.md) §6）。

### 読者は ADR を読まなくてよい

読者向けルートでは ADR / TS へのリンクは任意。核心命題は Manuscript 内で完結させる。用語の入口は [GLOSSARY.md](../GLOSSARY.md)。

### 研究者は Manuscript だけで足りない

Accepted になった内容は ADR → TS → Manuscript の順で追跡できる。Manuscript だけ読んでも「なぜ採択されたか」は不足する。

### 同一内容、異なる粒度

| 内容 | 研究層 | 読者層 |
|---|---|---|
| 注意は有限 | ADR-0001 | Ch 9 Attention Scarcity |
| 利用者≠商品 | ADR-0005 | Ch 7 §7.3 |
| ドパガキ＝適応 | ADR-0004 | Part I Ch 2–3 |

---

## 現在の成熟度

| 層 | 状態 |
|---|---|
| 研究基盤（Constitution, ADR, TS） | 成立 |
| 読者層（Accepted Manuscript） | Part I Ch 2–3, Part II Ch 6/7.3/9 が読める |
| Research Log | 未整備 |
| 研究全体の単一読み物化 | 未実施（将来） |

---

## 次の改修

- Part I Ch 1、Part II Ch 4–5 の Accepted 原文化
- Ch 7 §7.1–7.2、Ch 8 obsolete ブリッジ執筆
- Research Log の開始
- 読者向け「一章まとめ」ページの検討
