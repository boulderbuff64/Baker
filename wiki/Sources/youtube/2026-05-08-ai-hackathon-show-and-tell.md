---
type: source
source_type: youtube
url: https://youtu.be/qO1wZ4nqACo
video_id: qO1wZ4nqACo
title: "AI Hackathon Show & Tell"
channel: Inventory Hero
channel_url: https://www.youtube.com/@InventoryHeroAI
published: 2026-05-08
duration: "01:21:33"
views: 0
likes: 0
comments: 0
verdict: watch
ingested: 2026-05-09
ingested_by: ai-creators-youtube
transcript_source: youtube-transcript-api (en, auto-generated)
topics:
  - "[[LLM Wiki Pattern]]"
  - "[[Farmer Pattern]]"
  - "[[Command Centre]]"
  - "[[Trust Tier System]]"
  - "[[Intel Channel]]"
  - "[[Enigma Engine]]"
  - "[[Lightning Bolt Acknowledgment]]"
  - "[[Pre-mortem Prompt]]"
people:
  - "[[Andrew Erickson]]"
  - "[[Robb Green]]"
  - "[[Jake Langwith]]"
  - "[[Chad Drew]]"
  - "[[Jennifer Baker]]"
  - "[[AJ]]"
  - "[[Mike P]]"
  - "[[Jason]]"
  - "[[Andrej Karpathy]]"
  - "[[Cabral]]"
related_repos:
  - https://github.com/boulderbuff64/Baker
  - https://github.com/mksglu/context-mode
tags: [source/youtube, verdict/watch, topic/architecture, topic/pattern, self-referential]
---

▶️ WATCH **[AI Hackathon Show & Tell](https://youtu.be/qO1wZ4nqACo)**
*Inventory Hero (32 subs) · 0 views · 2026-05-08 · 01:21:33*

> Recorded weekly hackathon hosted by [[Andrew Erickson]] (Inventory Hero
> channel). Heavyweight segment is [[Robb Green]]'s walkthrough of the
> [[Command Centre]] — his unified platform for autonomous,
> knowledge-compounding agents (Memory & Skills + Orchestration + Interface
> & Comms). Andrew then demos building this exact wiki and farmer skill
> *live on the call*: creates the [Baker](https://github.com/boulderbuff64/Baker)
> public GitHub repo, scaffolds `transcribe-zoom-names`, then `apify-youtube-scrape`,
> then ingests Karpathy's LLM Wiki video into a brand-new Obsidian vault — all
> on screen-share. The vault you're reading right now is the artifact.
>
> *Why: Primary material. Worth full watch for Robb's architecture
> (~28-34 min) and Andrew's live build (~16-21 min creating the Baker repo,
> 47-52 min creating the Apify YouTube skill, 1:15-1:18 wiring the wiki).
> Also Robb's Enigma Engine demo (~1:08) is the strongest "what's actually
> possible right now" beat in the call. The middle (~35-58 min) is more
> conversational — skim.*

## Notes

### Timestamps & Key Beats

#### Opening — file management & cloud sync (0:00 – 14:30)
- Group warm-up on portability problems: how do you keep agent state synced
  across desktop/laptop/multiple machines when you travel.
- [[Robb Green]] (~5:30): keeps everything in cloud (Pinecone for vector
  memory, Supabase for state) so location doesn't matter; mirrors locally
  but agents *run* in the cloud.
- [[AJ]] (~13:25): use `tmux` / `screen` so Claude can run perpetually on a
  VPS while you disconnect SSH; schedule batches across the 4-hour credit
  reset window so you don't burn through quota in one shot.

#### Andrew's first live build — Baker repo + Zoom-name skill (15:00 – 22:00)
- [[Andrew Erickson]] uses iTerm + Claude Code to build a new skill from
  scratch: `transcribe-zoom-names` from a screenshot of the call itself.
  ~17:11: "I took a screenshot of you guys while you guys were talking"
  — the very screenshot transcribed earlier in this vault's session history.
- ~18:14 [[Jake Langwith]] reminds: gitignore secrets — "you get well and
  truly fucked if that gets leaked." Bots scrape public GitHub for keys.
- ~18:44 Andrew creates the **Baker** GitHub repo live, named for
  [[Jennifer Baker]]. Pushes the skill. Repo:
  https://github.com/boulderbuff64/Baker

#### Robb's Command Centre walkthrough (28:30 – 34:00)
- ~28:30 Memory trade-off framing: **fast LLM-Wiki ingestion** (inaccuracy
  compounds) vs **full provenance retrieval** (accurate but slow + token-
  expensive). Robb expects a hybrid eventually; "kind of like long-term
  vs short-term memory."
- ~30:00 Walks through his Mission Control dashboard: projects, mission
  control, cron jobs, agents, chat, memories, hive mind, usages.
- ~30:18 [[Trust Tier System]]: "everybody starts in a probationary period
  T0. As they earn metrics qualifying them, they earn up to T1, T2, T3."
- ~31:54 Coins **"context farming"** for the proactive ingestion pattern —
  see [[Farmer Pattern]].
- ~32:25 Daily Apify-driven YouTube digest into Slack with skim/skip/watch
  verdicts; calls it the **[[Intel Channel]]**.
- ~33:26 "Highly highly recommend context farming. Cloud code connects to
  Apify. There's an actor for everything."

#### Andrew's second live build — Apify YouTube skill (47:00 – 52:30)
- ~47:30 Andrew rebuilds Robb's pattern in real time: "create a skill for
  YouTube scraping, I want to use Apify." Feeds Robb's skim/skip/watch
  screenshots as the format spec.
- ~49:30 Tests it on Karpathy's LLM Wiki tutorial video → gets back a
  formatted entry. Pastes API key in plain text first ("good rule of thumb
  is to *not* use plain text"), then redoes via env file.
- ~51:30 Commits the skill to Baker. Now public at
  https://github.com/boulderbuff64/Baker/tree/main/skills/apify-youtube-scrape

#### Memory deep-dive (52:30 – 58:00)
- ~52:30 Andrew: "my farmer is three pieces. The skill is the first part.
  Then if you set up the LLM Wiki" — explicitly states the
  skill + farmer-config + wiki triad this vault implements.
- ~53:50 [[Chad Drew]] on calibration: "10 days of running this, almost
  all skim/skip — maybe more skip. Have to find new people. When you get
  a watch, you watch it." Verdict heuristics need real-world tuning.
- ~57:30 Robb on prompts: ask AI for a **[[Pre-mortem Prompt|pre-mortem]]**
  before starting a project — "what could go wrong" before, not after.

#### Tools, models, frameworks (58:00 – 1:05:00)
- Open Claw vs Hermes: consensus is Hermes is better right now —
  self-learning loop is built in (per Robb), easier integrations.
- ~1:00 [[Robb Green]] on AI not doing what you ask: "use all the
  profanities and tell it not to be lazy. Usually gets the hint."
- ~1:02 [[Lightning Bolt Acknowledgment]]: Robb's "Jarvis" (his Open Claw
  agent) emoji-reacts ⚡ on receive in Telegram/Slack so there's no "black
  hole" silent-wait. ~30 LOC inside the orchestrator (the Notifier in his
  architecture doc).
- ~1:03 Robb model-agnosticism: built everything to be swappable across
  Claude/Codex/whatever next.

#### Robb's Enigma Engine — Meta ads (1:07 – 1:14)
- ~1:07 [[Enigma Engine]] / "Ditto Ads": Meta ads creative-at-scale tool
  built in 2 weeks with Lucas. 40 pre-built ad concept templates.
- ~1:08 "Click Create Showcase → 40 ads with concepts in your tone with
  perfect text." Includes Canva-style refinement (mask, delete element,
  reload images), import-from-competitor, variation generation.
- ~1:14 Named after the Turing/WWII Enigma machine. "I can take one
  slideshow and make 10 billion variations" — they only generate ~1000
  per template/day per brand on TikTok, but the variation space defeats
  duplicate-content detection.
- Andrew suggests adding a feedback loop: ingest performance metadata
  (clicks, ROAS, conversions) back in to train the next set. Robb says
  they already do this on the 50k slideshows/day side.

#### Closing — meta moment (1:15 – 1:18)
- ~1:15 Andrew explicitly does what this vault now records: feeds the
  Karpathy LLM Wiki YouTube link to Claude Code, asks it to use Robb's
  3-piece framework, creates the Wiki structure inside the Baker repo, and
  drops the Karpathy video summary as Source #1.
- ~1:17 "I will take this recording and put it on YouTube so it's public.
  I'll then have this bot consume that and create another wiki article."
  → That's exactly what is happening in this Source note. Self-referential
  loop closed.

### Operating Principles (from Robb's architecture doc)

Robb shared a `Command_Centre_Architecture.md` separately — see [[Command Centre]] for the full breakdown. Operating principles:

1. **Quality first, then speed** — speed without quality is just fast garbage.
2. **Assemble best-in-class first;** build custom only where the market doesn't deliver.
3. **Agents earn autonomy by proving reliability over time.**
4. **Real-time alerts on failures;** passive on successes.
5. **Every learning becomes a skill or a wiki entry** — nothing wasted.
6. **One UI, many projects** — roofer audit, TikTok ops, real estate, all one platform.

### Tools mentioned

- Apify (actor-based scrape platform) — Robb's preferred fetcher for context farming.
- Pinecone (vector memory, cloud) — Robb's long-term store; he prefers it over local Obsidian for portability.
- Supabase (project state, agent runs, task queue) — system of record.
- Claude Code, Codex, ChatGPT 5.5 — runtime options; Robb is model-agnostic.
- Open Claw, Hermes, Paperclip — competing agent frameworks. Consensus on call: Hermes leads on self-learning loop.
- iTerm, tmux/`screen` — terminal multiplexing for long-running agents.
- Tailscale — Mac-to-Mac remote access (AJ).
- One Password, Bitwarden — credential management.
- Telegram, OpenDitto bridge — interface layer; see [[Command Centre]].
- Manus — generic agent that "takes over" sites once logged in (Jake's experience).
- Google Stitch — Google's open-sourced design skill, `design.md` (Jake mentions ~55:55).

### Self-referential note

This source file is itself an artifact of the meta loop demonstrated at the
end of the video: the captions of *this* video were ingested into the wiki
that *this* video shows being created, in the repo that *this* video shows
being created, by the host of *this* video using the skills shown being
built in *this* video. The original ingest (yesterday) was off the
description text only — see the git history of this file for the
correction.
