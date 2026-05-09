# Lightning Bolt Acknowledgment

A small UX pattern from [[Robb Green]] that solves the "black hole" problem: when you message an agent and don't know if it received you. The agent emoji-reacts ⚡ on receive, before it starts work.

## Why

> "When I asked Jarvis [Robb's Open Claw agent] something, he gives me a
> lightning bolt to acknowledge that he's received the message. So now I
> know and I don't have to wait for to see the typing typing. It
> acknowledges immediately with a lightning bolt. And now if I don't see a
> lightning bolt, I assume he did not get the message and something broke."
> — Robb, [[2026-05-08-ai-hackathon-show-and-tell]] ~1:03

## Key Claims

- **Black hole = the worst UX failure mode.** You don't know if it received you, started work, crashed, or is still thinking. Same complaint people have about humans who don't acknowledge.
- **Reaction emoji is cheap and unambiguous.** Distinct from "still thinking" indicators — it's a guaranteed receive-confirm before any work.
- **Failure mode = absent emoji.** No lightning bolt = retry / check pipeline, in seconds rather than minutes.
- **Implementable in ~30 LOC.** Maps to the Notifier component in Robb's [[Command Centre]] architecture.

## Generalization

Pattern applies anywhere agents accept async input — Slack, Discord, Telegram, email, webhook intake. The specific emoji doesn't matter; the *receive-confirm distinct from result* does.

## Related

- [[Command Centre]] — the Notifier (~30 LOC inside the orchestrator) is the plumbing.

## Sources

- [[2026-05-08-ai-hackathon-show-and-tell]] — Robb describes the pattern and the underlying complaint about "black holes" ~1:02–1:04.
