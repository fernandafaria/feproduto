# Interfaces — Product Evolution System

Pub: `product.feedback_signal`, `product.evolution_proposal`,
`product.friction_alert`, `product.release_event`

Sub: `market.demand_signal`, `human.customer_input`, `research.finding`,
`platform.health_report`, `simulation.product_result`

Memory: RW `collective_memory/product/`; RO market_memory, research, behavioral_models.

API:
```
GET /product/friction?segment={...}
GET /product/proposals?status={...}
GET /product/decisions?since={ts}
```
