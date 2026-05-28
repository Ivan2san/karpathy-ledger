#!/usr/bin/env python3
"""Karpathy watcher.

Polls Karpathy's RSS-able channels and HTML-diffs his static sites.
For each new item, opens a GitHub Issue with a copy-paste `/ingest <URL>` line.
State is persisted to .watch/state.json and committed back by the workflow.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import feedparser
import requests

STATE_PATH = Path(".watch/state.json")
PRUNE_TO = 200
USER_AGENT = "karpathy-ledger-watcher/1.0 (+https://github.com/Ivan2san/karpathy-ledger)"

FEEDS = {
    "github": "https://github.com/karpathy.atom",
    "bearblog": "https://karpathy.bearblog.dev/feed/",
    "medium": "https://karpathy.medium.com/feed",
}

STATIC = {
    "karpathy.ai": "https://karpathy.ai/",
    "eurekalabs.ai": "https://eurekalabs.ai/",
}

YOUTUBE_HANDLE = "AndrejKarpathy"


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"feeds": {}, "static": {}, "config": {}, "bootstrap": True}
    return json.loads(STATE_PATH.read_text())


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def resolve_youtube_feed(state: dict) -> str | None:
    cached = state.setdefault("config", {}).get("youtube_channel_id")
    if cached:
        return f"https://www.youtube.com/feeds/videos.xml?channel_id={cached}"
    try:
        r = requests.get(
            f"https://www.youtube.com/@{YOUTUBE_HANDLE}",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30,
        )
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"warn: youtube handle fetch failed: {e}", file=sys.stderr)
        return None
    m = re.search(r'"channelId":"(UC[a-zA-Z0-9_-]{22})"', r.text) or re.search(
        r'"externalId":"(UC[a-zA-Z0-9_-]{22})"', r.text
    )
    if not m:
        print(f"warn: could not extract channel id for @{YOUTUBE_HANDLE}", file=sys.stderr)
        return None
    cid = m.group(1)
    state["config"]["youtube_channel_id"] = cid
    print(f"info: resolved youtube channel id: {cid}")
    return f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"


def fetch_feed(name: str, url: str) -> feedparser.FeedParserDict | None:
    try:
        r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"error: feed {name} fetch failed: {e}", file=sys.stderr)
        return None
    parsed = feedparser.parse(r.content)
    if parsed.bozo and not parsed.entries:
        print(f"error: feed {name} unparseable: {parsed.bozo_exception}", file=sys.stderr)
        return None
    return parsed


def diff_feed(name: str, parsed: feedparser.FeedParserDict, state: dict) -> list[dict]:
    seen = set(state["feeds"].get(name, {}).get("seen", []))
    new_items = []
    current_ids = []
    for entry in parsed.entries[:50]:
        eid = entry.get("id") or entry.get("link")
        if not eid:
            continue
        current_ids.append(eid)
        if eid not in seen:
            new_items.append({
                "id": eid,
                "title": entry.get("title", "<untitled>"),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
            })
    updated_seen = list(seen | set(current_ids))[-PRUNE_TO:]
    state["feeds"][name] = {"seen": updated_seen}
    return new_items


def diff_static(name: str, url: str, state: dict) -> bool:
    try:
        r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"error: static {name} fetch failed: {e}", file=sys.stderr)
        return False
    sha = hashlib.sha256(r.content).hexdigest()
    prior = state["static"].get(name, {}).get("sha256")
    state["static"][name] = {"sha256": sha, "checked_at": int(time.time())}
    return prior is not None and sha != prior


def open_issue(title: str, body: str, dry_run: bool) -> None:
    if dry_run:
        print(f"[dry-run] would open issue: {title}")
        return
    subprocess.run(
        ["gh", "issue", "create", "--title", title, "--body", body],
        check=True,
    )


def main() -> int:
    state = load_state()
    bootstrap = state.pop("bootstrap", False)
    if bootstrap:
        print("info: bootstrap run — state will be seeded; no issues will be opened")

    yt_url = resolve_youtube_feed(state)
    feeds_to_poll = dict(FEEDS)
    if yt_url:
        feeds_to_poll["youtube"] = yt_url

    for name, url in feeds_to_poll.items():
        parsed = fetch_feed(name, url)
        if parsed is None:
            continue
        new_items = diff_feed(name, parsed, state)
        print(f"info: {name}: {len(new_items)} new")
        if bootstrap:
            continue
        for item in new_items:
            title = item["title"]
            link = item["link"]
            published = item["published"]
            body = (
                f"**Source channel:** {name}\n"
                f"**Title:** {title}\n"
                f"**URL:** {link}\n"
                f"**Published:** {published}\n\n"
                f"To ingest, open Claude Code in the repo and run:\n\n"
                f"```\n/ingest {link}\n```\n\n"
                f"Close this issue once ingested or rejected."
            )
            open_issue(f"New Karpathy source ({name}): {title}", body, dry_run=False)

    for name, url in STATIC.items():
        changed = diff_static(name, url, state)
        print(f"info: {name}: {'CHANGED' if changed else 'unchanged'}")
        if bootstrap or not changed:
            continue
        body = (
            f"**Source channel:** {name} (HTML-diff)\n"
            f"**URL:** {url}\n\n"
            f"Page content changed since last poll. Open the URL and judge whether the change is substantive (new project, new essay, new about-page text) versus noise (analytics, deploy hash, timestamp). "
            f"If substantive, ingest with:\n\n"
            f"```\n/ingest {url}\n```\n\n"
            f"Close this issue once ingested or rejected as noise."
        )
        open_issue(f"New Karpathy source ({name}): page changed", body, dry_run=False)

    save_state(state)
    return 0


if __name__ == "__main__":
    sys.exit(main())
