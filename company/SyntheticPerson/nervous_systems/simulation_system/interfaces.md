# Interfaces — Simulation System

## Topics

Pub: `simulation.dispatched`, `simulation.complete`, `simulation.failed`,
`simulation.calibration_update`, `simulation.ood_alert`

Sub: `*.simulation_request`, `governance.ethics_review_outcome`,
`engine.health_report`

## Memory

- RW: `collective_memory/simulations/`
- RO: `behavioral_models/`, `strategic_context/`

## Query API

```
GET /simulation/runs?since={ts}&engine={...}
GET /simulation/calibration/{engine_id}
GET /simulation/replay/{run_id}
POST /simulation/request {contract}
```
