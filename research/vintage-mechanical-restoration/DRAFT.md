# Right To Fix And The Loss Of Mechanical Knowledge

**Sean Campbell** · Working draft · June 2026

**Tags:** `right-to-repair`, `mechanical-literacy`, `skilled-labor`, `disassembly-learning`, `parts-book`, `honda-cub`, `vespa`, `two-stroke`, `ai-enclosure`, `local-first-ai`, `inspectability`, `repair-autonomy`

---

If I asked a chatbot to explain the ignition system on a Honda Cub, it would most likely get it right. It is one of the most-produced vehicles in history. The manuals, diagrams, forum posts, and repair notes are everywhere.

But the specifics of different model years mean it would probably get at least one thing wrong.

And in repair, one wrong thing is not trivia. It is the difference between replacing the right part, chasing a ghost, or deciding the machine is beyond you.

This is not a paper about nostalgia. It is not an argument that boomers were right, that old machines were simply better, or that the world should turn back the clock. It is a paper about capacity: what happens when people lose the ability to learn systems by taking them apart — and when new tools, especially AI, make fluent explanation feel like the same thing as understanding.

---

## I took the thing apart

A few months ago, talking with a friend about my AI usage, I said something that turned out to be the whole argument:

> I took the thing apart — how LLMs work — figured it out, and put it back together.

That was not a metaphor borrowed from shop talk. It was a description of how I actually learn.

For most of the mechanical work I have done — home electrical, motorcycle engines, scooter rebuilds — I learned by taking the thing apart and putting it back together. Later, the parts book became the main reference. Exploded diagrams. Part numbers. Assembly sequence. What sits next to what. I reached for the service manual when I needed something the object itself could not teach safely: a torque spec, a clearance, a procedure, a model-year difference that would punish guessing.

That method is the spine of this paper.

Right-to-fix is not, for me, primarily a consumer-rights slogan. Skilled labor is not, for me, primarily a labor-market complaint. AI is not, for me, primarily a threat or a miracle. They are all connected because they all touch the same question:

Can ordinary people still learn systems by disassembling them?

---

## The loop

Repair knowledge is a form of autonomy, and for me it has almost always been learned through a loop:

Take the system apart far enough to see components, interfaces, and dependencies. Observe fit, sequence, wear, resistance, and failure. Reassemble the system into a working whole. Build a mental model strong enough to diagnose, modify, or operate with judgment. Consult external documentation only where the object cannot safely teach the rest.

That loop held whether I was tracing home electrical, splitting motorcycle cases, or rebuilding a two-stroke scooter.

Home electrical taught me to follow a path: load, junction, breaker, ground, failure under use. Motorcycle engines taught me that sequence matters — what must come out before what, what cannot be forced, what tolerance means when metal has been hot and moving. Scooter work taught me that small machines are not simple machines. Carburetion, ignition, compression, driveline, grounding, cable routing: each subsystem has its own logic, and the symptom you see is rarely the part that failed.

The parts book was often enough.

People underestimate it. A parts book does not always explain theory. It teaches structure. It shows how an assembly is organized, what can be separated, what must stay paired, what order matters, what the manufacturer assumed you would need to replace. That is systems thinking in diagram form. It is technical reading without requiring a classroom.

The service manual came later, and only for the knowledge that could not be inferred safely from the object: torque, timing, clearance, model-specific procedure. That distinction matters. The machine taught first. The manual confirmed where guessing would be expensive.

---

## What we are losing

The method still works where systems remain open. The conditions for learning it have eroded.

Machines became more sealed. Modules replaced assemblies. Fasteners became proprietary. Diagnostics moved behind dealer tools, software locks, and paired components. Service literature fragmented, disappeared, or went behind paywalls. Design favored replacement over rebuild. Repair work was culturally downgraded from skilled labor to grunt work. Ownership itself became conditional: subscriptions, cloud auth, remote permission, platform dependence.

This did not happen all at once. It happened in proportion.

As machines became harder to open, fewer people learned by opening them. As fewer people learned by opening them, fewer people could teach the method. As fewer people could teach it, repair literacy became specialist property. The public capacity to understand physical systems thinned.

That is what right-to-fix is really about, at least for me. Not only whether I can replace the battery in my phone. Whether the object can still teach. Whether the manual still exists. Whether the tools are available. Whether skilled labor can still make a living passing the method on. Whether disassembly remains a legitimate way to learn.

A society that cannot repair its machines eventually cannot learn from them either. Understanding and repair are not separate virtues. They are one loop.

---

## AI makes the gap harder to see

The Honda Cub is a useful opening because it exposes the difference between corpus knowledge and material knowledge.

A chatbot may know the general ignition architecture. It may know the common failure modes. It may sound authoritative because the Honda Cub has been documented more thoroughly than most objects on earth.

But repair does not happen in the corpus. It happens in the variant:

- this model year, not the generic diagram
- this prior owner's hack
- this corroded connector
- this weak spark under load
- this part in your hand, not the part in the illustration

AI is strong at the corpus layer: manuals, forums, likely causes, fluent summaries. It is weak at the material layer: this machine, this year, this test result, this consequence if you are wrong.

The deeper problem is epistemic. A person can read a fluent AI explanation and mistake it for the kind of knowledge that comes from having taken a system apart. Language is complete. The explanation sounds like understanding because language always sounds like understanding. But explanation is not verification. Retrieval is not disassembly. Fluency is not capability.

That is uncomfortably similar to the enclosure happening in mechanical systems.

| Mechanical enclosure | AI enclosure |
|---------------------|--------------|
| Sealed engine module | Closed model weights |
| Dealer-only diagnostics | Cloud-only inference |
| Missing service manual | Missing training data and logs |
| Proprietary fasteners | Proprietary APIs and policies |
| "Replace the assembly" | "Use our platform" |
| Cannot learn by disassembly | Cannot learn by inspection, logging, or local operation |

The risk is not only that AI gets things wrong. The risk is that fluent explanation masks the loss of inspectability. A person can feel informed without becoming capable.

---

## The same method, applied to LLMs

I did not approach AI as magic. I did not approach it as consumer software whose inner life was none of my business. I approached it the way I approach a motorcycle engine: take it apart conceptually, identify the components, see what depends on what, rebuild a working mental model, then use that model to operate, troubleshoot, modify, and build.

Tokenization. Context windows. Prediction. Retrieval. Tool routing. Memory. Hallucination. Failure under load. Each of those became a part I could name, inspect, and reason about.

That is how Willow happened.

Not because I began with a grand theory of agent platforms, but because I needed systems I could inspect, rerun, log, and repair at the operator layer. If AI was going to shape my work, I was not willing to treat it as a sealed appliance.

This connects directly to the argument in [*The Illusion of Sovereign AI*](../sociotechnical-ai-sovereignty/README.md). That paper asks what operational control over intelligent systems requires. Willow is one practical answer at operator scale: not total sovereignty, but repairability at the workflow layer.

Keep the manual. Retain prompts, handoffs, and documentation locally.

Keep the logs. Use durable stores, ledgers, source trails, audit history.

Keep the parts. Prefer open or local models, exportable data, owned stores.

Test before trusting. Use gates, verification loops, human attestation.

Fix without calling headquarters. Use local tools, local execution, bounded workers.

Learn by disassembly. Inspect prompts, traces, stores, and tool calls rather than treating output as opaque.

That is not a claim that local AI is automatically truthful. It is a claim that inspectable systems are more learnable systems — whether the substrate is aluminum and spark plugs or Postgres and embeddings.

---

## The bench case

Most of my hands-on mechanical work has lived in small machines: Vespa and Stella scooters, classic two-stroke designs, home electrical, motorcycle engines. Blue Smoke Garage is the operational context — enthusiast restoration, hands-on troubleshooting, learning by doing. Not a claim of formal mechanical engineering certification, and not necessarily a commercial shop brand unless stated elsewhere. A place where the method gets practiced.

These machines matter because they are still legible enough to teach.

Carburetion teaches mixture and feedback. Ignition teaches timing, gap, and measurement. Compression teaches wear and leakage. The driveline teaches adjustment and cable stretch. Electrical work teaches grounds, corrosion, and the punishment for guessing. Documentation teaches what the object cannot: torque, tolerance, specification.

A person with modest tools, a parts book, and patience can still form a hypothesis, test it, and learn something transferable. That transferability is the point. The scooter is not the argument. The method is.

---

## What this is not

This paper does not claim that older machines are universally better than newer ones.

It does not claim that AI is useless for repair or learning. At the corpus layer, it can be genuinely helpful.

It does not claim that local-first AI eliminates error, bias, or vendor dependence.

It does not claim nostalgic superiority for any generation, labor market, or technology era.

It does not claim peer-reviewed status or formal mechanical engineering credentials.

It claims something narrower and, I think, more important:

The ability to learn systems by taking them apart is a public capacity worth defending.

When that capacity is blocked — by sealed design, lost manuals, proprietary diagnostics, labor devaluation, or fluent black-box software — people do not merely lose convenience. They lose a method of understanding the world.

---

## Conclusion

If I asked a chatbot to explain the ignition system on a Honda Cub, it would probably do a decent job.

If I handed you the parts book, a basic tool set, and the machine itself, you still would not know what you were doing until you took it apart.

That difference is the paper.

Mechanical knowledge, skilled labor, and the right to fix are not separate causes. They are what remain when people are still allowed to learn by disassembly. AI has entered the same terrain. It can describe systems beautifully. The question is whether we will still be allowed to inspect them, verify them, rerun them, and put them back together.

I learned motorcycles, wiring, and small engines by taking things apart.

I learned LLMs the same way.

The method transfers. The right to use it does not come automatically.

---

*Working draft. Public packet and claim boundaries: [README.md](README.md)*
