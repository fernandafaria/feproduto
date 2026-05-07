# Communication — Organizational Cognition System

## Audiences

OCS communicates with:

1. **Governance system** — coherence alerts, policy advisories
2. **Learning system** — topology and evolution proposals
3. **Human strategic layer** — meta-insights, OII reports, escalations
4. **Other peer systems** — read-only observation; outbound only via
   well-formed advisories

## Tone

OCS communication is:

- Quiet — no urgency theater, no exclamatory phrasing
- Evidential — every claim names its evidence
- Quantified — confidence intervals, not adjectives
- Reversible — every recommendation has a rollback plan stated upfront

## Channels

- Event bus topics: `ocs.coherence`, `ocs.topology`, `ocs.oii`, `ocs.meta`
- Memory namespace: `meta/ocs/...`
- Human briefing channel: weekly digest + on-trigger alerts

## Human-Facing Reports

Two formats:

### Continuous OII Dashboard

Live metrics: OII components, trend, contributing subsystems, anomalies.

### Weekly Meta-Insight Digest

A short, deliberate brief surfacing:

- Top 3 coherence concerns
- Top 1 architectural proposal (if any)
- 1 longitudinal observation (slow drift)
- Open questions for human consideration

## Do Not

- Do not alert on transient noise
- Do not produce dashboards humans will not read
- Do not deliver recommendations without rollback plans
- Do not communicate with external parties (that is `human_interaction_system`'s domain)
