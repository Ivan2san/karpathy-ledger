# Part 4: Software 3.0 and the new programming paradigm

**P16. The two paradigm rules, cleanly stated.** Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify. The single sharpest line in the corpus. Every "should we build, automate, or outsource this?" question runs through these two filters first. `[VER]`

**P17. AI is a new computing paradigm, not a new technology.** The strongest historical analogy is not electricity or the industrial revolution; it is computing itself. Both are fundamentally about automating digital information processing. This frames diffusion and timelines: AI spreads like computing did, in pieces over years, not as a single discrete invention. `[VER, DWA]`

**P18. The 1980s analogy: specifiability then, verifiability now.** To forecast which jobs computing would automate around 1980, you asked whether a task was mechanically specifiable (typing, bookkeeping). The equivalent question now is whether a task is verifiable. Same shape of question, different predicate. The cleanest non-technical framing for stakeholders. `[VER]`

**P19. Software 3.0: the context window is the program, the LLM is the interpreter.** 1.0 is explicit code, 2.0 is learned weights, 3.0 is programming an LLM through prompts, context, tools, examples, memory, and instructions. The unit of programming shifts from a function to a paragraph. `[SEQ-B]`

**P20. Some apps should not exist.** When a multimodal model can transform input directly to output (the MenuGen photo becomes an overlaid menu image via one model call), the entire app stack between them is scaffolding. Do not only ask "what can AI speed up?" Ask "what should disappear entirely?" Reinforced by the smart-home example where six apps collapsed into one chat. `[SEQ-B, NP 9:30]`

**P21. The verifiability environment test: resettable, efficient, rewardable.** Before assuming a task is automatable in the new paradigm, run the three-part test. Can you start a clean new attempt (resettable)? Can the agent practise many attempts cheaply (efficient)? Is there an automated process to score each attempt (rewardable)? Fail any one and the task is not in the sweet spot. The operational form of P16. `[VER]`

**P22. The startup wedge is valuable plus verifiable plus undertrained.** Coding and maths are heavily targeted by the labs. Many economically important domains have latent verifiable structure that has not been exploited. That gap is where to build. And almost everything is verifiable to some degree, even writing via a council of LLM judges; the frontier is ease, not possibility. `[SEQ-T 15:14, SEQ-B]`

**P23. Markdown is the programming language of Software 3.0.** In AutoResearch, `program.md` is "essentially a super lightweight skill" and the only file the human edits, while the agent edits the code. The roles invert: humans write prose, agents write code. `[AR, WIKI]`

**P24. Information processing, not just code, is the real prize.** The shift is broader than coding. LLMs make whole classes of information transformation possible that previously required no equivalent program. The LLM knowledge base is the canonical example: no classical program could maintain a synthesised wiki across messy human documents. Ask not "what does AI speed up?" but "what was impossible before that is now natural?" `[SEQ-T 7:24, SEQ-B, WIKI]`

**P56. The Software 3.0 predicate (inferred): integratability.** Verifiability gives the 1.0 and 2.0 predicates. The LLM Wiki gist suggests the 3.0 predicate: a task suits Software 3.0 if its outputs can be incrementally integrated into a persistent, evolving structure that compounds. Code generation qualifies (AutoResearch); knowledge work qualifies (LLM Wiki); one-off creative tasks probably do not. Marked inferred, not stated by Karpathy; revise if a later source contradicts. `[WIKI, inferred]`

**P61. There is a structural overproduction of bespoke apps.** Most consumer apps should not exist as apps; they should be APIs that agents glue together with intelligence on the fly. The Dobby home-automation setup proves the principle: an agent hacked into Sonos, lights, HVAC, pool, and security by IP scan plus web search plus API discovery, collapsing six apps into one chat. `[NP 13:00]`
