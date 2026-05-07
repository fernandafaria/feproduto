# Contextual Redistribution

When the working context exceeds an agent's budget, context is redistributed
across peer agents. Redistribution rules:

- Salience-preserving: high-salience artifacts replicate; low-salience
  refer-by-handle
- Authority-preserving: redistribution does not expand any agent's scope
- Audit-preserving: every redistribution is logged
- Reversible: original context retrievable

The `context_compression_skill` is the primary tool; the
`coordination_routing_skill` handles routing.
