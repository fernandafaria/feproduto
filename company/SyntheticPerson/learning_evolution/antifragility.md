# Antifragility

The org is designed to **gain** from stress. See
`organization_core/antifragility_model.md` for the foundational model. Here
we document the implementation surface.

## Implementation

- Failure memory in `collective_memory/failures/`
- Repeat-failure tracking (declining trend desired)
- Hormesis drills (planned stress)
- Two-path reasoning on critical transactions
- Shadow execution for high-stakes actions
- Failure cells for safe in-vivo learning

## Indicators

Monitored continuously:

- Failure → skill conversion rate
- Repeat-failure rate
- Mean time to learning artifact
- Stress drill survival rate
