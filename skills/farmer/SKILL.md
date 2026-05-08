---
name: farmer
description: Use when the user wants to run, edit, or troubleshoot a "farmer" — a scheduled context-ingestion config that pulls external data (YouTube, RSS, papers, etc.) into their Obsidian LLM Wiki at ~/Obsidian/Wiki. Triggers include "run the farmer", "ingest from X farmer", "create a farmer", "what farmers do I have", "fix the ai-creators-youtube digest", or any reference to ~/Obsidian/Wiki/farmers/.
---

# Farmer

## Overview

A **farmer** is a scheduled context-ingestion config. Three pieces stitched together:

1. **This skill** (`~/.claude/skills/farmer/`) — knows how to load a farmer config, dispatch its fetcher, apply verdicts, and write into the wiki.
2. **Farmer config** (`~/Obsidian/Wiki/farmers/<name>.md`) — declares fetcher, schedule, args, tracked creators/keywords/etc. YAML frontmatter + markdown body.
3. **Wiki vault** (`~/Obsidian/Wiki/`) — destination. See its `CLAUDE.md` for curator rules and the `Sources/` / `Topics/` / `People/` / `Digests/` layout.

The fetcher itself is whatever the config names: `apify`, `yt-dlp`, `rss`, `custom-script`. Each has a script under `~/.claude/skills/farmer/scripts/`.

## Run a Farmer (manual)

1. **Load config.** Read `~/Obsidian/Wiki/farmers/<name>.md`. Parse frontmatter + the `creators:`, `keywords:`, and fetcher-args YAML/JSON blocks in the body.
2. **Dispatch fetcher.** Pick by `fetcher:` field:
   - `apify` → use the **apify-youtube-scrape** skill (token at `~/.claude/skills/apify-youtube-scrape/.env.local`).
   - `yt-dlp` → `yt-dlp --dump-json --skip-download URL` per item.
   - `rss` → `curl` the feed URL, parse with python's `feedparser` or `xml.etree`.
   - `custom-script` → run the path in `fetcher_script:`.
3. **Dedupe.** For each item, check `~/Obsidian/Wiki/Sources/<source_type>/` for existing `video_id` (or `url` for non-video sources). Skip duplicates.
4. **Apply verdicts.** Editorial pass per the farmer's `## Verdict Heuristics` section. Vocabulary: ▶️ WATCH / 👀 SKIM / 📎 CLIP / ⏭️ SKIP. See apify-youtube-scrape skill for the full rubric.
5. **Write Sources.** One file per kept item: `Sources/<type>/YYYY-MM-DD-slug.md` with frontmatter per the wiki's `CLAUDE.md` template.
6. **Update Topics & People.** For each new source, add backlink bullet to relevant Topic notes; create stubs if missing. Same for People.
7. **Write digest.** `Digests/YYYY-MM-DD-<farmer-name>.md` — grouped by verdict (WATCH → SKIM → CLIP → SKIP), each entry in the digest format from apify-youtube-scrape.

## Create a Farmer

1. Pick kebab-case slug (becomes the `.md` filename).
2. Copy the template below to `~/Obsidian/Wiki/farmers/<slug>.md`.
3. Fill creators/keywords/args. Default `enabled: false` until tested manually.
4. If using a custom fetcher, drop the script in `~/.claude/skills/farmer/scripts/`.
5. Run once manually before enabling on schedule.

### Config Template

```markdown
---
name: <slug>
description: <one-line what this collects and why>
fetcher: apify | yt-dlp | rss | custom-script
fetcher_script: ~/.claude/skills/farmer/scripts/<file>.py   # optional
schedule: "0 6 * * *"   # cron
ingest: auto            # auto | manual-review
enabled: false
---

# <slug>

<paragraph: what, why>

## Tracked <creators|feeds|searches>
```yaml
creators:
  - handle1
```

## Topical Keywords
```yaml
keywords:
  - "term"
```

## Fetcher Args
```json
{}
```

## Verdict Heuristics
<editorial guidance>
```

## List Farmers

```bash
ls ~/Obsidian/Wiki/farmers/
```

Read frontmatter `enabled:` and `schedule:` to surface only active ones.

## Common Mistakes

- **Writing into Sources/ without dedupe.** Always check by `video_id` / canonical URL first.
- **Skipping the Topic update.** A Source with no Topic backlink is an orphan — defeats the purpose of the wiki.
- **Generic summaries.** The wiki's value is in *specific claims with backlinks*, not paraphrases. Lift quotes.
- **Auto-enabling new farmers.** Run manually first; the verdict heuristics need calibration before unattended runs.
- **Bypassing the wiki's CLAUDE.md.** That file owns the schema. Read it before writing into the vault.

## Cross-References

- **apify-youtube-scrape** skill — Apify auth, actor selection, digest format, verdict rubric. Required for `fetcher: apify` farmers.
- **Wiki schema** — `~/Obsidian/Wiki/CLAUDE.md`. Source/Topic/Person frontmatter + curator rules.
