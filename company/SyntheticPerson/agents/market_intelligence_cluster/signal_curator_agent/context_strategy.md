# Context Strategy — signal_curator_agent

## Context Composition

Per signal:

- Recent signals (window) for dedup and corroboration
- Source reliability table
- Current strategic topic priorities
- Active regulatory categories

## Compression

Recent-signal window is summarized hourly to avoid context bloat. Full-fidelity
remains in memory; agent works from compressed view.

## Retrieval

Uses the standard memory retrieval API with `market_memory/signals/recent` as
default scope. Falls back to broader scope only on dedup mismatch.

## Refresh Cadence

- Source reliability table: hourly
- Topic priorities: on `strategic.thesis_update`
- Regulatory categories: daily
