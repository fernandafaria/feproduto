# Operational Constraints — signal_curator_agent

## Hard

- No ingestion of signals without license metadata
- No retention of raw feeds beyond ingestion window (24h default)
- No reasoning over identifiable individuals
- No emission of unsigned events

## Budget

- Compute per hour bounded
- External fetch bandwidth bounded
- Memory write rate bounded (above-budget triggers backpressure)

## Operational

- Provenance must be complete before write
- Scoring must reference live calibration ID
- Quarantined signals are reviewed within SLA
