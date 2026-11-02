---
name: stl-price-manager
description: Automated short-term rental (Airbnb/VRBO) pricing manager. Pulls AirROI live calendars for weighted comps + self listing, analyzes rate/occupancy gaps, generates seasonal pricing tables and actions. Uses 1Password for secrets and a private Git repo (or local files) for data storage. Use for STR rate optimization, comps tracking, or scheduled market reviews.
when-to-use: Use when the user asks to check pricing, pull comps, optimize Airbnb rates, generate a pricing table, review occupancy gaps, analyze market, or schedule weekly pricing reviews for a short-term rental.
license: MIT
compatibility: Python 3.12+, 1Password CLI (`op`) with desktop app biometric unlock or service account, AirROI API key in 1Password, GitHub access for private data repo (optional). Prefers AirROI MCP tools when available in the agent.
metadata:
  author: ekastle
  version: "0.2.0"
  short-description: STR pricing & comps manager (AirROI + 1Password + private git)
---

# STL Price Manager Skill

When this skill is invoked:

1. Confirm the user's own listing ID and the current comps set (core / secondary / zero-weight). Load from the user's private operational data repo (`config/comps.csv`) or a local `config/comps.csv`. Always include the self listing with Tier=Self and high weight.
2. Retrieve the AirROI API key securely via 1Password CLI (`op read "op://YourVault/AirROI API Key/credential"` or equivalent secret reference) or via 1Password for Agents. Never print or log the key.
3. For each active listing (own + comps), call the AirROI live calendar endpoint:
   `GET https://api.airroi.com/listings/live/calendar?listing_id=<ID>&currency=usd`
   with header `x-api-key: <key>`.
   Prefer AirROI MCP tools if available in the agent environment; otherwise use `scripts/pull_calendars.py` under `op run`.
4. Save the raw snapshot as a dated CSV (e.g. `snapshots/Calendar Snapshot YYYY-MM-DD.csv`) by committing it to the user's private operational data repo via GitHub tools / git, or save locally. Keep all historical snapshots.
5. Compute weighted averages for the next 30/60/90 days (available nights only, excluding own listing for the comp average). Calculate the gap % vs own listing. Use match weights from comps.csv.
6. Produce a recommended pricing table and concrete actions (e.g. temporary near-term rate cut, New Listing Promotion, weekly discount). Commit the analysis output (markdown or CSV) to the private repo under `analysis/` if desired.
7. Flag any delisted or zero-rate listings; update Active status in comps.csv if needed and commit.
8. Report cost (number of calls × $0.20) and stay under the user's monthly budget ceiling.

Safety rules:
- Never store or echo API keys, tokens, or 1Password references in chat, Drive files, or git.
- Respect the user's stated monthly budget ceiling.
- Keep all historical snapshots; never delete prior data.
- Enforce local legal minimum stays (e.g. some markets require 6+ nights).
- Operational data (real Listing_IDs, snapshots) lives in a private Git repo or local files; the skill itself remains public and generic.

Required access: AirROI account + API key in 1Password (desktop app + CLI or 1Password for Agents), private GitHub repo for data storage (recommended), optional Google Drive as fallback.
