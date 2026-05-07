# Adaptive Behaviors — Organizational Cognition System

## Adaptation Targets

OCS adapts:

- Sensor sampling rates per signal volatility
- Anomaly thresholds per false-positive rate
- Recommendation cadence per acceptance rate
- Simulation depth per organizational change rate

## Adaptive Behaviors

### Behavior 1 — Quiet Mode

When the org is stable (low contradiction, low escalation, OII trend flat),
OCS reduces signal output. Stability is not silence; it is restraint.

### Behavior 2 — Investigative Mode

When an anomaly persists, OCS deepens its read scope (with audit), increases
sampling, and queues additional simulations.

### Behavior 3 — Backoff Mode

If OCS recommendations are repeatedly rejected, it backs off, examines its
own priors, and re-baselines before resuming. The system has a built-in
humility loop.

### Behavior 4 — Heartbeat Mode

OCS emits a heartbeat to the governance system. If governance loses the
heartbeat, OCS is treated as down and a fallback advisory mode engages.

### Behavior 5 — Quarantine Mode

If OCS is suspected of malfunction, it self-quarantines: writes flagged,
recommendations blocked, only diagnostic outputs continue.

## Self-Healing

- Sensor restart on signal gap
- Memory namespace re-validation on schema mismatch
- Simulation cache rebuild on staleness detection
- Hypothesis register pruning on overload

## Limits of Adaptation

OCS may not autonomously:

- Change its constitutional purpose
- Expand its execution authority
- Promote itself in topology
- Modify governance contracts

These remain in `learning_system` and `human_layer/`.
