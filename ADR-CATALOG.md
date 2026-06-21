# ADR-CATALOG.md

Project:
ドパガキは模範生

Repository:
dopagaki-transition

Status:
Accepted

Last Updated:
2026-06-21

---

# Purpose

本ファイルは『ドパガキは模範生』プロジェクトにおける Architecture Decision Record の正典カタログである。

ADR は本プロジェクトにおける判例であり、理論上の重要な意思決定を記録する。

後続の TS および Manuscript は ADR を根拠として構築される。

---

# Accepted ADRs

## ADR-0001 Attention Scarcity

### Status

Accepted

### Decision

Attention Inflation を棄却する。

Attention Scarcity を採択する。

### Rationale

Attention は人口、時間、認知帯域幅によって制約される。

```text
Attention Capacity
<= Population x Time x Cognitive Bandwidth
```

情報のみが無限へ近づく。

Attention は有限である。

### Supplement (Layer 2)

ADR-0001 の Decision（Layer 1: Ontological Scarcity）は改変しない。

Layer 2（Economic Access Scarcity）——Platform Capital / Participation Capital、Effective Population——は Ch 9 §9.2.1–9.2.3 および [research-log/ISSUE-001-attention-capital-constraints.md](research-log/ISSUE-001-attention-capital-constraints.md)（素案比較 §）に従い Manuscript へ反映した。

### Related ADR

- ADR-0002 Meaning Allocation

### Related Research Log

- [ISSUE-001 Attention が制約される要因の欠如](research-log/ISSUE-001-attention-capital-constraints.md)

### Tags

- attention
- scarcity
- economics

---

## ADR-0002 Meaning Allocation

### Status

Accepted

### Decision

Meaning は Attention Allocation Mechanism と定義する。

### Rationale

Meaning は情報そのものではない。

Meaning は有限 Attention の配分規則である。

### Related ADR

- ADR-0001 Attention Scarcity
- ADR-0003 Religion as Attention Allocation System

### Tags

- meaning
- attention
- allocation

---

## ADR-0003 Religion as Attention Allocation System

### Status

Accepted

### Decision

```text
Religion != Supernatural Belief System
Religion = Attention Allocation System
```

### Rationale

宗教は社会において、何へ Attention を向けるべきかを決定する。

### Related ADR

- ADR-0002 Meaning Allocation

### Tags

- religion
- attention
- civilization

---

## ADR-0004 Dopagaki as Adaptation

### Status

Accepted

### Decision

ドパガキを病理として定義しない。

ドパガキを情報過剰環境への認知適応として定義する。

### Rationale

人類は進化史の大半において情報不足環境で生存してきた。

現代は情報過剰環境である。

ドパガキ的行動は、探索回路が過剰な情報環境へ適応した結果として理解できる。

### Related ADR

- ADR-0001 Attention Scarcity

### Related TS

- TS-0001 Dopagaki Definition
- TS-0002 Dopamine as Exploration

### Tags

- dopagaki
- adaptation
- cognition
- attention

---

## ADR-0005 User Is Not Product

### Status

Accepted

### Decision

```text
User != Product
Prediction = Product
```

### Rationale

広告主が購入しているのは利用者そのものではない。

利用者が将来どのような行動を取るかという予測可能性である。

価値の源泉は個人ではなく、予測精度に存在する。

### Related ADR

- ADR-0001 Attention Scarcity

### Related TS

- TS-0004 Attention Capitalism
- TS-0005 Prediction Market Model

### Tags

- attention
- capitalism
- prediction
- platform
- economics

---

# Dependency Graph

```text
ADR-0001 Attention Scarcity
            |
            v
ADR-0002 Meaning Allocation
            |
            v
ADR-0003 Religion as Attention Allocation System

ADR-0004 Dopagaki as Adaptation
            |
            v
TS-0001 Dopagaki Definition
            |
            v
TS-0002 Dopamine as Exploration

ADR-0001 Attention Scarcity
            |
            v
ADR-0005 User Is Not Product
            |
            v
TS-0004 Attention Capitalism
            |
            v
TS-0005 Prediction Market Model
```

---

# Future ADR Candidates

## ADR-P001 Surplus Attention Value

Candidate for Chapter 12（旧 §7.4）。

## ADR-P002 Meaning Economy

Candidate for Part III.

## ADR-P003 Civilizational Transition

Candidate for Part V.
