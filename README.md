# GenPark Presburger Linear Integer Arithmetic Solver Skill

Presburger linear integer arithmetic decision procedure solving systems of linear inequalities.

Read more at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph TD
    C[Linear Integer Inequalities Ax <= b] --> S[Presburger Decision Procedure]
    S --> D{Satisfiable in Z^k?}
    D -->|Yes| M[Integer Certificate Model x*]
    D -->|No| U[Unsat Safety Invariant Guarantee]
    style C fill:#e1f5fe
    style S fill:#fff9c4
    style D fill:#ffcdd2
    style M fill:#c8e6c9
    style U fill:#d1c4e9
```

## Features
- Quantifier-free linear integer arithmetic constraint satisfaction.
- Zero external dependencies.
