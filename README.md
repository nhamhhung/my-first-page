# my-first-page

A governed **web** (python, owner: ocean@torilab.ai) — Web app: password login, dashboard, one bounded 'Ask AI' action.

```bash
pip install -r requirements.txt && uvicorn app:app --port 8080     # keyless: the connector seam falls back to the simulator
python3 -m unittest discover -s tests -q
```

`GET /healthz` is a secret-free liveness check. `GET /.well-known/agent-card.json` is the A2A
discovery card. The single LLM call is bounded through the guardrails module.

## Contract

`agent.yaml` is the thin `platform.solo-unicorn.ai/v1` Workload contract: Docker facts, the HTTP
interface + `/healthz`, and env NAMES. Governance, deploy placement, monitoring, and the
kill-switch are **platform guarantees** held server-side. Check it with the `compliance-check` skill.
