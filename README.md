# Karpathy Ledger

A living, source-tagged synthesis of Andrej Karpathy's public thinking on LLMs and agentic engineering, covering October 2025 onward.

This repo is itself an instance of the [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) Karpathy described: a persistent, compounding knowledge artefact maintained by an agent, where knowledge is compiled once and kept current rather than re-derived on every query. The agent writes; the human curates, sources, and questions.

## What this is

A set of ~118 principles distilled from sixteen primary Karpathy sources (essays, podcasts, repos, posts) plus two community implementation reports. Each principle is paraphrased in plain language and tagged to its source so any claim can be traced back. The principles are organised into thirteen sections that run, roughly, from the deepest philosophical foundation up to day-to-day operating practice.

The intellectual arc is coherent and chronological. It starts from "what is an LLM, at the level of optimisation pressure" (the Space of Minds and Animals vs Ghosts essays) and builds up through capability theory (Verifiability, RLVR), the state of the field (the 2025 Year in Review), and finally operating practice (AutoResearch, the No Priors conversation, the Sequoia talk, the LLM Wiki gist).

## What this is not

This is not a reproduction of Karpathy's writing. The `raw/` folder holds bibliographic cards (title, date, link, short paraphrased summary), not the source texts themselves, which remain his copyright. To read the originals, follow the links. The principles here are transformative synthesis in the maintainer's own words.

This is also not the maintainer's applied/strategic layer. Any application of these ideas to a specific business lives elsewhere, deliberately separated so that Karpathy's thinking and the maintainer's inferences never blur.

## Structure

```
README.md            this file
AGENTS.md            the schema: how the ledger is structured and maintained
index.md             catalog of every principle and section
log.md               chronological record of every ingest and revision
raw/                 immutable source cards (links + paraphrased summaries)
wiki/
  principles/        one file per section, P1 through P118
  sources.md         the chronological source map with tags
  cross-threads.md   threads that span multiple sources
  open-questions.md  unresolved threads worth watching
```

## How to use it

Clone the repo and open the folder in [Obsidian](https://obsidian.md/) (or any markdown reader with backlink/graph support). The repo is the durable store and version history; Obsidian is the reading and navigation layer. This mirrors Karpathy's own setup: agent on one side, Obsidian on the other.

To extend it: hand a new Karpathy source to your agent with "ingest this per AGENTS.md". The agent integrates it across existing principles, flags contradictions, adds new principles, and updates the index and log. See `AGENTS.md` for the full workflow.

## Source weighting

Karpathy-direct sources are authoritative. Community/field-test sources are weighted lower and are never allowed to invent a "Karpathy principle"; they only describe what practitioners hit when implementing his ideas. The tags make the distinction explicit everywhere.

## Status

Synthesised through May 2026. Karpathy joined Anthropic on 19 May 2026; future sources from him will likely be more guarded on lab-internal topics. The ledger is a snapshot of his public thinking up to that point, kept current by ongoing ingest.

Last lint: 1 August 2026. Three sources were ingested the same day, two as named pre-window exceptions, so the synthesis window is unchanged; the coverage gaps that lint identified are now closed or recorded as scope decisions in `log.md`.

## Licence

The synthesis (principle text, structure, tags) is offered under CC-BY-4.0. The underlying ideas belong to Andrej Karpathy; follow the source links for his originals.
