# Patrol economics: a sensitivity model
## Purpose
Express what a quotation and site trial must establish. All numbers below are illustrative assumptions, not ARVO pricing, trial results or a forecast.

Let:
- F = annual fixed cost of robot access, installation amortization and support.
- H = scheduled patrol hours per year.
- a = fraction of scheduled hours delivering useful patrol service, after charging and failures.
- r = review/intervention labor hours per useful patrol hour.
- w = loaded labor cost per review hour.

Then useful hours U = H × a, and cost per useful patrol hour C = F / U + r × w.

This cost does not imply equivalence to a human guard. Reception, judgment, access control and emergency obligations may remain outside the robot's service.

## Illustrative sensitivity
Hold H = 4,000 hours/year, r = 0.10 and w = 20 currency units/hour. These assumptions are chosen to expose sensitivity, not to describe a real facility.

| Annual fixed cost F | a = 0.50 | a = 0.75 | a = 0.90 |
| --- | --- | --- | --- |
| 10,000 | 7.00 | 5.33 | 4.78 |
| 20,000 | 12.00 | 8.67 | 7.56 |
| 30,000 | 17.00 | 12.00 | 10.33 |

Units are currency units per useful patrol hour. Cells are rounded to two decimals. For example: 20,000/(4,000×0.75) + 0.10×20 = 8.67.

## Interpretation
Doubling useful availability reduces the fixed-cost burden per delivered hour; it does not remove review labor. A cheaper robot can still have a higher delivered cost if site failures lower availability. Human review intensity is a separate driver and should be measured rather than assumed away.

For a comparable alternative cost B, positive useful hours and B > r×w, the availability threshold is a > F/[H×(B-r×w)]. A threshold above 1 means the assumed configuration cannot beat B on this cost basis. This algebra is only valid if both alternatives supply the same narrowly defined patrol service.

## Missing costs and evidence
Energy, insurance, compliance, financing, disposal and major repair can require additional terms. Avoid double counting costs already included in F. Obtain a quotation, measure availability and review effort, and define the equivalent baseline before using this model for a decision.
