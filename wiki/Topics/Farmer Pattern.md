# Farmer Pattern

A scheduled, fetcher-driven ingestion pipeline that pulls external data (YouTube, RSS, papers, etc.) into a knowledge vault on a cron, dedupes against prior runs, and writes both Source skeletons and a daily Digest. Composed of three pieces:

1. **Farmer skill** (the runner) — knows how to load configs, dispatch fetchers, and write into the vault per its `CLAUDE.md` schema.
2. **Farmer config** — one markdown file per farmer (`farmers/<name>.md`), declaring fetcher, schedule, tracked sources, and editorial heuristics.
3. **Vault** — the destination, structured per the [[LLM Wiki Pattern]].

Implemented in this vault as `~/.claude/skills/farmer/` + `wiki/farmers/` + this Wiki.

## Key Claims

- **Farmers separate fetching from curation.** The farmer guarantees coverage and dedupe; a separate (manual or LLM) curator pass assigns verdicts and lifts claims. — [[2026-05-08-ai-hackathon-show-and-tell]]
- **One config per source-pattern.** A single farmer for "AI creators on YouTube" beats N ad-hoc scripts because the verdict heuristics and dedupe live in one place.
- **Default to disabled** until the verdict heuristics are calibrated by hand on a few real runs.

## Related

- [[LLM Wiki Pattern]] — the schema the farmer writes into.
- [[Vibe Coding]] — farmers are part of the supporting infra.

## Sources

- [[2026-05-08-ai-hackathon-show-and-tell]] — demos the YouTube-farmer integration end-to-end.
- [[2026-04-12-karpathy-llm-wiki-setup]] — establishes the wiki schema farmers ingest into.
