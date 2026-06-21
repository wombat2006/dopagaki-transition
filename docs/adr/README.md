# ADR: Architecture Decision Records

このディレクトリでは、『ドパガキ・トランジション』における重要な理論判断、構成判断、概念変更を ADR として管理する。

ADR は単なるメモではなく、本文・理論仕様・査読履歴・Gate 判定へ接続される意思決定記録である。

## 目的

ADR の目的は次の通り。

- なぜその理論判断を採用したかを残す
- 後続章への影響範囲を明示する
- 査読コメントから理論変更までの経緯を追跡可能にする
- TS、Gate、Manuscript、Research Log との接続点を作る

## ADR と他ドキュメントの関係

```text
ADR
↓
TS
↓
Gate
↓
Manuscript
↓
Research Log
```

- ADR: 意思決定の理由と影響
- TS: 採用済み理論の仕様・定義
- Gate: リリース判定条件
- Manuscript: 本文への反映先
- Research Log: 思考過程・査読過程・議論の痕跡

## 命名規則

```text
ADR-0001-attention-scarcity.md
ADR-0002-meaning-allocation.md
ADR-0003-religion-layer.md
```

## Status

ADR の状態は以下を使用する。

- Proposed
- Accepted
- Rejected
- Superseded

Accepted となった ADR のみ、本文・TS・Gate へ正式反映する。

## 推奨構成

各 ADR は以下の構成を基本とする。

```markdown
# ADR-0001: Title

## Status

Accepted

## Context

なぜこの判断が必要になったか。

## Decision

採用した判断。

## Reason

判断理由。

## Consequences

この判断によって何が変わるか。

## Affected Files

- manuscript/...
- docs/ts/...

## Related

- docs/gates/...
- docs/research-log/...
```

## 初期 ADR 候補

- ADR-0001: Attention Scarcity
- ADR-0002: Meaning Allocation
- ADR-0003: Religion as Attention Allocation System
