# STL Price Manager Skill

A reusable skill and bot setup for automated short-term rental (Airbnb / VRBO / STR) pricing, competitive set (comps) tracking, and market analysis.

Designed for Grok bots (and compatible agents) with **minimal human input** after initial setup. Uses AirROI live calendar data, 1Password for secrets, and a private Git repo (or local storage) for dated snapshots and trackers.

## What it does

- Pulls live calendar data (nightly rates + availability) for a defined set of comps + your own listing via the AirROI API (`GET /listings/live/calendar`).
- Stores dated snapshots (CSV) by committing to a private Git repo or saving locally.
- Computes weighted average comp rates, occupancy signals, and pricing gaps.
- Generates recommended pricing tables and actions (near-term cuts, peak holds, etc.).
- Keeps API keys and credentials out of chat and source code via 1Password.

## Quick start

1. Install the 1Password desktop app and CLI (`op`). Enable CLI integration and Touch ID / biometric unlock. (Or connect 1Password for Agents in Grok Bot.)
2. Store your AirROI API key in 1Password (e.g. vault `STR`, item `AirROI API Key`, field `credential`).
3. Create a private GitHub repo for your operational data (or use a local folder). Copy `config/comps.example.csv` → `config/comps.csv` and fill in real Listing_IDs (include your own listing as Tier=Self).
4. Add this skill to your Grok bot environment (see install section below).
5. Run or schedule the pull / skill routine. Bot commits snapshots to your private data repo.

See `docs/setup.md` for full details and `SKILL.md` for the agent skill definition.

## Install as a Grok skill

- Copy the repo (or just the skill folder) into `~/.grok/skills/stl-price-manager/` or your bot's skills library.
- Or clone and point your Grok config / bot at it.
- Invoke with `/stl-price-manager` or by asking the bot to run the pricing manager skill.

## Share as a Grok Bot template

1. Create a Grok Bot whose system prompt includes the workflow from `prompts/bot-system-prompt.md` (or embed the skill).
2. In the Bot settings, choose **Share as template** → publish publicly or to your team.
3. Recipients get their own independent copy and connect their own 1Password + AirROI key. They do not get your data or secrets.
4. Promote the share link on X. For the Template Rewards Pilot (invite-only), use the paid partnership label when posting.

## Cost notes

AirROI live calendar is ~$0.20 per listing per pull. A typical weekly cadence for ~10–20 comps stays well under $30/month. Always include your own listing in every pull.

## License

MIT — feel free to adapt, fork, or embed in your own bots and templates.

## Monetization ideas

- Open skill for maximum adoption + visibility.
- Package into a public Grok Bot template (eligible for Template Rewards Pilot if invited).
- Offer paid setup, custom comps research, or ongoing pricing reviews as a service.
- List on community Agent Skills marketplaces if they support paid skills.
