# Coordination — Simulation System

Pub: `simulation.dispatched`, `simulation.complete`, `simulation.failed`,
`simulation.calibration_update`

Sub: `*.simulation_request`, `governance.ethics_review_outcome`,
`engine.health_report`

## Hand-offs

- Routes to engines in `simulation_layer/`
- Returns results to requester via correlation ID
- Forwards calibration outcomes to `learning_system`
