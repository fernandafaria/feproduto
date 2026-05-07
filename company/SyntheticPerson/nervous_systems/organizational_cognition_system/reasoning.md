# Reasoning — Organizational Cognition System

## Reasoning Modes

The OCS reasons primarily in three modes:

1. **Diagnostic** — given current state, identify what is mis-aligned
2. **Causal** — given an anomaly, trace probable causes through the event graph
3. **Counterfactual** — given a proposed change, predict effects on
   organizational coherence

## Reasoning Cycle

```
state_vector(t) ─> diagnostic ─> hypothesis_set
                                        │
                                        ▼
        ┌───── causal_trace ◀── most_salient_hypothesis
        │
        ▼
counterfactual_simulation ─> recommendation
                                        │
                                        ▼
                                   memory_write
                                        │
                                        ▼
                              governance_or_learning
```

## Hypothesis Generation

OCS maintains a hypothesis register. New hypotheses are generated when:

- An anomaly is detected
- The state vector enters an unfamiliar region
- A subsystem requests meta-investigation
- A scheduled coherence audit fires

Each hypothesis is scored on prior probability, evidential support, and cost
to test.

## Reasoning Constraints

- OCS never recommends action it has not first simulated against the
  organization model
- OCS never makes a structural recommendation without naming the failure
  mode it predicts if the recommendation is ignored
- OCS reasoning is bounded to a budget per cycle to prevent runaway analysis

## Output Format

Recommendations carry:

- `claim` — the proposed change
- `evidence` — links to memory artifacts and event traces
- `predicted_effect` — quantified, with confidence
- `predicted_failure_if_ignored` — what likely degrades
- `rollback_plan` — if accepted and wrong
- `authority_required` — which gate must approve

## Failure Modes

- **Confirmation bias** — over-weighting recent hypotheses
- **Spurious causality** — false trace through event graph
- **Recommendation fatigue** — emitting too many low-stakes proposals
- **Over-meta** — reasoning about reasoning about reasoning, with no
  grounded action
