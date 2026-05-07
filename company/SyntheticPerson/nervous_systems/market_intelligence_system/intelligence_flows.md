# Intelligence Flows — Market Intelligence System

## Flows

### Flow 1 — Sense → Synthesize

```
external streams + internal telemetry ──► dedup ──► score ──► model update ──► state vector
```

### Flow 2 — Predict → Validate

```
state vector ──► simulation ──► prediction ──► outcome (post-hoc) ──► calibration update
```

### Flow 3 — Alert

```
anomaly in signal stream ──► debounce ──► competitor_move or category_shift event ──► strategic + humans
```

### Flow 4 — Reconcile with Strategy

```
market state ──► compared against strategic thesis ──► if contradiction ──► coherence alert
```

## Cross-System

- Provides ground for `strategic_intelligence_system`
- Feeds `product_evolution_system` demand-side context
- Feeds narrative cluster competitive context
- Receives strategic theses to test

## Volume Profile

- High-volume signal in
- Medium-volume curated artifacts out
- Low-volume strategic events out
