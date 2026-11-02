# STL Price Manager Skill

A reusable skill and bot setup for automated short-term rental (Airbnb / STR) pricing, competitive set (comps) tracking, and market analysis.

Designed for Grok bots (and compatible agents) with **minimal human input** after initial setup. Built from real Cape Coral / Turtle Creek work using AirROI live calendar data, 1Password for secrets, and Google Drive/Sheets for snapshots and trackers.

## What it does

- Pulls live calendar data (nightly rates + availability) for a defined set of comps + your own listing via the AirROI API (`GET /listings/live/calendar`).
- Stores dated snapshots (CSV or Google Sheets).
- Computes weighted average comp rates, occupancy signals, and pricing gaps.
- Generates recommended pricing tables and actions (near-term cuts, peak holds, etc.).
- Keeps API keys and credentials out of chat and source code via 1Password.

## Quick start

1. Install the 1Password desktop app and CLI (`op`). Enable CLI integration and Touch ID / biometric unlock.
2. Store your AirROI API key in 1Password (e.g. vault `STR`, item `AirROI API Key`, field `credential`).
3. Clone this repo or add it as a skill in your Grok bot environment.
4. Configure your comps list (see `config/comps.example.csv`).
5. Run or schedule the pull script / bot routine.

See `docs/setup.md` for full details and `SKILL.md` for the agent skill definition.

## Cost notes

AirROI live calendar is ~$0.20 per listing per pull (Standard). A typical weekly cadence for ~10–20 comps stays well under $30/month. Always include your own listing in every pull.

## License

MIT — feel free to adapt for your market.
