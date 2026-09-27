#!/usr/bin/env python3
"""
execution/download_ngdr_priority.py
Downloads key priority NGDR datasets (Geology 2M, Hydrocarbon Blocks,
Drilling Boreholes, Lineaments, and Lithology 50k metadata/parquet).
"""

import sys
import urllib.request
from pathlib import Path

TARGET_DIR = Path(__file__).resolve().parent.parent / "data" / "ngdr"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

DOWNLOADS = [
    {
        "name": "NGDR_Geology_2M.geojsonl.7z",
        "url": "https://github.com/ramSeraph/indian_land_features/releases/download/geology/NGDR_Geology_2M.geojsonl.7z",
        "desc": "Indian Geology 1:2M Pan-India Stratigraphy"
    },
    {
        "name": "NGDR_Geology_2M.parquet",
        "url": "https://github.com/ramSeraph/indian_land_features/releases/download/geology/NGDR_Geology_2M.parquet",
        "desc": "Indian Geology 1:2M Parquet (Columnar/Fast SQL)"
    },
    {
        "name": "NGDR_Hydrocarbon_Blocks.geojsonl.7z",
        "url": "https://github.com/ramSeraph/indian_land_features/releases/download/mining/NGDR_Hydrocarbon_Blocks.geojsonl.7z",
        "desc": "Indian Hydrocarbon Exploration & Exploitation Blocks"
    },
    {
        "name": "NGDR_Mining_Exploration_Drilling_Boreholes.geojsonl.7z",
        "url": "https://github.com/ramSeraph/indian_land_features/releases/download/mining/NGDR_Mining_Exploration_Drilling_Boreholes.geojsonl.7z",
        "desc": "Indian Drilling Boreholes & Well Locations"
    },
    {
        "name": "NGDR_Lineament_250k.geojsonl.7z",
        "url": "https://github.com/ramSeraph/indian_land_features/releases/download/geomorphology/NGDR_Lineament_250k.geojsonl.7z",
        "desc": "Indian Subsurface Lineaments & Fault Networks 1:250k"
    },
    {
        "name": "NGDR_Obvious_Geological_Potential.geojsonl.7z",
        "url": "https://github.com/ramSeraph/indian_land_features/releases/download/mining/NGDR_Obvious_Geological_Potential.geojsonl.7z",
        "desc": "Obvious Geological Potential (OGP) Areas"
    }
]

def download_file(item):
    dest = TARGET_DIR / item["name"]
    if dest.exists() and dest.stat().st_size > 1000:
        print(f"[SKIP] {item['name']} already exists ({round(dest.stat().st_size/(1024*1024), 2)} MB)")
        return True
    
    print(f"[DOWNLOADING] {item['name']} - {item['desc']} ...")
    req = urllib.request.Request(item["url"], headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req) as resp, open(dest, "wb") as f:
            total = int(resp.headers.get("Content-Length", 0))
            downloaded = 0
            chunk_size = 1024 * 1024
            while True:
                chunk = resp.read(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                downloaded += len(chunk)
                if total > 0:
                    pct = (downloaded / total) * 100
                    print(f"  {pct:.1f}% ({round(downloaded/(1024*1024),1)}/{round(total/(1024*1024),1)} MB)\r", end="")
        print(f"\n[DONE] Saved to {dest}")
        return True
    except Exception as e:
        print(f"\n[ERROR] Failed to download {item['name']}: {e}", file=sys.stderr)
        return False

def main():
    print("=" * 65)
    print("  Downloading Priority NGDR Geoscience Datasets")
    print("=" * 65)
    for item in DOWNLOADS:
        download_file(item)
    print("=" * 65)
    print(f"All files saved in: {TARGET_DIR}")

if __name__ == "__main__":
    main()
