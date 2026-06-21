# META-SPECIFICATION.md

Project:
Dopagaki Transition

Status:
Canonical

Last Updated:
2026-06-21

Purpose:

本ファイルは Dopagaki Transition Project における知識管理構造を定義する。

本ファイルは理論そのものを定義しない。

理論をどのように管理し、どのように採択し、どのように発展させるかを定義する。

---

# 1. Repository Philosophy

本リポジトリは論文リポジトリではない。

本リポジトリは Research Repository である。

保存対象は成果物だけではない。

- 思考過程
- 査読
- 意思決定
- 理論変遷

も保存対象とする。

---

# 2. Knowledge Hierarchy

```text
Constitution
↓
ADR
↓
TS
↓
Manuscript
↓
Research Log
```

---

# 3. Constitution Philosophy

Constitution は憲法である。

最高位の規範であり、下位文書は Constitution に反してはならない。

構成:

- CONSTITUTION.md
- C-0001 Reality First
- C-0002 Review First
- C-0003 Traceability
- C-0004 Separation of Concerns
- C-0005 Reproducibility
- C-0006 Falsifiability
- C-0007 Versioned Knowledge

---

# 4. ADR Philosophy

ADR は判例である。

重要な理論的意思決定を記録する。

TS および Manuscript は ADR を根拠とする。

---

# 5. TS Philosophy

TS は法律・仕様である。

ADR によって採択された決定を再利用可能な理論モジュールとして定義する。

---

# 6. Manuscript Philosophy

Manuscript は学術論文層である。

ADR と TS を読者向けに再構成する。

Manuscript は理論を発明しない。

---

# 7. Research Log Philosophy

Research Log は議事録である。

採択前の議論、棄却された仮説、査読コメントを保存する。

---

# 8. Gate Philosophy

Gate は成果物ではない。

Gate は状態遷移条件である。

Example:

- GATE-01 Constitution Complete
- GATE-02 ADR Complete
- GATE-03 TS Complete

Gate は Done List ではない。

State Transition Machine である。

---

# 9. Goal Philosophy

Goal は状態である。

Gate は通過条件である。

Goal 達成には複数 Gate を必要とする。

---

# 10. AS-IS / TO-BE

AS-IS

現在成立している知識。

- Constitution
- ADR
- TS

TO-BE

将来成立予定の知識。

- Gate
- Goal
- Planned ADR
- Planned TS

---

# 11. Traceability

すべての理論は追跡可能でなければならない。

```text
Project Context
↓
ADR
↓
TS
↓
Manuscript
```

---

# 12. Repository End State

理想状態では GitHub Repository を読むだけで

- なぜそう考えたか
- 何を採択したか
- 現在どこにいるか
- 次にどこへ行くか

が追跡できる。

PROJECT-CONTEXT.md が不要になるほど、文脈が Repository Structure に埋め込まれることを最終目標とする。
