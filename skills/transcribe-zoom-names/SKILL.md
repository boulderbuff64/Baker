---
name: transcribe-zoom-names
description: Use when the user provides a screenshot of a Zoom (or similar video call) and asks to list, extract, transcribe, or copy the participant names. Triggers include "names from this zoom", "who's on this call", "list the participants", "transcribe the attendees".
---

# Transcribe Zoom Names

## Overview

Extract every participant name visible in a Zoom call screenshot and return them as a clean list. Names appear in three places depending on view:

1. **Video tile name labels** — bottom-left corner of each tile (gallery or speaker view)
2. **Participants panel** — right sidebar list (when open)
3. **Active speaker banner** — top of speaker view

## Workflow

1. **Read the image** with the Read tool (works on PNG/JPG paths the user provides).
2. **Identify the view type** — gallery grid, speaker view, or participants panel open. Note it in your reply so the user can confirm coverage.
3. **Scan every tile and the panel if visible.** Don't skip:
   - Tiles showing initials/avatars (still have a name label)
   - Tiles showing "(Host)", "(Co-host)", "(me)" suffixes — strip these unless asked to keep
   - Off-screen participants indicated by "+N more" — report the count, don't invent names
   - The participants panel if open (it's authoritative; prefer it over tile labels when both visible)
4. **Output** as a numbered or bulleted list, one name per line, preserving the spelling exactly as shown (including diacritics, capitalization, emoji, pronouns in parentheses).
5. **Flag uncertainty** for any name that is partially occluded, low-resolution, or cut off — mark with `[?]` and show your best guess.

## Output Format

Default to a plain markdown list:

```
1. Jane Doe
2. Carlos Martínez (he/him)
3. priya.k [?]
4. Sam Wong
```

If the user asks for CSV, JSON, or "just the names comma-separated", honor that.

## Quick Reference

| Situation | What to do |
|---|---|
| Both tile labels and participants panel visible | Use panel; cross-check against tiles |
| Name truncated with `…` | Output what's visible + `[?]` |
| Tile shows only initials, no name label | Skip and note "1 tile with initials only, no name visible" |
| Duplicate (same person in tile + panel) | List once |
| "+12 more" indicator | Add line: "...and 12 more not shown" |
| Pronouns/role suffixes ((he/him), (Host)) | Keep pronouns by default; strip role tags unless asked |

## Common Mistakes

- **Inventing names for avatar-only tiles.** If there's no text label, don't guess from the avatar image.
- **Normalizing spelling.** Output names verbatim — don't "correct" `Mohammad` to `Muhammad` etc.
- **Missing the participants panel.** Always check the right edge of the screenshot for an open panel; it's the most reliable source.
- **Counting yourself twice.** A tile labeled "Me" and a panel entry with the user's real name are the same person.
- **Dropping non-Latin scripts.** Transcribe names in any script as shown (Cyrillic, CJK, Arabic, etc.).

## When the Screenshot Is Unclear

If resolution is too low to read names confidently, say so explicitly and list only the names you can read with confidence. Do not pad the list with guesses. Offer to re-run on a higher-resolution version.
