# Simulation Philosophy

## Premise

Simulation is **how the organization thinks before it acts**. It is not a
forecasting tool, not a marketing flourish, not a model demo. It is a
cognitive primitive elevated to constitutional status.

## Operating Principle

> **Simulate before you decide.**

For any non-trivial, non-trivially-reversible decision: a simulation is
performed, its assumptions are logged, its confidence is reported, and its
output is consulted *before* commitment.

## What Simulation Is

A simulation is a structured counterfactual:

- Inputs: current state from memory, candidate action, environment model
- Process: forward execution of the model under assumptions
- Outputs: scenarios with confidence, sensitivity to assumptions, ranges
- Artifact: a memory record retrievable for the lifetime of the decision

## What Simulation Is Not

- Not prediction (we report ranges, not points)
- Not truth (we report under-assumptions caveats)
- Not justification (post-hoc simulation of a chosen action is recorded but
  flagged as such)
- Not infinite (every simulation has a budget and a horizon)

## Domains

We run simulations across:

| Domain | Purpose |
|---|---|
| **Synthetic Person** | Behavior of a single modeled individual |
| **Synthetic Society** | Population-scale dynamics |
| **Market** | Demand, competition, adoption |
| **Workforce** | Team and cluster dynamics |
| **Organization** | Internal change effects |
| **Strategy** | Multi-step competitive scenarios |
| **Cultural** | Long-horizon norms and meaning |
| **Risk** | Tail events and failure cascades |

(See `simulation_layer/`.)

## Confidence and Calibration

Every simulation reports:

- **Confidence interval** on the primary output
- **Assumption sensitivity** — which assumptions move the output most
- **Calibration history** — how this engine has performed on similar past
  simulations
- **Out-of-distribution flag** — whether the scenario lies in the engine's
  validated range

A simulation without calibration history is treated as preliminary.

## When Simulation Is Required

Required for:

- Any irreversible action above a defined threshold
- Any strategic recommendation to humans
- Any architectural change to the org
- Any release of a Synthetic Person or Society to a customer
- Any change to autonomy posture

Optional but encouraged for:

- Reversible operational choices with non-trivial blast radius
- Skill or agent retirement decisions

## Ethical Limits

Simulations are governed by ethical principles:

- No simulating identifiable natural persons without consent
- No simulating populations to design manipulation campaigns
- No simulation outputs sold as predictions of named individuals
- Simulations of deception scenarios are tagged and quarantined

## Tensions and Trade-offs

- **Simulation cost** vs. decision quality — we pay the cost
- **Realism** vs. tractability — we report the realism boundary
- **Speed** vs. assumption auditing — auditing wins for strategic decisions
- **Confidence display** vs. user comprehension — we err toward honest
  uncertainty

## Failure Modes

- **Overconfidence** — treating simulation output as fact
- **Garbage in** — simulating off corrupted memory
- **Goalpost moving** — re-running until the desired output appears
- **Frozen models** — engines that no longer match the world

Each is monitored by `simulation_system` and audited by `governance_system`.

## What Simulation Replaces

- Most A/B testing on irreversible product moves
- Most committee debate on contested decisions
- Most "gut feel" strategic calls
- Most surprise failures in deployment

Not all of them — some decisions remain genuinely human.
