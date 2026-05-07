# Interfaces — Governance System

Pub: governance.* events. Sub: authority requests, ethics requests,
escalations, learning proposals, OCS alerts, human governance input. API:
`/governance/policies`, `/governance/authorizations`,
`/governance/escalations`, `POST /governance/authorize {request}`,
`POST /governance/escalate {request, route}`.
