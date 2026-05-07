# Simulation — Market Intelligence System

## Simulation Use

- Competitor scenario runs
- Adoption curve sensitivities
- Demand response under pricing/feature shifts
- Category emergence cascades

## Engines

Hands off to `simulation_layer/market_simulation/` for execution. MIS provides
inputs, receives results, integrates into market state.

## Inputs Provided

- Calibrated priors
- Recent state vectors
- Constraint set (regulatory, ethical)

## Outputs Consumed

- Scenario distributions with confidence
- Sensitivity tables
- Out-of-distribution flags

## Constraints

- No simulation of identifiable customers' future behavior
- No simulation results published as predictions of named competitors' actions
- Market simulation outputs are marked as scenarios, not forecasts
