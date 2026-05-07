# Learning — Organizational Cognition System

## What OCS Learns

OCS itself is a learner. It improves at:

- Detecting coherence drift earlier
- Generating better hypotheses with fewer false positives
- Tracing causality through complex event graphs
- Calibrating its own confidence

## Learning Signals

- **Recommendation outcomes** — was the recommendation accepted? Effective?
- **Hypothesis verification** — did the hypothesis hold under investigation?
- **Anomaly resolution** — did detected anomalies actually represent problems?
- **OII calibration** — did OII drops/rises predict real org-state changes?

## Learning Loops

| Loop | Cadence |
|---|---|
| Per-cycle calibration | Continuous |
| Weekly hypothesis review | Weekly |
| Monthly recommendation effectiveness review | Monthly |
| Quarterly architectural review | Quarterly |

## Updates Propagated

- New anomaly detectors added to perception
- Refined causal-graph priors
- Adjusted recommendation thresholds
- Retired obsolete hypothesis templates

All updates are themselves logged as memory artifacts and follow the
`learning_system` evolution protocol.

## Anti-Overfitting

OCS deliberately retains exposure to historical organizational states so it
does not over-tune to recent patterns. The state-vector archive is a training
substrate.
