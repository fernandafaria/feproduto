# Retrieval

## Contracts

```
GET /memory/read {
  query: <semantic | structural | temporal>,
  scope: [<namespace>...],
  context: <requester_state>,
  authority: <chain>,
  budget: { tokens, latency, candidates }
}
```

Returns ranked artifacts within authority and budget.

## Policies

- Default visibility: org-wide
- Compartmentalization: explicit, justified, ratified
- Authority gating: enforced at entry, not at result filtering
- Salience reranking: per-requester, per-task, calibration-tuned

## Anti-patterns

- Raw lexical match (we use semantic + graph)
- Fixed top-K (we use budget + saturation)
- Stale snapshots (always live unless requester opts in to a snapshot)
