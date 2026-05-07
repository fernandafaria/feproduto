# Reasoning — Market Intelligence System

## Reasoning Modes

1. **Demand modeling** — surfaces of willingness, urgency, segment behavior
2. **Competitive simulation** — likely competitor moves under scenarios
3. **Category cartography** — boundaries, adjacencies, emergence
4. **Reflexivity reasoning** — accounting for market self-fulfilling effects

## Models

- Demand surface model per product family
- Adoption-curve model per Synthetic Person / Society offering
- Competitor move-prior models
- Category-graph model

## Cycle

```
signals ──► dedup/score ──► model update ──► simulation ──► prediction
                                                       ╲
                                                        └─► strategic memory write
```

## Calibration

Every prediction is paired with a calibration ID. Outcomes are scored
(Brier-style) and feed back into priors. The system tracks its own
overconfidence ratio.

## Constraints

- No market reasoning that depends on private illegitimate signals
- No reasoning over individual identifiable persons in market data
- Predictions outside calibrated range are flagged and de-rated
