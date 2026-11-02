---
name: stl-price-manager
description: Use when managing short-term rental pricing, pulling AirROI calendars for comps, analyzing market gaps, or generating pricing recommendations for an Airbnb listing. Includes 1Password secret handling. Stores operational data in a private Git repo.
---

# STL Price Manager Skill

When this skill is invoked:

1. Confirm the user's own listing ID and the current comps set (core / secondary / zero-weight). Load from the private operational data repo (e.g. ekastle/turtlecreek-pricing/config/comps.csv) or local config/comps.csv.
2. Retrieve the AirROI API key securely via 1Password CLI (`op read "op://STR/AirROI API Key/credential"` or equivalent secret reference) or via 1Password for Agents. Never print or log the key.
3. For each active listing (own + comps), call the AirROI live calendar endpoint:
   `GET https://api.airroi.com/listings/live/calendar?listing_id=<ID>&currency=usd`
   with header `x-api-key: <key>`.
   Prefer AirROI MCP tools if available in the agent environment; otherwise use the Python script under `op run`.
4. Save the raw snapshot as a dated CSV (e.g. `snapshots/Calendar Snapshot YYYY-MM-DD.csv`) by committing it to the private operational data repo (e.g. ekastle/turtlecreek-pricing) via GitHub tools / git. Keep all historical snapshots.
5. Compute weighted averages for the next 30/60/90 days (available nights only, excluding own listing for the comp average). Calculate the gap % vs own listing. Use match weights from comps.csv.
6. Produce a recommended pricing table and concrete actions (e.g. temporary near-term rate cut, New Listing Promotion, weekly discount). Commit the analysis output (markdown or CSV) to the private repo under analysis/ if desired.
7. Flag any delisted or zero-rate listings; update Active status in comps.csv if needed and commit.
8. Report cost (number of calls × $0.20) and stay under the user's monthly budget ceiling.

Safety rules:
- Never store or echo API keys, tokens, or 1Password references in chat, Drive files, or git.
- Respect the user's stated monthly budget ceiling.
- Keep all historical snapshots; never delete prior data.
- Cape Coral (and similar cities) may have a 6-night minimum stay — do not recommend lowering below local legal minimums.
- Operational data (comps with real Listing_IDs, snapshots) lives in a private Git repo; the skill itself remains public and generic.

Required access: AirROI account + API key in 1Password (desktop app + CLI or 1Password for Agents), private GitHub repo for data storage (e.g. ekastle/turtlecreek-pricing), optional Google Drive as fallback.
