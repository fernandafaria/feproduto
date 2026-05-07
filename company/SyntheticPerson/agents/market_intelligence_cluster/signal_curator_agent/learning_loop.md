# Learning Loop — signal_curator_agent

## Continuous

- Per-signal outcome scoring (was the signal predictive?)
- Source reliability table updates

## Weekly

- Review false-positive rate of quarantines
- Review duplicate-detection misses

## Monthly

- Calibration recalibration window
- Source-list review with `regulation_watcher_agent` and governance

## Inputs to Learning

- Outcome data from downstream (modeler, market system)
- Backtests from `simulation_layer/market_simulation/`
- Failure memory in `collective_memory/failures/market/`

Updates to scoring weights are proposed to the learning system, not applied
unilaterally.
