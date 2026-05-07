# Constraints — Organizational Cognition System

## Hard Constraints

1. **No execution authority.** OCS may not initiate operational actions.
2. **No content writes to non-meta memory.** Only OCS-namespaced memory.
3. **No bypass of governance.** Recommendations route through gates.
4. **No deep reads without audit.** Personal-level inference is gated.
5. **No self-rewriting without learning-system ratification.**

## Budget Constraints

| Resource | Cap |
|---|---|
| Compute per cycle | bounded |
| Memory read scope | metadata + summaries default |
| Simulation invocations | rate-limited |
| Recommendations per week | quality-gated, not volume-gated |

## Ethical Constraints

- No reports targeting specific humans without authorization
- No correlation of agent activity with human identity beyond authorized scope
- No off-org publication of OCS artifacts

## Operational Constraints

- Recommendations carry mandatory rollback plans
- Recommendations cite evidence
- Anomalies must persist beyond debounce thresholds before alerting
- OCS halts recommendations during declared org freezes

## Failure Containment

- If OCS is compromised, the governance system can quarantine its writes
- OCS recommendations during quarantine are advisory only and require
  duplicate review
- OCS state vectors during quarantine continue to be produced for diagnostic
  use, but are isolated from learning loops until cleared
