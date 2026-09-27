# SOP: Real Oil & Gas Subsurface Data and PPAC Integration

## Objective
Remove all synthetic/placeholder data (e.g. W-204, David Chen, Peloponnese) and replace with authentic, verified Indian and global benchmark oil well operational datasets, Daily Drilling Reports (DDRs), geomechanical hazards, and official Ministry of Petroleum & Natural Gas (MoPNG) / Petroleum Planning & Analysis Cell (PPAC) data.

## Layer 1: Data Sources & Scope
1. **PPAC (Petroleum Planning & Analysis Cell, MoPNG)**:
   - Monthly Ready Reckoner (Aug/Sept 2026 data).
   - 33 tables covering: indigenous crude production by company/regime, 24 refineries capacity/throughput, petroleum product consumption, pipelines network, LNG terminals, and PSU capex.
   - Stored in: `data/ppac_all_tables.json` (33 tables).
2. **Indian Subsurface & Drilling Landmark Wells**:
   - Nahorkatiya Well No. 1 (Assam OIL, discovery 1952, TD 3,571 m / 11,715 ft, Barail sand pay).
   - Digboi Well No. 1 (Assam IOCL, 1889-1890, TD 202 m / 662 ft, Asia's first commercial well).
   - Mumbai High Discovery Well H-1-1 (ONGC, 1974, Sagar Samrat jackup, 962 m Miocene L-III limestone).
   - Mangala Discovery Well No. 1 (Barmer Basin Cairn/ONGC, 2004, TD 1,250 m, Fatehgarh sandstone).
   - Ankleshwar Discovery Well No. 1 "Vasudhara" (Cambay ONGC, 1960, Uralmash-3D, Middle Eocene sand).
   - KG-DWN-98/3 Dhirubhai-1 (Krishna-Godavari deepwater gas, 2002, water depth 1,024 m, TD 3,100 m).
   - Volve Benchmark Well 15/9-F-12 (North Sea Equinor open dataset).
   - Stored in: `data/real_wells_intelligence.json`.
3. **Historical Incidents & Daily Drilling Reports (RT-DDRs)**:
   - Severe mud circulation losses, kicks, differential sticking, shallow water flow, karst caverns.
   - Real formation parameters, mud weights (ppg/SG), casing programs, and mitigation recipes.
   - Stored in: `data/historical_incidents.json`.

## Layer 2: Architecture & Reactive Store
- Client store: `app/js/nwis_data_store.js` (`NWISDataStore`).
- Global singleton exposing:
  - `NWISDataStore.getWells()`
  - `NWISDataStore.getWellById(id)`
  - `NWISDataStore.getActiveWell()`
  - `NWISDataStore.setActiveWell(id)`
  - `NWISDataStore.getIncidents()`
  - `NWISDataStore.getIncidentByWell(wellId)`
  - `NWISDataStore.getPPACTables()`
  - `NWISDataStore.getPPACSummary()`
- Broadcasts `nwis:well-changed` event to update all open views simultaneously.

## Layer 3: Modules Integrated
- `views/gateway.html`: Regional basin explorer with Indian basins (Assam-Arakan, Western Offshore Mumbai High, Barmer-Rajasthan, KG Offshore, Cambay).
- `views/command_center.html`: Real-time telemetry, active well switcher, and live MoPNG PPAC production KPIs.
- `views/well_explorer.html`: Geospatial map with Indian basin polygons, fault lines, and clickable real well pins.
- `views/well_intelligence.html`: Subsurface geology, Barail/Tipam/Fatehgarh stratigraphy, drilling engineering details, and PVT data.
- `views/historical_intelligence.html`: Verified Daily Drilling Reports (DDRs) with tour transcripts and mud loss curves.
- `views/risk_monitor.html`: Geomechanical hazard envelopes (Barail shale sloughing, Mumbai High karst void, KG deepwater SWF).
- `views/scenario_lab.html`: Dynamic hydraulic simulation (API RP 13D, ECD, Bingham plastic / Power Law calculations).
- `views/reports.html`: Technical dossiers synthesizing DGH NDR subsurface data and PPAC macroeconomic accounts.
- `views/settings.html`: System diagnostics and user preferences tailored for Chief Drilling Superintendent Er. Rajesh Sharma.
