# Memory — Platform Intelligence System

Writes: `collective_memory/platform/health/...`, `.../drift/...`,
`.../incidents/...`, `.../capacity/...`.

Reads: telemetry namespaces, model registry, dependency catalog.

Retention: rolling 90d for raw; permanent for incidents and capacity decisions.
