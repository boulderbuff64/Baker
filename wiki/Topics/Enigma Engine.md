# Enigma Engine

[[Robb Green]]'s Meta ads creative-at-scale system, built in roughly two weeks with Lucas. Demoed in [[2026-05-08-ai-hackathon-show-and-tell]] (~1:07–1:14) under the brand name "Ditto Ads".

Named after the WWII Enigma cipher machine — the value is in the *number of variations*, not any single output.

## What It Does

1. Brand load-in: typography, voice, tone, visual identity.
2. **40 pre-built ad concept templates** that "already work" — bait-and-switch, negative marketing, etc.
3. Click **Create Showcase** → 40 ads generated, on-brand, with text rendered correctly.
4. Canva-style refinement: import competitor ads, mask + delete elements, regenerate selected regions, swap images.
5. **Variation explosion**: any winning ad can spawn 1k–10B permutations. They run ~1000/template/day per brand on TikTok.

## The Insight

> "I can take one slideshow and make 10 billion variations if I wanted. […]
> That thousand gets past duplicate content because we've got enough
> variation now because of the Enigma."
> — Robb ~1:15

The mechanism beats TikTok/Meta duplicate-content filters by treating creative variation as combinatorics across every variable in every image, not as creative iteration.

## Key Claims

- **Zero text rendering problems.** Robb (~1:11): "Now there are zero text problems. Zero. So like it's crossed the chasm now, guys."
- **Reinforcement-learning friendly.** Andrew (~1:12) suggests piping click/ROAS/conversion data back as feedback. Robb confirms they already do this on the 50k slideshows/day side; same loop applies once Meta attribution is hooked up.
- **Built in 2 weeks** — illustrates Robb's "speed of build" thesis.

## Related

- [[Command Centre]] — the platform this likely sits on top of (Project Engine + skills registry).
- [[Pre-mortem Prompt]] — Robb's general practice; relevant to spec'ing variation rules.

## Sources

- [[2026-05-08-ai-hackathon-show-and-tell]] — live demo ~1:07–1:14, Turing/Enigma origin story ~1:14:50.
