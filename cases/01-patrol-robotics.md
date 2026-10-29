# Patrol robotics: the deployment boundary
## Decision
Treat ARVO S3 as a candidate for supervised site evaluation, not a demonstrated replacement for existing safety infrastructure.

W02 and W03 establish a team presentation about the robot. W03's investment-style language is rhetorical; this analysis replaces that framing with operational questions.

## Mechanism
V01 describes an indoor patrol platform with cameras and environmental sensing, wireless charging and remote fire response. Its page lists 50 kg mass, 2 m/s maximum speed, a 15-degree slope and 3 cm threshold capability. These are vendor specifications, not measured results.

A significant discrepancy is visible: W02 gives height 1,200 mm while V01 currently lists 573 mm. Width and depth agree at 732 and 540 mm. Neither number is silently corrected; configuration, revision or page error must be resolved before a clearance assessment.

## Engineering analysis
Localization estimates position; it is not a guarantee of safe motion. T01 presents visual, visual-inertial and multi-map SLAM across camera configurations. It does not establish that ARVO implements ORB-SLAM3. Deployment still needs evidence about difficult lighting, repetitive corridors, occlusion and recovery after tracking loss.

Remote intervention adds another dependency: sensing, alert delivery, operator interpretation, authorization and actuation must all succeed. A successful stage demonstration cannot identify the reliability of this chain.

## Proposed evaluation — not performed
| Question | Measurement | Decision implication |
| --- | --- | --- |
| Can patrols finish in the intended environment? | Completed routes / attempted routes, with intervention causes | Frequent manual rescue undermines unattended coverage |
| Are alerts actionable? | True/false alerts and missed labeled events; include exposure hours | High nuisance burden can erase operator benefit |
| Does response arrive in time? | Distribution of detection-to-operator and operator-to-action delay | Report tail latency, not only mean |
| What happens on network loss? | Document stop/recovery behavior under controlled disconnect | Undefined recovery blocks deployment |
| Can docking sustain shifts? | Docking success and unavailable minutes across repeated cycles | Charging time reduces available coverage |

Tests require facility permission and qualified supervision. Fire functionality should be evaluated with safe simulations and applicable professional procedures.

## Commercial reasoning
A procurement decision depends on completed useful patrol hours and operator burden, not nominal top speed. Compare lease/depreciation, maintenance, mapping, network installation, charging downtime and review labor with the actual existing workflow. W03's one-third labor-cost assertion has no traceable calculation and is excluded from the conclusion.

Partnership logos do not establish paid fleet size. A broad security-robotics forecast does not establish the addressable indoor patrol segment. No verified revenue, pricing or customer retention data is supplied.

## What changes the decision
A dated configuration sheet resolving dimensions; an independently inspectable site trial; downtime and intervention logs; and a full-cost quotation would move the case beyond a plausible mechanism.
