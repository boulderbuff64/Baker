---
type: source
source_type: youtube
url: https://www.youtube.com/watch?v=iXd0t60YmMw
video_id: iXd0t60YmMw
title: "Karpathy's LLM Wiki - Full Beginner Setup Guide"
channel: Teacher's Tech
channel_url: https://www.youtube.com/@TeachersTech
published: 2026-04-12
duration: "00:15:05"
views: 282134
likes: 8300
comments: 377
verdict: skim
ingested: 2026-05-08
ingested_by: ai-creators-youtube
topics:
  - "[[LLM Wiki Pattern]]"
people:
  - "[[Andrej Karpathy]]"
  - "[[Teachers Tech]]"
tags: [source/youtube, verdict/skim, topic/pattern, topic/tool]
---

👀 SKIM **[Karpathy's LLM Wiki - Full Beginner Setup Guide](https://www.youtube.com/watch?v=iXd0t60YmMw)**
*Teacher's Tech (1.15M subs) · 282134 views · 2026-04-12 · 00:15:05*

> Hands-on walkthrough of [[Andrej Karpathy]]'s "LLM Wiki" pattern — Obsidian
> as the store, Claude Code as the curator, replacing per-query RAG with a
> once-read, structured, interlinked vault. Covers folder layout, a
> `CLAUDE.md` schema, Web Clipper ingestion, graph view, cross-source queries,
> and a linting pass. Beginner-pitched, no coding required.
>
> *Why: The wiki-instead-of-RAG framing is the reusable beat — read once,
> structure once, grow over time. Skim for the `CLAUDE.md` schema shape and
> the linting step; skip the Obsidian-install portion. If you already know
> Karpathy's framing, the conceptual half is faster from his own posts.*

## Notes

### Key claims (from the video)
- **RAG falls short** because every query re-searches raw docs from scratch — nothing accumulates. The [[LLM Wiki Pattern]] flips this: read once, structure once, grow.
- **Three layers** to the system: raw inputs → structured wiki → query layer.
- **`CLAUDE.md` is the schema file** — it tells the curator LLM how to organize, link, and lint the vault.
- **Linting is a first-class step** — periodic pass to catch orphans, broken links, duplicates.

### Timestamps
- 1:00 — What is RAG and why it falls short
- 1:51 — How the LLM Wiki fixes the problem
- 2:40 — Karpathy's analogy: Obsidian, LLM, the wiki
- 2:59 — The three layers of the system
- 3:54 — Setting up Obsidian and folder structure
- 5:50 — Creating the schema file (`CLAUDE.md`)
- 8:03 — Installing the Obsidian Web Clipper
- 8:12 — Ingesting your first source document
- 10:23 — Wiki and graph view
- 10:42 — Adding a second source, watching it update
- 11:31 — Cross-source questions
- 11:57 — Linting your wiki for quality
- 13:43 — Limitations

### Useful artifacts
- `CLAUDE.md` schema template: https://go.teachers.tech/LLM_Wiki_CLAUDE
- Obsidian: https://obsidian.md
