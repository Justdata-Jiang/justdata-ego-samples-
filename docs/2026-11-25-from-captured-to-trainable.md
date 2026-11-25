# From 'Captured' to 'Trainable': Three Alignments in Embodied Training Data

**— A cognitive reframing by an embodied-data engineer**

## Prologue

One observation keeps surfacing on the front lines of the industry: of the Ego (first-person) data circulating in the market today, only a very small fraction is genuinely qualified and ready to go directly into embodied-model training — some in the field even estimate it at under ten percent. This is not a rigorous statistical conclusion; it is a shared observation from both the capture side and the training side. But it points to a problem we once collectively misread:

Training a robot does not require "video." It requires a set of multimodal data strictly aligned in time and space. We used a "shoot a video" mindset to produce data, so naturally all we got was video — and video alone is nowhere near enough to support training.

This article aims to make three layers clear: where we went wrong cognitively, where we went wrong scientifically, and where we went wrong in engineering.

## Layer One: Cognitive Reframing — Training data is "vision + description," not just "footage"

Our initial understanding of first-person data could be summed up in one sentence: as long as there are hands in the frame and the action was captured, it counts. Acceptance was done by human eye, a subjective judgment.

Following that logic, we also fell for "the more cameras, the better" — scaling from monocular to stereo, then four, six, seven cameras, believing that more lenses meant higher-quality data.

But if we truly understand the training objective of embodied models, one basic fact becomes clear: what the model must learn is "action," and action is a physical process unfolding at a specific time and in a specific space. To fully describe that process, pixels alone are not enough.

The model needs to know at least four things simultaneously:

1. What it saw — the imagery itself;
2. What it was seeing — semantics (this is a hand, this is tightening a screw);
3. Where and when it happened — spatiotemporal coordinates (which device, which moment, which position);
4. Whether these signals cross-validate — whether the IMU's acceleration, the depth derived from stereo disparity, and the geometric relations given by calibration parameters can mutually verify one another.

This is also why the default recording format in the robotics world (ROS 2) is MCAP — a container that can hold camera frames, IMU readings, robot state, and calibration parameters together, with every message carrying a nanosecond-level timestamp. Its very existence is about encapsulating "vision" and "description" on a single timeline.

We used to get the order exactly backwards: shoot the video first, then leave the descriptive information — timestamps, IMU, calibration, SOP, localization — to be filled in later during cleaning and labeling. But timestamps, IMU readings, calibration parameters, and on-site context are all physical facts that exist at the moment of capture; they cannot be reconstructed after the fact. The video is isolated, the description is patched on afterwards, and the two never line up — such data is worth close to nothing to the model.

This is not "slightly lower quality"; it is "the wrong data modality."

## Layer Two: Respect for the Science — Alignment happens at the physical layer, not in post-processing

If the first layer is "thinking about it wrong," the second is "shooting it wrong." And this error hides in the physical details.

**Temporal alignment.** To control cost, much of the equipment in the past used rolling shutters. A rolling shutter exposes line by line — within a single frame, the first row and the last row do not capture the same instant. When a hand moves quickly, the pixels within a frame are temporally misaligned. The human eye is insensitive to this; but to a machine, this frame has no single "true instant," and the timing information itself is contaminated.

Worse still is software frame interpolation: frames "filled in" by an algorithm to inflate frame rate carry no genuine physical timestamp. Once the two stereo channels fall out of sync, the most direct consequence is distorted disparity computation. Stereo depth estimation relies on the left and right channels capturing the same instant to infer spatial distance; when the two channels are temporally inconsistent, the precision of depth estimation goes out of control, and the geometric relations become untrustworthy.

This is settled engineering: visual-inertial systems (VSLAM) require microsecond-level hardware synchronization; even a few milliseconds of offset accumulates into trajectory drift. Qualified equipment must therefore trigger frames at the hardware level in sync, rather than relying on software post-hoc alignment.

**Spatial alignment.** We once assumed a nominal baseline of 65mm is simply 65mm. But if the enclosure is 3D-printed, tolerances and errors exist — the nominal baseline is not the true baseline, and the intrinsic and extrinsic parameters are not unified at the lowest level. What does calibration quality mean? Published research repeatedly demonstrates that calibration degradation directly harms downstream depth estimation, 3D detection, and SLAM; temperature, vibration, and stress all cause calibration to drift silently. A device that has not been calibrated unit by unit produces not "low-precision data" but "geometrically untrustworthy data."

So the logic of professional practice becomes clear: use an aluminum die-cast enclosure to lock the relative position of lenses and sensors at sub-millimeter level, and calibrate each unit along the X/Y/Z axes individually — this is not nitpicking; it is holding the baseline of spatial alignment.

## Layer Three: Respect for Engineering and Standards — Accuracy is the first principle, speed is the second

One detail worth recording: when we asked whether we could first make an enclosure with CNC machining, the quote we received was — a small part of roughly 10×3×2.5 centimeters, at a cost of twenty to thirty thousand RMB apiece.

That number makes one thing clear: precision has a price, and a steep one. Industrial-grade tolerances, the heat dissipation of a metal enclosure, per-unit three-axis calibration — every link is paying for "accuracy."

Why a metal enclosure? Beyond geometric precision, there is heat dissipation. Rising temperature damages sensors, drifts the accuracy of the IMU and sensors, and in turn degrades calibration. A metal enclosure is not about aesthetics; it is the physical guarantee of precision stability.

Consider bitrate, another point that is easy to misread: 8–10 Mbps for a monocular stream is not a "recommended value" but a floor — below this, the image exhibits blocking artifacts, mosaic degradation, and aggravated motion artifacts, rendering the data unusable. Higher is of course better, but every step up in bitrate drives up storage and thermal cost. This is not a simple "the higher the better" problem, but an engineering trade-off optimizing between "usable" and "cost."

These details all point to one principle: first make it accurate, then make it fast. Pursuing "fast" at the expense of "accuracy" produces scrap.

## Epilogue

This is not a pitfall any single company fell into; it is a problem facing the entire human-perspective data collection industry. When the industry focuses on scale metrics such as "hours captured" and "scenarios covered," the most fundamental alignment — temporal alignment, spatial alignment, geometric alignment — is often overlooked.

And that means: the competition in embodied data collection is shifting from the scale of hours toward who can, from the hardware level up, produce truly aligned, cross-validatable multimodal training data.

This is also why we must rebuild from the hardware up — when the foundation is wrong, no matter how high you build, it remains a dangerous structure.
