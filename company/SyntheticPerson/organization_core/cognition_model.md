# Organizational Cognition Model

## Definition

Organizational cognition is the continuous process by which the organization
**perceives** its environment, **reasons** over its memory, **simulates**
candidate futures, **decides** within authority bounds, **acts**, **observes**
outcomes, and **updates** memory.

## The Cognitive Loop

```
   ┌──────────┐    ┌──────────┐    ┌────────────┐
   │ Perceive │ ─> │ Memorize │ ─> │  Reason    │
   └──────────┘    └──────────┘    └────────────┘
        ▲                                │
        │                                ▼
   ┌──────────┐    ┌──────────┐    ┌────────────┐
   │ Observe  │ <─ │   Act    │ <─ │  Simulate  │
   └──────────┘    └──────────┘    └────────────┘
                                         │
                                         ▼
                                   ┌────────────┐
                                   │   Decide   │
                                   └────────────┘
```

The loop runs continuously across **every** subsystem. There is no batch mode.

## Cognitive Levels

| Level | Time horizon | Subsystems involved | Authority |
|---|---|---|---|
| **Reflexive** | < 1s | Skills, single agent | Autonomous |
| **Deliberative** | seconds — minutes | Agent cluster | Autonomous within sandbox |
| **Strategic** | minutes — hours | Multiple nervous systems | Human ratification |
| **Existential** | days — months | Whole org + human layer | Human authority |

Each cognitive transaction is tagged with its level, which determines its
authority path and memory persistence policy.

## Memory as Cognitive Substrate

Cognition is not implemented in any single agent. It is implemented in the
**round trip through memory**. An agent that does not write its reasoning to
memory is, by definition, not contributing to organizational cognition.

This implies:

- All meaningful reasoning produces a memory artifact
- All decisions cite the memory artifacts they consulted
- All simulations produce memory artifacts that survive the simulation

## Reasoning Modes

The org supports five reasoning modes, selected per transaction:

1. **Retrieval** — pattern-match against memory
2. **Compositional** — combine memory artifacts
3. **Counterfactual** — simulate alternatives
4. **Causal** — trace effects through the knowledge graph
5. **Reflective** — reason about reasoning (meta)

Each mode has a corresponding skill family in `skills/`.

## Coherence Mechanism

Coherence is enforced by:

- Single source of truth for memory
- Contradiction detection skill running continuously
- Periodic coherence audits by the governance system
- Refusal to act when contradiction is detected above threshold

## Bounded Cognition

Cognition is bounded by:

- **Compute budget** per cognitive level
- **Memory access limits** for cost control
- **Simulation horizon** caps for tractability
- **Authority gates** at each level boundary

When bounds are hit, the system escalates rather than degrades silently.

## Failure Modes

- **Hallucinated cognition** — outputs without memory grounding
- **Stuck loops** — perception without action or update
- **Action without simulation** when policy required it
- **Reasoning without retrieval** when memory was relevant

Each is detectable and triggers escalation per `governance_system/`.

## Trade-offs

- Deeper reasoning costs latency and compute; bounded by level budgets.
- Aggressive memorization risks pollution; bounded by compression skills.
- Autonomous action speeds throughput; bounded by reversibility checks.
