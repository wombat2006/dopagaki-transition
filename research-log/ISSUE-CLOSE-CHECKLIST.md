# Issue Close Checklist

Project:
ドパガキは模範生

Status:
Canonical

Governed by:
[C-0003 Traceability](../constitution/C-0003-Traceability.md)

---

GitHub Issue を **close する前** に、以下をすべて満たすこと。  
満たさない場合、Traceability 不充足として close してはならない（ISSUE-001 reopen 教訓）。

## Research Log

- [ ] `research-log/ISSUE-{N}-{slug}.md` が存在する
- [ ] **Issue 要約** — 提起者の指摘が書かれている
- [ ] **素案比較** — 検討した案（A/B/C…）が表または箇条書きで列挙されている
- [ ] **棄却理由** — 採用しなかった案それぞれに理由がある
- [ ] **採択理由** — 採用案を選んだ理由が明示されている
- [ ] **決定** — ADR / TS / Manuscript への反映先が書かれている
- [ ] 単一案のみの場合 — 他案を検討しなかった理由が1行以上ある

## 正典への反映

- [ ] 決定どおり ADR / Manuscript（該当ファイル）が **merge 済み**
- [ ] 反映が不要な場合 — Research Log にその理由が書かれている

## GitHub Issue

- [ ] close コメントに **Research Log へのリンク** がある
- [ ] close コメントに **素案比較の要約**（表または3行以内）がある
- [ ] close コメントが **採択結果だけ** になっていない

## 事後

- [ ] Research Log の「次のアクション」が更新されている
- [ ] `research-log/README.md` 索引に行が追加されている（新規 ISSUE の場合）

---

## close コメントテンプレート

```markdown
## 議論結果（案{X} 採択）

Research Log（素案比較）: {URL to ISSUE-N md, #素案比較 anchor}

| 案 | 概要 | 結果 |
|---|---|---|
| A | … | 棄却 — … |
| B | … | 棄却 — … |
| C | … | **採択** |

**採択理由:** …

反映先: …
```

---

## 参照

- [research-log/README.md](README.md) — ISSUE ログ必須項目
- [ISSUE-001](ISSUE-001-attention-capital-constraints.md) — 適用例
