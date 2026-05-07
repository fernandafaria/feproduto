# Members — Market Intelligence Cluster

| Agent | Role | Status |
|---|---|---|
| `signal_curator_agent` | Continuous ingestion, dedup, scoring of external signals | Active |
| `competitor_modeler_agent` | Maintains competitor move-prior models | Active |
| `category_cartographer_agent` | Category graph + emergence detection | Active |
| `regulation_watcher_agent` | Regulatory feed tracking + impact mapping | Active |
| `demand_surface_agent` | Demand surface artifact maintenance | Active |
| `narrative_signal_agent` | External narrative monitoring (cross-cluster) | Shared |

Detailed cognitive contracts for the first two appear in their respective
folders. The remaining agents follow the same template structure and will be
promoted to fully-detailed contracts as their transaction patterns
stabilize.

## Cluster Promotion Watchlist

Patterns under observation for possible promotion to dedicated agents:

- `pricing_radar_agent` (currently a skill in `skills/system_specific/market/`)
- `partnership_signal_agent` (skill-level)
- `talent_market_agent` (skill-level)
