# Coordination Protocols

## Read-Reason-Write

Default for stateless cognition. Read shared context, reason locally, write
back artifacts. No explicit handoffs.

## Subscribe-Observe-React

Subscribe to event topics; observe passively; react when trigger conditions
match. Pre-declared trigger conditions per subscriber.

## Co-Simulate

Two or more agents enter a shared simulation, propose moves, emerge with a
consensus output. Used for strategic transactions.

## Escalate-Wait-Resume

Reach an authority gate, escalate, suspend, resume on response. No busy-waiting.

## Quorum Decision

Ad-hoc quorum forms for decisions requiring multiple specialists; dissolves
on resolution.

## Heartbeat / Liveness

Each agent and system emits heartbeats. Loss of heartbeat triggers fallback
behavior in subscribers.
