# Simulation Layer

The execution surface for simulation. `nervous_systems/simulation_system/`
dispatches contracts to these engines and collects their outputs. Each
engine is independently versioned, calibrated, and bounded.

## Engines

| Engine | Domain |
|---|---|
| `market_simulation/` | Market and adoption dynamics |
| `synthetic_person_simulation/` | Individual-level behavior |
| `synthetic_society_simulation/` | Population-scale dynamics |
| `workforce_simulation/` | Team and cluster dynamics |
| `organizational_simulation/` | Internal change effects |
| `strategic_simulation/` | Multi-step competitive scenarios |
| `behavior_prediction/` | Short-horizon behavioral forecasts |
| `cultural_simulation/` | Long-horizon norm and meaning shifts |
| `risk_simulation/` | Tail risk and cascade dynamics |
| `scenario_engine/` | Multi-engine composed scenarios |

## Per-Engine Anatomy

```
engine.md             # What it is, when to use it
variables.md          # Input variables, ranges, defaults
behavioral_models.md  # Underlying behavioral assumptions
adaptive_loops.md     # In-simulation feedback loops
outputs.md            # Output schema, confidence, sensitivity
confidence_scores.md  # How confidence is computed
premises.md           # Required premises, OOD boundary
validation.md         # Calibration, validation history
ethical_limits.md     # Forbidden uses, ethics gates
```
