# Part 5: Agentic engineering as a discipline

**P25. Vibe coding raises the floor; agentic engineering raises the ceiling.** Vibe coding lets anyone build software by describing it. Agentic engineering is the professional discipline of coordinating fallible agents while preserving correctness, security, taste, and maintainability. The first is fine for prototypes; the second is what serious teams need. `[SEQ-B, LC]`

**P26. The new 10x is much more than 10x (cautious version).** Karpathy's actual phrasing is that people very good at agentic workflows seem to peak well beyond the old 10x benchmark, because they parallelise judgement, not just code. Anecdotal, not measured. Directional, not benchmarked. `[SEQ-T 17:11]`

**P27. Spec design beats plan mode.** Plan mode is a useful feature; the real practice is collaboratively designing detailed specs (essentially the docs) with the agent, then having the agent execute against them. Continuous spec work, not a discrete pre-execution step. `[SEQ-T 20:43]`

**P28. Hiring should change.** Stop the puzzle interviews. Give a candidate a substantial project, have them deploy it securely, then have adversarial agents try to break it. This tests the real skill: decomposing work for agents, writing useful specs, preserving quality, reviewing generated work, hardening a system. `[SEQ-B]`

**P29. Constrain the surface, expand the autonomy.** AutoResearch lets the agent edit exactly one file; everything else is frozen. Tight scope is what makes overnight autonomy safe and diffs reviewable. The smaller the editable surface, the more autonomy you can grant inside it. `[AR, WIKI]`

**P30. One scalar metric per loop.** A single scalar metric (validation bits per byte in AutoResearch, lower is better) is the rewardability axis of the verifiability test applied to the agent loop. The agent cannot game what it cannot interpret, and you cannot supervise what you cannot measure cleanly. No scalar means autoresearch-style loops do not apply. `[AR, VER]`

**P31. Fix the time budget to make experiments comparable.** Every AutoResearch run is exactly five minutes of wall clock. This makes experiments directly comparable regardless of what the agent changed, and optimises for what is best on your own compute. The cost is that results stop being comparable across platforms; worth it. `[AR, VER]`

**P32. Throughput math determines the loop's value.** Roughly twelve experiments per hour means around a hundred while you sleep. That is the unit economics of overnight autonomy. If your loop cannot reach about a hundred attempts a night, the keep-or-revert pattern is probably the wrong shape. `[AR, VER]`

**P33. Frozen evaluator, editable code, scalar metric.** The three-file AutoResearch architecture is the minimal viable autonomous loop and a literal implementation of resettable plus efficient plus rewardable. An immutable test harness, a constrained code surface, a metric, a brief. The repo is the Verifiability essay made executable. `[AR, VER]`

**P62. Remove yourself from the bottleneck.** The sharpest framing of the new discipline: to get the most from the tools, arrange things so you are not in the loop to prompt the next step. The skill is not "use agents", it is "arrange so I am not in the loop". This is the principle behind AutoResearch and behind parallelising agents. `[NP 16:30]`

**P63. Move in macro actions, not lines of code.** The unit of work has shifted: you delegate functionality, not functions. Multiple agents work on non-interfering chunks in parallel. The new muscle memory is identifying macro actions that can be cleanly partitioned and dispatched. `[NP 4:24]`

**P64. Personality and reward calibration matter.** When Claude gives praise, Karpathy feels he slightly deserves it because it does not over-reward weak ideas; Codex is "dry" and indifferent to what you are building. Not a vibes claim: a calibrated reward signal from the agent shapes the human's behaviour over time. Pick tools with calibration appropriate to the work. `[NP 8:10]`

**P65. Trust gating is the legitimate brake on full adoption.** Karpathy has not given his agent access to email or calendar; it is "still very new and rough around the edges". Security, privacy, and the cost of mistakes scale with the surface area you grant. Permissioning is not an afterthought, it is the deliberate choke point that makes everything else safe. Reinforces P42. `[NP 16:00]`

**P113. The LLM Council pattern.** A practical coordination technique: query multiple models in parallel; each ranks the others' outputs blind to identity (so favouritism does not bias the ranking); a chairman model synthesises the final answer. The architecture exploits jagged intelligence across models (P6) and operationalises the "council of LLM judges" mentioned in P22. The chairman is itself a single model, so the pattern reduces single-model dependency without eliminating it. Karpathy describes the implementation as a weekend vibe-coded hack. `[LC]`

**P114. The orchestration stack is six layers, each its own skill ceiling.** Karpathy enumerates six levels of the agentic stack, each a separate and currently underdeveloped competency: the raw LLM, the agent wrapped around it, a persistent harness that holds state, multiple harnesses running in parallel, the instructions you give them, and the optimisation over those instructions. Leverage compounds up the stack, and the "psychosis" of P57 is the felt recognition that all six are immature at once. Connects the throughput framing (P60) and the remove-yourself-from-the-bottleneck discipline (P62, P63). `[NP]`
