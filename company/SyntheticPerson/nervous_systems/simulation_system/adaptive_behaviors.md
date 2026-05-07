# Adaptive Behaviors — Simulation System

## Adaptations

- Routing weights per engine reliability
- Budget allocation per requester quality
- OOD thresholds per engine maturity
- Ethics gate strictness scaled with stakes

## Modes

- **Normal** — standard routing
- **Surge** — high request volume, prioritize critical requesters
- **Conservative** — narrow OOD tolerance, raised gates
- **Audit** — replay-and-validate sweeps

## Self-Healing

- Engine failover via redundant engines
- Stuck requests time out and escalate
- Calibration drift triggers recalibration sweep
