# Multi-view Ego Data Collection: A Methodology Note

## Why embodied AI needs multi-view ego data

For embodied robots to perform real-world manipulation — grasping, assembly, transport — one of the most effective learning paths is to learn from the first-person perspective of human operators. Traditional datasets are mostly recorded from fixed, third-person cameras. What the robot sees in such footage differs sharply from what a human sees while performing the task: the fine details of hand motion, and the contact relationship between the tool and the manipulated object, are frequently occluded or lost from the third-person viewpoint.

Ego (egocentric) data exists to close exactly this gap: cameras are worn by the operator, positioned and oriented close to the human eye, recording the entire operation. But monocular ego data is still insufficient. A single lens has a limited field of view; rapid hand movements, bimanual coordination, and operation details that deviate from the gaze direction cannot all be captured at the same time.

Multi-view approaches address this by placing viewpoints across the head and both hands, simultaneously recording information at three granularities — global field of view, hand close-ups, and first-person view — providing a complete observational basis for action understanding and imitation learning.

## Three core principles of the collection methodology

**First, multi-view synchronization.** The central difficulty of multi-view data lies in temporal alignment across lenses. We adopt a microsecond-level time-synchronization scheme so that frames from different viewpoints can be precisely paired during training. Without it, a hand action and the global scene would be misaligned by a few milliseconds, introducing systematic error into fine-grained tasks such as grasping.

**Second, breadth of scene coverage.** A single scene cannot support generalization. Our dataset spans factory, hotel, home, retail, logistics, agriculture, and food-service environments, with more than 160,000 hours (161,200 hours) of annotated data, of which six-view (six-camera) data accounts for roughly 30 percent. Because these are real-world scenes rather than studio setups, the data naturally carries the distribution characteristics of lighting variation, occlusion, and cluttered backgrounds.

**Third, standardized output.** Raw video enters the training pipeline only after cleaning, alignment, and label structuring. Through Pre-Token standardization, we convert multi-view video and annotations into a structured format that can be fed directly into models, so the same dataset can be reused across different robot manufacturers and algorithm teams.

## Quality before quantity

Data is the "fuel" of embodied intelligence, but impurities in the fuel translate directly into model error. Our principle is simple: every hour of data must be able to answer the question "what can this footage teach a robot?" — otherwise it is not kept. The extra cost of multi-view collection buys a property that single-view data cannot match: collect once, reuse many times, and transfer across tasks.

JUST DATA (嘉穑数据) positions itself as a provider of "real-world data assets," focused on delivering high-quality multi-view ego data to domestic robot manufacturers and embodied AI companies — turning data into assets that can be accumulated, reused, and passed down.