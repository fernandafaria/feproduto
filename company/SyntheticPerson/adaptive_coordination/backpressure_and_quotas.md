# Backpressure and Quotas

The org runs continuous; load varies. To stay coherent under load:

- Per-subscriber quotas on event consumption
- Per-publisher quotas on event emission
- Memory-write rate limits per namespace
- Simulation invocation rate limits per requester
- Compute budgets per cognitive level

Backpressure surfaces as `coord.backpressure` events; the coordination
system reroutes or de-rates affected flows. Persistent backpressure escalates.
