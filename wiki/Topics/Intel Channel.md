# Intel Channel

A team-distribution pattern: a single Slack channel that receives the daily output of all [[Farmer Pattern|context farmers]], formatted as **skim/skip/watch** verdict + title + one-line "Why". Coined by [[Robb Green]] in [[2026-05-08-ai-hackathon-show-and-tell]] (~32:56).

## Why It Works

> "You need asymmetric information and then put everybody in the same Slack
> channel. So whatever you're focused on, whether it's paper clip or open
> claw, whatever, everybody gets all the same information every morning and
> then they can skim it, skip it, or watch it depending on their level of
> knowledge."
> — Robb ~32:56

## Key Claims

- **Asymmetric information distribution beats per-person research.** One agent farms once, the whole team consumes the same digest. Cuts redundant research across N people.
- **Verdict tag enables triage.** Reader scans verdicts first, reads the "Why" only for items in their lane, opens the source only on `WATCH`.
- **Daily cadence forces narrow keywords.** Broad keywords flood the channel and people stop reading; tight keywords keep signal high.
- **The "Why" line is the differentiator.** Without editorial commentary it's just a feed reader. The Why is what makes a digest a digest.

## Format

Robb's Slack output (per the screenshot Andrew referenced earlier in this vault):

```
👀 SKIM **Title**
*Channel | Source · views · date · duration*

Summary paragraph (what).

*Why: editorial — what to look for, what's weak, whether to watch.*
```

This format is now the wiki's digest standard — see the apify-youtube-scrape skill in the Baker repo.

## Related

- [[Farmer Pattern]] — the upstream ingestion that feeds the channel.
- [[Command Centre]] — the Notifier component is the delivery mechanism in Robb's architecture.

## Sources

- [[2026-05-08-ai-hackathon-show-and-tell]] — Robb's verbatim coining ~32:56 plus follow-up at ~38:35 ("The video, the title, a little blurb about it, and then a why").
