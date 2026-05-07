# Memory Architecture

## Stores

- **Document store**: structured artifacts with full content
- **Vector store**: semantic embeddings for retrieval
- **Graph store**: knowledge graph triples
- **Time-series store**: ordered observations (telemetry, signals)

A single transaction may write to multiple stores; cross-store consistency is
maintained via transaction IDs and versioned references.

## Provenance

Every artifact carries:

```
{
  "id": "<artifact_id>",
  "namespace": "<path>",
  "agent_id": "<agent_or_system>",
  "version": "<semver>",
  "timestamp": "<iso8601>",
  "transaction_id": "<tx_id>",
  "authority_chain": [...],
  "inputs_hash": "<hash>",
  "calibration_id": "<id_or_null>",
  "license": "<source_license_or_null>",
  "visibility": "<org|compartment|external>",
  "supersedes": "<prior_id_or_null>"
}
```

## Retrieval

Context-aware: who is asking, why, with what authority, in what budget. The
retrieval pipeline composes:

1. Authority gate
2. Namespace policy gate
3. Embedding-based candidate set
4. Graph-based expansion
5. Salience and recency reranking
6. Privacy/compartment filtering

## Compression

Originals are append-only. Compression runs alongside, producing summaries
and embeddings retrievable in place of raw content. Originals always
recoverable until retention policy archives them (still recoverable from cold).

## Versioning

All artifacts versioned. Updates are new versions plus a `supersedes` link.
No silent overwrites. Replay possible to any past memory state.

## Integrity

- Provenance signing
- Continuous pollution scans
- Contradiction registry
- Privacy scans
- Audit trails permanent
