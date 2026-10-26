# Data Provenance and Metadata Governance for Embodied AI Datasets

Embodied AI models learn manipulation not from static images but from hours of first-person video — the world as a worker, a housekeeper, or a warehouse operator actually sees it. A corpus of 161,200 hours of annotated multi-view ego-centric video is only as useful as a team's ability to trust and trace every hour. That trust is the job of metadata governance and data provenance.

## Why provenance decides whether a dataset can be used at all

Training and evaluation both fail quietly when provenance is missing. A policy model that drops a fragile object may have learned the wrong thing from a single corrupted session, a mislabeled sensor, or a clip whose timestamps drifted. Reproducibility — the ability to re-run an experiment against the exact same inputs — is impossible without a recorded chain from capture to delivery. For embodied AI, where errors are physical and costly, provenance is not a documentation nicety; it is a safety property.

## The metadata we record for every hour

At JUST DATA, each hour of video is stored as a paired MP4 stream plus a JSON annotation sidecar. This dual-track design makes the annotation a first-class object, not a fragile in-band overlay. Around that pair we attach structured metadata along several dimensions:

- **Scene taxonomy.** Every clip is classified into one of eight scenes — factory (22.5%), hotel (21.2%), home (14.9%), retail (11.5%), logistics (11.2%), agriculture (8.2%), catering (5.1%), and other (5.3%) — so a client can filter to exactly the distribution their model needs.
- **Sensor configuration.** Multi-view rigs capture the same moment from several perspectives; roughly 30% of the corpus is six-view footage. The metadata records which views were active, their mount positions, and their calibration state.
- **Temporal alignment.** Views are synchronized to the microsecond level, and the alignment parameters are themselves part of the record — not an assumption baked into the pipeline.
- **Quality gates.** Each clip carries the outcome of cleaning and validation steps: what was removed, why, and which checks passed.

## The traceability chain

Provenance is a chain, not a label. We track four stages — capture, cleaning, annotation, and delivery — so any delivered subset can be mapped back to the raw session it came from. Pre-Token standardization sits inside this chain: it makes the transformation from raw video to token-ready sequences deterministic and reproducible, so two parties processing the same clip produce the same input tensors. Annotation provenance is recorded the same way, including when and by which pipeline a label was produced — human-in-the-loop review or our self-developed annotation algorithm, which clients can deploy privately.

## What this means in practice

The practical consequence is versioning. A delivered dataset is a versioned artifact: a client that trained against a given snapshot can later ask for an exact diff or a re-delivery of the identical subset, and we can reconstruct it from the record. That is the difference between "a pile of video files" and a data asset that a serious engineering team can build on — and audit.

Metadata governance does not make a dataset larger. It makes it trustworthy. For embodied AI, where every model is only as reliable as the hours it was trained on, trust is the real deliverable.
