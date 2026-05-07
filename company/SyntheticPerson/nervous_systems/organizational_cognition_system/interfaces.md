# Interfaces — Organizational Cognition System

## Public Contracts

### Event Topics (publishes)

| Topic | Payload | Consumers |
|---|---|---|
| `ocs.coherence_alert` | `{anomaly, severity, evidence, suggested_owner}` | governance, learning |
| `ocs.topology_proposal` | `{change, evidence, predicted_effect, rollback}` | learning, governance |
| `ocs.oii_update` | `{components, trend, contributors}` | human layer, dashboards |
| `ocs.meta_insight` | `{insight, salience, lifespan}` | learning, human layer |

### Event Topics (subscribes)

- `*.observation` (all)
- `*.decision` (all)
- `*.escalation` (all)
- `governance.policy_change`
- `learning.evolution_event`
- `memory.health_report`

### Memory Contracts

- Namespace `meta/ocs/state/`: read-write
- Namespace `meta/ocs/recommendations/`: append-only
- Namespace `meta/ocs/oii/`: append-only
- All other namespaces: read-only

### Query API

```
GET /ocs/oii?since={ts}
GET /ocs/recommendations?status={open|accepted|rejected}
GET /ocs/state-vector?at={ts}
GET /ocs/hypotheses?topic={...}
```

(Query interface is internal-only; not exposed externally.)

## Versioning

- All artifacts versioned with `ocs_version` field
- Schema changes follow learning-system protocol
- Breaking changes require human ratification

## SLOs

- Coherence alert latency: target < 60s from sensor signal
- OII update freshness: ≤ 5 minutes
- Recommendation evidence completeness: 100%
- Recommendation rollback-plan presence: 100% (constitutional)
