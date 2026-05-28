# Part 3: Mental models for how LLMs actually work

**P13. Weights are hazy recollection; the context window is working memory.** Anything in context is directly accessible. Anything in weights is lossily compressed. Feeding a full chapter beats asking about the book. This drives all context-engineering decisions. `[DWA 00:17:00]`

**P14. Ghosts, not animals.** LLMs are not failed attempts at animal intelligence; they are a different point in the space of possible intelligences, arising from imitation of human text rather than evolution. Anthropomorphic intuitions mislead. Karpathy's own caveat is that the framing is "a little philosophical", but the Space of Minds essay (Part 13) upgrades it into something with predictive power. `[AvG, SEQ-T 24:25, DWA 00:07:00]`

**P15. The cognitive core is small.** Karpathy's guess is roughly a billion parameters for a useful intelligent core within a decade, if you strip out memorisation and force the model to look things up. Current models are bloated with knowledge they should not need to memorise. `[DWA 00:59:00]`

**P60. Tokens are the new flops; throughput is the new bottleneck.** For a decade engineers did not feel compute-bound. Now they do again, in a new unit. The relevant question is "what is your token throughput?" The leverage has moved from individual productivity to parallel orchestration capacity. The old nervousness about idle GPUs is now nervousness about idle subscription tokens. `[NP 5:33, NP 6:00]`

**P86. Pretraining is "crappy evolution", a candidate solution to the cold-start problem.** Billions of parameters need rich, high-density supervision. Evolution provides this for animals via DNA-encoded priors built over millions of years. We cannot rerun evolution, but we have mountains of internet documents. Pretraining is the only practical way to gather enough soft constraints to reach a useful initialisation rather than starting from scratch. `[AvG]`

**P87. Animal learning is mostly finetuning on top of evolved priors.** The newborn zebra running within minutes is not learning; it is executing a deeply pre-trained model encoded in DNA. Much of what looks like animal learning is maturation, and even the real learning is finetuning on a powerful pre-existing initialisation. This is why pure tabula-rasa reinforcement-learning approaches have not worked: no real intelligence has ever started from a blank slate. `[AvG]`

**P88. The bitter lesson is platonic, not achievable in practice today.** Frontier LLMs are heavily engineered artefacts with humanness at every stage: pretraining data is human text, finetuning data is human and curated, reinforcement-learning environments are tuned by human engineers. There is no clean turn-the-crank algorithm that learns from experience alone. The bitter lesson is something to pursue, not necessarily to reach. The corrective to any "just add compute" pitch. `[AvG]`

**P89. Ghosts and animals: planes versus birds is a live possibility.** Maybe LLMs converge toward animal-like properties over time as we finetune them; maybe they diverge permanently and stay un-animal-like but still world-altering, the way planes are nothing like birds yet solve flight. Both are plausible. Karpathy puts double-digit-percent uncertainty on this. Reframed and sharpened by P112. `[AvG]`

**P90. Animal-inspired ideas worth borrowing into LLMs.** Karpathy's explicit list of what LLMs are algorithmically missing that biological intelligence has: intrinsic motivation, fun, curiosity, empowerment, multi-agent self-play, culture. A research watch-list: any of these landing in a frontier model would be a meaningful capability shift. `[AvG]`

**P91. In-context learning is the LLM equivalent of test-time adaptation.** When critics say LLMs lack continual learning, they mean weight-based learning. But the context window is itself a form of test-time adaptation, which is why few-shot prompting works. Recent memory work (CLAUDE.md files, skills) uses text and context as the substrate for test-time learning instead of weights. `[AvG appendix]`
