# Sandbox Protocols

## What Sandboxes Are

Bounded execution environments where reversible actions can be performed
without authorization. Sandbox boundaries:

- Authorized memory namespaces (no unauthorized writes)
- Authorized event topics (no out-of-scope publishes)
- Authorized simulation invocations (within budget)
- Authorized side effects (logged, reversible)

## Sandbox Sizes

| Sandbox | Description | Reversibility window |
|---|---|---|
| Reflexive | Per-skill, per-invocation | Stateless |
| Deliberative | Per-agent, per-transaction | Tx-level rollback |
| Cluster | Cluster-wide ad-hoc work | Hour-day |
| Subsystem | Nervous-system-wide changes | Day-week |

## Sandbox Hygiene

- Every sandbox carries a budget
- Every sandbox writes to a transaction log
- Every sandbox commits or rolls back atomically
- Sandbox spillage is a governance event
