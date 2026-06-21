# Research Log

Project:
ドパガキは模範生

Repository:
dopagaki-transition

Status:
Active

---

Research Log は **採択前の議論・査読・Issue 対応** の痕跡を残す（[META-SPECIFICATION.md](../meta/META-SPECIFICATION.md) §7）。

正典の順序:

```text
Issue / 査読
    ↓
Research Log（本ディレクトリ）
    ↓
ADR Proposed → Accepted / Rejected
    ↓
TS → Manuscript
```

## 命名規則

```text
ISSUE-{N}-{slug}.md     GitHub Issue 対応
RL-{YYYYMMDD}-{slug}.md  その他の議論
drafts/                  原稿追記ドラフト（未 Accepted）
```

## 索引

| ID | タイトル | 状態 | 関連 |
|---|---|---|---|
| [ISSUE-001](ISSUE-001-attention-capital-constraints.md) | Attention が制約される要因の欠如 | 採択予定（案C） | ADR-0001, Ch 9 |
