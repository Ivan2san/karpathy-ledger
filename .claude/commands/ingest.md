---
description: Ingest a new Karpathy source into the ledger per AGENTS.md
argument-hint: <source path, URL, or pasted text>
---

Ingest the source below into the Karpathy Ledger.

**Source:** $ARGUMENTS

Follow the ingest workflow defined in @AGENTS.md exactly. Specifically:

1. Add a source card to `raw/` using the card format in AGENTS.md.
2. Add the source to `wiki/sources.md` with its tag, date, and one-line description, in chronological order.
3. Walk every existing principle in `wiki/principles/` and classify the source's effect: **reinforce**, **sharpen**, **contradict**, or **add**. Honour the no-smoothing rule (P79): preserve contradictions, do not blend them.
4. Update `index.md` for any new principles.
5. Append a dated entry to `log.md` in the form `## [YYYY-MM-DD] ingest | <Source title>` recording what reinforced, what sharpened, what contradicted, and what new principle ids were added.
6. Honour the source weighting rule: Karpathy-direct is authoritative; field-test sources go in Part 11 and are never attributed as Karpathy principles.

**Stop before committing.** Report:
- What reinforced (which principles, which tags added)
- What sharpened (which principles, what changed)
- What contradicted (which principles, what tension was flagged)
- What was added (new principle ids and section)
- A summary of the diff for review

Wait for the human to approve before staging or committing. When approved, commit as `Ingest: <tag> <source name>` per the convention in AGENTS.md.
