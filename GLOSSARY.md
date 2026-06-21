# GLOSSARY.md

Project:
ドパガキは模範生

Status:
Reader Reference

---

## この用語集について

本研究で使う語の多くは、日常語を **拡張・再定義** した専門語である。ここでは一行定義と「よくある誤解」を示し、詳細は TS（理論仕様）・ADR（判例）・Manuscript（原稿）へリンクする。

**定義の正典は TS である。** 本ファイルは読者向けの要約である。

候補語の機械抽出: `python3 scripts/glossary_extractor.py`（要 [requirements-dev.txt](../requirements-dev.txt) — fugashi + unidic-lite）。出力は [meta/glossary-candidates.json](meta/glossary-candidates.json)。採択は人間が `GLOSSARY.md` に反映する。

---

## 必読（8 語）

### ドパガキ

**一行:** 情報過剰環境への認知適応状態。病気の診断名でも、道徳ラベルでもない。

**≠ よくある誤解:** SNS 依存・意志薄弱・若者問題——本研究はこれらをそのまま採用しない。

| 根拠 | リンク |
|---|---|
| TS-0001 | [ts/TS-CATALOG.md#ts-0001-dopagaki-definition](ts/TS-CATALOG.md) |
| ADR-0004 | [adr/ADR-CATALOG.md#adr-0004-dopagaki-as-adaptation](adr/ADR-CATALOG.md) |
| 原稿 | [manuscript/part01/ch02-dopamine-is-not-pleasure.md](manuscript/part01/ch02-dopamine-is-not-pleasure.md) |

---

### 模範生

**一行:** 注意経済において、探索・滞在・反応を続ける利用者——プラットフォームから見た「理想的経済主体」。

**≠ よくある誤解:** 本当に褒めているわけではない。**挑発的リフレーム** である。工業社会の常識（規律・集中）から見れば問題児だが、注意社会のインセンティブから見れば「模範」に見える——この **逆転** を突く語。

| 根拠 | リンク |
|---|---|
| TS-0006 | [ts/TS-CATALOG.md#ts-0006-great-inversion](ts/TS-CATALOG.md) |
| 原稿 | [manuscript/part02/ch07-digital-capital-theory.md](manuscript/part02/ch07-digital-capital-theory.md) §7.3 |

---

### 注意（Attention）

**一行:** 意識・時間・認知処理を特定対象に向けること。本研究では **プラットフォームが競争する有限資源**。

**≠ よくある誤解:** 「気をつける」「注意深さ」だけの話ではない。滞在時間・スクロール・通知確認など、**測定・奪い合いの対象** になる。

| 根拠 | リンク |
|---|---|
| ADR-0001 | [adr/ADR-CATALOG.md#adr-0001-attention-scarcity](adr/ADR-CATALOG.md) |
| 原稿 | [manuscript/part02/ch06-attention-capitalism.md](manuscript/part02/ch06-attention-capitalism.md) |

---

### 注意経済

**一行:** 企業収益が「モノの販売」より **人間の注意の捕捉** で決まる経済。

**≠ よくある誤解:** マクロ経済学の「経済（GDP・物価）」と同一ではない。ここでの「経済」は **何を希少資源として競争するか** という意味。

| 根拠 | リンク |
|---|---|
| TS-0004 | [ts/TS-CATALOG.md#ts-0004-attention-capitalism](ts/TS-CATALOG.md) |
| 原稿 | [manuscript/part02/ch06-attention-capitalism.md](manuscript/part02/ch06-attention-capitalism.md) |

---

### 注意資本主義（Attention Capitalism）

**一行:** 工業社会が `価値＝労働` だったのに対し、注意社会では `価値＝注意` となる資本主義の段階。

**≠ よくある誤解:** 「注意経済」とほぼ同じ文脈で使うが、本研究では **資本論的な抽出構造**（捕捉→価値化）を強調するときに「注意資本主義」と呼ぶ。

```text
Industrial Capitalism  → 労働抽出 → 価値創出
Attention Capitalism   → 注意捕捉 → 価値創出
```

| 根拠 | リンク |
|---|---|
| TS-0004 | [ts/TS-CATALOG.md#ts-0004-attention-capitalism](ts/TS-CATALOG.md) |

---

### Attention ≠ ∞（注意の有限性）

**一行:** 注意は無限に増やせない。総人口・1 日 24 時間・認知帯域幅で上限が決まる。

**≠ よくある誤解:** 情報が増えれば注意も増える、という **Attention Inflation** 仮説は本研究では **棄却** する。

```text
Attention Capacity <= Population × Time × Cognitive Bandwidth
```

| 根拠 | リンク |
|---|---|
| ADR-0001 | [adr/ADR-CATALOG.md#adr-0001-attention-scarcity](adr/ADR-CATALOG.md) |
| 原稿 | [manuscript/part02/ch09-attention-scarcity.md](manuscript/part02/ch09-attention-scarcity.md) |

---

### 予測＝商品（Prediction = Product）

**一行:** プラットフォームの最終製品は広告ではなく、**利用者の将来行動の予測可能性**。

**≠ よくある誤解:** 「If you're not paying, you are the product」は **厳密には不正確**。商品なのは人間そのものではなく、クリック・購買・滞在などの **確率分布** である。

```text
User != Product
Prediction = Product
```

| 根拠 | リンク |
|---|---|
| ADR-0005 | [adr/ADR-CATALOG.md#adr-0005-user-is-not-product](adr/ADR-CATALOG.md) |
| TS-0005 | [ts/TS-CATALOG.md#ts-0005-prediction-market-model](ts/TS-CATALOG.md) |
| 原稿 | [manuscript/part02/ch07-digital-capital-theory.md](manuscript/part02/ch07-digital-capital-theory.md) §7.3 |

---

### 大転倒（The Great Inversion）

**一行:** 文明の「理想的行動」が、工業社会から注意社会へ **反転** している、という thesis。

```text
Industrial Society:  規律 / 反復 / 集中
Attention Society:   探索 / 反応 / 共有
```

**≠ よくある誤解:** 道徳の堕落ではなく、**価値生成原理の変更** として記述する。

| 根拠 | リンク |
|---|---|
| TS-0006 | [ts/TS-CATALOG.md#ts-0006-great-inversion](ts/TS-CATALOG.md) |
| 原稿 | [manuscript/part02/ch07-digital-capital-theory.md](manuscript/part02/ch07-digital-capital-theory.md) §7.3 |

---

## Part II 語彙（Accepted 原稿）

Ch 2–9 で再定義・強調される語。必読 8 語のあとに読むと原稿が通りやすい。

### 探索（Exploration）

**一行:** ドーパミン回路が駆動する「次を探す」行動。快楽追求ではない。

**≠ よくある誤解:** 日常の「探検」「調査」と同義ではない。神経科学的には **期待と予測誤差** に結びつく。

| 根拠 | リンク |
|---|---|
| TS-0002 | [ts/TS-CATALOG.md#ts-0002-dopamine-as-exploration](ts/TS-CATALOG.md) |
| 原稿 | [manuscript/part01/ch02-dopamine-is-not-pleasure.md](manuscript/part01/ch02-dopamine-is-not-pleasure.md) |

---

### ドーパミン

**一行:** 快楽物質ではなく、探索・予測・学習・期待を支援する神経伝達物質。

**≠ よくある誤解:** 「ドーパミン＝快楽・中毒」の通俗説は本研究では採用しない。

| 根拠 | リンク |
|---|---|
| TS-0002 | [ts/TS-CATALOG.md#ts-0002-dopamine-as-exploration](ts/TS-CATALOG.md) |

---

### 進化的不一致（Evolutionary Mismatch）

**一行:** 神経系（旧環境向け）と情報環境（新）のズレ。ドパガキはその **適応** として読む。

| 根拠 | リンク |
|---|---|
| 原稿 | [manuscript/part01/ch03-exploration-in-information-flood.md](manuscript/part01/ch03-exploration-in-information-flood.md) |

---

### スキナー箱（Skinner Box）/ 工業化されたスキナー箱

**一行:** 変動報酬で行動を強化する装置。SNS を ** planetary scale の Skinner Box** とみなす比喩。

**≠ よくある誤解:** 陰謀論ではなく、**強化学習＋プラットフォーム競争** の構造比喩。

| 根拠 | リンク |
|---|---|
| TS-0003 | [ts/TS-CATALOG.md#ts-0003-skinner-box-sns-model](ts/TS-CATALOG.md) |
| 原稿 | [manuscript/part02/ch05-skinner-box-planetary-scale.md](manuscript/part02/ch05-skinner-box-planetary-scale.md) |

---

### Variable Reward（変動報酬）

**一行:** 報酬の大きさ・タイミングが一定でない設計。探索・エンゲージメントを最大化しやすい。

```text
Variable Reward → Exploration → Reinforcement Learning → Continued Engagement
```

| 根拠 | リンク |
|---|---|
| TS-0003 | [ts/TS-CATALOG.md#ts-0003-skinner-box-sns-model](ts/TS-CATALOG.md) |

---

### Attention Capture（注意捕捉）

**一行:** 注意を引きつけ・拘束して価値化するプロセス。Attention Capitalism の抽出メカニズム。

```text
Attention Capitalism → Attention Capture → Value Creation
```

| 根拠 | リンク |
|---|---|
| TS-0004 | [ts/TS-CATALOG.md#ts-0004-attention-capitalism](ts/TS-CATALOG.md) |

---

### Attention Inflation

**一行:** 「情報が増えれば注意も増える」という仮説。**本研究では棄却**。

**≠ よくある誤解:** 採用されている概念ではない。Ch 9 の出発点はその **反証**。

| 根拠 | リンク |
|---|---|
| ADR-0001 | [adr/ADR-CATALOG.md#adr-0001-attention-scarcity](adr/ADR-CATALOG.md) |
| 原稿 | [manuscript/part02/ch09-attention-scarcity.md](manuscript/part02/ch09-attention-scarcity.md) §9.1 |

---

### Attention Capacity / Capture（容量と獲得）

**一行:** **Capacity**＝注意の潜在総量（人口×時間×帯域）。**Capture**＝その有限プールを誰が取るか。

**≠ よくある誤解:** 日常語の「容量」「捕獲」と混同しやすい。本研究では **Layer 1 / Layer 2** で層を分ける。

```text
Layer 1  Ontological Scarcity     … Attention Capacity
Layer 2  Economic Access Scarcity … Capture 競争・参加条件
```

| 根拠 | リンク |
|---|---|
| 原稿 | [manuscript/part02/ch09-attention-scarcity.md](manuscript/part02/ch09-attention-scarcity.md) §9.2.1 |
| Log | [research-log/ISSUE-001-attention-capital-constraints.md](research-log/ISSUE-001-attention-capital-constraints.md) |

---

### Cognitive Bandwidth（認知帯域幅）

**一行:** 同時に処理できる注意量。Population・Time と並ぶ **Layer 1** の制約因子。

| 根拠 | リンク |
|---|---|
| ADR-0001 | [adr/ADR-CATALOG.md#adr-0001-attention-scarcity](adr/ADR-CATALOG.md) |

---

### Platform Capital / Participation Capital

**一行:** **Platform Capital**＝獲得側（広告費・CAPEX 等）。**Participation Capital**＝参加側（端末・通信料等の自己負担）。

**≠ よくある誤解:** 「資本＝お金」だけではない。後者は **土俵に載るための参入コスト**。

| 根拠 | リンク |
|---|---|
| 原稿 | [manuscript/part02/ch09-attention-scarcity.md](manuscript/part02/ch09-attention-scarcity.md) §9.2.2 |
| Log | [research-log/ISSUE-001-attention-capital-constraints.md](research-log/ISSUE-001-attention-capital-constraints.md) |

---

### Effective Population（実効人口）

**一行:** 注意市場に実際に載る母集団。`Effective Population <= Population` — Participation Capital により間引かれる。

| 根拠 | リンク |
|---|---|
| 原稿 | [manuscript/part02/ch09-attention-scarcity.md](manuscript/part02/ch09-attention-scarcity.md) §9.2.3 |

---

### Participatory Resource（参加型資源）

**一行:** 労働者でも消費者でもない第三の位置。賃金なく価値を生み、参加には **Participation Capital** が要る。

| 根拠 | リンク |
|---|---|
| 原稿 | [manuscript/part02/ch07-digital-capital-theory.md](manuscript/part02/ch07-digital-capital-theory.md) §7.3 |

---

### 行動採掘（Behavioural Extraction Economy）

**一行:** 検索・滞在・クリック等の **行動データを原材料** として採掘する経済。

| 根拠 | リンク |
|---|---|
| 原稿 | [manuscript/part02/ch07-digital-capital-theory.md](manuscript/part02/ch07-digital-capital-theory.md) §7.3 |

---

### ゼロサム（に近い競争）

**一行:** 注意の総量が有限のとき、プラットフォーム間の獲得競争は **ゼロサムに近い**。

| 根拠 | リンク |
|---|---|
| 原稿 | [manuscript/part02/ch09-attention-scarcity.md](manuscript/part02/ch09-attention-scarcity.md) §9.2 |

---

## 続き（Part III 以降）

### 意味の配分（Meaning Allocation）

**一行:** 有限の注意を **何に向けるか** を決める規則。意味は情報そのものではない。

| 根拠 | リンク |
|---|---|
| ADR-0002 | [adr/ADR-CATALOG.md#adr-0002-meaning-allocation](adr/ADR-CATALOG.md) |

---

### 意味経済（Meaning Economy）

**一行:** 情報・注意の次に、**意味** が希少資源になる段階（構想中）。

```text
情報 → 注意 → 意味
```

| 根拠 | リンク |
|---|---|
| 構想 | [meta/TO-BE.md](meta/TO-BE.md) — ADR-P002, TS-0007 |

---

### 宗教（注意配分システム）

**一行:** 超自然信仰そのものではなく、社会における **注意配分の制度** として再定義する。

```text
Religion != Supernatural Belief System
Religion = Attention Allocation System
```

| 根拠 | リンク |
|---|---|
| ADR-0003 | [adr/ADR-CATALOG.md#adr-0003-religion-as-attention-allocation-system](adr/ADR-CATALOG.md) |

---

## 補足（索引）

Part II 語彙および必読 8 語に統合済み。以下はエイリアス・式のみ。

### User ≠ Product / Prediction = Product

→ 必読「[予測＝商品](#予測＝商品prediction--product)」参照。

### ドーパミン経済

→ Part II「探索」「Variable Reward」および [manuscript/part02/ch04-industrialization-of-exploration.md](manuscript/part02/ch04-industrialization-of-exploration.md)

---

## 読む順の提案

1. 必読 8 語（10 分）
2. Part II 語彙（15 分）— Ch 2–9 を読む前でも可
3. [manuscript/README.md](manuscript/README.md) の推奨ルート（30 分）
4. 気になる語の TS / ADR へ
