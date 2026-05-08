---
name: apify-youtube-scrape
description: Use when the user wants to scrape YouTube — channel uploads, video metadata, search results, comments, or transcripts — via the Apify platform. Triggers include "scrape YouTube", "Apify YouTube", "pull videos from channel X", "YouTube digest", "track AI creators on YouTube", or building a farmer/fetcher with `fetcher: apify` against YouTube data.
---

# Apify YouTube Scrape

## Overview

Apify hosts ready-made "Actors" that scrape YouTube. Don't write a scraper from scratch — call an Actor's run-sync-get-dataset-items endpoint and parse the JSON.

**Auth:** `APIFY_API_TOKEN`. If not in env, source it from `~/.claude/skills/apify-youtube-scrape/.env.local` (chmod 600). Get a new one at https://console.apify.com/account/integrations.

```bash
set -a && . ~/.claude/skills/apify-youtube-scrape/.env.local && set +a
```

**Plan caveat:** Current account is FREE tier ($5/mo compute credit, 7-day dataset retention, max 25 concurrent runs). Persist results outside Apify if you need them >7 days.

## Pick the Right Actor

| Goal | Actor | Notes |
|---|---|---|
| Channel uploads, video metadata, search | `streamers/youtube-scraper` | Most popular, robust, handles channel URLs, search keywords, single video URLs |
| Same as above, often cheaper/faster | `apidojo/youtube-scraper` | Good fallback / cost comparison |
| Transcripts/subtitles | `pintostudio/youtube-transcript-scraper` | Separate run; feeds it video URLs |
| Comments only | `streamers/youtube-comments-scraper` | Heavy — limit `maxComments` |
| Shorts | `streamers/youtube-scraper` with `videoType: "shorts"` | |

When in doubt, default to `streamers/youtube-scraper`.

## Core Pattern (sync, small jobs)

For runs that finish in <5 min and return <9MB, use the synchronous endpoint — one HTTP call, items come back in the response body.

```python
import os, requests

ACTOR = "streamers~youtube-scraper"  # note the tilde, not slash, in the URL path
TOKEN = os.environ["APIFY_API_TOKEN"]

payload = {
    "startUrls": [{"url": "https://www.youtube.com/@AnthropicAI/videos"}],
    "maxResults": 50,           # per startUrl
    "maxResultsShorts": 0,
    "maxResultStreams": 0,
    "subtitlesLanguage": "en",  # omit if you don't want subtitles
    "subtitlesFormat": "srt",
}

r = requests.post(
    f"https://api.apify.com/v2/acts/{ACTOR}/run-sync-get-dataset-items",
    params={"token": TOKEN},
    json=payload,
    timeout=600,
)
r.raise_for_status()
videos = r.json()  # list[dict]
```

## Async Pattern (large jobs)

For long runs, start the actor and poll, or read the dataset after completion:

```python
# Start a run (returns immediately with run id + defaultDatasetId)
run = requests.post(
    f"https://api.apify.com/v2/acts/{ACTOR}/runs",
    params={"token": TOKEN},
    json=payload,
).json()["data"]

# Wait for it (or poll run["status"] until SUCCEEDED/FAILED)
requests.get(
    f"https://api.apify.com/v2/actor-runs/{run['id']}/wait-for-finish",
    params={"token": TOKEN, "waitForFinish": 600},
)

# Read items
items = requests.get(
    f"https://api.apify.com/v2/datasets/{run['defaultDatasetId']}/items",
    params={"token": TOKEN, "clean": "true", "format": "json"},
).json()
```

## Common Inputs for `streamers/youtube-scraper`

```jsonc
{
  "startUrls": [
    {"url": "https://www.youtube.com/@channel/videos"},   // channel uploads
    {"url": "https://www.youtube.com/results?search_query=ai+agents"}, // search
    {"url": "https://www.youtube.com/watch?v=VIDEO_ID"}   // single video
  ],
  "keywords": ["ai agents", "claude code"],   // alternative to search URLs
  "maxResults": 50,                            // videos per startUrl
  "maxResultsShorts": 0,
  "maxResultStreams": 0,
  "dateFilter": "week",                        // hour|today|week|month|year
  "sortVideosBy": "NEWEST",                    // RELEVANCE|UPLOAD_DATE|VIEW_COUNT|RATING — actor uses NEWEST/POPULAR/OLDEST in some versions
  "subtitlesLanguage": "en",                   // include captions in output
  "subtitlesFormat": "srt"                     // srt|vtt
}
```

Always check the actor's input schema page on apify.com — field names drift between versions.

## Output Shape (typical fields)

Each item from `streamers/youtube-scraper`:

- `title`, `id`, `url`
- `channelName`, `channelUrl`, `channelId`
- `viewCount`, `likes`, `commentsCount`
- `date` (ISO), `duration` (seconds), `text` (description)
- `subtitles` (list of `{language, url, srt}`) when requested
- `thumbnailUrl`

Don't assume — `print(items[0].keys())` once when integrating.

## Cost & Rate-Limit Tips

- **Cap `maxResults`.** A channel with 5k videos at full pull is expensive; for daily digests, 20–50 is plenty when combined with `dateFilter: "today"` or `"week"`.
- **Filter dates server-side** with `dateFilter` rather than fetching everything and filtering locally.
- **Skip subtitles** unless you actually need them — they add time and cost. Pull transcripts in a second pass for only the videos you keep.
- **Dedupe by `id`** across runs; channels re-emit the same uploads.
- **Use `keywords` OR search-URL `startUrls`, not both** — they double-up.

## Digest Output Format

When the scrape feeds a human-readable daily digest (e.g., the `ai-creators-youtube` farmer), render each kept video as a markdown blockquote-style block with this shape:

```markdown
👀 SKIM **[Consumer AI Has a Problem Nobody's Naming.](https://youtu.be/VIDEO_ID)**
*AI News & Strategy Daily | Nate B Jones · 42929 views · 2026-05-05 · 00:32:55*

> Argues the real bottleneck in consumer AI isn't model capability but the
> 'anticipation gap' — agents are still reactive, forcing users to remember,
> prompt, and supervise. Frames a permission ladder (read → suggest → draft
> → act-with-confirm → autonomous) and reads Poke, Clicky, Clueless, and
> Cowork against it.
>
> *Why: Decent conceptual frame and a useful lens for evaluating consumer
> agent products, but it's commentary rather than hands-on — worth scrubbing
> for the permission-ladder model and product takes.*
```

**Required pieces, in order:**

1. **Verdict tag** — emoji + ALL-CAPS label. Vocabulary:
   - `▶️ WATCH` — high-signal, watch in full
   - `👀 SKIM` — worth scrubbing for specific bits; not full watch
   - `📎 CLIP` — one segment matters, rest is filler
   - `⏭️ SKIP` — logged for completeness, not worth time
2. **Title** as a markdown link to the video, bolded.
3. **Meta line** in italics: `Channel | Source-or-Show · N views · YYYY-MM-DD · HH:MM:SS`. Use raw integers for views (no "42K"). Duration in `HH:MM:SS`.
4. **Summary** (what the video is/does — neutral, no editorializing). 2–4 sentences.
5. ***Why:*** *italic editorial line* — the ingester's take: what to look for, what's weak, whether to actually watch. This is the differentiator from a generic recap and is mandatory.

**Tone for `Why:`** — opinionated and specific. "Skim for X" / "Watch if you care about Y" / "Mostly marketing, one good beat at Z". Not: "Interesting video about AI."

**Ordering inside the digest:** group by verdict (`WATCH` → `SKIM` → `CLIP` → `SKIP`), then by views desc within each group.

## Daily Digest Pattern (for farmer-style cron jobs)

```python
payload = {
    "startUrls": [{"url": f"https://www.youtube.com/@{handle}/videos"} for handle in CREATORS],
    "keywords": TOPIC_KEYWORDS,
    "maxResults": 20,
    "dateFilter": "today",   # only videos posted in last 24h
    "maxResultsShorts": 0,
    "maxResultStreams": 0,
}
```

Persist `id`s seen → next run skip already-ingested videos.

## Common Mistakes

- **Slash vs tilde in actor ID.** REST URL needs `streamers~youtube-scraper` (tilde). The web console shows `streamers/youtube-scraper` (slash). Both refer to the same actor.
- **Token in URL vs header.** Either works (`?token=...` query OR `Authorization: Bearer <token>` header). Don't log the URL form.
- **Sync endpoint timeouts.** `run-sync-get-dataset-items` caps around 5 min. Anything bigger → use the async pattern.
- **Trusting `viewCount` as int.** Actor sometimes returns "1.2M" strings depending on version. Coerce defensively.
- **Forgetting `videosOnly`-style filters.** Without `maxResultsShorts: 0` and `maxResultStreams: 0`, results include shorts and live streams.
- **Hardcoding actor version.** Apify actors update; if a field disappears, check the actor's README on the console.

## When to Skip Apify

- **Single video metadata only** → `yt-dlp --dump-json URL` is free and faster.
- **Just transcripts** → `youtube-transcript-api` (Python) is free and avoids a paid run.
- **Live monitoring (push)** → YouTube Data API v3 with PubSubHubbub; Apify is pull-based.
