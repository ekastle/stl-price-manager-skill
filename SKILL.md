---
name: stl-price-manager
description: Use when managing short-term rental pricing, pulling AirROI calendars for comps, analyzing market gaps, or generating pricing recommendations for an Airbnb listing. Includes 1Password secret handling.
---

# STL Price Manager Skill

When this skill is invoked:

1. Confirm the user's own listing ID and the current comps set (core / secondary / zero-weight).
2. Retrieve the AirROI API key securely via 1Password CLI (`op read "op://STR/AirROI API Key/credential"` or equivalent secret reference). Never print or log the key.
3. For each active listing (own + comps), call the AirROI live calendar endpoint:
   `GET https://api.airroi.com/listings/live/calendar?listing_id=<ID>&currency=usd`
   with header `x-api-key: <key>`.
4. Save the raw snapshot as a dated CSV (e.g. `Calendar Snapshot YYYY-MM-DD.csv`) to the designated Google Drive Snapshots folder or local path.
5. Compute weighted averages for the next 30/60/90 days (available nights only, excluding own listing for the comp average). Calculate the gap % vs own listing.
6. Produce a recommended pricing table and concrete actions (e.g. temporary near-term rate cut, New Listing Promotion, weekly discount).
7. Update the Comp Tracker sheet / Weekly_Summary if Google Sheets is connected.
8. Report cost (number of calls × $0.20) and flag any delisted or zero-rate listings.

Safety rules:
- Never store or echo API keys, tokens, or 1Password references in chat, Drive files, or git.
- Respect the user's stated monthly budget ceiling.
- Keep all historical snapshots; never delete prior data.
- Cape Coral (and similar cities) may have a 6-night minimum stay — do not recommend lowering below local legal minimums.

Required access: AirROI account + API key in 1Password, Google Drive (for snapshots), optional Google Sheets.
