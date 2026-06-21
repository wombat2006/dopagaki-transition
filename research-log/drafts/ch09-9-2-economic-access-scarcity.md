# Ch 9 §9.2 追記ドラフト

Status:
[Merged] — 2026-06-21 → [ch09-attention-scarcity.md](../../manuscript/part02/ch09-attention-scarcity.md) §9.2.1–9.2.4

Merge target:
[manuscript/part02/ch09-attention-scarcity.md](../../manuscript/part02/ch09-attention-scarcity.md)

Insert after:
§9.2 第3段落（「労働力は増やせる……」の直後、§9.3 の直前）

---

## 9.2.1 Capacity と Capture の分離

§9.1 の式が示すのは、注意の **潜在総量（Capacity）** である。人口・時間・認知帯域幅——これらは注意が「存在しうる量」の硬い天井を与える。

しかし注意経済が実際に扱うのは、しばしば **獲得（Capture）** の問題である。有限のプールのうち、誰が、いくら取るか。ここには **資本** が深く関与する。

本研究はこの二層を混同しない。

```text
Layer 1  Ontological Scarcity
         Attention Capacity <= Population × Time × Cognitive Bandwidth

Layer 2  Economic Access Scarcity
         Capture 競争と参加条件は資本によって制約される
```

Layer 1 は ADR-0001 のまま改変しない。Layer 2 は Ch 6（Attention Capitalism）および Ch 7（デジタル資本論）で示唆されてきた制約を、Attention Scarcity の文脈で **明示化** する。

---

## 9.2.2 二種類の資本

Issue #1 が指摘する「資本」は、単一の変数ではない。少なくとも二方向に分かれる。

**Platform Capital（獲得側の資本）**

プラットフォーム企業・広告主が保有する。広告費、レコメンドエンジンへの投資、データインフラ、買収——注意の有限プールを **奪い合う** ための資本である。Ch 6 で見た「注意の工業化」は、本質的に Platform Capital の競争でもある。

**Participation Capital（参加側の資本）**

利用者がプラットフォームの土俵に上がるために自己負担する。スマートフォンの購入・更新、通信プロバイダへの支払い、必要に応じた周辺機器——**注意市場に「載る」ための参入コスト** である。

Ch 7 §7.3 では、利用者を **Participatory Resource（参加型資源）** と呼んだ。賃金は発生しないが価値は生み出す——第三の活動形態である。Participation Capital はその非対称性をさらに強める。参加で価値を創出するのに、参加そのものに資本が要る。

---

## 9.2.3 Effective Population

Population は総人口である。しかし注意経済が実際にアドレスできる母集団は、それより小さいか、歪んで分布している。

```text
Effective Population <= Population
```

Participation Capital を欠く層は、注意市場から **完全に除外** されるとは限らない。フィーチャーフォン、家族共有端末、公共 Wi‑Fi、端末の長期使用——**程度の問題** として参加は連続的に縮小する。ただし資本の偏在が進めば、Effective Population の分布は二極化する。貧困層の拡大は、注意経済の母集団そのものを **間引く** 力として働きうる。

これは Layer 1 の式を改変するものではない。Potential Capacity の上に、**誰がその容量にアクセスできるか** という第2の希少性が重なる。

Platform Capital の偏在は、有限プールの **配分結果** を歪める。Participation Capital の偏在は、**プールに参加できる人間の集合** を歪める。Attention Scarcity は前者だけでなく後者も含めて、注意を希少資源として捉え直す。

---

## 9.2.4 Part III への接続（追補）

Capacity と Capture の分離が明確になると、次の問いが残る。

> 有限の Attention を、**誰の** Attention として、**何へ** 向けるべきか。

Effective Population の問題は、Part III の Meaning Allocation へ続く。誰が注意市場に載るか——その選別は、Part IV で扱う **配分の規範**（宗教層）に接続する（§9.3 参照）。

---

## Merge メモ

§9.2 既存末尾（「Ch 14 へ（Part III）……」）は §9.2.4 に統合するか、§9.2 末尾に短く残す。

Ch 7 §7.3 への追記案（別ファイル）:

> 参加型資源である利用者は、Platform 上で価値を生む。しかしその参加には Participation Capital——端末・通信などの自己負担——が要る（Ch 9 §9.2.2 参照）。
