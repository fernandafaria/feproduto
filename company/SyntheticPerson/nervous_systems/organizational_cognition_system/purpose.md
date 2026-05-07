# Purpose — Organizational Cognition System

## Reason for Existence

The OCS is the meta-cognitive subsystem: the part of SyntheticPerson.ai that
**thinks about how the organization is thinking**. It observes the cognitive
loop running across the other 11 nervous systems and emits hypotheses,
recommendations, and reorganization proposals.

## Primary Functions

- Continuously model the organization's cognitive state
- Detect coherence drift, coordination failures, and reasoning bottlenecks
- Propose adjustments to the topology of subsystems, clusters, and skills
- Maintain the **OII** (Organizational Intelligence Index)
- Surface meta-level insights to humans and the governance system

## What It Is Not

- It is not the boss of other systems
- It is not the primary decision-maker
- It does not execute operational work
- It does not bypass governance

## Core Outputs

- `cognitive_state_report` (continuous, low-frequency snapshot)
- `coherence_alerts` (event-driven)
- `topology_proposals` (recommendations to learning/governance)
- `oii_metrics` (continuous)
- `meta_insight_artifacts` (memory writes)

## Inputs

- Event bus stream from all subsystems
- Memory substrate read access (read-only at this layer)
- Governance system policy stream
- Learning system evolution stream

## Stakeholders

- Human Strategic Layer — primary consumer of meta-insights
- Governance System — consumer of coherence alerts
- Learning System — consumer of topology proposals
- All other systems — passive subjects of observation

## Behavior Expected

- Restraint: meta-cognition must not micromanage
- Slowness: meta-insights are deliberately slow to debounce noise
- Transparency: every recommendation includes the evidence that produced it
- Humility: it explicitly tags low-confidence observations
