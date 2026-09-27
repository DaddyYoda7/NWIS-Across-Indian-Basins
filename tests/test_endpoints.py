"""
Tests for NWIS Web Endpoints and Module Availability
Verifies that all 8 NWIS module HTML pages and portal routes return HTTP 200.
"""

import unittest
from urllib.request import Request, urlopen

BASE_URL = "http://127.0.0.1:3000"

PAGES = [
    "index.html",
    "views/gateway.html",
    "views/command_center.html",
    "views/well_explorer.html",
    "views/well_intelligence.html",
    "views/historical_intelligence.html",
    "views/risk_monitor.html",
    "views/scenario_lab.html",
    "views/reports.html",
    "app/js/router.js",
    "app/css/glacial_modules.css",
]


class TestNWISEndpoints(unittest.TestCase):
    """
    Validates availability and integrity of all module views.
    """

    def test_all_pages_serve_200(self):
        for page in PAGES:
            with self.subTest(page=page):
                url = f"{BASE_URL}/{page}"
                req = Request(url, method="GET")
                with urlopen(req, timeout=5) as response:
                    self.assertEqual(response.status, 200)
                    body = response.read()
                    self.assertGreater(len(body), 500)


if __name__ == "__main__":
    unittest.main()
