# Scaling Multi-View Ego Data Annotation: A Self-Hosted Pipeline

The bottleneck in embodied AI training data is shifting from scarcity to usability. For VLA (vision-language-action) models, raw video is raw material; structured annotations are the trainable signal. A single hour of multi-view ego video produces several synchronized high-definition streams, and manual frame-by-frame labeling is not only costly but hard to keep consistent across annotators. That consistency problem is the first gate any scaled data asset must pass.

At Just Data, we process 161,200 hours of annotated multi-view ego video across eight scenarios — factory, hotel, home services, retail, logistics packing, agriculture, catering, and others — with six-view footage accounting for roughly 30%. What makes this tractable is not manual effort but a self-developed annotation pipeline.

The pipeline rests on three components.

**First, microsecond-level time synchronization and multi-view alignment.** Multiple camera streams are synchronized at microsecond precision before any labeling, so the same action lines up across viewpoints. That cross-view alignment is the precondition for associating labels across cameras.

**Second, Pre-Token standardization.** Before annotation, raw video is converted into a unified intermediate representation: coordinate systems, object poses, and action timing are normalized against a common standard. This means the algorithm's output can be consumed directly by downstream models, avoiding the familiar failure where each source labels and formats data in its own way and the results cannot be merged.

**Third, self-developed annotation algorithms with human quality gates.** For high-frequency, repetitive tasks — fastening screws, making beds, packing boxes — we use action-recognition and keypoint/object-relation models to generate structured annotations automatically, with each video paired one-to-one with JSON labels. Human reviewers sample-verify and correct rather than label from scratch, forming an "algorithm pre-label + human audit" quality gate.

The value of this pipeline becomes clearer in the context of current embodied models. VLA training benefits far more from data where action boundaries, contact points, and tool-object relationships are explicit than from hours of unlabeled footage. Automated pre-labeling lets us attach that structure at the volume implied by 161,200 hours, while keeping a human in the loop precisely where errors are expensive: novel motions, occlusions, and cross-view correspondence.

We do not claim this pipeline removes human effort entirely. The quality gate exists precisely because automated labels are imperfect; the goal is to shift human attention from routine frame-by-frame labeling to verification and correction.

A point worth underlining: this annotation stack supports private, third-party deployment. A customer can run the same pipeline inside their own compute center, feeding newly collected data through it to keep producing annotations in a consistent format — without the data ever leaving their domain. For security-sensitive customers who need to accumulate annotation assets continuously, this is the core of a "data + algorithm" delivery. It turns a one-off data transaction into a durable annotation capability.

That, in turn, defines our positioning. We do not just supply annotated data; we supply the capability to keep producing high-quality annotated data. The path from data supplier to scenario-level co-pilot follows naturally from that.

(Note: figures above are project-level public figures; "160k+ hours" refers to 161,200 hours. Delivered metrics are subject to the actual delivery agreement.)