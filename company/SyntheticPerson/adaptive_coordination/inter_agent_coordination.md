# Inter-Agent Coordination

Within a cluster:

- Agents share a cluster-local sub-bus and a cluster-local namespace
- Cluster cohesion is monitored
- Quorum decisions form ad-hoc when multi-specialist input is needed

Across clusters:

- Coordination via global event bus and shared memory
- No direct calls — always asynchronous
- No "owner" agent for cross-cluster work — coordination by intent
  broadcasting

Anti-patterns:

- Synchronous handoff
- One agent waiting on another
- Direct private channels
- Polling other agents for state
