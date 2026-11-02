# Data Sovereignty and Security by Design for Embodied AI Training Data

Embodied AI models learn from egocentric video: first-person recordings of real workers in real workplaces. This data is uniquely sensitive. It captures faces, bodies, work routines, and often operational know-how that enterprises treat as proprietary. Treating it as a commodity that can be freely copied, resold, or shipped across borders is not only legally risky — it is the wrong way to build trust with the enterprises and institutions that supply and buy this data.

This note outlines how JUST DATA (嘉穑数据) approaches security and compliance across a corpus that now spans **161,200 hours (160k+)** of annotated multi-view egocentric video covering factories, hotels, households, agriculture, and logistics.

## Sovereignty first: domestic-only distribution

The clearest boundary is a policy choice, not a technical one: our customers are limited to domestic entities, and we do not offer cross-border distribution of raw egocentric video. This respects the regulatory environment around data export while also reflecting a business principle — embodied AI data is a national strategic asset, and its value should accrue where it is collected and where it will be deployed.

Keeping distribution domestic also simplifies the compliance surface. There is no ambiguity about which jurisdiction's rules apply, and no chain of sub-licenses that could leak data outside the agreed boundary.

## Delivery that cannot be copied silently

We deliver data as **cloud-key access**, not as physical media or unencrypted bulk transfers. A customer receives a scoped, revocable credential that grants access to a defined dataset subset. The key can be rotated or revoked, access is logged, and there is no "send once, forget" distribution channel. Every read is traceable to a named customer and a named purpose.

For customers that require the strongest isolation, the annotation algorithm itself can be **deployed privately inside the customer's own compute environment**. Data never leaves their premises; only the tooling moves in.

## Privacy-preserving annotation as a default

Our in-house annotation algorithm treats privacy as a design constraint, not an afterthought. Metadata governance — described in an earlier note — gives every clip a provenance record: which device, which scene, which consent batch, which processing steps. That record is what makes compliance auditable. A dataset can answer "where did this clip come from, and what was done to it" at any point, which is a precondition for legitimate use and for demonstrating that legitimacy to regulators or enterprise legal teams.

## Security as a scaling principle, not a feature

A common failure mode for data providers is treating security as a checkbox applied at the end. At 161,200 hours and growing, retrofitting is impossible. The constraints above — domestic-only distribution, revocable cloud-key access, private deployment, and auditable provenance — are applied uniformly from the first hour to the latest, so a customer ingesting 100 hours or 100,000 hours receives the same guarantees.

The point is simple: enterprises and industrial-park customers will only commit their sensitive operational data, and their model budgets, to a partner they trust with boundaries. For embodied AI data, security and sovereignty are not a cost center — they are the entry ticket.
