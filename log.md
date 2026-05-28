# Log

Append-only record of ingests, revisions, and lint passes. Newest entries at the bottom. Prefix each entry consistently so it stays greppable.

## [2026-05-28] init | Ledger created
Initial build of the ledger from ten Karpathy-direct sources plus two field-test sources. 112 principles across 13 sections. Sources, in chronological order of original publication: Animals vs Ghosts (Oct 2025), Dwarkesh interview (Oct 2025), Verifiability (Nov 2025), The Space of Minds (Nov 2025), 2025 Year in Review (Dec 2025), AutoResearch README (Mar 2026), Sequoia Ascent blog summary and transcript (Apr 2026), LLM Wiki gist, No Priors interview (May 2026). Field-test: OpenBrain analysis, Cowork implementation walkthrough.

Repo structured per the LLM Wiki three-layer pattern: raw source cards (links, not reproductions, for copyright), the wiki principles, and the AGENTS.md schema. Karpathy-direct and field-test sources tagged and weighted distinctly. Applied/strategic layer deliberately kept out of this public repo.

## [2026-05-28] ingest | LLM Council repo
Source: https://github.com/karpathy/llm-council (vibe-coded weekend hack, 22 Nov 2025). Inserted in `sources.md` between VER and SoM.

**Reinforced** (added `[LC]` tag, text unchanged):
- P6 (jagged intelligence has two axes) — the council pattern exploits inter-model jaggedness.
- P22 (startup wedge: valuable plus verifiable plus undertrained) — Karpathy's "council of LLM judges" gesture is now realised in code.
- P25 (vibe coding raises the floor; agentic engineering raises the ceiling) — Karpathy calls the repo "99% vibe coded".
- P61 (structural overproduction of bespoke apps) — Karpathy's "libraries are over" line matches the thesis.
- P97 (vibe coding terraforms software) — "Code is ephemeral now and libraries are over" is the strongest version of the principle's claim yet.

**Sharpened:** none.

**Contradicted:** none.

**Added:**
- P113 (Part 5: agentic engineering) — The LLM Council pattern. Parallel answers, anonymised cross-ranking, chairman synthesis. Caveat: chairman is itself a single model, so the pattern reduces but does not eliminate single-model dependency.

## How to add the next entry
When ingesting a new source, append a dated line in the form:
`## [YYYY-MM-DD] ingest | <Source title>`
followed by a short note of what reinforced, what sharpened, what contradicted, and what new principle ids were added. For lint passes use `## [YYYY-MM-DD] lint` and record what was found and fixed.
