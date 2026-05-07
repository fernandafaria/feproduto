# Reasoning — Simulation System

## Modes

- **Routing reasoning** — which engine fits the request
- **Budget reasoning** — fit within compute and time bounds
- **Validity reasoning** — is this question in-distribution
- **Ethics reasoning** — is the simulation permissible

## Cycle

```
request ──► validate ──► ethics_gate ──► route ──► dispatch ──► collect ──► calibrate ──► return
```
