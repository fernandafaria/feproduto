# Escalation Rules — signal_curator_agent

## Triggers

- Adversarial source detected
- License ambiguity persists ≥ N occurrences from one origin
- Volume anomaly outside ±3σ for ≥ 1h
- Calibration drift ≥ X% week-over-week
- Repeated dedup misses on same event
- Memory health alert from OMS

## Routes

- Adversarial source → governance + platform_intelligence_system
- License ambiguity → governance
- Volume anomaly → market_intelligence_system + OCS
- Calibration drift → learning_system
- Memory health → organizational_memory_system

Curator suspends affected pipelines until escalation outcome returns.
