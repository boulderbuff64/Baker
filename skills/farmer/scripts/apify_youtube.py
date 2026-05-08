#!/usr/bin/env python3
"""
Farmer fetcher: Apify YouTube → ~/Obsidian/Wiki.

Usage:
  apify_youtube.py <farmer-config-path>
  apify_youtube.py --dry-run <farmer-config-path>

Reads a farmer config (markdown with YAML frontmatter + creators/keywords/args
blocks), runs streamers/youtube-scraper for each tracked channel and keyword,
dedupes against existing Sources/youtube/ files by video_id, writes new Sources
with frontmatter, and emits a daily Digest grouped by verdict.

Verdict assignment is left as TODO=skim — a curator pass (manual or LLM) should
re-rate before the digest is shared. The script's job is plumbing: fetch,
dedupe, write skeletons.

Env: sources APIFY_API_TOKEN from ~/.claude/skills/apify-youtube-scrape/.env.local
if not already in the environment.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path

import urllib.request

WIKI_ROOT = Path.home() / "Obsidian" / "Wiki"
SOURCES_DIR = WIKI_ROOT / "Sources" / "youtube"
DIGESTS_DIR = WIKI_ROOT / "Digests"
ENV_FILE = Path.home() / ".claude" / "skills" / "apify-youtube-scrape" / ".env.local"
ACTOR = "streamers~youtube-scraper"
APIFY_BASE = "https://api.apify.com/v2"


def load_env() -> str:
    token = os.environ.get("APIFY_API_TOKEN")
    if token:
        return token
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if line.startswith("APIFY_API_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("APIFY_API_TOKEN not found (env or ~/.claude/skills/apify-youtube-scrape/.env.local)")


def parse_farmer_config(path: Path) -> dict:
    """Pull frontmatter + the creators/keywords/args YAML/JSON code blocks."""
    text = path.read_text()
    cfg: dict = {"name": path.stem, "creators": [], "keywords": [], "args": {}}

    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            front = text[3:end]
            for line in front.splitlines():
                if ":" in line and not line.lstrip().startswith("-"):
                    k, v = line.split(":", 1)
                    cfg[k.strip()] = v.strip().strip('"').strip("'")
            text = text[end + 4 :]

    def extract_block(lang: str, header: str) -> str | None:
        # Find "## <header>" then the next ```<lang> ... ``` block
        m = re.search(rf"^##\s+{re.escape(header)}.*?\n```{lang}\n(.*?)\n```", text, re.S | re.M)
        return m.group(1) if m else None

    creators_yaml = extract_block("yaml", "Tracked Creators") or extract_block("yaml", "Tracked")
    if creators_yaml:
        for line in creators_yaml.splitlines():
            line = line.strip()
            if line.startswith("- "):
                cfg["creators"].append(line[2:].strip().strip('"').strip("'"))

    kw_yaml = extract_block("yaml", "Topical Keywords")
    if kw_yaml:
        for line in kw_yaml.splitlines():
            line = line.strip()
            if line.startswith("- "):
                cfg["keywords"].append(line[2:].strip().strip('"').strip("'"))

    args_json = extract_block("json", "Fetcher Args")
    if args_json:
        try:
            cfg["args"] = json.loads(args_json)
        except json.JSONDecodeError:
            cfg["args"] = {}

    return cfg


def apify_run_sync(token: str, payload: dict, timeout: int = 540) -> list[dict]:
    url = f"{APIFY_BASE}/acts/{ACTOR}/run-sync-get-dataset-items?{urllib.parse.urlencode({'token': token, 'timeout': timeout})}"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout + 30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def existing_video_ids() -> set[str]:
    ids: set[str] = set()
    if not SOURCES_DIR.exists():
        return ids
    for f in SOURCES_DIR.glob("*.md"):
        m = re.search(r"^video_id:\s*(\S+)", f.read_text(), re.M)
        if m:
            ids.add(m.group(1).strip().strip('"').strip("'"))
    return ids


def slugify(s: str) -> str:
    s = re.sub(r"[^\w\s-]", "", s.lower())
    s = re.sub(r"[\s_-]+", "-", s).strip("-")
    return s[:60] or "untitled"


def write_source(item: dict, farmer_name: str) -> Path:
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    pub = (item.get("date") or "")[:10] or dt.date.today().isoformat()
    slug = slugify(item.get("title") or item.get("id", "video"))
    path = SOURCES_DIR / f"{pub}-{slug}.md"
    desc = (item.get("text") or "").strip()
    desc_short = desc[:600] + ("…" if len(desc) > 600 else "")
    fm = {
        "type": "source",
        "source_type": "youtube",
        "url": item.get("url"),
        "video_id": item.get("id"),
        "title": item.get("title"),
        "channel": item.get("channelName"),
        "channel_url": item.get("channelUrl"),
        "published": pub,
        "duration": item.get("duration"),
        "views": item.get("viewCount"),
        "likes": item.get("likes"),
        "comments": item.get("commentsCount"),
        "verdict": "skim",  # TODO: curator pass to re-rate
        "ingested": dt.date.today().isoformat(),
        "ingested_by": farmer_name,
        "topics": [],
        "people": [],
        "tags": ["source/youtube", "verdict/skim", "needs-curator-pass"],
    }
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            if not v:
                lines.append(f"{k}: []")
            else:
                lines.append(f"{k}:")
                for x in v:
                    lines.append(f"  - {json.dumps(x, ensure_ascii=False)}")
        elif v is None:
            lines.append(f"{k}: ")
        elif isinstance(v, (int, float)):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {json.dumps(str(v), ensure_ascii=False)}")
    lines.append("---")
    lines.append("")
    lines.append(f"👀 SKIM **[{item.get('title')}]({item.get('url')})**")
    lines.append(f"*{item.get('channelName')} · {item.get('viewCount')} views · {pub} · {item.get('duration')}*")
    lines.append("")
    lines.append("> " + (desc_short.replace("\n", "\n> ") or "*(no description)*"))
    lines.append("")
    lines.append("> *Why: TODO — curator pass.*")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- TODO: lift specific claims, link to Topics & People.")
    path.write_text("\n".join(lines))
    return path


def write_digest(farmer_name: str, kept: list[dict], skipped: int) -> Path:
    DIGESTS_DIR.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    path = DIGESTS_DIR / f"{today}-{farmer_name}.md"
    lines = ["---"]
    lines.append("type: digest")
    lines.append(f"farmer: {farmer_name}")
    lines.append(f"run_date: {today}")
    lines.append(f"items_total: {len(kept) + skipped}")
    lines.append(f"items_kept: {len(kept)}")
    lines.append(f"items_skipped: {skipped}")
    lines.append("fetcher: apify")
    lines.append("actor: streamers/youtube-scraper")
    lines.append("---")
    lines.append("")
    lines.append(f"# {today} — {farmer_name}")
    lines.append("")
    if not kept:
        lines.append("*No new videos.*")
    else:
        lines.append("## 👀 SKIM (pending curator pass)")
        lines.append("")
        for item in kept:
            pub = (item.get("date") or "")[:10]
            lines.append(
                f"- 👀 SKIM **[{item.get('title')}]({item.get('url')})** — "
                f"*{item.get('channelName')} · {item.get('viewCount')} views · {pub} · {item.get('duration')}*"
            )
    path.write_text("\n".join(lines) + "\n")
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("config", type=Path, help="Path to farmer config .md")
    ap.add_argument("--dry-run", action="store_true", help="Fetch but don't write")
    args = ap.parse_args()

    if not args.config.exists():
        sys.exit(f"Config not found: {args.config}")

    cfg = parse_farmer_config(args.config)
    token = load_env()

    fetcher_args = cfg.get("args", {})
    start_urls = [{"url": f"https://www.youtube.com/@{h}/videos"} for h in cfg["creators"]]
    payload = {
        "startUrls": start_urls,
        "keywords": cfg["keywords"],
        "maxResults": fetcher_args.get("maxResultsPerCreator", 20),
        "maxResultsShorts": 0 if not fetcher_args.get("includeShorts") else 10,
        "maxResultStreams": 0 if not fetcher_args.get("includeStreams") else 5,
        "dateFilter": fetcher_args.get("dateFilter", "today"),
    }
    if fetcher_args.get("subtitlesLanguage"):
        payload["subtitlesLanguage"] = fetcher_args["subtitlesLanguage"]
        payload["subtitlesFormat"] = "srt"

    if not start_urls and not cfg["keywords"]:
        sys.exit("Farmer has no creators or keywords")

    print(f"[{cfg['name']}] fetching: {len(start_urls)} creators, {len(cfg['keywords'])} keywords")
    items = apify_run_sync(token, payload)
    print(f"[{cfg['name']}] received {len(items)} items")

    seen = existing_video_ids()
    new = [i for i in items if i.get("id") and i["id"] not in seen]
    skipped = len(items) - len(new)
    print(f"[{cfg['name']}] {len(new)} new, {skipped} dupes")

    if args.dry_run:
        for i in new:
            print(f"  - {i.get('id')} {i.get('title')[:80]}")
        return 0

    for item in new:
        p = write_source(item, cfg["name"])
        print(f"  wrote {p.relative_to(WIKI_ROOT)}")

    digest_path = write_digest(cfg["name"], new, skipped)
    print(f"[{cfg['name']}] digest: {digest_path.relative_to(WIKI_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
