# Intelligence Flows — Organizational Cognition System

## Primary Flows

### Flow 1 — Continuous Health

```
event bus ──► sensors ──► state vector ──► OII ──► dashboard
                                       ╲
                                        └──► anomaly detector ──► alert
```

### Flow 2 — Hypothesis to Recommendation

```
anomaly ──► hypothesis ──► causal trace ──► simulation ──► recommendation ──► governance/learning
                                                              │
                                                              └──► memory write
```

### Flow 3 — Outcome Feedback

```
recommendation ──► (accepted / rejected / deferred) ──► OCS learning loop ──► refined priors
```

### Flow 4 — Meta-Insight Curation

```
state archive + hypothesis archive ──► weekly synthesis ──► meta-insight ──► human digest
```

## Information Volume

OCS receives orders of magnitude more signal than it emits. This asymmetry is
intentional. The work is **distillation**.

## Bottlenecks Anticipated

- **Causal trace expense** under high event-volume periods
- **Simulation queue contention** during architectural proposals
- **Human-digest backlog** if humans disengage from review

## Cross-System Choreography

OCS does not orchestrate; it advises. The pattern is:

- OCS emits → consuming system schedules → response logged → OCS observes → OCS learns

There is no synchronous waiting.
