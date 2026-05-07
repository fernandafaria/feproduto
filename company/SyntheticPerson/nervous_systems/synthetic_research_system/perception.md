# Perception — Synthetic Research System

## What It Senses

- Inbound research questions (event topic `research.request`)
- Population model health (from `simulation_layer/synthetic_society_simulation/`)
- Validation feeds: where real-world outcomes exist, they are matched against
  prior synthetic predictions
- Methodology drift signals (research-quality declines)

## Sensors

- `research_question_intake`
- `population_health_sensor`
- `validation_match_sensor`
- `methodology_drift_sensor`

## Quality Floor

A study cannot be initiated unless:

- Research question is well-formed and ethically reviewed
- Population model is in-distribution for the question
- Calibration history exists (or the study is explicitly exploratory)
- Validation plan is registered
