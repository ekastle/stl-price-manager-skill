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

## 3. Comps list

Copy `config/comps.example.csv` and fill in your listing IDs, match scores, and tiers. Always include your own listing with weight 100 / tier Self.

## 4. Google Drive / Sheets

Create a folder structure:
- Snapshots/ (dated CSVs)
- Comp Tracker (Google Sheet with Comps, Calendar_Snapshots, Weekly_Summary sheets)

Grant the bot access if using a Grok Bot computer.

## 5. Bot routine example

Schedule a Grok bot (or use Automations) to run every Monday and Thursday:

> Run the stl-price-manager skill. Pull calendars for all active comps + self. Save snapshot to Drive Snapshots. Update Weekly_Summary. Flag if own near-term rate is >15% above weighted core comps. Stay under the $30 monthly ceiling.

## 6. Local script test

```bash
op run --env-file=.env.tpl -- python scripts/pull_calendars.py
```

Where `.env.tpl` contains:
```
AIRROI_API_KEY=op://STR/AirROI API Key/credential
```
