# Ramble sessions with LLMs

- Tag: RAM
- Type: post
- Author: Andrej Karpathy
- Date: 22 Jul 2026
- Weight: direct
- Link: https://x.com/karpathy/status/2079610838143623371

## Summary
Karpathy describes a working pattern for getting more context into an agent cheaply. Rather than composing a careful brief, he switches to voice and talks for around ten minutes with no structure, sometimes announcing up front that he has switched to dictation and that typos will follow. He finds models reconstruct long incoherent rambles well, and that the model's echo of the ramble often reads cleaner than what he started with. The stated payoff is a better shared model of intent, so less correction is needed from that point on.

## Key claims
- The binding constraint is often that the model lacks bits about your intent, and typing them is effortful enough that you skip it. Supports P117, P13.
- Voice removes the cost of supplying those bits: roughly ten minutes of unstructured stream of consciousness, anything goes. Supports P117.
- Models are good at reconstructing incoherent input, and the reconstruction is often cleaner than the original formulation. Supports P117, P44.
- The ramble sometimes becomes a short interview of a few turns rather than a monologue. Supports P27, P117.
- The payoff is a better shared model of intent, which reduces downstream correction. Supports P117, P47.
