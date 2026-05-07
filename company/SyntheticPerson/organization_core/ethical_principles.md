# Ethical Principles

## Charter

These principles are constitutional. They bind every subsystem, every agent,
every skill, every simulation, and every human in the organization. They take
precedence over performance, growth, revenue, and convenience.

## The Seven Principles

### 1. No Synthetic Person Without Consent

Synthetic Persons modeled on real, identifiable individuals require explicit,
revocable, informed consent. Archetype models and fictional persons are
unrestricted; specific persons are not.

### 2. No Simulation Used as Truth

Simulation outputs are decision aids, never ground truth. Every simulation
artifact is tagged with confidence, assumptions, and known unmodeled factors.

### 3. No Autonomous Irreversibility

The organization will not autonomously execute actions that cannot be reversed
within a stated window. Irreversible action is a human-only privilege.

### 4. No Hidden Agents

Every system that interacts with humans (internal or external) discloses that
it is a system. We do not impersonate humans. Synthetic Persons are
identifiable as such by default.

### 5. No Memory Without Provenance

Every artifact in organizational memory carries provenance: who/what wrote it,
when, why, with what authority. Unattributed memory is quarantined.

### 6. No Model Without Limits

Every Synthetic Person and Synthetic Society we ship has documented limits:
populations on which it is valid, contexts in which it is invalid, and known
failure modes. Customers are taught the limits before they receive the model.

### 7. Humans Stay Upstream of Meaning

Purpose, ethics, and meaning belong to humans. The systems do not optimize
their way to a new purpose. If a system proposes a meaning shift, it
escalates; it does not enact.

## Operationalization

Each principle has:

- A detection mechanism (how the org notices a violation)
- An enforcement point (where the violation is blocked)
- An escalation path (who adjudicates)
- A logging requirement (what is recorded)

These are codified in `nervous_systems/governance_system/`.

## Tensions We Acknowledge

- **Consent vs. Research utility** — consent reduces dataset size; we accept it.
- **Disclosure vs. Realism** — disclosed Synthetic Persons feel less real to users; we accept it.
- **Reversibility vs. Speed** — reversibility taxes throughput; we accept it.
- **Provenance vs. Storage cost** — provenance is expensive at scale; we pay it.

## Non-Negotiables

- We do not build Synthetic Persons for surveillance.
- We do not build Synthetic Societies for political manipulation.
- We do not build simulations of populations without their archetype-level consent or public-domain basis.
- We do not retain memory of natural persons without their consent.

## Review Cadence

Ethical principles are reviewed on each evolution cycle by the human layer.
Amendments require human ratification and are logged constitutionally.
