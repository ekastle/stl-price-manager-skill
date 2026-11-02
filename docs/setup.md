# Setup Guide

## 1. 1Password

Install the 1Password desktop app and the CLI:

```bash
# macOS
brew install --cask 1password-cli
# or see https://developer.1password.com/docs/cli/get-started
```

In the 1Password app: Settings → Developer → Integrate with 1Password CLI. Enable biometric unlock.

Create a vault (or use Private) and an item:
- Title: `AirROI API Key`
- Field: `credential` (password type) containing your AirROI `x-api-key`

Reference it as `op://YourVault/AirROI API Key/credential`.

For Grok Bot / agents that support 1Password for Agents, connect the agent in the 1Password app so it can request fills without seeing the secret.

## 2. AirROI

1. Create an account at https://www.airroi.com/
2. Add credits (pay-as-you-go). Live calendar is $0.20 per listing.
3. Generate an API key and store it only in 1Password.

## 3. Comps list and private data repo

Create a **private** GitHub repo for operational data (e.g. `ekastle/turtlecreek-pricing`). Structure:
- `config/comps.csv` — real Listing_IDs, match scores, tiers. Always include your own listing with weight 100 / tier Self.
- `snapshots/` — dated CSVs from pulls (committed by the bot).
- `analysis/` — pricing tables and gap reports.

The public skill repo stays generic; never put real listing data in it.

Copy `config/comps.example.csv` from the skill as a template, then fill and commit the real version to the private data repo.

## 4. Storage preference

**Primary:** Private Git repo. Bot uses GitHub tools / git to commit snapshots and updates after each pull. This replaces Google Drive for data retention and versioning.

**Fallback:** Google Drive Snapshots folder (if preferred for some workflows).

## 5. Bot routine example

Schedule a Grok bot (or use Automations) to run every Monday and Thursday:

> Run the stl-price-manager skill. Pull calendars for all active comps + self from the private data repo's comps.csv. Commit the dated snapshot CSV to the private repo's snapshots/ folder. Generate pricing table and commit analysis if useful. Flag if own near-term rate is >15% above weighted core comps. Stay under the $30 monthly ceiling. Use 1Password for the API key.

## 6. Local script test

```bash
op run --env-file=.env.tpl -- python scripts/pull_calendars.py
```

Where `.env.tpl` contains:
```
AIRROI_API_KEY=op://STR/AirROI API Key/credential
```

Then commit the resulting snapshot from the local `snapshots/` folder into the private data repo.
