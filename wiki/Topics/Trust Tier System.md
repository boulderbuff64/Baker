# Trust Tier System

A governance pattern from [[Robb Green]]'s [[Command Centre]]: agents earn autonomy by demonstrating reliability over time, modeled like an employment progression rather than a static permissions matrix.

## Tiers

- **T0 — Probationary.** New agents start here with full guardrails. Output reviewed; limited tool access; capped cost per run.
- **T1, T2, T3** — Proven tiers, each unlocking more autonomy. Earned through metrics that qualify the agent.

> "Everybody starts off in a probationary period which is T0. And then as
> they earn themselves and metric and qualify them, they can earn themselves
> up to a T1, T2, T3."
> — Robb, [[2026-05-08-ai-hackathon-show-and-tell]] ~30:18

## Key Claims

- **Trust is earned, not granted.** Mirroring how a human team handles a new hire — probation → tenure — rather than giving every agent the same permissions on day one.
- **Metrics qualify the move up.** Reliability over time is the lever; specific metrics weren't named in the call.
- **Pairs with the [[Skill Evaluator|Skill Evaluator]].** The same `agent_runs` data that trains the Skill Evaluator's learning loop also feeds tier promotion decisions.

## Related

- [[Command Centre]] — the layer-2 Orchestration component this lives in.
- [[Farmer Pattern]] — agents running farmers might earn promotion based on verdict-accuracy backtests.

## Sources

- [[2026-05-08-ai-hackathon-show-and-tell]] — Robb introduces it ~30:18 and references it in his architecture doc as the GOVERNANCE component.
