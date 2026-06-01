# Part 7: Agent-native infrastructure

**P38. Rebuild the stack for agents, not humans.** Most software is still built for humans clicking through screens, but increasingly the user is the human's agent. Products need agent-native surfaces: markdown docs, CLIs, APIs, MCP servers, structured logs, machine-readable schemas, copy-pasteable instructions, safe permissioning, auditable actions, headless setup. `[SEQ-B]`

**P39. Any "go to this URL, click here" doc is now legacy.** Karpathy's visceral test: every time he is told to navigate, click, or configure manually, his reaction is "no". Agent-first documentation is the new floor. If a workflow assumes a human reading and acting, it is already obsolete. `[SEQ-T 25:53]`

**P40. The MenuGen deployment test.** Can you say "build and deploy this" and have the agent wire up hosting, auth, payments, DNS, secrets, and production config without you touching a settings panel? When the answer is yes, the infrastructure has become agent-native. `[SEQ-B]`

**P41. Sensors and actuators are the right abstraction.** A sensor turns world state into digital information; an actuator lets an agent change something. The future stack is agents using sensors and actuators on behalf of people and organisations. `[SEQ-B, NP 56:30]`

**P42. "Disable all permissions" is part of the design.** AutoResearch instructs you to spin up the agent with permissions disabled. Tight surface plus sandboxed permissions equals safe overnight runs. Permissioning is the structural reason the loop can run unsupervised, not a security afterthought. `[AR]`

**P43. Future state: agents represent people and organisations.** Your agent talks to my agent to settle meeting details and other tasks. Plan for this as the default interaction model, not an exotic case. `[SEQ-T 27:14]`

**P68. People want AI personas, not raw LLMs.** What humans expect from an AI is an entity behind a chat interface that remembers them and can be told things. An LLM is a token generator. The gap between the two is doing real work today: Dobby has a name, a personality, and a WhatsApp channel. UX wrapping is the type-check between what users expect "AI" to mean and what an LLM actually is. `[NP 12:00]`

**P115. The agent-as-glue orchestrator is the third reference implementation.** Alongside AutoResearch (the autonomous loop, P29 to P33) and the LLM Wiki (the accumulating artefact, P49 to P55), Dobby is the third concrete Software 3.0 implementation: an agent that discovers and glues disparate APIs on the fly, collapsing many single-purpose apps into one conversational surface. It is the operational proof of P61 (apps should be APIs that agents glue) and pairs with the persona wrapping of P68. None of the three implementations look alike; most real workflows resemble the Wiki more than AutoResearch. `[NP 12:00, NP 13:00]`
