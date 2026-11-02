# STL Price Manager Skill

A reusable skill and bot setup for automated short-term rental (Airbnb / VRBO) pricing, competitive set (comps) tracking, and market analysis.

Designed for Grok bots (and compatible agents) with **minimal human input** after initial setup. Uses AirROI live calendar data, 1Password for secrets, and a private Git repo (or local files) for snapshots and trackers.

## What it does

- Pulls live calendar data (nightly rates + availability) for a defined set of comps + your own listing via the AirROI API (`GET /listings/live/calendar`).
- Stores dated snapshots by committing to a private Git repo (or locally).
- Computes weighted average comp rates, occupancy signals, and pricing gaps.
- Generates recommended pricing tables and actions (near-term cuts, peak holds, etc.).
- Keeps API keys and credentials out of chat and source code via 1Password.

## Quick start

1. Install the 1Password desktop app and CLI (`op`). Enable CLI integration and biometric unlock.
2. Store your AirROI API key in 1Password (e.g. vault `STR`, item `AirROI API Key`, field `credential`).
3. Create a private GitHub repo for your operational data (or use local files). Copy `config/comps.example.csv` and fill in your real Listing_IDs (include your own listing as Tier=Self).
4. Clone this repo or add it as a skill in your Grok bot environment.
5. Run or schedule the pull / skill.

See `docs/setup.md` for full details and `SKILL.md` for the agent skill definition.

## Install as a Grok skill

- Point your Grok bot at this repo, or copy the skill folder into your skills directory (`.grok/skills/` or equivalent).
- Invoke with `/stl-price-manager` or by asking the bot to run the pricing manager skill.

## Share as a Grok Bot template

1. Create a Grok Bot whose system prompt includes the instructions from `prompts/bot-system-prompt.md` and enables this skill.
2. In the Bot settings, choose **Share as template** → publish publicly or to your team.
3. Recipients import the template and connect their own 1Password + AirROI key. They get an independent copy.

## Cost notes

AirROI live calendar is ~$0.20 per listing per pull. A typical weekly cadence for ~10–20 comps stays well under $30/month. Always include your own listing in every pull.

## License

MIT — feel free to adapt for your market.
