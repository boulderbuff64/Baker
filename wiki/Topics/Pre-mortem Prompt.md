# Pre-mortem Prompt

A prompting pattern from [[Robb Green]]: before starting a project, ask the AI to enumerate failure modes. Distinct from a post-mortem — done *before* execution, when there's still time to fix things.

## The Prompt Shape

> "Go ask the AI to do a pre-mortem project. It's not a post-mortem, a
> pre-mortem. And have the AI analyze your project and say, 'Hey, what am
> I not seeing that could go wrong?' And tell me all the things that could
> go wrong. And so now I can see if I want to fix those or not."
> — Robb, [[2026-05-08-ai-hackathon-show-and-tell]] ~57:30

## Why It Works

- **AIs are good at enumeration, bad at judgment.** Listing N risks is exactly what they do well; you decide which to mitigate.
- **Surfaces unknown unknowns.** The model has seen N similar projects fail in training data. Asking forces it to retrieve those failure patterns explicitly.
- **Cheap insurance.** One prompt, minutes to read, can save hours of rework.

## Companion Prompts (also from Robb)

- **"Hold my hand through this process"** — Todd's prompt for getting unstuck without re-explaining everything.
- **"Based on what you know about me and my goals, what tasks can you do to get us closer to our mission, and what tools can you build to make us more productive?"** — Robb's go-to for self-directed agent work, requires the agent to have durable memory of you.

## Key Claims

- **Frameworks beat fluency.** Robb (~58:00): "I'm a big believer in models and frameworks and thinking through frameworks. […] Just getting a set of questions or a set of frameworks will be the biggest unlock in building things."

## Related

- [[Command Centre]] — the kind of structured thinking this implies fits Robb's "Quality first, then speed" operating principle.

## Sources

- [[2026-05-08-ai-hackathon-show-and-tell]] — Robb introduces the pre-mortem prompt ~57:30, reinforces the framework-thinking point ~58:00, posts the "Based on what you know about me…" prompt in chat ~1:05.
