# Command Centre

[[Robb Green]]'s unified platform for autonomous, knowledge-compounding agents. Three numbered layers, with input flowing top-to-bottom from a human brief through interface → orchestration → memory & skills. Source: Robb's `Command_Centre_Architecture.md` (shared on the [[2026-05-08-ai-hackathon-show-and-tell]] call) plus the live walkthrough at ~28-34 min.

## Architecture

### Input
**YOU (Robb) → brief**, via one of three Interface Channels: Dashboard, Telegram, WhatsApp.

### 3. Interface & Comms
*Report-out only — no babysitting required. "Where you live."*

| Component | Tag | Description |
|---|---|---|
| **OpenDitto** | TELEGRAM | Production Telegram bridge — multi-chat, 24/7, memory-durable. Command Centre subscribes to its events. New channels only added when a real recipient exists. |
| **Mission Control** | DASHBOARD | Self-hosted dashboard for fleet status, task dispatch, cost tracking. Supabase-backed, realtime subscriptions. |
| **Notifier** | ALERTS | ~30-LOC function inside the orchestrator that posts task state changes through OpenDitto. Real-time on failures, passive on success. *"Not a product."* |

### 2. Orchestration
*Break briefs → spawn agents → coordinate execution.*

| Component | Tag | Description |
|---|---|---|
| **Claude Code** | RUNTIME | Core agent runtime. Subscription-billed, not API. Swappable for Codex if better tool emerges. |
| **Runner** | RUNNER | Worktree-isolated executor (ported from Auto-Claude). Spawns Claude CLI per task; Supabase task queue + git worktrees handle parallelism without MetaSwarm/Overstory. |
| **Project Engine** | WORKFLOW | "Roofer AI audit" = a project. Holds workflow definition, attached skills, agent assignments, state. |
| **Trust Tier System** | GOVERNANCE | New agents → guardrails. Proven agents → autonomy. See [[Trust Tier System]]. |

### 1. Memory & Skills
*The part that compounds — your real moat.*

| Component | Tag | Description |
|---|---|---|
| **LLM Wiki (Karpathy)** | KNOWLEDGE | Markdown knowledge base agents read & maintain. Inbox → processed → wiki. See [[LLM Wiki Pattern]]. |
| **Wiki Indexer** | INDEXING | `packages/wiki` — TypeScript module that hashes, indexes, and search-syncs the inbox→processed→wiki vault into Supabase. Native to the stack, no Go runtime. |
| **Skills Registry** | SKILLS | `SKILL.md` files = scripts + process + metadata (cost, prereqs, reliability). Agents query, don't hunt. |
| **Skill Evaluator** | v0 + DEFERRED | Per-workflow scoring. v0 ships with Phase 1; v1 learning loop waits until ~100+ `agent_runs` exist to train a real signal. |
| **Skill Authoring (SkillForge)** | AUTHORING + DEFERRED | Fires when the Evaluator returns no fit ≥ 0.5 and the operator approves. SkillForge's 4-phase rigor (triage → analysis → spec → multi-agent review) generates a new SKILL.md, registered into the registry. |
| **Supabase** | DATA | Project state, agent runs, task queue, structured data. The system of record. |

## Operating Principles

1. **Quality first, then speed** — speed without quality is just fast garbage.
2. **Assemble best-in-class pieces first;** build custom only where the market doesn't deliver.
3. **Agents earn autonomy by proving reliability over time.** ([[Trust Tier System]])
4. **Real-time alerts on failures;** passive on successes. (Notifier)
5. **Every learning becomes a skill or a wiki entry** — nothing wasted.
6. **One UI, many projects** — roofer audit, TikTok ops, real estate, all one platform.

## Key Claims

- **Memory is the moat.** Layer 1 (Memory & Skills) is what compounds; orchestration and interface are commodity. — [[2026-05-08-ai-hackathon-show-and-tell]]
- **Subscription-billed Claude beats API for runtime.** Cost predictability + tool maturity. Swap to Codex iff a clearly better tool emerges.
- **Worktrees + Supabase task queue replace heavyweight orchestrators.** No MetaSwarm/Overstory needed for parallelism if you commit to git worktrees per task.
- **Defer the learning loop until you have 100+ agent runs.** Skill Evaluator v1 needs real data to train on; ship v0 (per-workflow scoring) first.
- **Failure-only alerts.** Don't notify on success — the Notifier is real-time on failures, passive otherwise. Avoids alert fatigue.

## Related

- [[LLM Wiki Pattern]] — the Memory layer's knowledge base.
- [[Trust Tier System]] — the Orchestration layer's governance.
- [[Farmer Pattern]] — Robb's "context farming" feeds the wiki's inbox.
- [[Intel Channel]] — output side: how the Notifier surfaces farmer results.

## Sources

- [[2026-05-08-ai-hackathon-show-and-tell]] — Robb's live walkthrough at ~28-34 min plus his standalone architecture doc.
