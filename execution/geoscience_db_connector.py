#!/usr/bin/env python3
"""
execution/geoscience_db_connector.py
Backend service & ingestion pipeline connecting Indian National Geoscience Data (NGDR),
DGH NDR petroleum well telemetry, and LAS/DLIS well log parsers.
"""

import sys
import json
from pathlib import Path
import pyarrow.parquet as pq

ROOT = Path(__file__).resolve().parent.parent
NGDR_DIR = ROOT / "data" / "ngdr"
PARSERS_DIR = ROOT / "data" / "parsers"

# Add las_py to python path
sys.path.insert(0, str(PARSERS_DIR / "las_py"))


def lookup_geology(lat: float, lon: float):
    """Query NGDR 1:2M Pan-India geological formations containing coordinates."""
    parquet_path = NGDR_DIR / "NGDR_Geology_2M.parquet"
    if not parquet_path.exists():
        return {"error": "NGDR_Geology_2M.parquet not found"}
    
    table = pq.read_table(str(parquet_path))
    df = table.to_pandas()
    
    # Filter by bounding box
    mask = df["bbox"].apply(
        lambda b: b["xmin"] <= lon <= b["xmax"] and b["ymin"] <= lat <= b["ymax"]
    )
    matches = df[mask]
    
    results = []
    for _, row in matches.iterrows():
        results.append({
            "id": row.get("id"),
            "supergroup": row.get("supergroup"),
            "group": row.get("group_"),
            "stratigraphy": row.get("stratigrap") or row.get("stratigrap_new"),
            "age": row.get("age"),
            "shape_area": row.get("shape_area"),
            "bbox": row.get("bbox")
        })
    return results


def get_lithology_50k_metadata():
    """Inspect schema and count of high-res 1:50,000 lithology quadrangles."""
    parquet_path = NGDR_DIR / "NGDR_Lithology_50k.parquet"
    if not parquet_path.exists():
        return {"status": "not_downloaded"}
    
    metadata = pq.read_metadata(str(parquet_path))
    schema = pq.read_schema(str(parquet_path))
    return {
        "num_rows": metadata.num_rows,
        "num_columns": len(schema.names),
        "columns": schema.names,
        "file_size_mb": round(parquet_path.stat().st_size / (1024 * 1024), 2)
    }


def sample_duliajan_well_correlation():
    """
    Correlates a target wellbore in Assam-Arakan Basin (Duliajan: 27.35° N, 95.32° E)
    with actual NGDR geological formations and lithological strata.
    """
    duliajan_lat, duliajan_lon = 27.35, 95.32
    geology = lookup_geology(duliajan_lat, duliajan_lon)
    litho_meta = get_lithology_50k_metadata()
    
    return {
        "basin": "Assam-Arakan Basin (Category I)",
        "target_location": {
            "name": "Duliajan Sector (Upper Assam)",
            "latitude": duliajan_lat,
            "longitude": duliajan_lon
        },
        "ngdr_geological_strata_identified": geology,
        "ngdr_lithology_50k_system": litho_meta,
        "data_providers": {
            "GSI_NGDR": "National Geoscience Data Repository (1:2M Pan-India + 1:50k Quadrangle)",
            "DGH_NDR": "Directorate General of Hydrocarbons National Data Repository (LAS, DLIS, WCR)"
        }
    }


def main():
    print("=" * 70)
    print("  NWIS Indian Geoscience & Well Intelligence Database Connector")
    print("=" * 70)
    
    correlation = sample_duliajan_well_correlation()
    print(f"\n[CORRELATION ANALYSIS] {correlation['basin']} - {correlation['target_location']['name']}:")
    print(f"Found {len(correlation['ngdr_geological_strata_identified'])} NGDR geological formation matches:")
    for g in correlation["ngdr_geological_strata_identified"][:5]:
        print(f"  * Stratigraphy: {g['stratigraphy']} | Group: {g['group']} | Age: {g['age']}")
        
    print(f"\n[NGDR 1:50,000 LITHOLOGY SYSTEM]:")
    print(f"  * Database file: NGDR_Lithology_50k.parquet ({correlation['ngdr_lithology_50k_system'].get('file_size_mb')} MB)")
    print(f"  * Total high-res lithology polygons: {correlation['ngdr_lithology_50k_system'].get('num_rows'):,}")
    
    out_file = ROOT / "data" / "duliajan_geoscience_sample.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(correlation, f, indent=2)
    print(f"\n[SAVED] Output sample saved to: {out_file}")
    print("=" * 70)


if __name__ == "__main__":
    main()
