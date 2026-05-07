# Memory — Simulation System

## Writes

- `collective_memory/simulations/runs/...` — every run, with inputs, outputs,
  engine version, calibration ID
- `collective_memory/simulations/calibration/...` — per-engine calibration
  histories
- `collective_memory/simulations/replays/...` — replayable artifacts

## Retention

- Run records: permanent (replay + audit)
- Calibration: permanent
- Raw intermediate state: retention window per engine
