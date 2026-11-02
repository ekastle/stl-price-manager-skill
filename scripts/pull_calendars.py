#!/usr/bin/env python3
"""
Pull AirROI live calendars for a comps set.
Expects AIRROI_API_KEY in the environment (inject via `op run`).
"""
import os
import csv
import json
import requests
from datetime import date
from pathlib import Path

API_KEY = os.environ.get("AIRROI_API_KEY")
if not API_KEY:
    raise SystemExit("AIRROI_API_KEY not set. Use op run or export the secret.")

BASE = "https://api.airroi.com"
HEADERS = {"x-api-key": API_KEY}

def pull_listing(listing_id: str):
    url = f"{BASE}/listings/live/calendar"
    params = {"listing_id": listing_id, "currency": "usd"}
    r = requests.get(url, headers=HEADERS, params=params, timeout=60)
    r.raise_for_status()
    return r.json()

def main():
    comps_path = Path("config/comps.csv")
    if not comps_path.exists():
        comps_path = Path("config/comps.example.csv")
    
    snapshot_date = date.today().isoformat()
    out_dir = Path("snapshots")
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / f"Calendar Snapshot {snapshot_date}.csv"
    
    rows = []
    with open(comps_path) as f:
        reader = csv.DictReader(f)
        for comp in reader:
            if comp.get("Active", "Y").upper() != "Y":
                continue
            lid = comp["Listing_ID"]
            print(f"Pulling {lid} ({comp.get('Name', '')})...")
            try:
                data = pull_listing(lid)
                # Adapt to actual AirROI response shape
                calendar = data.get("calendar") or data.get("nights") or []
                for night in calendar:
                    rows.append({
                        "Snapshot_Date": snapshot_date,
                        "Listing_ID": lid,
                        "Tier": comp.get("Tier", ""),
                        "Weight": comp.get("Weight", ""),
                        "Stay_Date": night.get("date"),
                        "Available": "Y" if night.get("available") else "N",
                        "Nightly_Rate": night.get("rate") or night.get("price"),
                        "Min_Nights": night.get("min_nights"),
                        "Currency": "USD",
                        "Source": "AirROI live/calendar",
                    })
            except Exception as e:
                print(f"  Failed: {e}")
    
    if rows:
        with open(out_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote {len(rows)} rows to {out_file}")
    else:
        print("No data pulled.")

if __name__ == "__main__":
    main()
