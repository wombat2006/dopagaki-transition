# PROJECT-CONTEXT.md

Project:
ドパガキは模範生

Repository:
dopagaki-transition

Status:
Canonical Context

Last Updated:
2026-06-21

---

# 1. Origin

本プロジェクトはインターネットスラング「ドパガキ」から始まった。

プロジェクトタイトル **『ドパガキは模範生』** は、注意経済における大転倒（The Great Inversion）を端的に示す。工業社会の価値観から見れば問題児であるドパガキが、注意資本主義から見れば模範的経済主体である——この逆転こそが本研究の挑発的出発点である。

当初の問いは単純だった。

> ドパガキとは何者なのか。

一般的には、SNSを延々とスクロールし、動画を見続け、次々と新しい刺激を求める人間を指す俗語である。

通常は以下のように説明される。

- 意志が弱い
- SNS依存
- ドーパミン中毒

しかし本プロジェクトでは、この理解をそのまま採用しない。

---

# 2. Core Transition

本プロジェクトで本当に重要だったのは、以下の論理の階段である。

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
```

ドパガキは出発点である。

目的地ではない。

---

# 3. First Transition: Dopamine Is Not Pleasure

最初の転換点はドーパミン理解だった。

ドーパミンは快楽そのものではなく、主として以下に関係する。

- 探索
- 予測
- 学習
- 期待

したがってドパガキは「快楽依存者」ではなく、情報過剰環境において探索回路が過剰刺激された状態として再定義された。

この決定は後に以下へ接続された。

- ADR-0004 Dopagaki as Adaptation
- TS-0001 Dopagaki Definition
- TS-0002 Dopamine as Exploration

---

# 4. Second Transition: Attention Is Scarce

Attention Economy を検討する過程で、Attention Inflation という仮説が提案された。

しかし査読により、Attention は無限に増加しないことが確認された。

Attention は以下により制約される。

```text
Attention Capacity
≤ Population × Time × Cognitive Bandwidth
```

情報は無限に近づきうる。

しかし Attention は人口、時間、認知帯域幅によって制約される。

このため Attention Inflation は棄却され、Attention Scarcity が採択された。

これは後に ADR-0001 Attention Scarcity となった。

---

# 5. Third Transition: User Is Not Product

SNS企業は広告を売っているように見える。

しかし実際に広告主が購入しているのは、利用者そのものではない。

購入されているのは、利用者の将来行動の予測可能性である。

したがって本プロジェクトは以下を採択した。

```text
User ≠ Product
Prediction = Product
```

これは後に ADR-0005 User Is Not Product となり、TS-0005 Prediction Market Model へ接続された。

---

# 6. Fourth Transition: Meaning Allocation

Attention Scarcity を認めると、次の問いが発生する。

> 有限の Attention を何へ向けるべきか。

本プロジェクトでは、Meaning を Attention Allocation Mechanism と定義する。

Meaning は情報そのものではない。

Meaning は有限 Attention の配分規則である。

これは後に ADR-0002 Meaning Allocation となった。

---

# 7. Fifth Transition: Religion

Meaning Allocation を社会規模で考えると、宗教の再定義が必要になる。

本プロジェクトでは宗教を超自然信仰そのものとしてではなく、社会的な意味配分システムとして扱う。

```text
Religion ≠ Supernatural Belief System
Religion = Attention Allocation System
```

これは後に ADR-0003 Religion as Attention Allocation System となった。

---

# 8. Current Project Identity

本プロジェクトはもはや単なるドパガキ論ではない。

現在の研究方向は以下である。

```text
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

『ドパガキは模範生』は、ドパガキ現象を入口として、Attention Civilization から Meaning Civilization への移行を考察する Research Repository である。

---

# 9. Repository Role

本リポジトリは論文リポジトリではない。

本リポジトリは Research Repository である。

保存対象は成果物だけではない。

- 思考過程
- 査読
- 意思決定
- 理論変遷
- 採択済み仕様
- 未採択候補

を保存対象とする。

理想状態では、GitHub Repository を読むだけで以下が追跡できる。

- なぜそう考えたか
- 何を採択したか
- 現在どこにいるか
- 次にどこへ行くか

PROJECT-CONTEXT.md が不要になるほど、リポジトリ構造そのものに文脈が埋め込まれることが最終目標である。
