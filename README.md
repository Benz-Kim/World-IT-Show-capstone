# World IT Show | Technology in Context
**What must be true for an exhibition technology to work outside the exhibition?**

A comparative research project connecting WIS team presentations with technical mechanisms, deployment constraints and commercial evidence. The cases span indoor patrol robotics, circular-resource platforms and immersive systems.

## Research position
A convincing demonstration starts a question; it does not settle it. This project turns product narratives into traceable claims, examines the weakest operational handoff and identifies the evidence needed for a defensible decision.

| Case | Central question | Current conclusion |
| --- | --- | --- |
| [Patrol robotics](cases/01-patrol-robotics.md) | Can mobile sensing deliver reliable, actionable coverage? | Configuration conflict and missing site results require a supervised evaluation |
| [Circular resources](cases/02-circular-resource-platforms.md) | Does a digital record establish a physical and environmental outcome? | Custody and accounting boundaries must be tested separately |
| [Immersive systems](cases/03-immersive-systems.md) | Is the system a scene, a live visualization or a validated model? | Evaluate the user task and data connection before accepting the label |

**Start with the [comparative synthesis](reports/synthesis.md).** Follow a conclusion through the [claim ledger](evidence/claim-ledger.csv), [source register](evidence/source-register.md) and [research method](METHODS.md).

## An example of the method
The WIS 2025 deck and current ARVO S3 page disagree on robot height. The case records both, preserves their temporal scope and requests a dated configuration sheet instead of selecting a convenient figure. Unsupported cost-saving claims are excluded from the conclusion.

## Project record
Kim Hyoin's activity record describes annual WIS participation during 2023–25, startup interviews, technology research and presentations to students. Available shared artifacts substantiate team presentation material for 2023 and 2025; no 2024 presentation or interview transcript is supplied.

The 2023 deck names Baek Seongho, Kim Jiyoon and Kim Hyoin. The 2025 deck names Kim Hyoin, Kang Chanyoung, Jung Sion and Lee Haim. The associated script uses Kang Chanyoung's presentation persona. These are team artifacts; individual slide authorship is not inferred.

The repository's October 2026 research layer adds evidence classification, technical interpretation, contradictions and evaluation designs. It reports no independent product testing, company employment or actual investment solicitation.

## Research artifacts
- [Source register](evidence/source-register.md): accessible originals, source classes and retrieval limits.
- [Method](METHODS.md): claim-level evaluation, comparison dimensions and design references.
- [Claim ledger](evidence/claim-ledger.csv): machine-readable dispositions and next evidence.
- [Case studies](cases/01-patrol-robotics.md): mechanisms, deployment boundaries and proposed measurements.
- [Sensitivity model](analysis/patrol-economics.md): transparent illustrative economics, with no vendor price assumptions.
- [Contribution rules](CONTRIBUTING.md): maintain the research as evidence changes.

## Reading the evidence
Vendor claims, shared presentations and analytical inferences are distinguished throughout. Technical papers explain mechanisms; they do not independently validate the featured products. Current websites do not establish historical specifications. Source links may require access permission; third-party materials remain under their original rights.

All Markdown analysis is maintained in English. Original source titles and content may be Korean.

## Check the repository
Run `python tools/check_research.py` with Python 3.10+ to validate internal Markdown links and claim-source references. This is a structural check, not an external-source verification.
