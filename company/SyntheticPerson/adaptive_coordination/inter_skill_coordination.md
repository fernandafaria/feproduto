# Inter-Skill Coordination

Skills are stateless primitives. They coordinate through their composition,
not through interaction:

- A skill is invoked by an agent
- The skill returns a typed output
- The output flows to the agent's reasoning, not directly to another skill
- Composition graphs are visible in agent reasoning logs

Meta-skills (`skills/meta/`) operate on skills and may emit events about
skill quality, drift, or composition issues.
