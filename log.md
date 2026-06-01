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

## [2026-06-01] lint
First monthly lint pass (per P83). Read the full ledger against the six checks in AGENTS.md: 13 principle files, 14 source cards, index, sources, cross-threads, open-questions, both READMEs. Index and principle files were in sync, P1 to P113 a complete sequence, no orphaned cross-references.

**Found and fixed (human-triaged):**
- Stale framing. P4 ("autocomplete with the human as architect" as Karpathy's default, DWA Oct 2025) predated the December 2025 inflection (P2). Added a dated snapshot note cross-referencing P2 rather than rewriting, per supersede-don't-delete.
- Stale counts. README said "~112 principles" and "P1 through P112"; the LLM Council ingest had added P113 without propagating. Updated to 115 and P1 through P115 (113 after that ingest, plus P114 and P115 added this pass).
- Tag convention. P112 carried `[SoM, AvG, P90]`; P90 is a principle, not a source. Dropped to `[SoM, AvG]` (P90 is still cited in the prose).
- Missing cross-reference. P17 and P99 both claim LLMs are the next computing paradigm with no link between them. Added reciprocal pointers (P99 is the generative sharpening of P17).
- Source-card hygiene. The DWA card and sources.md linked the Dwarkesh homepage with a month-only date. Replaced with the specific episode (https://www.dwarkesh.com/p/andrej-karpathy), dated 17 Oct 2025.
- NP date correction (full, maintainer-approved during triage). The No Priors interview was dated "May 2026" but published 20 Mar 2026 (verified via Apple Podcasts and YouTube). Re-dated the card and sources.md, added the episode link (https://www.youtube.com/watch?v=kwSVtQ7dziU), corrected the card's "around the Anthropic move" note (it predates the 19 May move by about two months), softened P71's "weeks before" to "about two months before", reordered NP between AR and SEQ-B in sources.md, and updated the corpus span to "Oct 2025 to Apr 2026" in sources.md and README. The init entry below (2026-05-28) is left unedited as append-only history; this entry supersedes its NP dating.

**Added** (formalising concepts already synthesised in cross-threads, both from the No Priors source, Karpathy-direct):
- P114 (Part 5). The orchestration stack is six layers, each its own skill ceiling. Previously only in cross-threads thread 6. Tagged `[NP]`; exact timestamp not pinned.
- P115 (Part 7). The agent-as-glue orchestrator (Dobby) is the third reference implementation. Previously only supporting evidence under P61 and P68 and cross-threads thread 3. Tagged `[NP 12:00, NP 13:00]`.
- Cross-threads threads 3 and 6 back-referenced to the new ids.

**Not changed this pass (by design):**
- FT-CW and FT-OB cards have no link ("source not retained"); kept as honest markers.
- P60 placement (sits in Part 3, reads as Part 5 material); not moved, since ids are permanent and only the section file would change.

## How to add the next entry
When ingesting a new source, append a dated line in the form:
`## [YYYY-MM-DD] ingest | <Source title>`
followed by a short note of what reinforced, what sharpened, what contradicted, and what new principle ids were added. For lint passes use `## [YYYY-MM-DD] lint` and record what was found and fixed.
