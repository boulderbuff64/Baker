# LLM Wiki Pattern

A knowledge-management pattern attributed to [[Andrej Karpathy]]: instead of running RAG over raw documents at every query, an LLM **reads each source once** and curates a structured, interlinked wiki of markdown files. Future queries hit the synthesis layer, which accumulates as more sources are added.

In [[Robb Green]]'s [[Command Centre]] architecture, this is the Layer-1 KNOWLEDGE component — markdown files that "agents read & maintain. Inbox → processed → wiki. Knowledge that compounds."

## Key Claims

- **RAG is stateless per query.** Every retrieval starts from scratch over raw chunks; nothing accumulates between queries. — [[2026-04-12-karpathy-llm-wiki-setup]]
- **A wiki accumulates structure.** Read-once + structured links means each new source extends an existing graph instead of bloating an undifferentiated corpus. — [[2026-04-12-karpathy-llm-wiki-setup]]
- **Three layers:** raw inputs → structured wiki → query layer. The middle layer is the moat.
- **`CLAUDE.md` is the schema file.** It tells the curator LLM how to organize, link, lint, and grow the vault.
- **Linting is first-class.** Periodic structural pass: orphans, broken links, duplicates, stub topics.
- **The trade-off [[Robb Green]] surfaced (~28:30):** wiki ingestion is fast at query time but inaccuracy compounds because the LLM decides what to summarize. Full-provenance retrieval (keep raw sources, query at runtime) is accurate but slow and token-expensive. Hybrid is the likely future. — [[2026-05-08-ai-hackathon-show-and-tell]]
- **Long-term vs short-term memory analogy.** Robb treats the LLM Wiki as long-term memory; the rolling conversation context is short-term. — [[2026-05-08-ai-hackathon-show-and-tell]] ~27:00
- **Inbox → processed → wiki.** The pipeline isn't direct ingestion — there's a processing step where raw inputs get triaged before promotion to wiki entries. — Command Centre architecture doc.

## Related

- [[Command Centre]] — Layer-1 component where this lives in production.
- [[Farmer Pattern]] — automated upstream ingestion that populates the inbox.
- [[Intel Channel]] — downstream output for human consumption.

## Sources

- [[2026-04-12-karpathy-llm-wiki-setup]] — Teacher's Tech end-to-end Obsidian + Claude Code walkthrough; introduces the three-layer model, schema file, and linting step.
- [[2026-05-08-ai-hackathon-show-and-tell]] — Robb's applied use as the long-term memory layer of his Command Centre, plus the explicit ingestion-vs-provenance trade-off framing (~28:30).
