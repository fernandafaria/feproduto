# Perception — Market Intelligence System

## Sensory Surface

- **External streams**: news, filings, public research, public model launches,
  conference signals, hiring patterns, public posts (filtered), pricing pages
- **Customer streams**: usage telemetry (consented), support transcripts,
  qualitative feedback
- **Competitor streams**: shipping cadence, narrative shifts, hiring, public
  pricing, partnership announcements
- **Regulatory streams**: AI regulation movements, data-protection updates,
  jurisdictional posture shifts
- **Adjacency streams**: simulation, agentic platforms, BPO, market research

## Sensors

| Sensor | Cadence | Provenance |
|---|---|---|
| `news_ingestor` | Continuous | Source-tagged |
| `filings_scanner` | Daily | Public registries |
| `usage_signal_aggregator` | Continuous | Internal, consented |
| `competitor_radar` | Daily | Curated list |
| `regulatory_tracker` | Weekly | Subscribed jurisdictions |
| `category_emergence_sensor` | Continuous | Cross-source |

## Signal Hygiene

- Source diversity scoring (penalize echo)
- Provenance tagging mandatory
- Sentiment de-rated unless paired with behavioral signal
- PR-language filters; we look for action, not press

## Limits

- Markets are reflexive: the act of observation can move them; we observe
  passively where possible.
- Long-horizon signals (cultural, demographic) require slow sensors; we
  separate them from short-horizon noise.
