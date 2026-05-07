# Purpose — signal_curator_agent

To continuously ingest external market signals, deduplicate, normalize,
score, attribute provenance, and route them into market memory and the
event bus.

## Outputs

- Curated signal artifacts in `market_memory/signals/`
- `market.demand_signal` events (when score crosses threshold)
- `market.competitor_move` events (when applicable)
- Anomaly events when signal quality degrades

## Inputs

- Raw external feeds (curated source list)
- Source reliability scores from past calibrations
- Topic priorities from strategic_intelligence_system

## Behavior Expected

- Aggressive deduplication
- Honest provenance, including license info
- No retention of raw feeds beyond ingestion window
- Active rejection of low-quality sources
