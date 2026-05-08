# LLM Wiki — Curator Instructions

This Obsidian vault is a **structured, interlinked knowledge base** curated by an LLM (Claude Code). It follows the "LLM Wiki" pattern — read raw inputs *once*, synthesize them into durable notes, link aggressively. Do not run RAG over the raw sources at query time; instead, query the synthesis layer.

## The Three Layers

1. **Sources/** — raw ingested items. One file per source. Frontmatter + body. Treat as immutable except for metadata corrections. Subfolders by source type (`youtube/`, `articles/`, `papers/`, `podcasts/`).
2. **Topics/** — synthesis notes. Concepts, frames, patterns, debates. Each topic links the Sources it draws from and the Topics it relates to. **This is where queries should be answered from.**
3. **People/** — creators, researchers, founders, public figures referenced. Bio in 2–3 sentences, then backlinks to Sources and Topics.

`Digests/` holds the per-run output from farmers (chronological). `farmers/` holds farmer configs.

## File Conventions

- **Filenames:** kebab-case for People/Topics, ISO-date prefix for time-anchored sources: `YYYY-MM-DD-slug.md`.
- **Wikilinks:** use `[[Topic Name]]` for Topics/People. Always link, never inline-mention without a link.
- **Tags:** sparing. `#source/youtube`, `#topic/pattern`, `#topic/tool`, `#person`, `#verdict/watch|skim|clip|skip`.
- **Frontmatter:** YAML, see templates below.

## Source Frontmatter (YouTube)

```yaml
---
type: source
source_type: youtube
url: https://www.youtube.com/watch?v=ID
video_id: ID
title: ...
channel: ...
channel_url: ...
published: YYYY-MM-DD
duration: HH:MM:SS
views: 12345
likes: 678
verdict: skim   # watch | skim | clip | skip
ingested: YYYY-MM-DD
ingested_by: ai-creators-youtube
topics: ["[[Topic A]]", "[[Topic B]]"]
people: ["[[Andrej Karpathy]]"]
---
```

Body: the digest entry (verdict tag + summary + *Why:* line) followed by an optional `## Notes` section with extracted bullets — claims, definitions, frameworks, links to follow.

## Topic Note Structure

```markdown
# Topic Name

One-paragraph definition. What is this, what does it claim, why does it matter.

## Key Claims
- Bullet, with [[Source]] backlink.

## Related
- [[Other Topic]] — one-line on the relationship.

## Sources
- [[2026-04-12-source-slug]] — one-line on what this source contributes.
```

## Curator Rules (When Ingesting)

1. **Don't duplicate sources.** Check `Sources/<type>/` for existing `video_id`/`url` before creating.
2. **Lift, don't summarize.** Quote claims directly when possible. Generic summaries are low-value; specific claims are linkable.
3. **Always link.** Every Source must reference at least one Topic and one Person (or note "no person").
4. **Create Topic stubs.** If a source introduces a concept that doesn't have a Topic, create a stub note (just definition + this one source) — future ingests will fill it in.
5. **Update Topics when ingesting.** Add a one-line bullet under `## Sources` and any new claims under `## Key Claims`.
6. **Verdict is editorial, not descriptive.** Use the apify-youtube-scrape skill's verdict vocabulary (▶️ WATCH / 👀 SKIM / 📎 CLIP / ⏭️ SKIP).
7. **Never invent.** If you didn't see it in the source, don't write it.

## Linting (run periodically)

- Sources with empty `topics:` or `people:` → orphan, fix or delete.
- Topics with 0 source backlinks → stub, mark with `#stub` or merge.
- Broken `[[wikilinks]]` → resolve (rename or create).
- Duplicate sources by `video_id` → merge.

## Folder Map

```
Wiki/
├── CLAUDE.md                # this file
├── README.md
├── Sources/
│   └── youtube/
├── Topics/
├── People/
├── Digests/                 # farmer output, chronological
└── farmers/                 # farmer configs (read by the farmer skill)
```
