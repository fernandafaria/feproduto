# Semantic Compression

Compression is performed by `compression_agent` and the
`context_compression_skill`. Strategies:

- Per-namespace summary trees (rolling hourly/daily/weekly)
- Embedding-based deduplication
- Graph triple distillation
- Reversible references to originals (originals are never deleted by compression)
