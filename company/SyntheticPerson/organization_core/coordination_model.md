# Coordination Model

## Premise

Coordination is **not** orchestration. We do not coordinate by routing tasks
through a central scheduler. We coordinate by **shared context**: when every
subsystem reads from the same memory and listens to the same event bus,
coordinated behavior emerges without instruction.

## Mechanisms

### 1. Shared Context

Every nervous system, agent, and skill reads from the same `collective_memory`.
Stale context is the root cause of most coordination failure; we attack it by
making memory live, fresh, and attributable.

### 2. Event Bus

Subsystems publish *cognitive events* to a global bus:

- `Observation` — a perception worth recording
- `Hypothesis` — a model proposing an interpretation
- `Decision` — an action committed
- `SimulationResult` — output of a simulation
- `Escalation` — a request for human or higher-authority adjudication
- `MemoryWrite` — a memory artifact created
- `Contradiction` — detected inconsistency

Subscribers self-select; there is no central dispatcher.

### 3. Intent Propagation

Each agent broadcasts its current intent. Other agents adjust their plans by
reading the intent stream, not by being assigned tasks.

### 4. Context Compression

Because everything is shared, compression matters. The `context_compression_skill`
runs continuously to keep the shared context tractable.

### 5. Conflict Detection

The contradiction skill scans memory and intent streams. When two subsystems
hold incompatible intents, the coordination layer triggers reconciliation.

## Coordination Patterns

### Pattern A — Read-Reason-Write

Default for stateless cognition. Agent reads context, reasons, writes back.
No explicit handoff.

### Pattern B — Subscribe-Observe-React

Agent subscribes to a class of events, observes them passively, reacts when a
trigger pattern matches.

### Pattern C — Co-simulate

Two or more agents enter a shared simulation environment, propose moves, and
emerge with a consensus output. Used for strategic transactions.

### Pattern D — Escalate-Wait-Resume

Agent reaches an authority gate, escalates to humans or governance, suspends,
resumes when authorization or denial returns.

### Pattern E — Quorum Decision

For decisions requiring multiple specialist agents, a quorum forms ad-hoc and
dissolves on resolution.

## Anti-patterns

- Synchronous handoffs between agents
- Assigning tasks via a central planner
- Polling each other for state instead of subscribing to events
- Decisions taken without writing intent first
- Acting on stale memory snapshots

## Human-Inclusive Coordination

Humans participate in coordination via:

- Subscriptions to escalation events
- Direct writes to memory (logged as human-origin)
- Strategic intent broadcasts
- Authorization responses on gated transactions

Humans never become bottlenecks at the operational level; they only gate
escalations.

## Trade-offs

- **Eventual consistency** — shared memory is not strictly synchronous; we
  pay reconciliation cost for resilience.
- **Discovery cost** — without a dispatcher, agents must self-organize; we
  invest in good intent broadcasting to keep this cheap.
- **Backpressure** — high event volumes can drown subsystems; we use topic
  filters and importance scoring.

## Failure Modes

- **Echo chambers** — clusters that only listen to each other
- **Silent partitions** — subsystems whose reads succeed but writes fail
- **Intent shadowing** — newer intents overwriting older without reconciliation
- **Coordination thrash** — oscillation between conflicting consensus states

All are monitored by the `adaptive_coordination_system`.
