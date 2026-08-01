# Vibe coding MenuGen

- Tag: MG
- Type: essay
- Author: Andrej Karpathy
- Date: 27 Apr 2025
- Weight: direct
- Link: https://karpathy.bearblog.dev/vibe-coding-menugen/

## Summary
An account of building a small image-generation app for restaurant menus, and then trying to ship it. The building was fast; the shipping was not. Authentication, payments, DNS, environment variables, and provider dashboards consumed the bulk of the effort, and several failures were configuration rather than code. Karpathy's conclusion is that the deployment stack assumes a human clicking through browser UIs, which is precisely what an agent cannot do. His phrase for the experience is "assembling IKEA furniture from the future".

Predates the declared corpus window (Oct 2025 to Apr 2026). Backfilled 2026-08-01 as a named exception because it is the primary source behind P20, P38, P39, and P40, all of which had been tagged to the SEQ talk of Apr 2026, a year later.

## Key claims
- Building was quick; deploying was the slog, across auth, payments, DNS, secrets, and provider configuration (P40).
- The friction is structural, not incidental: an LLM cannot manipulate configuration state spread across browser tabs and dashboards (P39).
- What services should offer instead: CLIs, curl-configurable backends, and markdown documentation rather than click-through UIs (P38).
- Several failures were environment and configuration rather than code, including secrets that never reached production and a deploy whose visibility was not what was intended (P40).
- The app may have been the wrong unit of software; the same function might sit better as a prompt-shaped artefact than as a full app with auth and payments (P20).
