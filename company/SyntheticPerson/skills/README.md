# Skills Layer

Skills are **reusable cognitive primitives** — modules of reasoning, function,
or evaluation that any agent or nervous system can invoke. They are
versioned, evaluable, and bounded.

## Folder Structure

```
skills/
├── global/             # Org-wide cognitive primitives
├── shared/             # Cross-system reusable skills
├── meta/               # Skills that operate on skills
└── system_specific/    # Skills tied to a specific nervous system
```

## Per-Skill Anatomy

Each skill has 10 files:

```
purpose.md
inputs.md
outputs.md
reasoning_model.md
execution_flow.md
constraints.md
evaluation.md
cost_profile.md
failure_modes.md
escalation_rules.md
```

## Lifecycle

1. Pattern detected
2. Skill drafted by `pattern_promoter_agent`
3. Reviewed by governance + learning
4. Adopted, versioned, and made discoverable
5. Continuously evaluated; retired when obsolete
