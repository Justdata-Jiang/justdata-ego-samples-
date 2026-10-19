# Why Embodied-AI Ego Data Uses a "Video + JSON" Dual Format

A foundational decision in building embodied-AI data assets — often overlooked but decisive for downstream usability — is the **storage format**. JUST DATA (嘉穑数据) stores its 160,000+ hours of multi-view ego video uniformly in a dual-track structure: raw video (MP4) plus structured annotations (JSON). This note explains the engineering rationale.

## Why video alone is not enough

First-person (ego) video is the raw material for embodied-AI training, but a video file is only a sequence of pixels. It carries **no semantics**: which object in a frame is graspable, which action belongs to a task step, and what pose the sensors held at that moment must all live in a separate layer.

Burning annotations into the video itself (overlays, filename conventions) creates three problems: any annotation revision forces re-encoding the entire clip; downstream consumers cannot filter data by condition quickly; and annotation styles across batches drift apart.

## What the JSON carries

Each JSON metadata file, paired one-to-one with its video, records three kinds of information:

1. **Scene and task labels** — scene membership (factory, hotel, home, retail, logistics, agriculture, and more) plus the specific process type;
2. **Temporal alignment** — working with microsecond-level time synchronization, it stores each camera stream's clock reference and sync offset, so the six views align precisely on the time axis;
3. **Annotation results** — structured labels for objects, actions, and interactions, ready for direct consumption in training and retrieval.

## What the separation buys

- **Lossless, replayable video**: raw frames stay unpolluted by annotations and can be reused across different tasks;
- **Lightweight, queryable JSON**: annotations are plain text, enabling second-level filtering of "a scene + a process + a six-view combination" without decoding any video;
- **Versionable schema**: as the annotation schema evolves, only the JSON migrates — the video assets stay untouched.

## Relationship to Pre-Token standardization

The JSON schema in this dual-track format is itself one landing point of **Pre-Token standardization**. Across 161,200 hours, roughly 30% of which are six-view, spanning eight scenes (factory 22.5%, hotel 21.2%, home 14.9%, retail 11.5%, logistics 11.2%, agriculture 8.2%, other 5.3%, catering 5.1%), a unified JSON schema is what keeps structure from fracturing between collection batches. Without it, downstream training would require repeated cleaning and realignment. A unified schema is what makes "collect once, reuse many times" possible — and it is the precondition for quality at scale.

---

**JUST DATA · 嘉穑数据 · Real-world data assets**
