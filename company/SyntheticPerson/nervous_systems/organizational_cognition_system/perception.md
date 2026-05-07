# Perception — Organizational Cognition System

## What It Senses

The OCS senses **the organization itself**, not the external world. Its
sensory surface is internal:

- Event bus traffic (volumes, patterns, anomalies)
- Memory write rate, types, provenance distribution
- Decision throughput per cognitive level
- Escalation rate per subsystem
- Simulation invocations, costs, and outcomes
- Contradiction frequency and resolution latency
- Inter-system message graphs

## Sensors

| Sensor | Source | Cadence |
|---|---|---|
| `event_volume_sensor` | Event bus | Continuous |
| `memory_health_sensor` | `organizational_memory_system` | 5-minute |
| `decision_flow_sensor` | Governance logs | Continuous |
| `simulation_outcome_sensor` | `simulation_system` | Per-sim |
| `coherence_sensor` | Contradiction skill | Continuous |
| `topology_sensor` | Coordination layer | Hourly |

## Signal Processing

Signals are filtered, normalized, and embedded into the **organizational
state vector**, a compressed representation of the org's cognitive condition.
The state vector is itself a memory artifact, versioned per snapshot.

## Anomaly Detection

OCS runs ongoing anomaly detection on:

- Sudden drops in event volume from any subsystem
- Memory write spikes (possible poisoning)
- Escalation spikes (possible governance failure)
- Simulation cost overruns
- Coherence drops below threshold

Anomalies are emitted as `coherence_alerts`.

## Boundaries

- OCS does not read the *content* of all memory; it reads metadata, headers,
  and aggregated summaries. Deep reads are performed only when investigating
  a specific anomaly with authorization.
- OCS does not sense the external environment. That is the job of
  `market_intelligence_system` and others.

## Failure Modes

- **Sensor blindness** when subsystems fail to emit canonical events
- **Signal saturation** under high load (mitigated by importance scoring)
- **Aggregate masking** where averages hide local pathologies
