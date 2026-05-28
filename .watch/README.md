# Karpathy watcher

Daily GitHub Action that polls Karpathy's publishing channels and opens an Issue for each new item, with a copy-paste `/ingest <URL>` line ready to run.

## What it watches

**RSS (cheap, reliable):**
- GitHub activity — `https://github.com/karpathy.atom` (new repos, gists, pushes)
- Bearblog — `https://karpathy.bearblog.dev/feed/`
- YouTube — channel atom feed (channel ID auto-resolved on first run)
- Medium — `https://karpathy.medium.com/feed` (near-dead, but cheap to keep watching)

**HTML diff (noisier, but no RSS available):**
- `https://karpathy.ai/`
- `https://eurekalabs.ai/`

## What it does not watch (and why)

- **X / Twitter** — no public RSS, paid API would cost ~$100/mo, scraping is fragile. Accepted gap; scan manually when you check X anyway.
- **Third-party podcasts and talks** — unenumerable in advance. Use Google Alerts for `"Andrej Karpathy" -site:karpathy.ai` and do a quarterly podcast-feed scan if it matters.

## How it runs

- `.github/workflows/karpathy-watch.yml` runs daily at 00:00 UTC (~10:00 AEST) and on manual `workflow_dispatch`.
- `.github/scripts/karpathy_watch.py` does the polling.
- `.watch/state.json` is the persisted state: last-seen feed item IDs, last-seen page SHAs, the resolved YouTube channel ID. Committed back to the repo by the workflow when it changes.

## First run

The first run is a **bootstrap**: it seeds `.watch/state.json` with everything currently in each feed and *does not* open issues. From the second run on, only genuinely new items trigger issues.

To trigger the bootstrap immediately rather than waiting for the daily cron:
```
gh workflow run "Karpathy watcher"
```

## When an issue lands

1. Open it. The body has the URL and a `/ingest <URL>` line.
2. Open Claude Code in the repo and paste the command.
3. The `/ingest` slash command does the rest (see `AGENTS.md` §Ingest workflow).
4. Close the issue once the source is ingested, or close as "not signal" if it's noise.

## Failure modes to know

- **Static-site diffs are noisy.** Analytics changes, deploy hashes, and timestamp updates will all trigger an issue. Triage by opening the URL and judging substance. If a site is consistently noisy, narrow the diff to a content selector inside the script.
- **YouTube channel ID resolution** depends on YouTube serving the channel page with the ID embedded in HTML. If YouTube changes its markup, resolution fails silently (logged as warning) and the YouTube feed is skipped until fixed.
- **First-run flood** is prevented by the bootstrap flag. Do not delete `.watch/state.json` casually; doing so re-bootstraps and you lose the seen-IDs history.
