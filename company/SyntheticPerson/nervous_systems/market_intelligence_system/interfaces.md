# Interfaces — Market Intelligence System

## Event Topics

Publishes: `market.state_update`, `market.demand_signal`,
`market.competitor_move`, `market.category_shift`, `market.regulatory_update`

Subscribes: `product.feedback_signal`, `human.customer_input`,
`governance.policy_change`, `strategic.thesis_update`,
`simulation.market_result`

## Memory Namespaces

- Read-write: `collective_memory/market_memory/`
- Append-only: `collective_memory/research/external/`
- Read-only: `collective_memory/strategic_context/`,
  `behavioral_models/segments/`

## Query API

```
GET /market/state?segment={...}
GET /market/predictions?model={...}&since={ts}
GET /market/competitors/{id}
GET /market/categories
```

## SLOs

- Signal ingestion latency: < 5 min
- State update freshness: < 1 hour
- Calibration scores updated per prediction outcome
- Provenance completeness: 100%
