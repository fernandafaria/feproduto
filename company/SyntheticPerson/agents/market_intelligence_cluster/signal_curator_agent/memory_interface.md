# Memory Interface — signal_curator_agent

## Reads

- `collective_memory/market_memory/signals/recent`
- `collective_memory/market_memory/sources/reliability`
- `collective_memory/strategic_context/topics/priorities`
- `collective_memory/governance/regulatory_categories`

## Writes

- `collective_memory/market_memory/signals/{date}/{signal_id}.json`
- `collective_memory/market_memory/contradictions/{contradiction_id}.json`
- `meta/agents/mic.signal_curator/audit/...`

## Provenance

Every write includes: agent ID, version, source URL/feed, license info,
ingestion timestamp, scoring inputs, calibration ID.
