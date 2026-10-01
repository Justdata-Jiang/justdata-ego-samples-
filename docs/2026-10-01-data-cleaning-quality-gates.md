# Data Cleaning and Quality Gates for Real-World Ego Video Assets

The ceiling of an embodied-AI model depends heavily on the floor of its training data: the minimum quality that survives cleaning. For real-world multi-view wearable ego video, the distance between raw recordings and deliverable training data is a pipeline of explicit quality gates.

Our annotated ego-video asset currently exceeds 160,000 hours (161,200 hours), of which synchronized six-view footage accounts for roughly 30%. The asset spans eight scenario families — factory (22.5%), hotel (21.2%), home (14.9%), retail (11.5%), logistics (11.2%), agriculture (8.2%), food service (5.1%), and other (5.3%). At this scale, loose cleaning lets noise propagate and get amplified during training.

## Four layers of quality gates

**1. Capture-side completeness.** Before any clip is accepted, we verify that every view stream is present, that durations match, and that there are no dropped frames or broken segments. A common multi-view failure is a clip that looks complete on one stream but only covers half the action on another. That must be caught at the source; otherwise downstream temporal alignment fails in cascade.

**2. Temporal alignment.** Six-view data demands high timestamp precision, so capture devices synchronize to microsecond resolution. The gate checks that inter-stream clock drift falls within an acceptable bound and that frame-level indices align. Footage that fails synchronization is flagged for rework rather than passed into annotation.

**3. Annotation consistency sampling.** The in-house annotation algorithm runs on the customer side via private deployment, but its output is still subject to human spot-checks and rule-based validation. The gate checks whether bounding boxes and keyframes match action semantics, and whether label vocabulary stays uniform across clips — the same action must not be called two different things in two segments.

**4. Pre-delivery triple check.** Before delivery we deduplicate (removing near-identical repeated scenes), backfill metadata (scenario, view layout, duration, capture time, annotation version), and run a compliance review. Only data that passes this gate ships, delivered through cloud-based key transfer.

## Gates are data, too

Every gate records its pass/fail outcome and the parameters it checked — drift bound, frame index, annotation version — as structured metadata. This makes a dataset reproducible and traceable: when a customer reports a frame-level issue, we can trace it back to the exact gate and version that produced it.

Paired with pre-token standardization (normalizing raw multimodal streams into a token-ready format before training), the gates turn an amorphous archive of footage into a queryable, versioned asset.

## Why the gates matter

The point of cleaning is not to count how many bad samples we threw away; it is that customers can drop the data straight into their training pipeline. For domestic embodied-AI customers, reliability outweighs raw size. A stream that aligns linearly, uses one labeling vocabulary, and carries trustworthy timestamps supports model iteration more predictably than three times the volume of noisy data.

Data quality has no end state. The gates must keep hardening as the asset grows — which is why we treat cleaning as an engineering discipline rather than a one-off pass.