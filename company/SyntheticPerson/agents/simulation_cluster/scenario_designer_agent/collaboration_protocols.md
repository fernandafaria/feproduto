# Collaboration Protocols — scenario_designer_agent

Subscribes to `*.simulation_request`. Hands off scenarios to
`validity_auditor_agent` for OOD check, then to engine. Coordinates with
`ethics_reviewer_agent` on ethics-tier-3+ requests.
