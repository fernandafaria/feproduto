# Antifragility Model

## Premise

We design the organization to **gain** from disorder, not merely survive it.
Antifragility is not robustness; robustness is the absence of breakage,
antifragility is the presence of *positive* response to stress.

## The Three Regimes

| Regime | Response to stress |
|---|---|
| Fragile | Worsens, breaks, or collapses |
| Robust | Returns to baseline |
| Antifragile | Improves above baseline |

We design every subsystem with an **antifragile budget**: a tolerance for
small, contained failures whose lessons are folded back into memory and
architecture.

## Sources of Antifragility

### 1. Failure as Memory

Every failure produces a structured memory artifact in
`collective_memory/failures/`. Future transactions retrieve these artifacts
when patterns rhyme.

### 2. Skill Emergence from Edge Cases

Recurrent edge cases that broke the org are converted to dedicated skills.
The org's edge-case competence grows monotonically.

### 3. Simulation of Predicted Stress

The simulation layer continuously rehearses tail scenarios. Stress that has
been simulated is partially survived.

### 4. Redundant Cognitive Pathways

No single agent, skill, or subsystem is a single point of failure on critical
transactions. We accept the duplication cost.

### 5. Heterogeneity

Multiple reasoning models in parallel. Multiple memory representations. The
diversity creates options under stress.

### 6. Hormesis

We deliberately inject small stresses (chaos drills) so the org strengthens
its responses without waiting for real shocks.

## Antifragility Budget

Each subsystem has a documented tolerance:

- Acceptable failure rate
- Maximum blast radius
- Recovery time objective
- Required learning artifact

Failures within budget produce learning. Failures over budget escalate to
governance.

## What Is Not Antifragile

- Identity (we want it stable)
- Ethics (we want them stable)
- Memory integrity (we want it monotonic)
- Authority chains (we want them inviolable)

These are designed for **robustness**, not antifragility.

## Antifragile Design Patterns

### Pattern A — Two-Path Reasoning

Critical reasoning runs on two independent paths. Disagreement is itself
information.

### Pattern B — Shadow Execution

For high-stakes transactions, the system shadow-executes alternatives in
simulation. Outcomes train future decisions.

### Pattern C — Failure Cells

When a subsystem misfires, it is quarantined to a failure cell. The cell is
allowed to fail safely; learnings are extracted; the subsystem rejoins.

### Pattern D — Memory Backflow

Failures backflow into memory immediately, with high salience, so subsequent
transactions cannot ignore them.

## Anti-Patterns

- Over-suppressing variance (we calcify)
- Punishing sub-budget failure (we kill learning)
- Treating failures as PR problems (they are training data)
- Centralizing all stress response (we lose local adaptation)

## Trade-offs

- Antifragility has a steady-state cost: redundancy, simulation, drills.
- Antifragility increases short-term variance.
- Antifragility requires patience: stress today, gain later.

We accept these costs explicitly.

## Indicators

The learning system tracks:

- **Failure→Skill conversion rate**
- **Repeat-failure rate** (should trend down)
- **Mean time to learning artifact**
- **Stress drill survival rate**
