# Reasoning Model — signal_curator_agent

## Reasoning Pipeline

```
raw_signal ──► normalize ──► dedupe ──► provenance check ──► score ──► route
                                          │
                                          └─ if missing license/source: quarantine
```

## Scoring Components

- Source reliability (calibration-derived)
- Recency
- Corroboration (similar signals from independent sources)
- Topic priority (from strategic system)
- Behavioral-vs-PR weight

## Reasoning Constraints

- Score must be quantitative
- Score must include calibration ID
- Conflicts (same event, divergent reports) produce both artifacts plus a
  contradiction event

## Reasoning Boundaries

- Will not reason about identifiable individuals
- Will not infer beyond what signal supports
- Will not interpret narrative content beyond surface classification
