# 研究する — 研究者向け入口

Project:
ドパガキは模範生

Audience:
Researcher

---

## この入口について

ここから入ると、**学術研究の場**としてのリポジトリ構造にたどり着く。

採択された結論だけでなく、思考過程・査読・棄却された仮説・理論の変更履歴を追跡できる。Manuscript は ADR と TS を根拠とし、Constitution に従う。

読者として読みたい場合は [manuscript/README.md](../manuscript/README.md)。

---

## 研究の読み方

### 1. 文脈

[PROJECT-CONTEXT.md](../PROJECT-CONTEXT.md) — なぜこの理論が生まれたか

### 2. 規範

[constitution/CONSTITUTION.md](../constitution/CONSTITUTION.md) — 憲法と知識階層

[meta/META-SPECIFICATION.md](../meta/META-SPECIFICATION.md) — 知識管理の仕様

[meta/DUAL-AUDIENCE.md](../meta/DUAL-AUDIENCE.md) — 読者／研究者の二層設計

### 3. 採択済み判断

[adr/ADR-CATALOG.md](../adr/ADR-CATALOG.md) — 判例（Architecture Decision Records）

[ts/TS-CATALOG.md](../ts/TS-CATALOG.md) — 理論仕様（Theory Specifications）

### 4. 本文（Manuscript）

[manuscript/MANUSCRIPT-v0.1.md](../manuscript/MANUSCRIPT-v0.1.md) — 論文目次

Accepted 原稿のみが TS へ反映される。

### 5. 位置づけ

[meta/AS-IS.md](../meta/AS-IS.md) — いま何が成立しているか

[meta/TO-BE.md](../meta/TO-BE.md) — 次に何を作るか

---

## 知識階層

```text
Constitution   憲法（最高位）
↓
ADR            判例（重要な理論的判断）
↓
TS             理論仕様（再利用可能な定義）
↓
Manuscript     読者向け再構成
↓
Research Log   採択前の議論・査読
```

下位は上位に反してはならない（[C-0004 Separation of Concerns](../constitution/C-0004-Separation-of-Concerns.md)）。

---

## 査読と貢献

状態: Draft → Proposed → Review Requested → **Accepted** / Rejected / Superseded

- [C-0002 Review First](../constitution/C-0002-Review-First.md) — 批判は歓迎
- [C-0003 Traceability](../constitution/C-0003-Traceability.md) — 重要な変更は ADR へ
- [C-0006 Falsifiability](../constitution/C-0006-Falsifiability.md) — 反証可能であること

Issue: https://github.com/wombat2006/dopagaki-transition/issues

Pull Request: https://github.com/wombat2006/dopagaki-transition/pulls

---

## 依存関係（要約）

```text
ADR-0004 Dopagaki as Adaptation
  → TS-0001, TS-0002, TS-0003

ADR-0001 Attention Scarcity
  → TS-0004 Attention Capitalism
  → TS-0006 Great Inversion

ADR-0005 User Is Not Product
  → TS-0005 Prediction Market Model

ADR-0002 Meaning Allocation
  → ADR-0003 Religion as Attention Allocation System
```

詳細: 各 ADR / TS カタログ内の Dependency Graph
