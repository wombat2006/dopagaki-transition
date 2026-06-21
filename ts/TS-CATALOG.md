# TS-CATALOG.md

Project:
Dopagaki Transition

Status:
Accepted Draft

Last Updated:
2026-06-21

---

# Purpose

本ファイルは Dopagaki Transition Project における Theory Specification の正典カタログである。

TS は ADR によって採択された決定を理論仕様として定義する。

---

# TS-0001 Dopagaki Definition

## Status

Accepted

## Definition

ドパガキとは情報過剰環境への認知適応状態である。

これは精神疾患の診断名ではない。

また道徳的評価を含む概念でもない。

本プロジェクトでは分析対象として扱う。

## Depends On

- ADR-0004 Dopagaki as Adaptation

---

# TS-0002 Dopamine as Exploration

## Status

Accepted

## Definition

ドーパミンは快楽物質ではない。

ドーパミンは主として

- 探索
- 予測
- 学習
- 期待

を支援する神経伝達物質である。

## Implications

ドパガキ行動は快楽追求ではなく、探索回路の活性化として解釈される。

## Depends On

- TS-0001 Dopagaki Definition

---

# TS-0003 Skinner Box SNS Model

## Status

Accepted

## Definition

SNS は Industrialized Skinner Box である。

## Model

Variable Reward
↓
Exploration
↓
Reinforcement Learning
↓
Continued Engagement

## Depends On

- TS-0002 Dopamine as Exploration

---

# TS-0004 Attention Capitalism

## Status

Accepted

## Definition

Industrial Society

Value = Labor

Attention Society

Value = Attention

## Model

Industrial Capitalism
↓
Labor Extraction
↓
Value Creation
↓
Attention Capitalism
↓
Attention Capture
↓
Value Creation

## Depends On

- ADR-0001 Attention Scarcity
- ADR-0005 User Is Not Product

---

# TS-0005 Prediction Market Model

## Status

Accepted

## Definition

プラットフォーム企業の主要商品は広告ではない。

予測可能性である。

## Model

User Behavior
↓
Data Collection
↓
Prediction
↓
Marketable Asset

## Depends On

- ADR-0005 User Is Not Product
- TS-0004 Attention Capitalism

---

# TS-0006 Great Inversion

## Status

Accepted

## Definition

文明の価値生成原理は反転している。

## Model

Industrial Society

- Discipline
- Repetition
- Concentration

↓

Attention Society

- Exploration
- Reaction
- Sharing

## Depends On

- TS-0004 Attention Capitalism
- ADR-0001 Attention Scarcity

---

# Dependency Graph

```text
ADR-0004
↓
TS-0001
↓
TS-0002
↓
TS-0003

ADR-0001
↓
TS-0004
↓
TS-0005

ADR-0001
↓
TS-0006

ADR-0005
↓
TS-0004
↓
TS-0005
```

---

# Future TS Candidates

TS-0007 Meaning Economy

TS-0008 Religion Layer

TS-0009 Civilizational Transition

TS-0010 AI Civilization Model

---

# Repository Role

TS は本プロジェクトにおける法律・仕様である。

ADR が採択した決定を再利用可能な理論モジュールとして定義する。
