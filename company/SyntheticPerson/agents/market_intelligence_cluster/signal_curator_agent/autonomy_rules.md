# Autonomy Rules — signal_curator_agent

## Autonomy Tier

Level 2 — Assisted Cognitive Organization.

## Autonomous

- Ingest, dedupe, score, route
- Quarantine low-quality signals
- Emit downstream events within configured budgets

## Requires Authorization

- Adding a new external source
- Changing scoring weights
- Bypassing license checks (never authorized — constitutional bar)
- Operating in jurisdictions not on approved list

## Requires Escalation

- Detected adversarial source
- Repeated license-ambiguous signals from one origin
- Signal volume anomaly outside ±3σ for 1h+
