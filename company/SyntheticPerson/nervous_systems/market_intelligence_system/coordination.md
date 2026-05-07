# Coordination — Market Intelligence System

## Posture

Producer of market memory; consumer for strategic and product systems.

## Topics

Publishes:

- `market.state_update`
- `market.demand_signal`
- `market.competitor_move`
- `market.category_shift`
- `market.regulatory_update`

Subscribes:

- `product.feedback_signal`
- `human.customer_input`
- `governance.policy_change`
- `strategic.thesis_update`

## Hand-offs

- Demand signals → `product_evolution_system`, `strategic_intelligence_system`
- Competitor signals → `strategic_intelligence_system`, narrative cluster
- Regulatory signals → `governance_system`

## Conflicts

When market state contradicts internal strategic thesis, contradiction is
written to memory and surfaced via `ocs.coherence_alert`.
