# Context Rot

#stub

Failure mode where an agent's working context becomes degraded over time — stale facts, contradictory instructions, irrelevant history crowding out load-bearing details, or implicit assumptions that no longer hold. Symptoms: confident-but-wrong outputs, repeated mistakes, drift from original goals.

Distinct from a single hallucination — context rot is *systemic and accumulating*.

## Key Claims

- **Structured memory layers prevent context rot** by separating durable knowledge (the wiki) from ephemeral working context (the conversation). The agent reads from the synthesis layer, not raw history. — [[2026-05-08-ai-hackathon-show-and-tell]]
- The [[LLM Wiki Pattern]] is one mitigation: read raw inputs once, structure into Topics/Sources/People, query the synthesis.

## Related

- [[LLM Wiki Pattern]] — the vault structure proposed as the mitigation.
- [[Vibe Coding]] — context rot is the dominant failure mode for long-running vibe-coded sessions.

## Sources

- [[2026-05-08-ai-hackathon-show-and-tell]] — names the failure mode and frames structured memory as the fix.
