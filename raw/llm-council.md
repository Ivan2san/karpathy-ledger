# llm-council repo

- Tag: LC
- Type: repo
- Author: Andrej Karpathy
- Date: 22 Nov 2025
- Weight: direct
- Link: https://github.com/karpathy/llm-council

## Summary
A local web app, vibe-coded as a Saturday hack, that turns a single user query into a multi-LLM consensus pipeline: each model answers, each then ranks the others' answers blind to identity (to defuse favouritism), and a designated chairman model synthesises the final response. Built originally for reading books with LLMs. Notable as a published implementation of the "council of LLM judges" gesture from the Sequoia talk (P22): a thesis from April 2026 realised in code five months earlier (the corpus reads coherently regardless of authoring order).

## Key claims
- The Council architecture: parallel answers, anonymised cross-ranking, chairman synthesis (new P113).
- Council exploits jagged intelligence across models, since no single model is reliably best (P6).
- Realisation of the "council of LLM judges" example used in P22's verifiability argument.
- Karpathy's stance on the codebase itself: "Code is ephemeral now and libraries are over." Reinforces P25, P61, P97.
- The chairman is itself a single LLM, so the pattern reduces but does not eliminate single-model dependency (caveat carried into P113).
