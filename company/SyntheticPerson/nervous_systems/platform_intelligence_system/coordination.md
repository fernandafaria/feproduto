# Coordination — Platform Intelligence System

Pub: `platform.health_report`, `platform.drift_alert`, `platform.capacity_alert`,
`platform.cost_alert`, `platform.security_alert`

Sub: `*.health_signal`, `governance.policy_change`, `learning.evolution_event`

Hand-offs: alerts to OCS, governance, learning; mitigations to coordination
layer; capacity proposals to strategic system.
