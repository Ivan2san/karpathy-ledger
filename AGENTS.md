# AGENTS.md

Schema and maintenance instructions for the Karpathy Ledger. This is the highest-leverage file in the repo (per principle P82). If this file is wrong, every ingest is wrong. Invest disproportionate care here.

## What this ledger is

A compounding synthesis of Andrej Karpathy's public thinking on LLMs and agentic engineering. The agent maintains it; the human curates sources and asks questions. Knowledge is compiled once at ingest and kept current, not re-derived on every query.

## Conventions

- **Language:** Australian English.
- **No em-dashes anywhere.** Use commas, semicolons, full stops, or parentheses.
- **Principle IDs are permanent.** Each principle has a stable `P<n>` id. Never renumber. If a principle is retired, mark it superseded; do not delete it and do not reuse its number.
- **Every principle carries source tags** in square brackets, e.g. `[SoM]`, `[DWA 00:40:05]`. Timestamps where available.
- **One quote per source, under fifteen words.** Karpathy's coined terms (for example "summoning ghosts", "crappy evolution", "sucking supervision through a straw") may be used as terminology. Everything else is paraphrase.

## Source weighting (do not violate)

- **Karpathy-direct sources are authoritative.** Essays, podcasts, repos, talks by Karpathy himself.
- **Field-test / community sources are weighted lower.** They describe what practitioners hit when implementing his ideas. They may never invent or be attributed a "Karpathy principle". Keep them in their own section (Part 11) and tag them distinctly (for example `[FT-OB]`, `[FT-CW]`).
- When a community source and a Karpathy-direct source conflict, the Karpathy-direct source wins on what Karpathy thinks; the community source may still stand as a real-world constraint.

## Ingest workflow

When the human supplies a new source and says "ingest this":

1. **Add a source card** to `raw/` (see card format below). Do not reproduce the full text; summarise and link. Respect copyright.
2. **Add the source** to `wiki/sources.md` with its tag, date, and one-line description, keeping chronological order.
3. **Walk the existing principles** and for the new source:
   - **Reinforce:** if it supports an existing principle, add its tag to that principle.
   - **Sharpen:** if it adds nuance, revise the principle and note what changed.
   - **Contradict:** if it conflicts, flag the tension. Do NOT smooth it into a bland middle (P79). Mark the principle contested, keep both readings.
   - **Add:** if it introduces something genuinely new, create a new principle with the next free `P<n>` id, in the most appropriate section.
4. **Update `index.md`** with any new principles.
5. **Append to `log.md`** a dated entry recording what was ingested and what changed.
6. **Report to the human** what reinforced, what sharpened, what contradicted, and what was added, before committing.

## No-smoothing rule (P79)

Contradictions are often the most valuable items in the ledger. If a new source contradicts an existing principle, preserve the tension. A flagged contradiction is a strategic signal, not a defect to be resolved.

## Supersede-don't-delete rule

When a principle stops holding, mark it `SUPERSEDED` with the date, the reason, and a pointer to whatever replaced it. The evolution of the ledger is part of its value. Git history plus explicit supersede markers give a full audit trail.

## Lint workflow (run monthly, per P83)

Health-check the whole ledger:

- Principles that newer sources have superseded but that were never marked.
- Orphaned cross-references (a principle cited that no longer exists or moved).
- Concepts mentioned repeatedly but lacking their own principle.
- Contradictions that crept in silently between sections.
- Source cards missing links or dates.
- Stale framing: anything that reads as current but predates a known shift.

Lint is the operation most maintainers skip, and skipping it is how a wiki drifts into confident misinformation (P76). Schedule it; do not rely on doing it ad hoc.

## Source card format (for `raw/`)

```
# <Source title>

- Tag: <e.g. SoM>
- Type: essay | podcast | repo | talk | community
- Author: Andrej Karpathy | <other>
- Date: <DD Mon YYYY>
- Weight: direct | field-test
- Link: <url>

## Summary
Two or three sentences, paraphrased, in the maintainer's own words.

## Key claims
- Short paraphrased bullets of the load-bearing points, each mapped to the principle id(s) it supports.
```

## Commit conventions

Git history is part of the ledger's evolution record. Keep commit messages greppable and aligned with `log.md` entries.

- **Ingest:** `Ingest: <tag> <source name>` (for example `Ingest: NP2 No Priors follow-up`). One commit per source. Pairs with the `## [YYYY-MM-DD] ingest | <Source title>` entry in `log.md`.
- **Lint:** `Lint: YYYY-MM` (for example `Lint: 2026-06`). One commit per monthly lint pass, after the human has triaged findings. Pairs with the `## [YYYY-MM-DD] lint` entry in `log.md`.
- **Schema or housekeeping changes** (edits to this file, `README.md`, `.gitignore`, etc.) use a short conventional prefix: `docs:`, `chore:`, `refactor:`.

The `/ingest` and `/lint` slash commands in `.claude/commands/` execute the workflows defined above and stop before commit so the human can review the diff.

## Outputs (export-only)

Authored deliverables generated from the ledger (reports, briefings, teaching artefacts) live in `outputs/` as `YYYY-MM-DD_short-name.md`. They are distinct from the wiki: the wiki is faithful synthesis of Karpathy's sources; outputs add selection, audience, and framing for a purpose.

Critical: outputs are export-only. They never feed back into `wiki/principles/`. Unlike an applied knowledge base, nothing an output reasons to is filed back as a principle, because the corpus is single-author and your framing is not Karpathy's claim. New principles arrive ONLY through ingest of a Karpathy-direct source. If a deliverable needs applied or business-specific framing, it does not belong in this repo at all.

Note that this is a deliberate departure from P52 (Karpathy-direct) and P84 (field-test), both of which require findings to flow back into the wiki. The departure is a consequence of single-author purity, not a judgement that those principles are wrong. Per the no-smoothing rule, the tension is flagged in P52 and P84 themselves rather than resolved in favour of this file.

## What lives elsewhere

The maintainer's applied or strategic layer (any application of these principles to a specific business or context) is kept in a separate, private location. It must never be merged into this repo. This repo is Karpathy's thinking only, so that his ideas and the maintainer's inferences never blur.
