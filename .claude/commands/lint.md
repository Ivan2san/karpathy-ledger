---
description: Run the monthly lint pass on the ledger per AGENTS.md
---

Run the lint workflow on the Karpathy Ledger as defined in @AGENTS.md (§Lint workflow).

**Report findings before changing anything.** This is a review pass, not an edit pass.

Check for:

1. **Silent supersessions** — principles that newer sources have effectively superseded but that were never marked `SUPERSEDED`.
2. **Orphaned cross-references** — a principle citing another `P<n>` that no longer exists, has moved, or has been renamed.
3. **Missing principles** — concepts mentioned repeatedly across sources or principles that lack their own `P<n>` entry.
4. **Silent contradictions** — tensions that crept in between sections without being flagged (P79 violations).
5. **Source card hygiene** — cards in `raw/` missing links, dates, weight, or tag.
6. **Stale framing** — anything that reads as current but predates a known shift (for example pre-December 2025 framing on agentic capabilities after the P2 inflection point).

For each finding, report:
- Where it is (file + principle id or line)
- What the issue is
- Suggested resolution (do not apply yet)

After reporting, wait for the human to triage. Only apply changes that are explicitly approved. When changes are applied, append a dated entry to `log.md` in the form `## [YYYY-MM-DD] lint` recording what was found and what was fixed, then commit as `Lint: YYYY-MM` per the convention in AGENTS.md.

Remember: skipping or rubber-stamping lint is how a wiki drifts into confident misinformation (P76). Be thorough.
