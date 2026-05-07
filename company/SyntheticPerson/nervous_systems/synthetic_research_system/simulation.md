# Simulation — Synthetic Research System

This system is a heavy consumer of `simulation_layer/`. It composes:

- `synthetic_person_simulation/` for individual-level questions
- `synthetic_society_simulation/` for population-level questions
- `behavior_prediction/` for short-horizon outcome questions
- `cultural_simulation/` for long-horizon norm questions

Each invocation declares: question, population, treatments, controls,
validity plan, ethical review ID. Outputs are tagged with the simulation
engine version and assumption set.
