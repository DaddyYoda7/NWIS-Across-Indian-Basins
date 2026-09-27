#!/usr/bin/env python3
"""
execution/pull_geoscience_data.py
Deterministic script to pull, organize, and catalog Indian land features,
shapefiles, GIS layers, and well log (LAS/DLIS) parsers for the NWIS backend.
"""

import sys
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TMP_REPOS = ROOT / ".tmp" / "repos"
DATA_DIR = ROOT / "data"
SPATIAL_DIR = DATA_DIR / "spatial"
PARSERS_DIR = DATA_DIR / "parsers"

REPOSITORIES = [
    {
        "name": "indian_land_features",
        "url": "https://github.com/ramSeraph/indian_land_features.git",
        "category": "geospatial_features"
    },
    {
        "name": "ht_shapefiles",
        "url": "https://github.com/HindustanTimesLabs/shapefiles.git",
        "category": "administrative_boundaries"
    },
    {
        "name": "imd_shapefiles",
        "url": "https://github.com/India-Meteorological-Department/India-shapefiles.git",
        "category": "meteorological_geospatial"
    },
    {
        "name": "india_shapefiles_bundle",
        "url": "https://github.com/data014/India-Shapefiles-Bundle.git",
        "category": "comprehensive_shapefiles"
    },
    {
        "name": "mivaa_las_dlis_converter",
        "url": "https://github.com/MIVAA-ai/mivaa-las-dlis-to-json-convertor.git",
        "category": "well_log_parsers"
    },
    {
        "name": "las_py",
        "url": "https://github.com/laslibs/las-py.git",
        "category": "well_log_parsers"
    }
]


def run_git_clone(repo):
    target = TMP_REPOS / repo["name"]
    if target.exists() and (target / ".git").exists():
        print(f"[EXISTS] {repo['name']} already cloned at {target}")
        return True
    
    print(f"[CLONING] {repo['name']} from {repo['url']} ...")
    cmd = ["git", "clone", "--depth", "1", repo["url"], str(target)]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"[OK] Successfully cloned {repo['name']}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to clone {repo['name']}: {e.stderr}", file=sys.stderr)
        return False


def _copy_repo_files(repo, src_path, catalog):
    """Copies files for an individual repository into spatial or parser directories."""
    repo_info = {"name": repo["name"], "url": repo["url"], "category": repo["category"]}
    if repo["category"] == "well_log_parsers":
        dest = PARSERS_DIR / repo["name"]
        if not dest.exists():
            shutil.copytree(src_path, dest, ignore=shutil.ignore_patterns(".git"))
        catalog["parsers"].append({
            "name": repo["name"],
            "path": str(dest.relative_to(ROOT)),
            "purpose": "LAS / DLIS wellbore log parsing to JSON for PostgreSQL ingestion"
        })
    else:
        dest_repo = SPATIAL_DIR / repo["name"]
        dest_repo.mkdir(parents=True, exist_ok=True)
        for ext in ["*.geojson", "*.json", "*.shp", "*.dbf", "*.shx", "*.kml", "*.csv"]:
            for file in src_path.rglob(ext):
                if ".git" in file.parts:
                    continue
                target_file = dest_repo / file.relative_to(src_path)
                target_file.parent.mkdir(parents=True, exist_ok=True)
                if not target_file.exists():
                    try:
                        shutil.copy2(file, target_file)
                    except Exception:
                        pass
                catalog["spatial_layers"].append({
                    "repo": repo["name"],
                    "file": file.name,
                    "path": str(target_file.relative_to(ROOT)),
                    "size_bytes": file.stat().st_size
                })
    catalog["sources"].append(repo_info)


def copy_spatial_assets():
    """Extract and organize spatial and parser files into project data directory."""
    SPATIAL_DIR.mkdir(parents=True, exist_ok=True)
    PARSERS_DIR.mkdir(parents=True, exist_ok=True)
    
    catalog = {
        "title": "NWIS Indian Geoscience & Well Intelligence Catalog",
        "updated_at": "2026-09-24",
        "sources": [],
        "spatial_layers": [],
        "parsers": [],
        "external_repositories": {
            "NGDR": {"name": "National Geoscience Data Repository", "url": "https://ngdr.gsi.gov.in/"},
            "DGH_NDR": {"name": "DGH National Data Repository", "url": "https://ndr.dghindia.gov.in/"}
        }
    }
    
    for repo in REPOSITORIES:
        src_path = TMP_REPOS / repo["name"]
        if src_path.exists():
            _copy_repo_files(repo, src_path, catalog)
    
    catalog_path = DATA_DIR / "catalog.json"
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)
    print(f"\n[CATALOG CREATED] -> {catalog_path} (Layers: {len(catalog['spatial_layers'])})")


def main():
    TMP_REPOS.mkdir(parents=True, exist_ok=True)
    success_count = 0
    for repo in REPOSITORIES:
        if run_git_clone(repo):
            success_count += 1
            
    print(f"\nCloned {success_count}/{len(REPOSITORIES)} repositories.")
    copy_spatial_assets()


if __name__ == "__main__":
    main()
