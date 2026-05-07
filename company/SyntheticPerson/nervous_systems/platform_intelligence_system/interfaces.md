# Interfaces — Platform Intelligence System

Pub: `platform.health_report`, `platform.drift_alert`, `platform.capacity_alert`,
`platform.cost_alert`, `platform.security_alert`, `platform.incident_event`

Sub: `*.health_signal`, `governance.policy_change`, `learning.evolution_event`

Memory: RW `collective_memory/platform/`. API: `/platform/health`,
`/platform/incidents`, `/platform/capacity`, `/platform/drift`.
