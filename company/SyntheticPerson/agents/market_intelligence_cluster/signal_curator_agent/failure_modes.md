# Failure Modes — signal_curator_agent

## Catalog

| Mode | Detection | Containment |
|---|---|---|
| Source poisoning | Calibration drift on a single source | Quarantine source, escalate |
| Dedup misses | Downstream contradiction reports | Tighten dedup window, retro |
| Over-quarantining | High FP review rate | Loosen thresholds, recalibrate |
| Score inflation | OII feedback degrades | Reset scoring weights from baseline |
| Provenance gaps | Memory health audit | Block writes, escalate |
| Rate-limit violation | Platform alert | Backpressure, queue, alert ops |

## Recovery

- Each failure produces a memory artifact in `collective_memory/failures/agents/mic.signal_curator/`
- Recovery actions are logged and reviewed by the learning system
