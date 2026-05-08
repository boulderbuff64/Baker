# LLM Wiki Pattern

A knowledge-management pattern attributed to [[Andrej Karpathy]]: instead of running RAG over raw documents at every query, an LLM **reads each source once** and curates a structured, interlinked wiki. Future queries hit the synthesis layer, which accumulates and gets smarter as more sources are added.

## Key Claims

- **RAG is stateless per query.** Every retrieval starts from scratch over raw chunks; nothing accumulates between queries. — [[2026-04-12-karpathy-llm-wiki-setup]]
- **A wiki accumulates structure.** Read-once + structured links means each new source extends an existing graph instead of bloating an undifferentiated corpus. — [[2026-04-12-karpathy-llm-wiki-setup]]
- **Three layers:** raw inputs → structured wiki → query layer. The middle layer is the moat. — [[2026-04-12-karpathy-llm-wiki-setup]]
- **`CLAUDE.md` is the schema file.** It tells the curator LLM how to organize, link, lint, and grow the vault. — [[2026-04-12-karpathy-llm-wiki-setup]]
- **Linting is first-class.** Periodic structural pass: orphans, broken links, duplicates, stub topics. — [[2026-04-12-karpathy-llm-wiki-setup]]

## Related

- *(none yet — add as more sources land)*

## Sources

- [[2026-04-12-karpathy-llm-wiki-setup]] — Teacher's Tech end-to-end Obsidian + Claude Code walkthrough; introduces the three-layer model, schema file, and linting step.
