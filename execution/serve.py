"""
NWIS Framework Local Server
Serves the NWIS Glacial Precision web framework on localhost for rapid inspection
and interactive browser testing.
"""

from http.server import SimpleHTTPRequestHandler
import socketserver
import sys

DEFAULT_PORT = 8000


class GlacialHTTPRequestHandler(SimpleHTTPRequestHandler):
    """
    Custom handler to set proper cache control and headers.
    """

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()


"""
Starts the local development server at the given port.
"""
def start_server(port: int = DEFAULT_PORT) -> None:
    print("=" * 60)
    print("  NWIS Glacial Precision Framework Server")
    print("=" * 60)
    print(f"  Portal URL:       http://localhost:{port}/index.html")
    print(f"  Direct NWIS:      http://localhost:{port}/nwis/index.html")
    print("=" * 60)
    print("  Available Modules:")
    print(f"  - Command Center: http://localhost:{port}/nwis/nwis_command_center_glacial_minimal_edition_page_02/code.html")
    print(f"  - Well Explorer:  http://localhost:{port}/nwis/nwis_well_explorer_glacial_minimal_edition_page_03/code.html")
    print(f"  - Well Profile:   http://localhost:{port}/nwis/nwis_well_intelligence_w_204_profile_page_04/code.html")
    print(f"  - Historical:     http://localhost:{port}/nwis/nwis_historical_intelligence_institutional_memory_page_05/code.html")
    print(f"  - Risk Monitor:   http://localhost:{port}/nwis/nwis_risk_monitor_proactive_subsurface_intelligence_page_06/code.html")
    print(f"  - Scenario Lab:   http://localhost:{port}/nwis/nwis_scenario_lab_interactive_decision_support_page_08/code.html")
    print(f"  - Reports:        http://localhost:{port}/nwis/nwis_reports_decision_support_minimalist_editorial_dossier/code.html")
    print(f"  - Entry Gateway:  http://localhost:{port}/nwis/nwis_entry_gateway_glacial_light_edition/code.html")
    print("=" * 60)

    socketserver.ThreadingTCPServer.daemon_threads = True
    with socketserver.ThreadingTCPServer(("", port), GlacialHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            httpd.server_close()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT
    start_server(port)
