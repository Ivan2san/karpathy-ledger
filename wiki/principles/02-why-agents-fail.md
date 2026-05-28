# Part 2: Why agents fail (and where)

**P5. Agents are bad at code that has never been written before.** This is the asymmetry that constrains the "AI automates AI research" story. They cannot hold a non-standard style across a codebase, they revert to internet-typical patterns, and they add defensive bloat. `[DWA 00:29:45]`

**P6. Jagged intelligence has two axes.** Capability spike is roughly verifiability times training attention times data coverage times economic value. The model flies inside the reinforcement-learning circuits and falls off them outside. The car-wash example: a state-of-the-art model tells you to walk 50 metres because it is "close", while the same model refactors a 100k-line codebase. `[SEQ-B, VER]`

**P7. The founder question: are you on the model's rails?** The practical test before betting on a model for a workflow. Is the task verifiable AND has the lab pushed training data there? If not, expect to bring your own evals, fine-tuning, or reinforcement-learning environment. `[SEQ-B, NP 26:00]`

**P8. RL is terrible, just less terrible than everything else.** Outcome reward "sucks supervision through a straw", upweighting every token of a successful trajectory including the wrong turns. This is why agents plateau on novel work. `[DWA 00:40:05]`

**P9. LLM-as-judge gets gamed.** Reinforcement learning against an LLM judge finds adversarial examples (nonsense strings that score 100 percent). You can patch them, but the space of adversarial examples is infinite. This makes process supervision harder than it looks. `[DWA 00:45:00]`

**P10. Model outputs are silently collapsed.** Any individual sample looks fine; the distribution is narrow. ChatGPT still tells the same three jokes it told years ago despite massive capability gains elsewhere. Do not over-rely on agent self-generated content for training, evals, or creative work without injecting entropy. `[DWA 00:50:00, NP 26:30]`

**P11. "Pulling teeth" is the felt signal of being off-rails.** When agent work feels slow, defensive, and like you are dragging the model somewhere it does not want to go, that is the sensory tell that you are outside the reinforcement-learning circuits. Trust the sensation; change approach rather than trying harder. The microGPT simplification attempt is the canonical case: no model could simplify aggressively because aesthetic minimalism is not in the reward. `[SEQ-T 23:08]`

**P12. If not verifiable, you are betting on generalisation magic or imitation.** When a task does not meet the verifiability conditions, the only paths are hoping the net generalises from adjacent training, or weaker imitation learning. Both are unreliable compared with reinforcement learning on a verifiable environment. This is why creative, strategic, and context-heavy tasks lag. `[VER, AvG]`

**P58. The PhD-plus-ten-year-old superposition.** The cognitive signature of working with current agents: simultaneously an extremely capable lifelong systems programmer and a confused child. Humans are far more coupled; capability and incompetence travel together in us. In agents they decouple wildly. Design workflows around this. `[NP 24:43]`

**P59. Generalisation across domains is not happening at the rate the labs claim.** Karpathy's direct take: gains in verifiable domains (code, maths) are not transferring meaningfully to non-verifiable ones (humour, taste, judgement). "Maybe a little bit, but not a satisfying amount." An important counter to the "smarter at code means smarter at everything" pitch. `[NP 28:00]`
