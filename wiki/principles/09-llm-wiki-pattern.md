# Part 9: The LLM Wiki pattern

**P49. RAG rediscovers; the wiki accumulates.** The default LLM-plus-documents pattern re-derives knowledge on every query and saves nothing between sessions. The LLM Wiki inverts this: knowledge is compiled once into a persistent artefact, then kept current. The cross-references already exist, the contradictions are already flagged, the synthesis already reflects everything read. `[WIKI]`

**P50. Three-layer architecture.** Raw sources (immutable, your source of truth) / wiki (LLM-generated, LLM-owned markdown) / schema (your AGENTS.md or CLAUDE.md telling the LLM how to behave). The human owns the sources and the schema; the LLM owns the wiki entirely. `[WIKI]`

**P51. Three operations: ingest, query, lint.** Ingest reads a new source and integrates it across all touched pages (ten to fifteen per source is typical). Query answers from the wiki with citations and files good answers back as new pages. Lint is a periodic health check for contradictions, stale claims, orphan pages, and missing cross-references. Lint is the operation most maintainers skip. `[WIKI]`

**P52. File good answers back into the wiki.** A comparison you asked for, a connection you discovered, an analysis you ran: these are valuable and should not vanish into chat history. File them back as pages. Your explorations compound, not just your sources. The difference between a knowledge base and a notebook. `[WIKI]`

**P53. The bookkeeping is the bottleneck, not the thinking.** Humans abandon wikis because the maintenance burden grows faster than the value: cross-references go stale, summaries get outdated, contradictions go unflagged. LLMs do not get bored and can touch fifteen files in one pass. The wiki stays maintained because the cost of maintenance is near zero. This is what makes the pattern work now that it did not before. `[WIKI]`

**P54. index.md plus log.md are the navigation primitives.** index.md is content-oriented (a catalog of every page with a one-line summary). log.md is chronological (an append-only record of every ingest, query, and lint). The index helps at query time; the log helps with audit and continuity across sessions. `[WIKI]`

**P55. The Memex was waiting for the maintainer.** Vannevar Bush's 1945 vision of a personal, curated knowledge store with associative trails was correct. What he could not solve was who does the maintenance. The LLM handles that. The LLM Wiki is the completion of an old idea, not a new one. `[WIKI]`

**P56. See Part 4** for the inferred Software 3.0 predicate (integratability), which connects this pattern to the broader paradigm.
