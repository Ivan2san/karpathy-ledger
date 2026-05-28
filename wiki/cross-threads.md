# Cross-source threads

Threads that run across multiple sources and tie the principles together.

## 1. The Karpathy worldview, foundation up

The corpus reads coherently bottom to top, each layer explaining the one above:

- **Deepest foundation (SoM):** intelligence is a large space; animals are one point, LLMs another. The four animal pressures and four LLM pressures (P105, P106) explain everything that follows. The asymptote is set by optimisation pressure (P108, P110).
- **Foundation (AvG):** LLMs are ghosts, not animals (P14). Pretraining is crappy evolution (P86).
- **Capability theory (VER, YR25):** verifiability plus RLVR drive the gains (P16, P92); jagged intelligence is the result (P6).
- **Mechanics (DWA, VER):** RL is terrible (P8); RLVR works because rewards are non-gameable (P92).
- **State of the field (YR25):** five paradigm shifts (P92 to P98); test-time compute; app layer; localhost; vibe coding; LLM GUI hints.
- **Practice (AR, SEQ, NP, WIKI):** Software 3.0 inversion (P19); remove yourself from the bottleneck (P62); markdown as programming (P23); persistent compounding artefacts (P49).
- **Human role:** taste, spec, understanding as bottleneck (P44, P69).

## 2. The Software 3.0 stack is complete

Predicate (P16, P56) to environment test (P21) to AutoResearch implementation (P29 to P33) to LLM Wiki implementation (P49 to P55) to org-level brief (P48). Five layers, all coherent. Two reference implementations for the same paradigm: one for code, one for knowledge.

## 3. Three implementations of the new paradigm

AutoResearch (autonomous loop), LLM Wiki (accumulating artefact), and Dobby (agent as glue over APIs). All three are Software 3.0. None look like each other operationally. Most workflows resemble the Wiki more than AutoResearch.

## 4. The 10x-becomes-100x claim has three mechanisms, not measurement

Parallel experiments overnight (AutoResearch), zero-cost maintenance of compounding artefacts (Wiki), and parallel orchestration of macro actions (Dobby). Directional, not benchmarked (P26).

## 5. The 1980s frame as a stakeholder primitive

Specifiability then, verifiability now (P18), extending to integratability (P56) and parallelisability (P62, P63). Strengthened by P99: "we are reliving 1970s and 80s computing innovations" is a stated Karpathy framework, not just an inference. The cleanest non-technical framing of the whole thesis.

## 6. The orchestration stack

Karpathy's own enumeration of six layers, each a separate skill ceiling: LLM, agent, persistent harness, multiple harnesses in parallel, instructions to them, and optimisation over the instructions. The "psychosis" (P57) is the recognition that all six are simultaneously underdeveloped.

## 7. The verifiability operational chain

The rule (P16) to the test (P21) to the AutoResearch implementation (P29 to P33). Where you can clear the three-part test (resettable, efficient, rewardable), the AutoResearch pattern applies. Where you cannot, you are betting on generalisation magic (P12) and should know it.

## 8. Optimisation pressure as a prediction tool

P107, P108, P110, P111 form a usable framework. To predict a model's failure modes, ask which selection pressure is missing. To predict where capability spikes next, ask which verifiable domains the labs are pouring RL compute into. To predict whether a behaviour increases or decreases, ask whether DAU optimisation rewards or punishes it.

## 9. The wiki tradeoff axis

Anyone implementing the LLM Wiki beyond personal research must make four explicit decisions: right-time versus query-time work (P80), synthesis-smoothing versus contradiction-preservation (P79), single-agent versus multi-agent write access (P77), and cadence-of-knowledge matching tool design (P78). Karpathy makes one set of choices for himself; production use often requires another, or the hybrid (P85).
