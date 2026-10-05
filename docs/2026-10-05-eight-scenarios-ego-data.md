# Eight Scenarios in 161,200 Hours of Real-World Ego Data

Embodied-AI models generalize only as far as the environments they have seen. A manipulation policy that learns inside one factory bay quietly breaks the moment flooring texture, lighting, or occlusion patterns change; the gap between "this works in the lab" and "this works in the world" is filled, in practice, by data that spans many environments.

Our annotated ego-video asset is built on that premise. It currently exceeds 160,000 hours (161,200 hours), about 30% of which is synchronized six-view footage, and it is not concentrated in a single domain. Instead, the asset is deliberately distributed across eight scenario families:

| Scenario | Share |
|---|---|
| Factory | 22.5% |
| Hotel | 21.2% |
| Home / housekeeping | 14.9% |
| Retail | 11.5% |
| Logistics | 11.2% |
| Agriculture | 8.2% |
| Other | 5.3% |
| Food service | 5.1% |

## Why diversity outranks any single scene

**Factory (22.5%)** anchors the asset. Manufacturing tasks — assembly, inspection, material handling — run on the shortest cycle times and demand the tightest precision. This is why they occupy the largest share, and why synchronized six-view capture matters most here: on a fast-moving line, a single forward-facing view misses the hands.

**Hotel and home / housekeeping (21.2% + 14.9%)** inject unstructured, human-adjacent environments. Corridors, furniture, beds, kitchens — these scenes are irregular and stress perception far harder than a fixed assembly station. For a mobile robot or a household assistant, coverage in this band decides whether a model can be deployed at all rather than demonstrated in a demo.

**Retail and logistics (11.5% + 11.2%)** contribute repetitive-but-varied manipulation: picking, packing, shelving, sorting. They offer high action density per hour, which makes them efficient for training grasp and placement policies.

**Agriculture (8.2%), food service (5.1%), and other (5.3%)** supply the long tail. These scenes are harder to scale — they are seasonal, dispersed, or lower in unit volume — but they are exactly where a domain gap bites hardest. A robot that has never seen uneven ground or wet surfaces has no reason to behave when it meets them.

## A distribution is a research decision

The shares are not arbitrary. They reflect where domestic embodied-AI deployments are actually heading and where synchronized multi-view capture is feasible at scale. Critically, every clip carries documented metadata — scenario, view layout, duration, capture time, annotation version — so the asset can be queried per-scenario.

That is the point of treating this as an asset rather than a folder of footage: a customer can assemble a training mixture matched to their own deployment target. "What is actually in this data" becomes a queryable property, not a hope, which is the first thing a serious training team asks before committing compute.