# Interfaces — Synthetic Research System

## Topics

Pub: `research.study_started`, `research.study_complete`, `research.finding`,
`research.methodology_update`, `research.validity_report`

Sub: `strategic.research_request`, `product.research_request`,
`market.research_request`, `governance.ethics_review_outcome`,
`simulation.study_result`

## Memory

- RW: `collective_memory/research/synthetic_studies/`,
  `collective_memory/research/methodologies/`
- RO: `behavioral_models/`, `market_memory/`, `strategic_context/`

## Query API

```
GET /research/studies?topic={...}
GET /research/findings?since={ts}
GET /research/methodologies
GET /research/validity/{study_id}
```
