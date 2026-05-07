# Cognitive Versioning

Memory is versioned at three levels:

1. **Artifact version** — semver per artifact
2. **Schema version** — per-namespace schema; migrations versioned
3. **Substrate version** — overall memory architecture version

Replay tools accept any version triple and return the historical view.
