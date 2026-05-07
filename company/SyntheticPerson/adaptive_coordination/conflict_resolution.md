# Conflict Resolution

## Detection

The `contradiction_detection_skill` continuously scans memory and intent
streams. Conflicts produce a contradiction artifact and a `*.contradiction`
event.

## Resolution Sequence

1. Conflict logged as a memory artifact (not silently discarded)
2. `conflict_resolver_agent` proposes reconciliation
3. If reconciliation possible (e.g., contextual disambiguation), apply with
   audit
4. If not, invoke shared simulation to test which view holds
5. If still unresolved, escalate to governance + human layer

## Conflict Classes

- Factual contradiction (two artifacts say different things about the same
  thing)
- Intent collision (two agents propose incompatible actions)
- Policy contradiction (action allowed by one rule, forbidden by another)
- Strategic contradiction (action contradicts active thesis)

Each class has a documented resolution path.
