#!/usr/bin/env python3
"""Ledger source watcher (config-driven).

Reads ledger.json at the repo root and polls the author's RSS-able channels,
HTML-diffs their static sites, and (for high-volume feeds) rolls items into a
weekly digest issue. For each new per-item source it opens a GitHub Issue with
a copy-paste `/ingest <URL>` line. State is persisted to .watch/state.json and
committed back by the workflow.

Author-specific values live in ledger.json, never in this file:
  feeds          per-item feeds (one issue per new item)
  digest_feeds   high-volume feeds (accumulated, one rollup issue per week)
  static         pages with no feed (HTML-diff)
  youtube_handle optional; resolved to a channel feed on first run
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
CONFIG_PATH = Path("ledger.json")
PRUNE_TO = 200


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        print(f"error: {CONFIG_PATH} not found; run this from the ledger root", file=sys.stderr)
        sys.exit(1)
    return json.loads(CONFIG_PATH.read_text())


CFG = load_config()
AUTHOR = CFG.get("author", "the author")
SLUG = CFG.get("slug", "ledger")
GITHUB_OWNER = CFG.get("github_owner", "owner")
USER_AGENT = f"{SLUG}-ledger-watcher/1.0 (+https://github.com/{GITHUB_OWNER}/{SLUG}-ledger)"
FEEDS = CFG.get("feeds", {}) or {}
DIGEST_FEEDS = CFG.get("digest_feeds", {}) or {}
STATIC = CFG.get("static", {}) or {}
YOUTUBE_HANDLE = CFG.get("youtube_handle", "") or ""


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"feeds": {}, "static": {}, "config": {}, "digest_pending": [], "bootstrap": True}
    state = json.loads(STATE_PATH.read_text())
    state.setdefault("feeds", {})
    state.setdefault("static", {})
    state.setdefault("config", {})
    state.setdefault("digest_pending", [])
    return state


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def resolve_youtube_feed(state: dict) -> str | None:
    if not YOUTUBE_HANDLE:
        return None
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
                "feed": name,
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


def open_issue(title: str, body: str) -> None:
    subprocess.run(
        ["gh", "issue", "create", "--title", title, "--body", body],
        check=True,
    )


def per_item_body(item: dict) -> str:
    return (
        f"**Source channel:** {item['feed']}\n"
        f"**Title:** {item['title']}\n"
        f"**URL:** {item['link']}\n"
        f"**Published:** {item['published']}\n\n"
        f"To ingest, open Claude Code in the repo and run:\n\n"
        f"```\n/ingest {item['link']}\n```\n\n"
        f"Close this issue once ingested or rejected."
    )


def digest_body(items: list[dict], week: str) -> str:
    by_feed: dict[str, list[dict]] = {}
    for it in items:
        by_feed.setdefault(it.get("feed", "?"), []).append(it)
    lines = [
        f"Rollup of {len(items)} new high-volume items since week {week}. "
        f"These feeds are too noisy for one issue per item, so they are batched. "
        f"Tick each line you ingest; reject the rest.\n",
    ]
    for feed in sorted(by_feed):
        lines.append(f"\n### {feed}\n")
        for it in by_feed[feed]:
            lines.append(f"- [ ] `/ingest {it['link']}` : {it['title']}")
    lines.append("\n\nClose this issue once every line is ingested or rejected.")
    return "\n".join(lines)


def main() -> int:
    state = load_state()
    bootstrap = state.pop("bootstrap", False)
    if bootstrap:
        print("info: bootstrap run; state will be seeded, no issues will be opened")

    now_week = time.strftime("%G-W%V")
    opened_ids: set[str] = set()

    # Per-item feeds (one issue per new item), plus optional YouTube.
    per_item = dict(FEEDS)
    yt_url = resolve_youtube_feed(state)
    if yt_url:
        per_item["youtube"] = yt_url

    for name, url in per_item.items():
        parsed = fetch_feed(name, url)
        if parsed is None:
            continue
        new_items = diff_feed(name, parsed, state)
        print(f"info: {name}: {len(new_items)} new (per-item)")
        if bootstrap:
            continue
        for item in new_items:
            if item["id"] in opened_ids:
                continue
            opened_ids.add(item["id"])
            open_issue(f"New {AUTHOR} source ({name}): {item['title']}", per_item_body(item))

    # Digest feeds (accumulate, flush once per week).
    pending = state.setdefault("digest_pending", [])
    pending_ids = {p["id"] for p in pending}
    for name, url in DIGEST_FEEDS.items():
        parsed = fetch_feed(name, url)
        if parsed is None:
            continue
        new_items = diff_feed(name, parsed, state)
        print(f"info: {name}: {len(new_items)} new (digest)")
        if bootstrap:
            continue
        for item in new_items:
            if item["id"] in opened_ids or item["id"] in pending_ids:
                continue
            pending_ids.add(item["id"])
            opened_ids.add(item["id"])
            pending.append(item)

    last_week = state["config"].get("last_digest_week")
    if bootstrap or last_week is None:
        state["config"]["last_digest_week"] = now_week
    elif pending and now_week != last_week:
        open_issue(f"Weekly {AUTHOR} digest: {last_week}", digest_body(pending, last_week))
        state["digest_pending"] = []
        state["config"]["last_digest_week"] = now_week

    # Static pages (HTML-diff).
    for name, url in STATIC.items():
        changed = diff_static(name, url, state)
        print(f"info: {name}: {'CHANGED' if changed else 'unchanged'}")
        if bootstrap or not changed:
            continue
        body = (
            f"**Source channel:** {name} (HTML-diff)\n"
            f"**URL:** {url}\n\n"
            f"Page content changed since last poll. Open the URL and judge whether the change is "
            f"substantive (new project, new essay, new about-page text) versus noise (analytics, "
            f"deploy hash, timestamp). If substantive, ingest with:\n\n"
            f"```\n/ingest {url}\n```\n\n"
            f"Close this issue once ingested or rejected as noise."
        )
        open_issue(f"New {AUTHOR} source ({name}): page changed", body)

    save_state(state)
    return 0


if __name__ == "__main__":
    sys.exit(main())
