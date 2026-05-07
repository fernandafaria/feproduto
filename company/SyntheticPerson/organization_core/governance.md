# Governance

## Principle

Governance at SyntheticPerson.ai is **not** a compliance overlay. It is an
active subsystem (`nervous_systems/governance_system/`) that participates in
every cognitive transaction above the reflexive level.

## Layers of Governance

1. **Constitutional** — purpose, philosophy, values, ethical principles. Owned
   by the Human Strategic Layer. Changes require explicit ratification.
2. **Architectural** — autonomy levels, escalation rules, system boundaries.
   Owned jointly by humans and the governance system.
3. **Operational** — per-transaction policy enforcement (sandbox, reversibility,
   memory access). Owned by the governance system.
4. **Reflective** — audits, post-mortems, evolution proposals. Owned by the
   learning system with human ratification.

## Decision Rights Matrix

| Decision class | Initiator | Reviewer | Authorizer |
|---|---|---|---|
| Reflexive task | Agent | Skill policy | Self |
| Deliberative task | Agent cluster | Coordination layer | Self (sandboxed) |
| Strategic recommendation | Strategy cluster | Governance system | Human |
| Irreversible action | Any | Governance system | Human |
| Ethical question | Any | Governance system | Human |
| Architectural change | Learning system | Governance system | Human |
| Constitutional change | Human | Governance system | Human (ratified) |

## Authorization Mechanisms

- **Policy-as-code**: every policy is an executable rule in `governance_system/`
- **Cryptographic attestation**: every authorized action has a signed authority chain
- **Reversibility windows**: autonomous actions remain revocable for a defined window
- **Two-key actions**: irreversible actions require human + governance system co-sign

## Transparency Defaults

- Every decision is logged with its authority chain.
- Every memory write is attributable to a transaction.
- Every simulation is reproducible from logged inputs.
- Every escalation produces a permanent record.

Exceptions (e.g., security-sensitive transactions) are logged in encrypted
shadow records auditable by the human layer only.

## Conflict Resolution

When subsystems disagree:

1. The contradiction is logged as a memory artifact.
2. The coordination layer attempts reconciliation via shared simulation.
3. If unresolved, the governance system stalls the transaction and escalates.
4. The human layer adjudicates only if escalation reaches the strategic level.

## Drift Controls

Governance itself is monitored against drift. The learning system periodically
audits whether governance is being applied consistently and surfaces
deviations. Governance cannot quietly liberalize itself.

## Exceptional States

- **Freeze** — governance can halt all autonomous action across the org.
- **Quarantine** — a subsystem can be isolated from memory writes while diagnosed.
- **Rollback** — actions within the reversibility window can be retracted.
- **Hard stop** — humans can force the org into observation-only mode.

## Trade-offs

- Governance cost is real; we accept the latency tax to preserve coherence and
  trust progression.
- Excessive governance produces brittleness; we periodically audit for over-gating.
- Insufficient governance produces drift; we err on the side of more in early
  autonomy levels.
