# Collaboration Protocols — signal_curator_agent

## With Peer Agents

- `competitor_modeler_agent`: hands off competitor-tagged signals via event
- `category_cartographer_agent`: hands off category-tagged signals
- `regulation_watcher_agent`: hands off regulatory-tagged signals

Hand-offs are event-driven, not call-stack. Curator does not wait.

## With Nervous Systems

- `market_intelligence_system`: subscribes to demand for topic priorities
- `governance_system`: defers on license-ambiguous signals
- `organizational_memory_system`: writes via the standard memory contract

## With Skills

Uses:
- `synthesis_skill` for normalization
- `contradiction_detection_skill` on multi-source events
- `context_compression_skill` for working window
