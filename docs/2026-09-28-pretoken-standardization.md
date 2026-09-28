# Pre-Token Standardization: Making Heterogeneous Ego Data Aligned at Ingestion

Embodied models consume tokens, but the data fed to them is often wildly heterogeneous: different rigs, different views, different resolutions and sampling rates, and annotation schemas written by different teams. If those differences are left to be sorted out at training time, they corrupt the structure after tokenization and force the model to spend capacity on noise that carries no signal. Pre-Token standardization takes the direct approach: before data ever becomes tokens, converge it onto a single schema.

## Why normalize upstream

Multi-view ego data is intrinsically scattered. Six-camera rigs account for roughly 30% of the dataset, with the remainder split across single- and dual-camera combinations; scenarios span eight categories—factory, hotel, home, retail, logistics, agriculture, food service, and more. Within one corpus of 160,000+ hours (161,200h), you may find high-resolution close-ups next to wide-angle panoramas, with annotation granularity and naming conventions that vary from batch to batch. Cleaning all of this downstream means cost that grows linearly with volume—and batches that refuse to align. Standardizing at the source compresses that one-time cost to the point of capture.

## How we standardize

Pre-Token standardization works at three layers. First, a uniform temporal regime: building on microsecond time synchronization, hardware-level timestamps for every frame are fixed onto a single coordinate system. Second, uniform structure and metadata: video and its companion structured signals—joint angles, force readings—are consolidated into fixed-schema JSON and delivered alongside the video. Third, uniform annotation: actions, object boundaries, and labels produced during annotation land on consistent naming and coordinate conventions. What ships out the door already carries a deterministic structure.

## Why it matters

The payoff of standardization is not prettiness—it is reusability. Data captured once can be sold many times: different customers receive the same schema and can plug it into their training pipelines without a second cleaning pass. After tokenization, the input structure is stable, and the model stops paying for format noise. This is precisely the precondition for treating data as an asset: scale only matters once the format is unified.