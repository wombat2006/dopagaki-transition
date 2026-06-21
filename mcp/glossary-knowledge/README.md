# Glossary Knowledge Filter MCP

Status:
**Stub** — NullProvider only. Discussion closed 2026-06-21; resume at Phase 2.5.

Related:
[RL-20260621](../../research-log/RL-20260621-knowledge-filter-mcp.md)
[D-002](../../meta/glossary-pipeline/DECISIONS.md#d-002)
[meta/glossary-pipeline/mcp/README.md](../../meta/glossary-pipeline/mcp/README.md)

---

## Purpose

MCP server for **general / domain / unknown** term classification. Glossary pipeline and Cursor call this server instead of embedding API clients in `scripts/glossary/`.

**Current behavior:** all terms → `unknown` (NullProvider). Safe default until a real provider is chosen.

---

## Setup

**Requires Python >= 3.10** (`mcp` package).

```bash
python3 -m pip install -r mcp/glossary-knowledge/requirements.txt
```

Provider logic only (no MCP SDK — smoke test on 3.9):

```bash
cd mcp/glossary-knowledge
PYTHONPATH=. python3 -c "
from glossary_knowledge_mcp.providers import ProviderRegistry
r = ProviderRegistry.from_config()
print(r.classify('探索').to_dict())
"
```

Optional config (copy example):

```bash
cp mcp/glossary-knowledge/providers.json.example mcp/glossary-knowledge/providers.json
```

---

## Run (stdio)

```bash
python3 -m glossary_knowledge_mcp
# from mcp/glossary-knowledge/:
cd mcp/glossary-knowledge && PYTHONPATH=. python3 -m glossary_knowledge_mcp
```

---

## Cursor MCP config (example)

Add to `.cursor/mcp.json` (project or user):

```json
{
  "mcpServers": {
    "glossary-knowledge": {
      "command": "/absolute/path/to/dopagaki-transition/.venv/bin/python",
      "args": ["-m", "glossary_knowledge_mcp"],
      "cwd": "/absolute/path/to/dopagaki-transition/mcp/glossary-knowledge",
      "env": {
        "PYTHONPATH": "/absolute/path/to/dopagaki-transition/mcp/glossary-knowledge"
      }
    }
  }
}
```

Use the project venv Python so `mcp` and dependencies resolve.

---

## Tools

| Tool | Description |
|---|---|
| `classify_term` | Single term → `{ term, label, confidence, reason, provider_id, cached }` |
| `classify_batch` | `{ results[], count }` |
| `list_providers` | `{ providers[] }` |
| `get_cache_stats` | Stub — cache not implemented |

Labels: `canonical` | `domain` | `general` | `unknown`

---

## Layout

```text
mcp/glossary-knowledge/
  README.md
  requirements.txt
  providers.json.example
  glossary_knowledge_mcp/
    __main__.py      … stdio entry
    server.py        … MCP tools
    providers.py     … NullProvider + registry
    models.py
```

---

## Not implemented (deferred)

- SQLite cache (`T2.5-3`)
- Wikipedia / LLM / stats adapters
- `glossary_extractor.py` MCP client integration
- First provider selection (K-003 / K-006 / K-008)

Re-open discussion when starting Phase 2.5.
