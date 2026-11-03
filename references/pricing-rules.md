# Pricing Rules & Analysis Logic

Example logic derived from real STR work. Adapt the ranges, min-stay, and fees for your market.

## Core Principles
- Always include your own listing in every calendar pull.
- Prioritize comps that match your property (bedrooms, sleeps, pool type, location style, non-waterfront if applicable).
- Weight by Match_Score (apply a capacity penalty for much larger homes).
- Drop delisted / zero-rate comps from future pulls; keep historical snapshots.
- Enforce the local legal minimum stay.
- Cost control: schedule pulls (e.g. Mon/Thu) and set a hard monthly ceiling.

## Gap Analysis
For next 30 / 60 / 90 days (available nights only):
1. Compute weighted average rate of active core comps (exclude self).
2. Compare to own listing average on the same nights.
3. Flag if own rate is meaningfully above the weighted core average (near-term friction risk for new or low-review listings).

## Example Pricing Table Structure
| Period | Own Current | Core Comp Avg | Suggested | Notes |
|--------|-------------|---------------|-----------|-------|
| Near-term (0-30d) | — | — | Temporary cut if gap is large | Improve visibility/occupancy |
| Shoulder | — | — | Match or small premium | |
| Peak / Holidays | — | — | Hold or slight premium | |

Fixed elements (adapt to your listing):
- Cleaning fee
- Minimum stay (legal minimum or higher)
- Optional add-ons (e.g. pool heat)
- Discounts: weekly / monthly, New Listing Promotion while building reviews

## Output
Produce a concrete pricing table the host can paste into the Airbnb calendar, plus 2-3 action items.
