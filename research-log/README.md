# Research Log

Project:
ドパガキは模範生

Repository:
dopagaki-transition

Status:
Active

---

Research Log は **採択前の議論・査読・Issue 対応** の痕跡を残す（[META-SPECIFICATION.md](../meta/META-SPECIFICATION.md) §7）。

議論の透明化は [C-0003 Traceability](../constitution/C-0003-Traceability.md) により義務付けられる。採択結果だけでなく、**検討した代替案と棄却理由** を残す（[C-0002 Review First](../constitution/C-0002-Review-First.md)、[C-0005 Reproducibility](../constitution/C-0005-Reproducibility.md) と併読）。

## ISSUE ログ必須項目

| 節 | 内容 |
|---|---|
| Issue 要約 | 提起者の指摘 |
| 素案比較 | 検討した案（A/B/C…）の概要 |
| 棄却理由 | 各案を採らなかった理由 |
| 採択理由 | 採択案を選んだ理由 |
| 決定 | ADR / Manuscript への反映 |
| 次のアクション | merge、Issue close 等 |

**Issue close 前:** [ISSUE-CLOSE-CHECKLIST.md](ISSUE-CLOSE-CHECKLIST.md) の全項目を確認すること（[C-0003](../constitution/C-0003-Traceability.md)）。

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
| [ISSUE-001](ISSUE-001-attention-capital-constraints.md) | Attention が制約される要因の欠如 | Merged（案C） | ADR-0001, Ch 9 |
| [RL-20260621](RL-20260621-knowledge-filter-mcp.md) | Knowledge Filter — API 比較と MCP 方針 | **Closed**（stub） | O-P002-004, D-002, mcp/glossary-knowledge |
