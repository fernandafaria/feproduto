# Purpose — Simulation System

To be the universal simulation invocation layer of the organization. Every
nervous system, agent, or human that needs to "simulate before they decide"
calls this system. It does not own the engines (those live in
`simulation_layer/`); it owns the *contract* — invocation, calibration,
provenance, ethics gates, and result distribution.

## Functions

- Accept simulation requests with structured contracts
- Dispatch to appropriate engine in `simulation_layer/`
- Enforce ethical and budgetary gates
- Record every simulation as a memory artifact
- Maintain calibration histories per engine
- Support replay and reproducibility
