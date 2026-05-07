# Coordination — Synthetic Research System

Publishes: `research.study_complete`, `research.finding`, `research.methodology_update`

Subscribes: `strategic.research_request`, `product.research_request`,
`market.research_request`, `governance.ethics_review_outcome`

## Flow

1. Receive question
2. Submit ethics review (always)
3. On approval, design study
4. Run via simulation system
5. Validate and publish

## Hand-offs

- Findings → strategic, product, market systems
- Methodologies → meta-research memory
