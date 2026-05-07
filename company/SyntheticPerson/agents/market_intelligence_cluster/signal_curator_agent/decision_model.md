# Decision Model — signal_curator_agent

## Decisions Made

- Whether to ingest a given signal
- Score assignment
- Routing tags
- Quarantine vs accept
- Emit downstream event vs. log only

## Decision Authority

All decisions reflexive within sandbox. No strategic decisions. No human-facing
decisions.

## Confidence Reporting

Every decision carries a calibration-tagged confidence. Decisions below
confidence floor are routed for review by `competitor_modeler_agent` or
`category_cartographer_agent` rather than acted on.

## Reversibility

- Ingestion: reversible within retention window
- Quarantine: reversible by curator with audit
- Event emission: irreversible (consumers may have acted), but retraction
  events can be emitted
