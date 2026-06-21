# ドパガキ・トランジション

**ドーパミン経済から意味経済へ**

神経科学・行動心理学・政治経済学・宗教学・AI 文明論を横断する、高度情報社会の認知適応に関する研究リポジトリ。

---

## このリポジトリについて

インターネット上で「ドパガキ」と呼ばれる人たち——ショート動画を止められず、通知が来るたびに画面を開き、次の刺激を待ち続ける人たち——は、たいていこう説明される。

意志が弱い。若者の問題。SNS 依存。ドーパミン中毒。

本プロジェクトは、その説明をそのまま受け入れない。

なぜなら、**人間の脳は壊れていないから**である。20 万年前のサバンナで「次に何があるか」を探す回路は、今も正常に動いている。変わったのは環境だけだ。探索の対象が、木の実から TikTok になっただけだ。

ここから先の議論は、道徳論ではない。適応の話であり、経済の話であり、やがて文明の話になる。

---

## 論理の階段

本プロジェクトは、次の階段を一歩ずつ登っていく。

```text
ドパガキ
　↓  病理ではなく、情報過剰環境への適応
ドーパミン
　↓  快楽物質ではなく、探索と期待の物質
探索行動
　↓  報酬予測誤差を利用した設計（スキナー箱、無限スクロール）
注意（Attention）
　↓  21 世紀資本主義が工業化した資源
注意の有限性
　↓  注意は無限ではない
意味の配分
　↓  有限の注意を、何に向けるか
宗教
　↓  超自然信仰ではなく、注意配分の社会制度
文明
　↓  工業→注意→意味→AI
```

ドパガキは出発点にすぎない。目的地ではない。

---

## いま採択されている核心

### ドパガキは病気ではない

情報過剰環境において、探索回路が過剰に駆動された状態として理解できる。快楽中毒ではなく、**探索回路の過剰駆動**に近い（[ADR-0004](adr/ADR-CATALOG.md)）。

### ドーパミンは快楽ではない

人は報酬を得た瞬間より、「得られるかもしれない」状況に強く反応する。ショート動画やガチャは、この期待を連続生成する装置である（[TS-0002](ts/TS-CATALOG.md)）。

### 注意は無限ではない

```text
Attention ≠ ∞
∵ 母集団が総人口によって制限されるから
```

情報は増え続ける。しかし注意を向けられる主体は、総人口・1 日 24 時間・認知の処理能力を超えない。プラットフォーム同士の争いは、ゼロサムに近い（[ADR-0001](adr/ADR-CATALOG.md)）。

### 利用者は商品ではない

広告主が買っているのは、あなた自身ではない。**あなたの将来行動の予測可能性**である（[ADR-0005](adr/ADR-CATALOG.md)）。

### 宗教は注意配分の仕組み

何を神聖視し、何に時間を捧げるか——宗教は historically、この問いに答える制度として機能してきた（[ADR-0003](adr/ADR-CATALOG.md)）。

---

## 論文リポジトリではない

このリポジトリは、完成した論文だけを置く場所ではない。**Research Repository** である。

採択された結論だけでなく、そこに至る思考過程、査読、反論、棄却された仮説、理論の変更履歴を残す。なぜそう考えたか、何を採択したか、いまどこにいるか、次にどこへ行くか——が追跡できる状態を目指している。

---

## 知識の階層

下位の文書は、上位の規範に反してはならない。

```text
Constitution（憲法）     … 最高位の規範
ADR（判例）             … 重要な理論的判断の記録
TS（理論仕様）          … 採択済み判断の再利用可能な定義
Manuscript（論文本文）  … 読者向けの再構成
Research Log（研究過程）… 採択前の議論と査読
```

詳細は [constitution/CONSTITUTION.md](constitution/CONSTITUTION.md) と [meta/META-SPECIFICATION.md](meta/META-SPECIFICATION.md) を参照。

---

## 論文の進捗

目次の正典: [manuscript/MANUSCRIPT-v0.1.md](manuscript/MANUSCRIPT-v0.1.md)

### Part I — ドパガキと探索する脳

採択済み

- 第 1 章: ドパガキ問題
- 第 2 章: ドーパミンは快楽ではない → [原稿](manuscript/part01/ch02-dopamine-is-not-pleasure.md)
- 第 3 章: 情報洪水のなかの探索 → [原稿](manuscript/part01/ch03-exploration-in-information-flood.md)

### Part II — 工業化された探索

執筆中（第 4–11 章）

- 第 4–6 章: 探索の工業化、スキナー箱、注意資本主義 → [第 6 章原稿](manuscript/part02/ch06-attention-capitalism.md)
- 第 7–8 章: 資本論・資本主義/共産主義（obsolete ブリッジ、未執筆）
- 第 9–11 章: 注意の有限性、予測が商品、大逆転 → [第 9 章原稿](manuscript/part02/ch09-attention-scarcity.md)

### Part III — 意味経済

構想段階

- 余剰注意の価値、意味の配分、意味経済

### Part IV — 宗教層

構想段階

- 宗教をインフラとして、競合する意味体系として再定義

### Part V — 文明の転換

構想段階

- 注意文明から意味文明へ、AI と情報コスト、エネルギー制約

---

## 採択済み ADR / TS

| ADR | 内容 |
|---|---|
| [ADR-0001](adr/ADR-CATALOG.md) | 注意は有限（Attention Scarcity） |
| [ADR-0002](adr/ADR-CATALOG.md) | 意味＝注意配分のメカニズム |
| [ADR-0003](adr/ADR-CATALOG.md) | 宗教＝注意配分システム |
| [ADR-0004](adr/ADR-CATALOG.md) | ドパガキ＝適応 |
| [ADR-0005](adr/ADR-CATALOG.md) | 利用者≠商品、予測＝商品 |

| TS | 内容 |
|---|---|
| [TS-0001–0003](ts/TS-CATALOG.md) | ドパガキ定義、ドーパミンと探索、SNS スキナー箱 |
| [TS-0004–0006](ts/TS-CATALOG.md) | 注意資本主義、予測市場、大逆転 |

---

## リポジトリ構成

```text
constitution/     憲法（C-0001 〜 C-0008）
adr/              判例（Architecture Decision Records）
ts/               理論仕様（Theory Specifications）
manuscript/       論文本文
meta/             管理・AS-IS / TO-BE
research-log/     研究過程
PROJECT-CONTEXT.md  プロジェクトの起源と転換点
```

---

## はじめに読む順

1. [PROJECT-CONTEXT.md](PROJECT-CONTEXT.md) — なぜこのプロジェクトが始まったか
2. [constitution/CONSTITUTION.md](constitution/CONSTITUTION.md) — ルールと知識の階層
3. [manuscript/part01/ch02-dopamine-is-not-pleasure.md](manuscript/part01/ch02-dopamine-is-not-pleasure.md) — 最初の転換点
4. [manuscript/part02/ch09-attention-scarcity.md](manuscript/part02/ch09-attention-scarcity.md) — 注意は無限ではない
5. [adr/ADR-CATALOG.md](adr/ADR-CATALOG.md) — 採択済みの判断一覧

---

## 参加について

理論的指摘、批判、反証、参考文献の提案を歓迎する（[C-0002 Review First](constitution/C-0002-Review-First.md)）。批判は失敗ではなく、知識の更新である。

- Issue: https://github.com/wombat2006/dopagaki-transition/issues
- Pull Request: https://github.com/wombat2006/dopagaki-transition/pulls

誤字修正や表現改善は PR で。理論の大きな変更は、先に Issue を立ててほしい。

---

## 査読の状態

Draft → Proposed → Review Requested → **Accepted** / Rejected / Superseded

Accepted になった内容だけが、理論仕様（TS）と論文本文（Manuscript）に正式反映される。

---

## ライセンス

[CC0 1.0 Universal](LICENSE) — パブリックドメインへの奉献。
