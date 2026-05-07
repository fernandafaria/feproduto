# Intelligence Flows — Simulation System

```
requester ──► request ──► validate ──► ethics_gate ──► route ──► engine
                                                                   │
                                                                   ▼
                                                              raw_result
                                                                   │
                                                                   ▼
                                                            calibrate + tag
                                                                   │
                                                                   ▼
                                                              memory write
                                                                   │
                                                                   ▼
                                                              return to requester
```

## Cross-System

- Universal back-end for all simulation-needing systems
- Feeds learning system with calibration data
- Surfaces OOD events to OCS and governance
