# GLOSSARY.md

Project:
ドパガキは模範生

Status:
Reader Reference

---

## この用語集について

本研究で使う語の多くは、日常語を **拡張・再定義** した専門語である。ここでは一行定義と「よくある誤解」を示し、詳細は TS（理論仕様）・ADR（判例）・Manuscript（原稿）へリンクする。

**定義の正典は TS である。** 本ファイルは読者向けの要約である。

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

**一行:** 文明の「理想的行为」が、工業社会から注意社会へ **反転** している、という thesis。

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

## 補足（原稿内の用語）

### 行動採掘経済（Behavioural Extraction Economy）

プラットフォームが検索履歴・滞在時間・クリックパターンなど **行動データを原材料** として採掘するモデル。原稿 §7.3 で導入。

→ [manuscript/part02/ch07-digital-capital-theory.md](manuscript/part02/ch07-digital-capital-theory.md)

### Participatory Resource（参加型資源）

労働者でも消費者でもない第三の位置。賃金なく価値を生み、意図せず企業利益へ変換される利用者。原稿 §7.3。

→ [manuscript/part02/ch07-digital-capital-theory.md](manuscript/part02/ch07-digital-capital-theory.md)

### ドーパミン経済

探索・期待を連続刺激する報酬系設計が、市場競争の対象になった状態。第 4–6 章の文脈語（TS 単独条目なし）。

→ [manuscript/part02/ch04-industrialization-of-exploration.md](manuscript/part02/ch04-industrialization-of-exploration.md)

---

## 読む順の提案

1. 本用語集（5 分）
2. [manuscript/README.md](manuscript/README.md) の推奨ルート（30 分）
3. 気になる語の TS / ADR へ
