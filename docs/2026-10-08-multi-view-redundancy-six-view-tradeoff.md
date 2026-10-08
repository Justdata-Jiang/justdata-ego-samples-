# Multi-view Ego Data Collection: View Redundancy and the "Six-view" Trade-off

A common misconception in embodied-AI data is treating "more viewpoints" as "better data." In reality, every additional camera carries extra collection cost, harder synchronization, and larger storage, cleaning, and annotation overhead. The real engineering question is not whether to go multi-view, but in which scenes, at what ratio, and with how many cameras.

## Why view redundancy matters

Fine manipulation — grasping, assembly, flipping objects, bimanual handling — is often instantaneous and heavily occluded. A single head-mounted view only covers the gaze direction; the moment both hands move toward the edge of the frame or occlude each other, key frames are lost. Multi-view collection exists so that a global head view and close-up hand views back each other up: what one camera cannot see, another can; a contact point occluded in one view is recovered from another. This redundancy is not waste — it is the source of labeling confidence for fine manipulation.

## "Six-view" is a decision, not a standard answer

Our data asset exceeds 160,000 hours (161,200 hours), of which synchronized six-view (six-camera) footage accounts for roughly 30 percent. That share is deliberate. The higher a scene's precision and speed requirements, the more six-view capture pays off — factory assembly lines, with their short cycle times, are the clearest case. In contrast, housekeeping or agriculture tasks, which lean more on mobility and scene understanding, are covered more efficiently with monocular or few-camera rigs. Combining six-view and monocular footage at roughly a 3:7 ratio is an exercise in constrained resource allocation between "detail redundancy" and "breadth of coverage."

## Redundancy only pays off with synchronization and standardization

The value of multi-view data rests on two technical supports. First, microsecond-level time synchronization — without it, frames across lenses cannot be aligned, and a hand action misaligned from the global scene by a few milliseconds injects systematic error into fine-grained tasks like grasping. Second, Pre-Token standardization — converting multi-camera video and annotations into a structured format that models can consume directly, so the same data can be reused across manufacturers and algorithm teams. Together these make view redundancy usable redundancy, rather than a pile of footage that is painful to align.

## Conclusion

The goal of multi-view ego collection is always that every hour of data can answer "what can it teach a robot?" View redundancy and the six-view ratio are engineering decisions made in service of that goal — not a blind chase of "more cameras is better."

JUST DATA (嘉穑数据) builds real-world data assets for embodied AI, delivering queryable, scene-distributed multi-view ego data to domestic robot manufacturers and embodied-AI teams.