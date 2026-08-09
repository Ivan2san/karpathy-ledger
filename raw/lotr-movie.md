# Lord of the Rings, rendered by Opus 5

- Tag: LOTR
- Type: post
- Author: Andrej Karpathy
- Date: 2 Aug 2026
- Weight: direct
- Link: https://x.com/karpathy/status/2083749667410727319

## Summary
Karpathy gave Opus 5 the opening paragraph of The Fellowship of the Ring, a one million token budget costing roughly ten dollars, and asked for a three.js rendering of it. The model worked for about two hours and produced 5500 lines of code that procedurally render the scene; the artefact is published at https://karpathy.ai/lotr-movie. He frames the experiment three ways: as a successor to simple vibe checks such as the pelican SVG test, as evidence that hyper-custom work no one would ever have funded is now close to free, and as an exposure of a specific weakness, which is that the model could not watch its own output.

## Context
The post opens against Simon Willison's pelican-on-a-bicycle test, the informal habit of asking a model for an SVG of a pelican riding a bicycle and eyeballing the result: https://simonwillison.net/2025/Jun/6/six-months-in-llms/. Karpathy names it as the thing this experiment generalises beyond. It is recorded here as context for the post rather than as a source in its own right; it is a benchmark cited inside a Karpathy source, not a practitioner implementation of his ideas, so it does not belong in the field-test tier.

## Key claims
- Simple vibe checks are being outgrown, so probes have to escalate as capability rises. Supports P101, P35.
- The run: one paragraph of prose in, roughly ten dollars and two hours spent, 5500 lines out, procedurally rendered and openly janky. Supports P24, P34.
- Placing and orchestrating polygon assets in (x,y,z) from prose, then writing the code that animates them, is a surprising capability. Supports P24.
- Stamina rather than speed is the economic unlock: LLMs have unlimited patience, so work no human would ever fund becomes nearly free. Supports P97, P103.
- The forward bet is hyper-custom single-use worlds a player can be dropped into. Recorded as an open question, not minted as a principle, because the source presents it as excitement rather than a finding.
- Worlds and games expose a self-audit gap: the model cannot efficiently or natively perceive video or play a game, so it iterated by taking slow screenshots, made mistakes, and left visible jank. Supports P118, P21, P6.
