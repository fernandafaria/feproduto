# Memory — Market Intelligence System

## Writes

- `collective_memory/market_memory/state/...` — current market state snapshots
- `collective_memory/market_memory/predictions/...` — issued predictions + IDs
- `collective_memory/market_memory/competitors/...` — competitor models
- `collective_memory/market_memory/categories/...` — category graphs
- `collective_memory/research/external/...` — sourced external research

## Reads

- All market_memory namespaces (own)
- `strategic_context/...` (read-only)
- `behavioral_models/segments/...` (read-only)

## Retention

| Artifact | Retention |
|---|---|
| Raw signals | 30d |
| Curated signals | 1y |
| Demand surfaces | 3y |
| Predictions + outcomes | Permanent (calibration) |
| Category graphs | Permanent (versioned) |

## Provenance

Every signal carries `source`, `timestamp`, `confidence`, `license`. Signals
without license info are quarantined.
