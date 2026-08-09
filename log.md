# Log

Append-only record of ingests, revisions, and lint passes. Newest entries at the bottom. Prefix each entry consistently so it stays greppable.

## [2026-05-28] init | Ledger created
Initial build of the ledger from ten Karpathy-direct sources plus two field-test sources. 112 principles across 13 sections. Sources, in chronological order of original publication: Animals vs Ghosts (Oct 2025), Dwarkesh interview (Oct 2025), Verifiability (Nov 2025), The Space of Minds (Nov 2025), 2025 Year in Review (Dec 2025), AutoResearch README (Mar 2026), Sequoia Ascent blog summary and transcript (Apr 2026), LLM Wiki gist, No Priors interview (May 2026). Field-test: OpenBrain analysis, Cowork implementation walkthrough.

Repo structured per the LLM Wiki three-layer pattern: raw source cards (links, not reproductions, for copyright), the wiki principles, and the AGENTS.md schema. Karpathy-direct and field-test sources tagged and weighted distinctly. Applied/strategic layer deliberately kept out of this public repo.

## [2026-05-28] ingest | LLM Council repo
Source: https://github.com/karpathy/llm-council (vibe-coded weekend hack, 22 Nov 2025). Inserted in `sources.md` between VER and SoM.

**Reinforced** (added `[LC]` tag, text unchanged):
- P6 (jagged intelligence has two axes). The council pattern exploits inter-model jaggedness.
- P22 (startup wedge: valuable plus verifiable plus undertrained). Karpathy's "council of LLM judges" gesture is now realised in code.
- P25 (vibe coding raises the floor; agentic engineering raises the ceiling). Karpathy calls the repo "99% vibe coded".
- P61 (structural overproduction of bespoke apps). Karpathy's "libraries are over" line matches the thesis.
- P97 (vibe coding terraforms software). "Code is ephemeral now and libraries are over" is the strongest version of the principle's claim yet.

**Sharpened:** none.

**Contradicted:** none.

**Added:**
- P113 (Part 5: agentic engineering). The LLM Council pattern. Parallel answers, anonymised cross-ranking, chairman synthesis. Caveat: chairman is itself a single model, so the pattern reduces but does not eliminate single-model dependency.

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

## [2026-08-01] lint
Second lint pass, one month late: the July pass was missed, which is P83 failing on its own ledger. Ledger content had not changed since the 2026-06-01 pass (all intervening commits are watcher state), so every finding is a miss from that pass or time-based drift, not new editorial damage.

**Structural checks, all clean:** P1 to P115 complete with no gaps and no duplicate definitions (the P56 double-entry is the deliberate Part 9 pointer); index and principle files in sync at 116 entries each; zero orphaned cross-references; every source tag resolves to `sources.md`; all thirteen source cards carry all six required fields; every key-claim bullet in `raw/` maps to a principle id.

**Found and fixed (human-triaged):**
- Silent contradiction, the significant one. P52 (Karpathy-direct) and P84 (field-test) both require findings to flow back into the wiki; `AGENTS.md` (Outputs) and `outputs/README.md` forbid exactly that. The schema's reasoning is sound (single-author purity) but the tension was resolved silently in the schema's favour, which is the no-smoothing rule (P79) failing at the schema-versus-principle boundary. Flagged in P52 and P84 with a reciprocal note in `AGENTS.md`; neither principle softened or deleted.
- Silent contradiction. P3 ("not a discontinuity", "no single magic moment", DWA Oct 2025) against P2 (a single-month flip Karpathy calls an inflection, six weeks later, generalised to "a full professional generation behind"). Reconcilable, since P3 describes the structural arc and P2 one practitioner's adoption curve, but marked rather than assumed, mirroring the P4 remedy from the previous pass. P36 noted as sitting with P3.
- Stale count. README said "ten primary Karpathy sources"; `sources.md` has listed eleven since the LC ingest. The previous pass fixed this class for principle counts and missed it for sources. Now "eleven".
- Stale framing. README Status read as current at three months old with no ingest since 28 May 2026. Added a last-lint line pointing at this entry.
- Convention. Nineteen fixes: eighteen em-dashes against the "no em-dashes anywhere" rule (`log.md`, `.watch/README.md`, `.claude/commands/lint.md`; ledger prose was already clean), plus an orphaned reference in `.watch/README.md` to `.github/scripts/karpathy_watch.py`, which the workflow actually runs as `.github/scripts/watch.py`. Em-dashes in this file's own earlier entry were normalised on the reading that the append-only rule protects facts, not punctuation.

**Found, deferred (recorded, not actioned):**
- Coverage gap, the one worth acting on. Five Karpathy-direct bearblog posts sit in the watcher's seen-list with no source card, no `sources.md` row, and no logged scope decision: `power-to-the-people`, `vibe-coding-menugen`, `chemical-hygiene`, `auto-grade-hn`, `finding-the-best-sleep-tracker`. Two bear on attribution: P20 and P40 rest on MenuGen via `[SEQ-B]`, and P100 is titled "Power to the people" via `[YR25]`, while dedicated primary essays exist unread. AGENTS.md ranks direct essays authoritative, so these principles may be sourced to secondary retellings. Not fixed here: lint does not ingest, and AGENTS.md reserves source curation to the human.
- Imprecise dates. AR is month-only ("Mar 2026"), WIKI is year-only ("2026"). The previous pass fixed this class for DWA and NP. Not fixed here because the true dates need verification against the sources; a guessed date is worse than a vague one.
- Stale framing, watch item only. P96 ("Localhost beats cloud for agents in the current era", YR25 Dec 2025) is the most time-sensitive claim in the ledger. No newer Karpathy source supersedes it, and inventing a supersession would breach the supersede-don't-delete rule. Watch it.
- `sources.md` field-test table carries no Date column while the direct table does. Cosmetic.
- The watcher rewrites `.watch/state.json` in a different order on every run, so it commits a diff even when nothing is new (61 such commits since the last lint). Sorting the seen-lists would make real changes visible.

## [2026-08-01] ingest | Power to the People
Source: https://karpathy.bearblog.dev/power-to-the-people/ (essay, 7 Apr 2025). Tagged `PTP`. Backfilled from the coverage gap recorded in this morning's lint.

**Scope note.** This source predates the declared corpus window (Oct 2025 to Apr 2026) by six months. Admitted as a named exception because it is the primary statement of P100, which had been tagged only to the YR25 restatement of Dec 2025. The window itself has not moved: Apr to Oct 2025 remains deliberately uncovered, and `sources.md` now says so rather than leaving the omission to be inferred.

**Reinforced:** none beyond P100 itself.

**Sharpened:**
- P100 (power to the people). The principle read as a settled inversion. The primary source makes it contingent and names its failure condition: it holds only while frontier performance stays cheap and roughly undifferentiated, distillation is the current counterforce, and train-time and test-time scaling plus ensembles push the other way by tying performance to spend. If money buys materially better models, institutions reconcentrate and an elite splits from the rest. Tag now `[PTP, YR25]`. This is a material change to the principle's operational advice, not a citation tidy-up.

**Contradicted:** none. The YR25 restatement is faithful, just compressed; it dropped the caveat rather than contradicting it.

**Added:** no new principle. The contingency is a sharpening of P100, not a separate claim. Added instead to `open-questions.md` as a watch item, since P100 is now one of the few principles carrying a stated expiry condition.

## [2026-08-01] ingest | Vibe coding MenuGen
Source: https://karpathy.bearblog.dev/vibe-coding-menugen/ (essay, 27 Apr 2025). Tagged `MG`. Backfilled from the coverage gap recorded in this morning's lint.

**Scope note.** Pre-window by six months, admitted on the same basis as PTP: it is the primary source behind four principles that had all been tagged to the SEQ talk of Apr 2026, a year later. The window is unchanged.

**Reinforced** (tag added, claim already correct):
- P20 (some apps should not exist). The claim originates here; Karpathy's own conclusion was that the function might sit better as a prompt-shaped artefact than a full app with auth and payments. Now `[MG, SEQ-B, NP 9:30]`.

**Sharpened:**
- P40 (the MenuGen deployment test). The principle named MenuGen without citing it. Added the origin: the test comes from a real attempt to ship, where building was quick and shipping was the slog, and several failures were configuration rather than code. Added Karpathy's phrase for the experience, "assembling IKEA furniture from the future". Now `[MG, SEQ-B]`.
- P38 (rebuild the stack for agents). The list of agent-native surfaces originates here, stated as CLIs, curl-configurable backends, and markdown documentation instead of click-through UIs. Now `[MG, SEQ-B]`.
- P39 (any "go to this URL, click here" doc is legacy). Added the mechanism, which the SEQ-T restatement leaves implicit: an LLM cannot manipulate configuration state spread across browser tabs and provider dashboards, so such an instruction is unexecutable rather than merely tedious. Now `[MG, SEQ-T 25:53]`.

**Contradicted:** none.

**Added:** no new principle. Everything in the essay lands on existing ids. The temptation was to mint one for the build-versus-ship asymmetry, but that is what P40 already says.

## [2026-08-01] ingest | Auto-grading Hacker News
Source: https://karpathy.bearblog.dev/auto-grade-hn/ (essay, 10 Dec 2025). Tagged `AGH`. Inserted in `sources.md` between SoM and YR25.

**Scope note.** Unlike PTP and MG this one is in-window and on-topic. It was simply missed, at the original build and again at the 2026-06-01 lint. It is the only true omission of the five posts the 2026-08 lint flagged; the other four are explained by the corpus window or by subject matter.

**Reinforced:**
- P22 (the startup wedge: valuable plus verifiable plus undertrained). Grading old predictions is latent verifiable structure of the cleanest kind, since the outcomes are already known and the reward signal is therefore free. Now `[SEQ-T 15:14, SEQ-B, LC, AGH]`.
- P24 (information processing is the real prize). The experiment is a clean instance of the "what was impossible before" test. Now `[SEQ-T 7:24, SEQ-B, WIKI, AGH]`.

**Sharpened:** none.

**Contradicted:** none.

**Added:**
- P116 (Part 4). The past becomes legible, so present conduct compounds forward. Verified against the source before minting, because a new principle should not rest on a summary: the claim that cheap enough intelligence permits a perfect reconstruction of the past is a load-bearing section of the essay, not an aside, and Karpathy connects it explicitly to present conduct. Nothing in P1 to P115 covered it. Tagged `[AGH]`.

**Scope decisions recorded, so future lints stop re-flagging these:**
- `chemical-hygiene` (18 Dec 2025) is in-window but off-topic: personal health and chemical exposure, nothing to do with LLMs or agentic engineering. Excluded by the ledger's stated scope.
- `finding-the-best-sleep-tracker` (24 Mar 2025) is both pre-window and off-topic: consumer sleep-tracking hardware. Excluded.
- Neither exclusion was previously written down, which is why the lint flagged all five posts together. Karpathy's bearblog carries material outside this ledger's subject; absence from `sources.md` is not by itself evidence of a miss.

## [2026-08-10] ingest | Ramble sessions with LLMs
Source: https://x.com/karpathy/status/2079610838143623371 (post, 22 Jul 2026). Tagged `RAM`. First source ingested under the reopened corpus window and the new `post` type.

**Date note.** The post renders as 21 Jul 2026 in its own timezone and 22 Jul 2026 in Australian time. The maintainer supplied 22 Jul, so the table uses that; the one-day ambiguity is recorded here rather than silently picked.

**Reinforced:**
- P13 (weights hazy, context is working memory). The ramble is this principle applied to intent rather than to reference material. Now `[DWA 00:17:00, RAM]`.
- P27 (spec design beats plan mode). The ramble is a low-cost input mode feeding spec work, including Karpathy's variant where it becomes a short interview. Now `[SEQ-T 20:43, RAM]`.

**Sharpened:**
- P47 (the human's job is the brief). The principle established that the brief is the artefact. This source says what makes a brief good, and it is not polish: it is how much intent reaches the model. Unstructured speech is the cheap way to raise that. Now `[AR, RAM]`.

**Contradicted:** none outright, but one tension recorded.
- P44 (you can outsource thinking, not understanding). Karpathy reports that the model's echo of a messy ramble often reads cleaner than his own starting formulation, which is the model doing part of the articulating. Flagged in P44 and left standing: the line holds only if articulation is separated from understanding. Recorded rather than resolved, per P79.

**Added:**
- P117 (Part 5). Raise the bandwidth of the brief, not its polish. Verified against the post before minting rather than against coverage of it. Nothing in P1 to P116 makes the bandwidth-over-polish claim: P47 says the brief is the artefact, P27 says specs are collaborative, neither says the input can be deliberately unpolished because the model supplies the polish. Tagged `[RAM]`.

## How to add the next entry
When ingesting a new source, append a dated line in the form:
`## [YYYY-MM-DD] ingest | <Source title>`
followed by a short note of what reinforced, what sharpened, what contradicted, and what new principle ids were added. For lint passes use `## [YYYY-MM-DD] lint` and record what was found and fixed.
