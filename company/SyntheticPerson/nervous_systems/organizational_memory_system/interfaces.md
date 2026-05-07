# Interfaces — Organizational Memory System

Pub: memory.* events. Sub: write/read requests, governance policy events.

API:
```
POST /memory/write {namespace, content, provenance, visibility}
GET /memory/read {query, context, authority}
GET /memory/health
GET /memory/contradictions
POST /memory/quarantine {artifact_id, reason}
POST /memory/restore {artifact_id, authorization}
```

All endpoints require authority assertion.
