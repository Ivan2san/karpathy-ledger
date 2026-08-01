# Part 11: Field-tested constraints on the LLM Wiki pattern

These are observations from people implementing Karpathy's LLM Wiki gist in production. They are useful as warnings and design constraints. They are weighted lower than Karpathy-direct sources and are never attributed to Karpathy as his own principles. Several flag real risks he does not address.

**P75. The editorial trap: AI synthesis decisions become invisible authority.** Every time the AI compiles a raw source into a wiki page, it makes editorial choices about framing, emphasis, and connection. Those are AI choices, not yours. Nuance can be dropped silently, and the wiki reads cleanly because it is meant to. Practitioners who do not keep going back to raw sources let the synthesis quietly become the trusted authority. Karpathy's architecture protects against this by keeping raw immutable, but the discipline is human. `[FT-OB]`

**P76. Wiki staleness reads as confident misinformation; database staleness reads as ignorance.** A neglected wiki page still reads with the authority of well-written prose, so the gaps are invisible. A neglected database returns nulls or fewer results, so the gaps are visible. Either can fail; the failure modes are not equivalent. `[FT-OB]`

**P77. The single-agent assumption is structural, not incidental.** The wiki pattern presupposes one agent maintaining one shared markdown surface. Multiple agents writing to the same page create merge conflicts and semantic drift. It is a solo-practitioner or one-curator-many-readers pattern, and does not scale to team-wide concurrent writes. `[FT-OB, FT-CW]`

**P78. Speed-of-business calibration is the real selection criterion.** The wiki pattern is optimised for papers-and-articles speed (weeks to months), not Slack-message-and-ticket speed (minutes to hours). The question before building is not "what tools do I have?" but "what is the natural cadence of the knowledge I am trying to capture?" `[FT-OB]`

**P79. Contradictions are sometimes the most valuable item in the knowledge base.** A wiki may smooth a contradiction into a coherent narrative (engineering says twelve weeks, sales promised eight, the wiki resolves to ten). A database preserves both views. For knowledge work, smoothing is good; for strategic operational signal, smoothing is dangerous. Match the structure to whether you want synthesised narratives or preserved tensions. `[FT-OB]`

**P80. Right-time versus query-time is the architectural fork.** Either the AI does the hard work when information comes in (wiki, right-time) or when you ask a question (database, query-time). Right-time means expensive ingest and cheap retrieval; query-time means cheap ingest and recurring retrieval cost. Choose based on the read-to-write ratio of your actual workflow. `[FT-OB]`

**P81. The scale ceiling is roughly 100 to 10,000 high-signal documents.** Karpathy says this in the gist and field reports confirm it. Above 10,000 documents you need search tooling beyond index.md; above that again you need structured storage. The wiki pattern is not company-knowledge-base infrastructure. Anyone selling it as such is misreading the gist. `[WIKI, FT-OB]`

**P82. The schema file is the highest-leverage document in the system.** If the schema is wrong, every ingest is wrong; if it underspecifies contradiction handling, contradictions get smoothed silently. The schema deserves disproportionate investment. Most practitioners underinvest. `[FT-OB, WIKI]`

**P83. Health-check and lint must be scheduled, not ad hoc.** Practitioners never remember to lint manually, and the wiki degrades silently between checks. If you do not schedule it, it does not happen, and the wiki rots. `[FT-CW]`

**P84. The compounding loop only works if outputs flow back into raw.** "File good answers back" does not happen by default. The schema has to require explicitly that reports go to outputs and outputs feed back into ingest. Without that loop, the wiki captures what you fed it but not what you discovered through it. Flagged tension (2026-08-01): this ledger's own schema forbids exactly this loop (`AGENTS.md`, Outputs, export-only), because the corpus is single-author and maintainer framing is not a Karpathy claim. P84 therefore stands as a general constraint that this instance knowingly does not satisfy, and the compounding it describes is accepted as forgone. Recorded rather than smoothed, per P79; see P52. `[FT-CW]`

**P85. The hybrid (database plus wiki-over-graph) is the most likely production shape.** Anything beyond solo research converges on a structured database as source of truth, with the wiki or synthesis as a compiled view generated on schedule from the database. The wiki is never edited directly; it is regenerated, which avoids the error-compounding problem (P75) and the multi-agent problem (P77). Not Karpathy's recommendation, but the natural endpoint when the pattern is pushed past solo use. `[FT-OB]`
