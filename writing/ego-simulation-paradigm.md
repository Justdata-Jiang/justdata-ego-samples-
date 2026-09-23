# EGO × Simulation: Building World Models on a Low-Fidelity Skeleton

*Why the fastest path to embodied AI is real ego-centric video for semantics, plus simulation for physics — and why neither alone is enough.*

---

**The next AI race is not about language. It is about physics.**

LLMs conquered text by predicting the next token, and they had a near-infinite supply of internet data to do it with. The next frontier — embodied AI, robots, world models — enjoys no such luxury. You cannot download the physical world.

Here is the uncomfortable number. Training a robot brain to anything near human competence is estimated to require on the order of **a billion hours** of real-world interaction data. What the world currently supplies is on the order of **a few million hours**. That is a roughly **200× gap** — and unlike text, physical data cannot be scraped. It has to be *earned*: one camera, one actor, one hour at a time.

Two obvious answers exist, and both are partial.

Crank up real-world collection, and costs explode. Teleoperation — the standard way to harvest genuine manipulation data — yields only a few usable hours per operator-day, and it does not scale gracefully.

Lean entirely on simulation, and you hit a subtler wall: **simulators are semantically hollow.** A synthetic kitchen has cups and plates, but not the long tail of real mess — the jammed drawer, the mismatched Tupperware, the way an actual human grips a mug with a full hand because the handle is too small. Train a model purely in sim, and it learns the physics of a world that does not quite exist.

There is a third path, and I believe it is the one that will actually get us there.

**Use ego-centric real video to build a *low-fidelity world skeleton* — not precise physics, but the structure, semantics, and interaction grammar of the real world — and let simulation inject the physics on top of that skeleton.**

---

## First, the skeleton: what EGO is uniquely good at

Do not ask ego-centric video to teach exact physics. Ask it for the thing it is uniquely cheap and abundant at: **what exists in the world, and how everything interacts.**

EGO produces a *world concept map*, not a physics engine. From millions of hours of first-person footage, a model can learn:

- **Layout and semantics** — where rooms, objects and people are; what categories things fall into.
- **Affordances and interaction grammar** — what a mug is *for*, that a door is pulled not pushed, that a cup can contain liquid.
- **Task sequences** — what "making coffee" means as an ordered chain of sub-actions.
- **Occlusion and egomotion** — how the world changes when a head turns or a hand moves, which is the raw material for view prediction.

This is the cheap part. Ego-centric data is abundant, long-tailed, and captures the world as humans actually live in it. It is the perfect tool for sketching the *macro-structure* of reality — the pencil sketch before the paint.

What EGO does **not** give you, reliably, is the physics: mass, friction, force, hidden states behind occlusions, objective coordinate frames, rare or extreme events. Not because those aren't present, but because a human's first-person experience *systematically ignores them*. Attention filters them out.

That is exactly what simulation is for.

## Second, the physics: what SIM injects

Simulation does three things EGO cannot:

1. **Controlled single-variable experiments.** In ego footage, the camera moves, the body moves, the hand moves — all at once. It is nearly impossible to tell whether a change in the image came from the camera or the object. Simulation lets you fix the camera and push only the object; fix the object and move only the camera. That is how you convert surface correlations into causal models — and causal understanding is the core of a world model.

2. **Reconstruct the missing background.** Human attention annotates the world by ignoring most of it. Simulation, seeded from the EGO-built skeleton, can render the complete environment — the corners nobody looked at, the objects nobody touched — and run full-state rollouts on them.

3. **Inject idealized physics as a constraint.** Once the skeleton says *what interacts with what*, simulation imposes the *how*: contact, mass, friction, stability.

Here's the mental model. **EGO draws the sketch; simulation paints it and assigns the rules.** The model never has to learn from scratch what a "cup" is or that you pour into it. It learns those cheaply from real video, and then simulation teaches it why the cup falls, spills, or stays put.

That division of labor is what makes training dramatically cheaper.

## Why the combination actually works

**It cures simulation's semantic void.** Pure sim must model thousands of real homes from scratch; EGO gives you the real semantic prior first, so sim only needs to *instantiate* physics on a skeleton that already understands the world. This is the single biggest win.

**It cures EGO's causal confound.** EGO supplies candidate hypotheses about "what happens"; sim tests them one variable at a time and discards the false correlations. The result is a model that reasons about *cause*, not just appearance.

**It fills attention bias.** EGO is a human's first-person note-taking; sim restores the full room from the notes and fills in what the notes left out.

**It lowers total cost.** You stop trying to model ten million real homes in a simulator. You extract skeletons from cheap abundant video, and instantiate physics only where you need it. Collection stays cheap, simulation stays bounded.

**It feeds downstream models twice over.** An embodied LLM inherits real task narratives and egomotion from EGO, and physical feasibility from sim — less "armchair planning." A VLA inherits affordances from EGO, and action consequences from sim — imitation that is actually physically realizable.

---

## The hard limits (the honest part)

This is not a panacea, and I want to be clear about where it breaks.

1. **The alignment gap.** The skeleton is built on visual appearance; sim physics is idealized engine physics. Friction, mass and restitution parameters rarely match reality, so an interaction that "looks right" in EGO may not reproduce in sim, and vice versa. You cannot close this with EGO + sim alone — you need *some* real ground-truth physical data for cross-domain calibration.

2. **Cognitive bias is inherited.** The skeleton encodes how *humans* think the world is, not how it objectively is. Things humans never look at — heavy objects, dangerous scenarios — are concepts the skeleton simply lacks, and sim can only add physics to object categories the skeleton already contains. An object EGO never saw is an object sim cannot semantically rescue.

3. **A ceiling on fidelity.** Visible-level observation cannot infer hidden variables like interior material or internal structure. What you end up with is *real semantics + idealized physics*, which is not the same as *real physics*. Out-of-distribution objects will still break it.

4. **Reconstruction error compounds.** Turning EGO video into a simulatable skeleton requires 3D reconstruction and instance segmentation, both of which are error-prone. Errors in geometry propagate into every downstream physics rollout, amplified at each step.

5. **Fusing two modalities is hard.** This is not "pre-train on EGO, then fine-tune on sim." The two data domains — real first-person footage and rendered simulation — have to be aligned in a shared representation space, and the loss must be designed so the model predicts real egocentric visual change *and* satisfies physical conservation. Get it wrong and you get a model with **two memories**: one that handles EGO frames, one that handles sim physics, and no generalization between them.

---

## The pipeline that follows from this

**Layer 1 — EGO (low-fidelity skeleton).** Train on large-scale ego-centric video to extract object semantics, spatial layout, hand-object interaction, task sequences, and egocentric view prediction. No precise physics. The output is a *world concept map*.

**Layer 2 — SIM (physics injection).** Instantiate simulation environments from the reconstructed skeletons. Run controlled interventions to learn physical rules, occluded states and missing background. Apply physics-consistency constraints on top of the skeleton.

**Layer 3 — A small amount of real-world ground truth.** Calibrate the sim-to-real gap with a *small* quantity of genuine robot interaction data. This is the bridge between idealized physics and the real world — and it cannot be skipped.

The result is a world model that carries real-world semantics *and* physical consistency — cheaply, and faster than either path alone.

---

## The bigger point

The field is moving from language to the physical world, and the bottleneck is not chips — it is **data that describes the real world**. That data will not come from simulation alone, and it cannot all come from teleoperation. It will come from the cheapest, most abundant source we have: the first-person experience of being in the world.

EGO gives us the skeleton of that experience. Simulation gives it the physics. Together, and only together, they get us from machines that *read* the world to machines that *live in* it.

The pencil was always more important than the paint. You just can't hang a painting on a sketch alone.

---

*— Xubo Jiang, Founder, JUST DATA*