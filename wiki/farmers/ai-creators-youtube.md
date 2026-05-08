---
name: ai-creators-youtube
description: Daily Apify YouTube digest from tracked AI creators + topical keywords.
fetcher: apify
fetcher_script: ~/.claude/skills/farmer/scripts/apify_youtube.py
schedule: "0 6 * * *"
ingest: auto
enabled: false
---

# ai-creators-youtube

Daily ingest of new YouTube uploads from tracked AI creators and topical keyword searches. Runs through Apify's `streamers/youtube-scraper` actor, dedupes against `Sources/youtube/`, applies a verdict to each kept video, and writes a dated digest into `Digests/`.

## Tracked Creators

Channel handles (without `@`). Add/remove freely.

```yaml
creators:
  - AnthropicAI
  - AndrejKarpathy
  - TwoMinutePapers
  - Ycombinator
  - aiDotEngineer
  - latentspacepod
  - swyxio
```

## Topical Keywords

Searched in addition to creator uploads. Keep tight — broad terms generate noise.

```yaml
keywords:
  - "claude code"
  - "ai agents"
  - "llm wiki"
  - "agent skills"
```

## Fetcher Args

Passed to the fetcher script as JSON. Override defaults here.

```json
{
  "maxResultsPerCreator": 20,
  "maxResultsPerKeyword": 10,
  "dateFilter": "today",
  "includeShorts": false,
  "includeStreams": false,
  "subtitlesLanguage": null
}
```

## Verdict Heuristics

Hand to the curator for editorial pass. Defaults if unsure:

- **▶️ WATCH** — hands-on tutorial with a reusable artifact (code, schema, prompt) you don't already have.
- **👀 SKIM** — concept/commentary worth scrubbing for the framing or one specific section.
- **📎 CLIP** — one timestamped segment matters; rest is filler.
- **⏭️ SKIP** — log the title for completeness, not worth time.

Bias toward SKIP for "X in N hours" course-funnel framing, "you won't believe", reaction videos, and shorts.
