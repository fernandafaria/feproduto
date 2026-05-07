# Organizational Theory

## Premise

The organization is theorized as a **distributed cognitive system** whose
boundary is defined by *what it can remember and act upon coherently*, not by
employment, equity, or geography.

## Formal Model

The organization `O` is a tuple:

```
O = ⟨ N, A, S, M, K, C, H, T ⟩
```

Where:

- `N` = set of cognitive **N**ervous Systems (12 at genesis)
- `A` = set of **A**gents grouped into clusters
- `S` = set of **S**kills (cognitive primitives)
- `M` = shared **M**emory substrate (episodic, semantic, procedural)
- `K` = **K**nowledge graphs spanning all subsystems
- `C` = **C**oordination protocols and message buses
- `H` = **H**uman strategic layer
- `T` = **T**ime axis (continuous, not periodic)

The organization's *intelligence* is the coordinated behavior of `O` over `T`,
constrained by `H` and grounded in `M`.

## Topology

Three superimposed topologies coexist:

1. **Subsystem topology** — 12 nervous systems, weakly hierarchical only via
   governance.
2. **Memory topology** — every subsystem reads from and writes to one shared
   memory, forming a star with `M` at the center.
3. **Coordination topology** — peer-to-peer event bus over which subsystems
   gossip context and intent.

There is **no reporting topology**. Authority flows from the Human Strategic
Layer down through governance contracts, not through line management.

## Unit of Work

The atomic unit is the **cognitive transaction**: an observation that produces
a memory write, a hypothesis, an optional simulation, and an action. Every
transaction is logged, attributable, replayable, and revocable within
reversibility windows.

## Variety and Viability

We adopt Ashby's Law of Requisite Variety: the organization's internal variety
must match the variety of the environments it acts on. Operationally:

- Cognitive subsystems are **provisioned to environment complexity**, not to
  org headcount.
- When an environment grows in variety, the response is to add agents, skills,
  or simulation capacity — never to reorganize or hire generic roles.

## Lifecycle of an Organizational Function

1. Detected as a recurring cognitive transaction pattern
2. Encoded as a **skill** (cognitive primitive)
3. If composite, lifted into an **agent**
4. If cross-cutting, promoted into a **nervous system**
5. If pervasive, encoded into the **organization core**

This is the only mechanism for structural growth. The org grows by promotion of
patterns, never by reorganization.

## Authority and Decision Rights

- **Reversible execution** — autonomous within sandbox
- **Reversible strategy** — agentic recommendation, human ratification
- **Irreversible action** — human authorization required
- **Existential or ethical** — human-only

These map directly to the Autonomy Framework (`autonomy_framework/`).

## Organizational Identity

Identity is the **stable invariant of memory plus values**. Reorganizations,
new agents, retired skills do not change identity. Identity changes only when
purpose, philosophy, or values change — and those changes are slow, ratified,
and logged.

## Failure Modes Predicted by Theory

- **Coherence collapse** under memory partition
- **Variety mismatch** when environment outpaces subsystem capacity
- **Goal drift** when subsystems optimize local objectives
- **Authority leakage** when autonomy expands faster than trust
- **Hollowing** when humans disengage from the strategic layer

Each is monitored in `nervous_systems/governance_system/`.
