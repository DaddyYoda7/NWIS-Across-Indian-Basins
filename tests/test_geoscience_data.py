"""
Unit tests for Indian Geoscience Data, NGDR Parquet datasets, and LAS Parsers.
"""

import unittest
from pathlib import Path
import pyarrow.parquet as pq

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
NGDR_DIR = DATA_DIR / "ngdr"
PARSERS_DIR = DATA_DIR / "parsers"


class TestGeoscienceData(unittest.TestCase):
    """
    Validates integrity of downloaded NGDR datasets, schemas, and parsers.
    """

    def test_ngdr_geology_2m_parquet_exists_and_readable(self):
        file_path = NGDR_DIR / "NGDR_Geology_2M.parquet"
        self.assertTrue(file_path.exists(), "NGDR_Geology_2M.parquet must exist")
        table = pq.read_table(str(file_path))
        self.assertGreater(table.num_rows, 4000)
        self.assertIn("stratigrap", table.column_names)
        self.assertIn("age", table.column_names)
        self.assertIn("bbox", table.column_names)

    def test_ngdr_lithology_50k_parquet_exists(self):
        file_path = NGDR_DIR / "NGDR_Lithology_50k.parquet"
        self.assertTrue(file_path.exists(), "NGDR_Lithology_50k.parquet must exist")
        metadata = pq.read_metadata(str(file_path))
        self.assertGreater(metadata.num_rows, 1000000, "Should have millions of lithology polygons")

    def test_ngdr_priority_archives_exist(self):
        expected_files = [
            "NGDR_Geology_2M.geojsonl.7z",
            "NGDR_Hydrocarbon_Blocks.geojsonl.7z",
            "NGDR_Mining_Exploration_Drilling_Boreholes.geojsonl.7z",
            "NGDR_Lineament_250k.geojsonl.7z",
            "NGDR_Obvious_Geological_Potential.geojsonl.7z"
        ]
        for f in expected_files:
            target = NGDR_DIR / f
            self.assertTrue(target.exists(), f"Expected archive {f} to exist")
            self.assertGreater(target.stat().st_size, 1000, f"File {f} must not be empty")

    def test_catalog_json_validity(self):
        catalog_path = DATA_DIR / "catalog.json"
        self.assertTrue(catalog_path.exists(), "data/catalog.json must exist")
        import json
        with open(catalog_path, "r", encoding="utf-8") as f:
            catalog = json.load(f)
        self.assertIn("spatial_layers", catalog)
        self.assertGreater(len(catalog["spatial_layers"]), 100)
        self.assertIn("parsers", catalog)

    def test_parsers_integrated(self):
        self.assertTrue((PARSERS_DIR / "las_py" / "las_py").exists())
        self.assertTrue((PARSERS_DIR / "mivaa_las_dlis_converter").exists())


if __name__ == "__main__":
    unittest.main()
