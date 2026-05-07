# Memory — Organizational Cognition System

## Memory Footprint

OCS reads broadly but writes narrowly. It is a heavy reader, light writer.

### Reads

- All event-bus headers and metadata
- All memory artifact headers (provenance, type, salience)
- Aggregated summaries from `organizational_memory_system`
- Deep content reads only with audit trail

### Writes

| Artifact type | Frequency | Retention |
|---|---|---|
| `state_vector` | Per cycle | 90d rolling, then summarized |
| `hypothesis` | As generated | Until resolved or expired |
| `recommendation` | As emitted | Permanent (constitutional log) |
| `coherence_alert` | Event-driven | 1y, then summarized |
| `meta_insight` | Curated | Permanent |
| `oii_update` | Continuous | Aggregated daily |

## Provenance

Every OCS artifact is signed by the OCS instance (with version, timestamp,
input hash). Provenance enables future replay and accountability.

## Compression Strategy

OCS state vectors are highly compressible — most cycles are similar to the
last. Compression: store deltas, snapshot full vector daily, full-fidelity
weekly.

## Privacy Considerations

OCS reads metadata broadly; this could enable inferences about specific
agents or humans. Therefore:

- OCS may not produce reports about *individual* humans without explicit
  authorization from `human_layer/`
- OCS may produce reports about agent clusters, subsystems, or aggregates

## Memory Ethics

OCS is constitutionally barred from suggesting memory deletions; it may only
propose archival. Deletion authority lies elsewhere.
