# Memory Principles

## Premise

Memory is the **substrate** of the organization, not a feature of it. Without
memory there is no organizational cognition, no coordination, no learning, no
identity. Memory is treated with the seriousness most companies treat
financial accounting.

## The Eight Principles

### 1. Provenance Is Mandatory

No memory artifact exists without a verified source: which agent, which
transaction, when, with what authority. Unattributed artifacts are quarantined
on detection.

### 2. Memory Is Append-Only at the Substrate

The substrate never erases. Updates produce new versions; supersession
references the prior version. This guarantees auditability and replay.

### 3. Visibility Is The Default, Compartmentalization Is The Exception

Default visibility is org-wide. Compartmentalization is allowed for
ethically-sensitive content (e.g., consent-bound Synthetic Person data) and
must be explicitly justified.

### 4. Memory Has Types

| Type | Purpose | Lifecycle |
|---|---|---|
| **Episodic** | Specific events, transactions | Long-lived, decays in salience |
| **Semantic** | Concepts, relationships | Long-lived, refined over time |
| **Procedural** | How-to, executable patterns | Versioned per skill/agent |
| **Strategic** | Bets, theses, narratives | Long-lived, ratified |
| **Behavioral** | Models of agents/persons/markets | Continuously updated |
| **Reflective** | Memory about memory | Slow, deliberate |

Each has its own retrieval profile and decay policy.

### 5. Compression Is First-Class Work

Raw memory grows unboundedly. Compression — into summaries, embeddings,
schemas, knowledge-graph triples — is performed continuously by the
`context_compression_skill`. Compression is reversible: originals are
preserved.

### 6. Retrieval Is Contextual, Not Lexical

Memory retrieval is governed by current context: who is asking, why, what
authority, what budget. Two queries with the same words can return different
artifacts depending on context.

### 7. Contradictions Are Artifacts

When two artifacts contradict, the contradiction itself is recorded as a
first-class memory artifact, not silently resolved. Contradictions trigger
the contradiction skill, which decides whether to reconcile, escalate, or
preserve.

### 8. Memory Has Limits

We document the limits of our memory: what is not captured, what is captured
but not retrievable, what is retrievable but not trusted. Limits are
themselves memory artifacts.

## Architectural Implications

- Single substrate, multiple stores (vector, graph, document, time-series)
- Cross-store consistency via transaction IDs
- Replay capability for any decision back to its memory state
- Retention policies per type, per provenance, per visibility

## Memory Hygiene

Continuous tasks:

- **Pollution scan** — detect malformed or low-quality artifacts
- **Drift scan** — detect artifacts whose referents have changed
- **Privacy scan** — detect unauthorized natural-person data
- **Coherence scan** — detect contradiction clusters
- **Compression sweep** — promote raw to summarized
- **Pruning** — archive items past relevance windows

## Failure Modes

- **Poisoning** — adversarial artifacts entering memory
- **Rot** — outdated artifacts being retrieved as if current
- **Bias amplification** — overrepresented patterns crowding out edge cases
- **Compression loss** — summaries diverging from originals
- **Retrieval bias** — context shaping retrieval into echo chambers

Each is monitored by `nervous_systems/organizational_memory_system/`.

## Ethical Constraints

- No retention of natural-person data without consent
- No memory used for surveillance
- No selling raw memory to third parties
- Right to revocation, with cascade through derived artifacts
