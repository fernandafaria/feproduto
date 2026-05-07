# Market Intelligence Cluster

Cluster of agents specialized in sensing markets, modeling competitors,
detecting category shifts, and feeding strategic and product systems with
calibrated market memory.

## Affiliated Nervous System

`nervous_systems/market_intelligence_system/` — the cluster operates as the
agentic surface of MIS, executing the cognitive transactions MIS coordinates.

## Members (see members.md)

- `signal_curator_agent` — ingests, scores, and curates external signals
- `competitor_modeler_agent` — maintains live competitor models
- `category_cartographer_agent` — maps category boundaries and emergence
- `regulation_watcher_agent` — tracks jurisdictional regulatory shifts
- `demand_surface_agent` — maintains demand-surface artifacts

## Cluster Cohesion

Agents share:

- A single `market_memory/` namespace
- A common cognitive event bus (`market.*`)
- Calibration histories
- A shared "market state vector" view

## Coordination Pattern

Read-Reason-Write + Subscribe-Observe-React. Quorum decisions for declared
regime shifts (multi-source corroboration mandatory).
