# Part II — Chapter 9

# Attention Scarcity

Status:
[Accepted Manuscript]

Target:
5,500字

Depends On:
ADR-0001 Attention Scarcity

Related TS:
TS-0004 Attention Capitalism

---

## 9.1 Attention Inflation 棄却

Attention Economy には暗黙の前提がある。

Attention は無限に増やせる。情報が増えれば、注意も増える。新しいプラットフォームが生まれれば、新しい注意の池が生まれる。

本プロジェクトはこの前提を **Attention Inflation** と呼び、棄却する（ADR-0001）。

```text
Attention ≠ ∞
∵ 母集団が総人口によって制限されるから
```

Attention Capacity は以下で上限が決まる。

```text
Attention Capacity <= Population × Time × Cognitive Bandwidth
```

- **Population:** 注意を向けられる主体は、総人口を超えない
- **Time:** 1人あたりの注意可能時間は24時間を超えない
- **Cognitive Bandwidth:** 同時処理可能な注意量は神経系によって制約される

情報は無限に近づきうる。コンテンツは複製できる。AI は生成を加速する。

しかし Attention は有限である。

情報のインフレと Attention の有限性——この非対称が、注意経済の根本矛盾である。

---

## 9.2 希少資源としての注意

Attention Capitalism（Ch 6）は注意を主要資産とした。しかし資産が「希少」であることを明示していなかった。

Attention Scarcity はその補正である。

注意市場の総量は、人口によって天井が設定される。新規ユーザーの獲得競争は、本質的に **ゼロサムに近い競争** である。あるプラットフォームが注意を獲得すれば、別のプラットフォームは失う。

労働価値説（Ch 7）では説明できなかった制約が、ここで初めて登場する。

労働力は増やせる（人口増、労働参加率向上）。注意は増やせない——少なくとも人口×時間×認知帯域幅の範囲内では。

Ch 10 へ: 注意が有限であるとき、プラットフォームは何を商品化するか。

Ch 14 へ（Part III）: 有限 Attention の配分規則としての Meaning。

---

## 9.3 宗教学への接続（予告）

Attention Scarcity が成立すると、次の問いが生じる。

> 有限の Attention を、何へ向けるべきか。

これは経済学の問いであると同時に、**配分の規範**に関する問いである。何を神聖視し、何を禁じ、何に時間を捧げるか——宗教は historically、この問いに答える制度だった（ADR-0003, Part IV 参照）。

Attention ≠ ∞ であることの確認は、意味経済および宗教層への接続条件である。宗教学的な論じ方は Part IV で展開する。
