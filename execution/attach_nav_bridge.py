"""
Attach Navigation Bridge Script
Injects the universal navigation bridge script into all NWIS module HTML pages
so cross-view routing works out of the box.
"""

from pathlib import Path

MODULE_DIRS = [
    "nwis_entry_gateway_glacial_light_edition",
    "nwis_command_center_glacial_minimal_edition_page_02",
    "nwis_well_explorer_glacial_minimal_edition_page_03",
    "nwis_well_intelligence_w_204_profile_page_04",
    "nwis_historical_intelligence_institutional_memory_page_05",
    "nwis_risk_monitor_proactive_subsurface_intelligence_page_06",
    "nwis_scenario_lab_interactive_decision_support_page_08",
    "nwis_reports_decision_support_minimalist_editorial_dossier",
]


"""
Attaches nav_bridge.js before closing body tag in target html file.
"""
def attach_bridge(file_path: Path) -> bool:
    if not file_path.exists():
        return False

    content = file_path.read_text(encoding="utf-8")
    bridge_tag = '<script src="../nav_bridge.js"></script>'
    if bridge_tag in content:
        return True

    if "</body>" in content:
        new_content = content.replace("</body>", f"{bridge_tag}</body>", 1)
    else:
        new_content = content + f"\n{bridge_tag}"

    file_path.write_text(new_content, encoding="utf-8")
    return True


"""
Iterates over all NWIS modules and connects the bridge.
"""
def main() -> None:
    root = Path.cwd() / "nwis"
    attached = 0
    for mod in MODULE_DIRS:
        html_file = root / mod / "code.html"
        if attach_bridge(html_file):
            attached += 1
            print(f"[OK] Attached bridge to {mod}/code.html")
        else:
            print(f"[WARN] File not found: {html_file}")
    print(f"Completed: {attached}/{len(MODULE_DIRS)} modules connected.")


if __name__ == "__main__":
    main()
