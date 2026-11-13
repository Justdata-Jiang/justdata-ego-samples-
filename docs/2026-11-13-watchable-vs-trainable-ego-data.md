# Of Those Millions of Hours, How Many Can Actually Train? The Watchable–Trainable Gap

The embodied-AI data race is increasingly measured by a single, misleading unit: hours. Over the past year, several leading players have publicly announced collection targets of millions of hours per year, reaching toward ten million within two. But hours by themselves say nothing. Between a clip that can be played and a clip that can train a model, there is a gap — and it is wider than most of the industry admits.

The gap in one sentence: "watchable" only requires that a video decodes, plays back, and can be browsed by a human. "Trainable" requires per-unit intrinsics/extrinsics calibration, microsecond-level time synchronization, near-lossless encoding, per-frame metadata, quality-check gates, and 2D/3D hand and action labels — all in place. The first can be produced with a camera and a memory card. The second requires an entire production chain, from capture hardware through cleaning and annotation.

To make this gap explicit, we propose a four-tier taxonomy: watchable (L0), material (L1), trainable (L2), and evaluation (L3).

- **Watchable (L0)**: dual video decodes and plays back; calibration, exposure sync, IMU, and metadata may all be relaxed. Usable only for scene inventory, demos, and rough screening — never for training or evaluation.
- **Material (L1)**: dual video plus per-unit intrinsics/extrinsics, timestamps, IMU, and raw archive packages, with sync meeting a basic threshold — but no systematic QC or labels yet. It can be re-processed and upgraded; it cannot train directly.
- **Trainable (L2)**: synchronization, per-unit calibration, near-lossless bitrate, per-frame metadata, QC thresholds, and 2D/3D hand and action labels all in place. This is the floor for pretraining, mid-training, and post-training of embodied models.
- **Evaluation (L3)**: on top of L2, adds metrological depth ground truth, confidence masks, re-runnable evaluation scripts, and a frozen split — and must be physically isolated from the training set.

The gaps between tiers are drawn with hard numbers. For synchronization: L0 sets no requirement; L1 requires stereo exposure sync σ<1ms with a single measurement; L2 requires σ<100µs with a histogram, ideally <10µs. For calibration: L0 does none; L2 requires per-unit K/D/R/t/b, camera–IMU extrinsics, and the fixed time offset, with reprojection RMS<0.5px. For encoding: L0 accepts 8 Mbps per stream; L2 demands 20–40 Mbps near-lossless.

The implication is uncomfortable and useful: under the headline of "massive scale," the hours that truly clear the trainable bar may be only a fraction of the total. JUST DATA starts from 161,200+ annotated hours of multi-view ego video, and holds every hour — through microsecond synchronization, Pre-Token standardization, and a self-developed annotation algorithm that supports private deployment — to the "trainable" standard rather than the "watchable" one. What the industry should actually be competing on is not hours, but trainable hours: a number that should be published, audited, and standardized.
