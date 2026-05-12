# Baker 🍞

> Built at the **AI Hackathon** — where caffeine meets Claude.

Baker is a sandbox of AI-powered tools and Claude Code skills hacked together in a single sprint. Less a polished product, more a workshop bench: experiments, sharp edges, and the occasional surprisingly-useful utility.

## Where this came from

This repo is the live-build artifact of the [InventoryHero AI Hackathon](https://InventoryHero.ai/openclaw) — a weekly community call where operators compare notes on Claude Code, custom skills, and agent systems. Everything here was built on-camera with the group watching.

📺 Watch the May 8 replay: https://youtu.be/qO1wZ4nqACo

## What's inside

### `skills/transcribe-zoom-names/`
A Claude Code skill that scans a Zoom screenshot and extracts the participant list — no copy-paste gymnastics, no manual squinting at tiny name labels.

- **When to use it:** You took a screenshot of a Zoom call (or any video grid) and want the attendees as text.
- **How to invoke:** Ask Claude: *"Transcribe the names from this Zoom screenshot"* and drop in the image.

### `skills/apify-youtube-scrape/`
A Claude Code skill that scrapes YouTube via the Apify platform — channel uploads, video metadata, search results, comments, and transcripts.

- **When to use it:** You want structured data from a YouTube channel, search, or single video. Powers the daily digest pattern below.
- **How to invoke:** Ask Claude: *"Pull the last 20 videos from @SomeChannel using the apify-youtube-scrape skill."*

### `skills/farmer/` — context farming
Inspired by Rob's live walk-through on the May 8 call: scrape a set of creators every morning, have Claude score each video **Skip / Skim / Watch**, and post the digest to Slack. Asymmetric intel on autopilot for your whole team.

- **When to use it:** You want a daily intel feed from sources you actually trust, without watching everything yourself.
- **How to invoke:** Ask Claude: *"Set up a YouTube farmer for these channels and keywords."* See the `apify-youtube-scrape` skill's `Digest Output Format` section for the schema.

## The hackathon vibe

- **Ship first, refactor never** (until next week).
- **Skills > scripts** — every tool here is reusable across Claude conversations.
- **Bring your own screenshot.**

## Getting started

**Requirements:**
- [Claude Code](https://claude.com/claude-code) installed
- An [Apify API token](https://console.apify.com/account/integrations) (only for the YouTube skill), saved in `skills/apify-youtube-scrape/.env.local`

**Clone and go:**

```bash
git clone https://github.com/boulderbuff64/Baker.git
cd Baker
claude
```

Claude Code picks up the skills from the `skills/` directory automatically — just ask for what you want and the relevant skill will activate.

## Come build with us

We run the AI Hackathon every Thursday. Bring whatever you're working on, see what other operators are building, and steal liberally. Sign up: https://InventoryHero.ai/openclaw

---

Made with ⚡ at the [InventoryHero AI Hackathon](https://InventoryHero.ai/openclaw) — come build the next one with us.
