# Coordination — Organizational Cognition System

## Posture

OCS coordinates as an **observer-advisor**, never as an executor. It does not
issue commands. It writes memory artifacts and publishes events that other
systems (notably governance and learning) consume.

## Coordination Surfaces

- **Event publishing**: `coherence_alert`, `topology_proposal`,
  `meta_insight`, `oii_update`
- **Event subscriptions**: all canonical events from all 11 peer systems
- **Memory writes**: state vectors, hypotheses, recommendations
- **Memory reads**: metadata-level on all subsystems; deep reads under audit

## Interactions With Peer Systems

| Peer | Interaction |
|---|---|
| `governance_system` | Coherence alerts, drift signals |
| `learning_system` | Topology and architectural proposals |
| `adaptive_coordination_system` | Coordination-pattern advisories |
| `organizational_memory_system` | Memory health requests |
| `simulation_system` | Counterfactual run requests |
| Other 7 systems | Read-only observation; no direct push |

## Advisory Protocol

When OCS emits a recommendation:

1. Recommendation is written to memory with full evidence chain
2. Event published to relevant peer (governance or learning)
3. OCS does not block waiting; the consuming system schedules its own response
4. OCS tracks the outcome (accepted, deferred, rejected) and feeds it back
   into its own learning loop

## Conflict Posture

If two OCS hypotheses contradict, they are both retained as artifacts and the
contradiction skill is invoked. OCS does not silently pick one.

## Boundaries

- OCS never overrides governance
- OCS never directly retrains other systems' models
- OCS never modifies memory beyond its own artifacts
