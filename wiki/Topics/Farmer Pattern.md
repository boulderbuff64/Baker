# Farmer Pattern

A scheduled, fetcher-driven ingestion pipeline that pulls external data (YouTube, RSS, papers, X, Instagram, etc.) into a knowledge vault on a cron, dedupes against prior runs, applies editorial verdicts, and writes both Source skeletons and a daily Digest into an [[Intel Channel]] for the team.

[[Robb Green]] coined this **"context farming"** in [[2026-05-08-ai-hackathon-show-and-tell]] (~31:54). [[Andrew Erickson]] rebuilt it live on the same call (~47:00–52:30) as the foundation of the Baker repo.

## Three Pieces

1. **Farmer skill** (the runner) — knows how to load configs, dispatch fetchers, and write into the vault per its `CLAUDE.md` schema.
2. **Farmer config** — one markdown file per farmer (`farmers/<name>.md`), declaring fetcher, schedule, tracked sources, and editorial heuristics.
3. **Vault** — the destination, structured per the [[LLM Wiki Pattern]].

Implemented in this vault as `~/.claude/skills/farmer/` + `wiki/farmers/` + this Wiki. Mirrored at https://github.com/boulderbuff64/Baker.

## Key Claims

- **Asymmetric information for teams.** Robb (~32:56): "you need asymmetric information and then put everybody in the same Slack channel." One farm, N readers. See [[Intel Channel]].
- **Apify is the right fetcher default.** Robb (~33:26): "Cloud code connects to Apify. There's an actor for everything. You can scrape almost anything nowadays. So it just makes it very simple. It's cheap to run."
- **YouTube > X for substance.** Robb (~34:30): "More substance in a YouTube video than a Twitter post. It's just more depth. So you could derive a playbook or a summary that's got more meat around the concept." X is more "AI slop"-prone.
- **Curate the people, not just keywords.** Robb (~34:30): "Hopefully you're able to pick people you somewhat trust. The human is now is like you've got to be curator. You've got to curate who you want to follow."
- **Calibration takes ~10 days of running.** Chad (~53:50): "I've done it for about 10 days now. Almost all skim/skip — maybe more skip. Have to find new people. When you get a watch, you watch it." — verdict heuristics need real-world tuning, not a-priori design.
- **One config per source-pattern.** A single farmer for "AI creators on YouTube" beats N ad-hoc scripts because the verdict heuristics and dedupe live in one place.
- **Default to disabled** until verdicts are calibrated by hand on a few real runs.
- **Use case generalizes.** Robb (~55:24): pickleball brand owner's case — scrape YouTube/TikTok daily for any mention of competitor paddle reviews, post to team Slack, surfaces ambassador candidates and bad reviews equally.

## Related

- [[LLM Wiki Pattern]] — the schema farmers write into.
- [[Intel Channel]] — the team-distribution output channel.
- [[Command Centre]] — Robb's full architecture this slots into.

## Sources

- [[2026-05-08-ai-hackathon-show-and-tell]] — Robb coins "context farming" ~31:54, demos the Slack output ~32:25, defends YouTube-over-X ~34:30. Andrew rebuilds it live ~47:00–52:30.
- [[2026-04-12-karpathy-llm-wiki-setup]] — establishes the wiki schema farmers ingest into.
