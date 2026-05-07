# Inter-System Coordination

How nervous systems coordinate:

- **Event bus**: every system publishes canonical events; every system
  subscribes selectively
- **Shared memory**: every system writes to and reads from canonical
  namespaces
- **Governance**: every system gates via the same policy graph
- **OCS**: the meta-cognitive system observes all and surfaces coherence

There is no master scheduler, no orchestrator. Coordination emerges.

## Hand-off Patterns

| Pattern | When |
|---|---|
| Direct event subscription | Continuous flows |
| Memory-mediated | When persistence required |
| Co-simulation | When joint reasoning needed |
| Escalation chain | When authority required |
