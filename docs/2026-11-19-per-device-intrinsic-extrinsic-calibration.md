# Per-Device Calibration: The First Gate of Trainable Ego Data

Two recordings can look identical on screen and yet be worlds apart for a robot. One decodes into geometry a model can train on; the other quietly injects systematic error into every sample. The dividing line is not resolution, not frame rate, and not file format — it is calibration, performed per device, every time.

## Why "per device" instead of "per model"

No two headsets off a production line are identical. Lenses are ground within tolerance, sensors are mounted with finite precision, and boards flex and settle under heat and handling. A focal length, principal point, or distortion coefficient that is averaged across a model — or even a batch — bakes a fixed bias into every frame.

For browsing, that bias is invisible. For stereo depth, it is fatal. Depth is computed as Z = f·b/d: if the calibrated focal length f or baseline b is off by a fraction of a percent, every pixel's depth is wrong by that same fraction, and the error grows with distance.

Per-device calibration means each unit receives its own parameter file — intrinsics K and distortion D for each camera, extrinsics R/t and baseline b between the two cameras, and, at the trainable and evaluation tiers, the camera–IMU extrinsic and the fixed time offset td. No shared model parameters. No batch-level substitutes.

## The four-tier ladder

In the EGO-S2 four-tier scheme, calibration is where the tiers actually separate.

- **L0 watchable**: no calibration required. The video decodes and plays; that is all.
- **L1 material**: K/D/R/t/b per device, with a single reprojection check around RMS < 2 px.
- **L2 trainable**: per-device K/D/R/t/b, plus camera–IMU extrinsic and per-device td; reprojection RMS < 0.5 px and epipolar offset < 1 px.
- **L3 evaluation**: all of the above, plus raw calibration observations and residuals delivered alongside the data; RMS < 0.3 px, epipolar < 0.5 px, and re-runnable scripts.

Each tier contains the one before it. You cannot skip L2's calibration and still call the data trainable; you cannot skip L3's residuals and still call it a benchmark.

## Calibration is not a one-time event

A headset is worn, bumped, heated, and cooled. Parameters drift. That is why the scheme requires re-calibration before and after every session at L2, and adds temperature-drift logging at L3. A parameter file captured once at the factory is a snapshot, not a guarantee.

## Why this matters to buyers

The cheapest tier is the most expensive if what you meant to buy was training data. Re-calibrating retroactively from video alone is hard and often impossible — the raw observations that made the original parameters trustworthy are gone. A calibration file is not a certificate; it is part of the data itself.

So the first question to ask any supplier is not "how many hours?" but "is every hour calibrated per device, with residuals I can inspect?" If the answer is no, those hours are watchable, not trainable.
