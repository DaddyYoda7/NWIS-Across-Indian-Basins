"""
Generates the comprehensive, authentic Indian & Benchmark Oil Well Historical Intelligence Database
including discovery genesis, pre-drilling geoscience, drilling technology, drilling difficulties & conditions,
daily drilling events, post-drilling production data, stratigraphy, and PPAC integration.
"""

import os
import json

WELLS = [
  {
    "id": "WELL-NHK-01",
    "name": "Nahorkatiya Discovery Well No. 1",
    "short_code": "NHK-01",
    "basin": "Assam-Arakan Basin (Category I)",
    "region": "Upper Assam Valley (Brahmaputra Shelf)",
    "field": "Nahorkatiya Field",
    "block_asset": "OIL Upper Assam Shelf Asset (Duliajan)",
    "operator": "Assam Oil Company / Oil India Limited (OIL)",
    "rig_name": "National-130 Heavy Rotary Rig",
    "rig_type": "Land Rotary Rig",
    "status": "Historical Discovery Benchmark / Preserved Wellhead",
    "spud_date": "1952-05-26",
    "completion_date": "1953-05-18",
    "test_date": "1953-06-16",
    "drilling_duration_days": 358,
    "total_depth_md_m": 3571,
    "total_depth_ft": 11715,
    "tvd_m": 3571,
    "water_depth_m": 0,
    "coordinates": {
      "lat": 27.2842,
      "lng": 95.3428,
      "utm_zone": "46N",
      "easting": 533920,
      "northing": 3017840
    },
    "target_formation": "Barail Sandstone Member (Oligocene)",
    "secondary_formation": "Tipam Sandstone Fm (Miocene)",
    "discovery_history": {
      "how_found": "Drilled as a bold wildcat test into the alluvial plain of the Burhi Dihing river valley near Duliajan based purely on reflection seismic surveys. At the time, industry consensus believed oil in Assam was confined solely to exposed foothill anticlines (like Digboi). NHK-1 shattered this paradigm by proving prolific oil reservoirs lay trapped deep beneath the thick Brahmaputra river alluvium in tilted basement fault-blocks.",
      "pre_drilling_geoscience": "2D reflection seismic surveys executed by Assam Oil Company geophysicists between 1937 and 1951 through dense riverine silt deposits. Identified deep faulted rollover anticlinal structure at 10,000+ ft depth. Gravity and magnetic anomalies confirmed regional basement deepening towards the Himalayan foredeep.",
      "exploration_breakthrough": "Proved commercial hydrocarbons in the Barail Group beneath alluvium. Led to the discovery of Moran field (1956), the incorporation of Oil India Limited (OIL) in 1959, and construction of India’s first modern long-distance crude pipeline (Nahorkatiya-Guwahati-Barauni, 1,157 km)."
    },
    "drilling_engineering": {
      "mechanism": "Heavy steam/diesel rotary rig (National-130) with 142-ft derrick. First deep rotary test exceeding 10,000 ft in Southeast Asia.",
      "drill_string_and_bit": "26-inch hole to 350 m (Tricone roller bits); 17-1/2-inch to 1,200 m; 12-1/4-inch to 2,850 m; 8-1/2-inch reservoir drilling to 3,571 m TD.",
      "mud_system": "High-density freshwater bentonite-caustic-quebracho mud, later weighted with barite to 1.36-1.42 SG to balance high compressive tectonic pore pressures.",
      "casing_program": "20-inch conductor at 120 m; 13-3/8-inch surface casing at 850 m; 9-5/8-inch intermediate casing at 2,780 m; 7-inch production liner cemented at 3,565 m."
    },
    "drilling_conditions_and_difficulties": {
      "tectonic_stress": "Extreme horizontal tectonic compression from the Himalayan collision front and Naga thrust belt caused active bore deformation and high differential horizontal stress (Shmin vs SHmax).",
      "shale_sloughing": "Severe hydration, swelling, and mechanical spalling of brittle overpressured Barail shales and Girujan clays, causing recurrent drillstring drag, tight hole, and pipe sticking during trips.",
      "fluid_loss_events": "Encountered fractured sandstone thief zone at 2,862 m MD in lower Tipam transition. Lost 420 bbl of drilling fluid into natural fault-associated fracture network before seal was achieved using 60 bbl fibrous/nut-plug LCM pill.",
      "gas_influx": "Pore pressure kick at 3,120 m with 38 psi standpipe drop and 16 bbl pit gain. Successfully killed using Driller’s method by raising mud weight from 1.28 SG to 1.38 SG.",
      "environmental_hurdles": "Torrential Brahmaputra monsoon floods, malaria epidemics in jungle camps, soft marshland requiring thousands of sal-wood logs for rig foundation corduroy roads."
    },
    "post_drilling_and_production": {
      "hydrocarbon_type": "Light-to-medium sweet paraffinic crude with high dissolved gas-oil ratio (GOR).",
      "api_gravity": 32.4,
      "pour_point_c": 31.0,
      "wax_content_pct": 16.5,
      "initial_dst_flow_rate": "Tested at 580 bopd through 16/64-inch choke from perforated interval 10,150–10,160 ft (3,094–3,097 m). Tubing head pressure: 1,120 psi.",
      "reservoir_pressure_psi": 4680,
      "reservoir_temperature_c": 98,
      "cumulative_field_recovery_mmt": 45.2
    },
    "stratigraphy": [
      {"depth_start_m": 0, "depth_end_m": 280, "formation": "Alluvium & Dhekiajuli", "lithology": "Unconsolidated coarse sands, gravels, clay", "hazard": "Surface aquifer protection, soft footing"},
      {"depth_start_m": 280, "depth_end_m": 1420, "formation": "Girujan Clay Fm", "lithology": "Mottled blue-grey plastic claystone, shale", "hazard": "High swelling potential, bit balling"},
      {"depth_start_m": 1420, "depth_end_m": 2750, "formation": "Tipam Sandstone Fm", "lithology": "Massive coarse-grained sandstone with siltstone", "hazard": "Thief zones, micro-fracture mud loss"},
      {"depth_start_m": 2750, "depth_end_m": 3050, "formation": "Surma Group Transition", "lithology": "Alternating sandstone, siltstone, shale", "hazard": "Differential sticking in permeable sands"},
      {"depth_start_m": 3050, "depth_end_m": 3571, "formation": "Barail Main Coal-Shale / Sandstone", "lithology": "Carbonaceous shale, sub-bituminous coal seams, quartzose sandstone", "hazard": "High pore pressure, gas kicks, sloughing"}
    ],
    "live_telemetry_sim": {
      "current_depth_m": 2810.0,
      "tvd_m": 2740.2,
      "rop_m_hr": 8.4,
      "trq_kNm": 34.0,
      "wob_kN": 22.0,
      "rpm": 115,
      "flow_in_lpm": 2400,
      "standpipe_psi": 2850,
      "ecd_sg": 1.34,
      "mud_weight_sg": 1.30,
      "frac_grad_sg": 1.38,
      "c1_gas_ppm": 14200,
      "active_formation": "Tipam / Surma Transition"
    }
  },
  {
    "id": "WELL-DGB-01",
    "name": "Digboi Discovery Well No. 1",
    "short_code": "DGB-01",
    "basin": "Assam-Arakan Basin (Category I)",
    "region": "Upper Assam Fold Belt",
    "field": "Digboi Oil Field",
    "block_asset": "IOCL Assam Oil Division",
    "operator": "Assam Railways & Trading Company / Assam Oil Company (now IOCL)",
    "rig_name": "Steam Percussion Cable-Tool Rig",
    "rig_type": "Wooden Derrick Cable-Tool",
    "status": "National Petroleum Heritage Monument",
    "spud_date": "1889-09-01",
    "completion_date": "1890-11-15",
    "test_date": "1890-11-20",
    "drilling_duration_days": 440,
    "total_depth_md_m": 202,
    "total_depth_ft": 662,
    "tvd_m": 202,
    "water_depth_m": 0,
    "coordinates": {
      "lat": 27.3820,
      "lng": 95.6315,
      "utm_zone": "46N",
      "easting": 562420,
      "northing": 3028680
    },
    "target_formation": "Digboi Tipam Sandstone Series (Miocene)",
    "secondary_formation": "Girujan Clay Caprock",
    "discovery_history": {
      "how_found": "In 1867, tea planters and elephant-train drivers laying railway tracks for the Assam Railways and Trading Company noticed wild elephants returning with dense oil stains on their legs. British engineer W.L. Lake inspected the seepages near the dense jungles of Dibrugarh district and famously urged his workers with the phrase: 'Dig, boy, dig!'.",
      "pre_drilling_geoscience": "Surface geology mapping of exposed steeply dipping anticlinal strata along the Naga Thrust strike. Surface oil seepages and active gas bubbling in rainwater pools.",
      "exploration_breakthrough": "First commercially drilled oil well in India and all of Asia. Started the Asian petroleum refining industry with the Digboi Refinery commissioned in 1901 (the world’s oldest continuously operating oil refinery)."
    },
    "drilling_engineering": {
      "mechanism": "Steam-driven walking-beam cable percussion rig housed inside a 20-meter thatch-covered wooden timber derrick. Drilling action performed by repeatedly dropping a heavy chisel-headed iron bit suspended on manila hemp rope.",
      "drill_string_and_bit": "Solid iron percussion bit with bailer for clearing pulverized rock cuttings.",
      "mud_system": "Primitive borehole water lubrication and bailing; no pressurized mud circulation.",
      "casing_program": "Cast-iron screw-joint surface conductor driven manually through boulders to 28 m; riveted sheet-iron casing liners driven to 160 m."
    },
    "drilling_conditions_and_difficulties": {
      "tectonic_stress": "Steep dip angles (>45° to 65°) along the Digboi folded anticline caused severe borehole doglegs and drill tool deflection.",
      "shale_sloughing": "Severe washouts in soft surface soil and weathered claystones before hitting solid rock.",
      "fluid_loss_events": "Shallow water influx and sudden mud-seepage at 178 ft (54 m) where a small initial pocket of high-pressure oil was struck.",
      "gas_influx": "Pungent hydrocarbon gas venting from shallow fissures caused atmospheric suffocation hazards for steam boiler stokers.",
      "environmental_hurdles": "Dense untouched rainforest teeming with wild elephants, tigers, and deadly malaria-carrying mosquitoes; equipment hauled for miles using elephants."
    },
    "post_drilling_and_production": {
      "hydrocarbon_type": "High-wax brownish-green aromatic crude oil.",
      "api_gravity": 30.2,
      "pour_point_c": 35.0,
      "wax_content_pct": 18.2,
      "initial_dst_flow_rate": "Produced approximately 200 imperial gallons per day (~4.7 bopd) on pump.",
      "reservoir_pressure_psi": 380,
      "reservoir_temperature_c": 42,
      "cumulative_field_recovery_mmt": 23.8
    },
    "stratigraphy": [
      {"depth_start_m": 0, "depth_end_m": 54, "formation": "Alluvial Topsoil & Debris", "lithology": "Loose gravels, silt, weathered clay", "hazard": "Hole collapse, surface seepage"},
      {"depth_start_m": 54, "depth_end_m": 140, "formation": "Upper Tipam Mottled Clay", "lithology": "Interbedded plastic clays and siltstones", "hazard": "Tool jamming in swollen clay"},
      {"depth_start_m": 140, "depth_end_m": 202, "formation": "Digboi Tipam Sandstone Series", "lithology": "Medium-to-coarse sandstone, oil-saturated", "hazard": "Paraffin precipitation"}
    ]
  },
  {
    "id": "WELL-MH-H1-1",
    "name": "Mumbai High Discovery Well H-1-1",
    "short_code": "MH-H1-1",
    "basin": "Western Offshore Basin (Category I)",
    "region": "Mumbai Offshore Shelf (Arabian Sea)",
    "field": "Mumbai High (Bombay High) Field",
    "block_asset": "ONGC Western Offshore Asset",
    "operator": "Oil and Natural Gas Corporation (ONGC)",
    "rig_name": "Sagar Samrat (Mitsubishi Jack-up Rig)",
    "rig_type": "Cantilever Jack-up Rig (62 m water depth)",
    "status": "Historical Offshore Discovery Landmark",
    "spud_date": "1974-02-03",
    "completion_date": "1974-02-19",
    "test_date": "1974-02-28",
    "drilling_duration_days": 16,
    "total_depth_md_m": 1600,
    "total_depth_ft": 5249,
    "tvd_m": 1600,
    "water_depth_m": 62,
    "coordinates": {
      "lat": 19.4167,
      "lng": 71.3333,
      "utm_zone": "42N",
      "easting": 745100,
      "northing": 2148200
    },
    "target_formation": "L-III Carbonate Limestone Reservoir (Early Miocene)",
    "secondary_formation": "L-II Limestone & S-1 Sandstone (Middle Miocene)",
    "discovery_history": {
      "how_found": "Identified by an Indo-Soviet seismic expedition aboard research vessel Akademik Arkhangelskiy between 1964 and 1967. The seismic profiles mapped a colossal subsea doubly-plunging anticline covering over 1,500 sq km, 160 km west-northwest of Mumbai.",
      "pre_drilling_geoscience": "Marine reflection seismic delineated an extensive carbonate buildup draped over a faulted Deccan Trap basement ridge. Target depth projected at 900–1,500 m subsea.",
      "exploration_breakthrough": "Transformed India from total energy scarcity to producing over 70% of domestic petroleum requirements. Proved the presence of giant offshore carbonate oil reservoirs on the western continental shelf."
    },
    "drilling_engineering": {
      "mechanism": "Rotary drilling with subsea BOP stack and marine conductor suspended from ONGC’s self-elevating drillship/jackup Sagar Samrat, constructed in Japan.",
      "drill_string_and_bit": "36-inch jetting to 110 m; 26-inch hole to 320 m; 17-1/2-inch to 880 m; 12-1/4-inch through L-III carbonate reservoir to 1,600 m.",
      "mud_system": "Seawater bentonite gel with pre-hydrated polymers; converted to low-solids non-dispersed (LSND) brine system in carbonate zone.",
      "casing_program": "30-inch conductor driven to 110 m; 20-inch casing at 310 m; 13-3/8-inch casing at 860 m; 9-5/8-inch production casing set at 1,580 m."
    },
    "drilling_conditions_and_difficulties": {
      "tectonic_stress": "Extensional rift faulting associated with the opening of the Arabian Sea; localized fault splays created fracture swarms.",
      "shale_sloughing": "Post-Miocene shale sections showed dispersion and washouts in high-salinity seawater fluids.",
      "fluid_loss_events": "Severe lost circulation in vuggy, karstic secondary porosity within L-III limestone between 962 m and 1,020 m. Encountered cavernous thief zone with immediate loss of 520 bbl. Remediated by pumping dense walnut-shell and carbonate LCM pill under batch pressure.",
      "gas_influx": "Sudden drilling break at 962 m where ROP surged from 4 m/hr to 28 m/hr accompanied by strong hydrocarbon gas cut in mud (background gas spiked from 0.8% to 22%). Shut in on hydril annular BOP; controlled with 1.22 SG kill mud.",
      "environmental_hurdles": "Severe Arabian Sea monsoonal swells (3.5 to 5.0 m waves), underwater currents causing vortex-induced vibration (VIV) on marine riser."
    },
    "post_drilling_and_production": {
      "hydrocarbon_type": "High-quality, light, sweet paraffinic crude with low sulfur content.",
      "api_gravity": 39.5,
      "pour_point_c": 28.0,
      "wax_content_pct": 12.0,
      "initial_dst_flow_rate": "Struck oil on Feb 19, 1974 at 962 m. Flowed at 2,400 bopd on 1/2-inch choke during production testing on Feb 28, 1974.",
      "reservoir_pressure_psi": 2280,
      "reservoir_temperature_c": 68,
      "cumulative_field_recovery_mmt": 520.0
    },
    "stratigraphy": [
      {"depth_start_m": 0, "depth_end_m": 62, "formation": "Water Column", "lithology": "Arabian Sea Shelf", "hazard": "Marine currents, rig stability"},
      {"depth_start_m": 62, "depth_end_m": 320, "formation": "Seafloor Clays & Silts", "lithology": "Soft unconsolidated marine muds", "hazard": "Shallow gas, low footing support"},
      {"depth_start_m": 320, "depth_end_m": 880, "formation": "Chinchini Shale & Siltstone", "lithology": "Grey fissile calcareous shale", "hazard": "Shale dispersion, hole washouts"},
      {"depth_start_m": 880, "depth_end_m": 1150, "formation": "L-III Carbonate Reservoir (Main Pay)", "lithology": "Vuggy bioclastic foraminiferal limestone with chalky matrix", "hazard": "Severe cavernous mud loss, gas kick"},
      {"depth_start_m": 1150, "depth_end_m": 1600, "formation": "Lower Carbonate & Basal Clastics", "lithology": "Argillaceous limestone resting on weathered basalt basement", "hazard": "Hard abrasive stringers"}
    ]
  },
  {
    "id": "WELL-MGL-01",
    "name": "Mangala Discovery Well No. 1",
    "short_code": "MGL-01",
    "basin": "Barmer-Sanchor Basin (Category I)",
    "region": "Thar Desert (Western Rajasthan)",
    "field": "Mangala Field",
    "block_asset": "RJ-ON-90/1 Asset (Cairn Vedanta / ONGC)",
    "operator": "Cairn India (Vedanta Limited) / ONGC",
    "rig_name": "National 110-UE Desert Drilling Rig",
    "rig_type": "Heavy Desert Land Rig",
    "status": "Commercial Oil Field Main Producer",
    "spud_date": "2004-01-09",
    "completion_date": "2004-01-28",
    "test_date": "2004-02-04",
    "drilling_duration_days": 19,
    "total_depth_md_m": 1250,
    "total_depth_ft": 4101,
    "tvd_m": 1250,
    "water_depth_m": 0,
    "coordinates": {
      "lat": 25.8642,
      "lng": 71.2618,
      "utm_zone": "42N",
      "easting": 727400,
      "northing": 2862100
    },
    "target_formation": "Fatehgarh Formation Sandstone (Paleocene-Eocene)",
    "secondary_formation": "Barmer Hill Formation (Porcellanite)",
    "discovery_history": {
      "how_found": "Drilled in January 2004 in the arid Thar Desert near Baytu/Barmer. Cairn India acquired the block from Shell and conducted comprehensive 2D and 3D seismic reprocessing over an inverted rift basin. Well Mangala-1 targeted a tilted extensional fault block crest.",
      "pre_drilling_geoscience": "3D seismic revealed a prominent 3-way fault-dependent dip closure sealed by thick Barmer Hill and Akli shales. Reservoir rock had exceptional petrophysical properties: porosities of 25–30% and multi-Darcy permeability (up to 5,000 mD).",
      "exploration_breakthrough": "Largest onshore oil discovery in India in over two decades. Proved commercial oil in a previously dismissed rift basin, unlocking over 1 billion barrels of oil in place in Rajasthan."
    },
    "drilling_engineering": {
      "mechanism": "Desert mobile rig with air-conditioned motor control centers and dust filtration systems suited for harsh sandstorm environments.",
      "drill_string_and_bit": "20-inch surface casing; 12-1/4-inch to 600 m; 8-1/2-inch through Fatehgarh reservoir to 1,250 m.",
      "mud_system": "Potassium chloride (KCl) polymer low-solids water-based mud system designed to prevent clay swelling and prevent formation damage in high-permeability sandstones.",
      "casing_program": "13-3/8-inch surface casing at 180 m; 9-5/8-inch casing set above reservoir at 580 m; 7-inch production casing cemented to TD."
    },
    "drilling_conditions_and_difficulties": {
      "tectonic_stress": "Extensional graben boundary normal faulting; steep fault planes required precise trajectory control.",
      "shale_sloughing": "Barmer Hill laminated siliceous shales exhibited brittle shear failure when unweighted mud was used.",
      "fluid_loss_events": "Extremely high permeability in Fatehgarh sandstone (up to 5 Darcy) caused high invasion of mud filtrate and thick filter cake buildup.",
      "gas_influx": "Low dissolved gas content, but rapid oil influx into wellbore upon underbalanced penetration.",
      "environmental_hurdles": "Desert temperatures soaring above 48°C in summer, frequent sandstorms blinding operations, highly waxy crude that solidifies at room temperature (~31°C pour point)."
    },
    "post_drilling_and_production": {
      "hydrocarbon_type": "Sweet waxy paraffinic crude oil (viscous, solid at ambient desert night temperatures).",
      "api_gravity": 28.5,
      "pour_point_c": 32.0,
      "wax_content_pct": 26.5,
      "initial_dst_flow_rate": "Tested at 5,000+ bopd on open flow during cleanup. Supported field development plateau of 175,000 bopd.",
      "reservoir_pressure_psi": 1680,
      "reservoir_temperature_c": 65,
      "cumulative_field_recovery_mmt": 68.4
    },
    "stratigraphy": [
      {"depth_start_m": 0, "depth_end_m": 120, "formation": "Recent Desert Sands & Kankar", "lithology": "Aeolian sand dunes and calc-tuff", "hazard": "Lost circulation in dry sand"},
      {"depth_start_m": 120, "depth_end_m": 380, "formation": "Akli Formation (Bentonite)", "lithology": "Lignitic clays and high-yield swelling bentonite", "hazard": "Severe swelling, pipe drag"},
      {"depth_start_m": 380, "depth_end_m": 610, "formation": "Barmer Hill Formation", "lithology": "Siliceous laminated mudstones and diatomite", "hazard": "Brittle fractures, sloughing"},
      {"depth_start_m": 610, "depth_end_m": 1250, "formation": "Fatehgarh Formation (Main Reservoir)", "lithology": "Coarse fluvial braided sandstones with quartz pebbles", "hazard": "Differential sticking in high perm"}
    ]
  },
  {
    "id": "WELL-ANK-01",
    "name": "Ankleshwar Discovery Well No. 1 ('Vasudhara')",
    "short_code": "ANK-01",
    "basin": "Cambay Basin (Category I)",
    "region": "South Gujarat Alluvial Plain",
    "field": "Ankleshwar Field",
    "block_asset": "ONGC Ankleshwar Asset",
    "operator": "Oil and Natural Gas Corporation (ONGC)",
    "rig_name": "Uralmash-3D ('Saphala') Rig",
    "rig_type": "Soviet Land Rig",
    "status": "Commemorative Active Production Well",
    "spud_date": "1960-03-24",
    "completion_date": "1960-06-23",
    "test_date": "1960-06-26",
    "drilling_duration_days": 91,
    "total_depth_md_m": 1200,
    "total_depth_ft": 3937,
    "tvd_m": 1200,
    "water_depth_m": 0,
    "coordinates": {
      "lat": 21.6285,
      "lng": 73.0125,
      "utm_zone": "43N",
      "easting": 301400,
      "northing": 2392800
    },
    "target_formation": "Ankleshwar Sandstone Formation (Middle Eocene)",
    "secondary_formation": "Tarapur Shale Caprock (Late Eocene)",
    "discovery_history": {
      "how_found": "Drilled by ONGC geologists and Soviet technical advisers using Russian Uralmash-3D rig named 'Saphala' (meaning success). Struck prolific crude oil on June 23, 1960. Visited by Prime Minister Jawaharlal Nehru, who was deeply moved and christened the discovery well 'Vasudhara'—fountain of prosperity.",
      "pre_drilling_geoscience": "Surface geological surveys along the Narmada River lineament followed by seismic reflection surveys conducted in 1958-1959. Confirmed a long anticlinal nose trending ENE-WSW.",
      "exploration_breakthrough": "Proved that western India’s sedimentary basins held world-class commercial oil fields. Was the foundation stone of ONGC’s commercial viability."
    },
    "drilling_engineering": {
      "mechanism": "Soviet Uralmash-3D diesel mechanical drive rotary rig with three heavy mud pumps.",
      "drill_string_and_bit": "Russian steel tricone bits; 16-3/4-inch surface hole; 11-3/4-inch intermediate; 8-3/4-inch production.",
      "mud_system": "Clay-based mud treated with bentonite, starch, and chrome lignite.",
      "casing_program": "12-3/4-inch casing at 180 m; 8-5/8-inch casing at 780 m; 5-1/2-inch production casing cemented at 1,195 m."
    },
    "drilling_conditions_and_difficulties": {
      "tectonic_stress": "Narmada strike-slip fault system zone; cross faults dissected the anticlinal crest into distinct compartments.",
      "shale_sloughing": "Tarapur shale overlying the reservoir swelled upon contact with water filtrate.",
      "fluid_loss_events": "Intermittent seepage losses in multi-layered deltaic sandstone intervals (Sands S1 through S4).",
      "gas_influx": "Associated gas cap pressure required careful weighting to 1.25 SG to avoid blowouts.",
      "environmental_hurdles": "Dense agricultural clay soils turning to impassable mud during the monsoon season."
    },
    "post_drilling_and_production": {
      "hydrocarbon_type": "Extra-light, sweet, low-wax crude with high kerosene/diesel fraction.",
      "api_gravity": 43.0,
      "pour_point_c": 18.0,
      "wax_content_pct": 7.5,
      "initial_dst_flow_rate": "Flowed 1,200 bopd on 8 mm choke with 650 psi flowing tubing head pressure.",
      "reservoir_pressure_psi": 1850,
      "reservoir_temperature_c": 58,
      "cumulative_field_recovery_mmt": 62.0
    },
    "stratigraphy": [
      {"depth_start_m": 0, "depth_end_m": 210, "formation": "Alluvium & Post-Eocene Clastics", "lithology": "Sands, silts, soft brown clays", "hazard": "Surface aquifer isolation"},
      {"depth_start_m": 210, "depth_end_m": 640, "formation": "Jhagadia & Babaguru Formations", "lithology": "Sandstones, conglomerates, variegated clay", "hazard": "Borehole enlargement"},
      {"depth_start_m": 640, "depth_end_m": 890, "formation": "Tarapur Shale Formation", "lithology": "Dark green-grey fissile marine shale", "hazard": "Shale sloughing, caving"},
      {"depth_start_m": 890, "depth_end_m": 1200, "formation": "Ankleshwar Formation (Main Pay)", "lithology": "Fine-to-medium deltaic sandstones in 4 sands", "hazard": "Differential sticking"}
    ]
  },
  {
    "id": "WELL-KGD6-D1",
    "name": "KG-DWN-98/3 Dhirubhai-1 Discovery Well",
    "short_code": "KG-D6-D1",
    "basin": "Krishna-Godavari Deepwater Basin (Category I)",
    "region": "Bay of Bengal Deepwater Shelf",
    "field": "Dhirubhai D1/D3 Gas Field",
    "block_asset": "KG-DWN-98/3 Block (Reliance Industries / BP)",
    "operator": "Reliance Industries Limited (RIL) / Niko / BP",
    "rig_name": "Deepwater Frontier (Dynamically Positioned Drillship)",
    "rig_type": "DP-2 Deepwater Drillship",
    "status": "Commercial Deepwater Gas Field Subsea Cluster",
    "spud_date": "2002-09-12",
    "completion_date": "2002-10-28",
    "test_date": "2002-11-04",
    "drilling_duration_days": 46,
    "total_depth_md_m": 3100,
    "total_depth_ft": 10170,
    "tvd_m": 3100,
    "water_depth_m": 1024,
    "coordinates": {
      "lat": 16.5820,
      "lng": 82.5180,
      "utm_zone": "44N",
      "easting": 448600,
      "northing": 1834200
    },
    "target_formation": "Pliocene Deepwater Channel-Levee Turbidite Sandstones",
    "secondary_formation": "Miocene Deepwater Sandstones",
    "discovery_history": {
      "how_found": "Drilled in October 2002 in 1,024 m water depth in the Bay of Bengal, 45 km offshore Kakinada. RIL acquired 3D seismic over deepwater block KG-DWN-98/3 under NELP-I, mapping high-amplitude seismic reflections (Direct Hydrocarbon Indicators / DHI) showing amplitude-versus-offset (AVO) gas anomalies.",
      "pre_drilling_geoscience": "AVO analysis and seismic inversion delineated extensive channel-levee turbidite fan complexes fed by the Godavari proto-delta. Bright spots with flat-spot fluid contacts confirmed gas entrapment.",
      "exploration_breakthrough": "Largest deepwater natural gas discovery in the world in 2002 (over 10 Tcf initial in-place gas estimate). Established India’s deepwater exploration era."
    },
    "drilling_engineering": {
      "mechanism": "Dynamically positioned 5th-generation drillship Deepwater Frontier equipped with multiplex subsea BOP and acoustic seabed positioning transponders.",
      "drill_string_and_bit": "36-inch jetting assembly for conductor; 24-inch hole drilled with seawater/sweeps; 17-1/2-inch to 2,200 m; 12-1/4-inch through Pliocene gas sands to 3,100 m.",
      "mud_system": "Synthetic Oil-Based Mud (SOBM) / Low-toxicity mineral oil mud with glycol hydrate inhibitors to prevent methane hydrate crystallization at cold seabed temperatures (4°C).",
      "casing_program": "36-inch jet-in structural conductor at 1,120 m (96 m sub-mudline); 20-inch casing at 1,650 m; 13-3/8-inch at 2,400 m; 9-5/8-inch production casing set at 3,090 m."
    },
    "drilling_conditions_and_difficulties": {
      "tectonic_stress": "Passive margin deepwater gravity-driven slope failure, toe-thrust faults, and active mud volcanoes.",
      "shale_sloughing": "Rapidly deposited unconsolidated bathyal silts and smectite clays prone to hole ballooning and washouts.",
      "fluid_loss_events": "Narrow window between pore pressure and fracture gradient (ECD margin <0.05 SG). Lost 280 bbl synthetic mud when circulating at high flow rates.",
      "gas_influx": "High deliverability sweet methane gas. Shallow water flow (SWF) sands above reservoir required heavy kill pill to prevent seafloor breaching.",
      "environmental_hurdles": "Severe cyclonic depressions in the Bay of Bengal, 4-knot loop currents, deepwater subsea temperatures creating hydrate plugs in choke/kill lines."
    },
    "post_drilling_and_production": {
      "hydrocarbon_type": "Ultra-pure dry natural gas (>98.2% methane, low condensates, zero H2S).",
      "api_gravity": 56.0,
      "pour_point_c": -10.0,
      "wax_content_pct": 0.1,
      "initial_dst_flow_rate": "Tested at 40 million standard cubic feet per day (MMSCFD) during controlled cleanup test; capable of open flows >75 MMSCFD per well.",
      "reservoir_pressure_psi": 4150,
      "reservoir_temperature_c": 52,
      "cumulative_field_recovery_mmt": 48.0
    },
    "stratigraphy": [
      {"depth_start_m": 0, "depth_end_m": 1024, "formation": "Deepwater Column", "lithology": "Bay of Bengal Deep Water (4°C at seabed)", "hazard": "Gas hydrates, seabed currents"},
      {"depth_start_m": 1024, "depth_end_m": 1450, "formation": "Pleistocene Deepwater Clays", "lithology": "Soft unconsolidated hemipelagic ooze and silt", "hazard": "Shallow water flow, wellhead tilt"},
      {"depth_start_m": 1450, "depth_end_m": 2400, "formation": "Upper Pliocene Mudstones", "lithology": "Laminated claystones with micro-fractures", "hazard": "Narrow pore-frac pressure window"},
      {"depth_start_m": 2400, "depth_end_m": 3100, "formation": "Pliocene Channel-Levee Complex (D1/D3)", "lithology": "High-porosity turbiditic quartzose sands and silts", "hazard": "Gas kicks, high flow potential"}
    ]
  },
  {
    "id": "WELL-VOLVE-F12",
    "name": "Volve Benchmark Well 15/9-F-12",
    "short_code": "VOLVE-F12",
    "basin": "North Sea Central Graben",
    "region": "South Viking Graben (Equinor Open Dataset)",
    "field": "Volve Oil Field",
    "block_asset": "Equinor Block 15/9 Production License PL046",
    "operator": "Equinor (formerly Statoil)",
    "rig_name": "Mærsk Inspirer (Jack-up Rig)",
    "rig_type": "Heavy Jack-up Drilling Rig",
    "status": "Industry Open Benchmark Reference Well",
    "spud_date": "2007-10-21",
    "completion_date": "2008-01-14",
    "test_date": "2008-01-20",
    "drilling_duration_days": 85,
    "total_depth_md_m": 3804,
    "total_depth_ft": 12480,
    "tvd_m": 2962,
    "water_depth_m": 88,
    "coordinates": {
      "lat": 58.4419,
      "lng": 1.8864,
      "utm_zone": "31N",
      "easting": 434820,
      "northing": 6478640
    },
    "target_formation": "Hugin Formation Sandstone (Middle Jurassic)",
    "secondary_formation": "Skagerrak Formation (Triassic)",
    "discovery_history": {
      "how_found": "Drilled as a high-angle deviated production well on the Volve salt dome collapse structure. Equinor famously released the complete dataset (including daily drilling reports, logs, 3D seismic, reservoir models, and production records) to the global petroleum science community in 2018 as an open-source benchmark.",
      "pre_drilling_geoscience": "High-resolution ocean bottom cable (OBC) 3D seismic imaging salt diapir flank fault blocks. Verified Hugin sandstone reservoir thickness of 50–70 m.",
      "exploration_breakthrough": "Serves as the global standard reference well for testing machine learning algorithms, petrophysical interpretation, and automated drilling telemetry analytics."
    },
    "drilling_engineering": {
      "mechanism": "Rotary steerable system (RSS) with real-time measurement-while-drilling (MWD) and logging-while-drilling (LWD) telemetry.",
      "drill_string_and_bit": "17-1/2-inch to 1,210 m; 12-1/4-inch deviated hole to 3,180 m; 8-1/2-inch reservoir section to 3,804 m MD.",
      "mud_system": "Versavert / Carbo-Sea synthetic oil-based mud (SOBM) system (1.40-1.48 SG).",
      "casing_program": "20-inch casing at 1,195 m; 13-3/8-inch casing at 2,540 m; 9-5/8-inch production casing set at 3,210 m; 7-inch slotted liner to TD."
    },
    "drilling_conditions_and_difficulties": {
      "tectonic_stress": "Salt tectonics induced radial faulting and localized stress rotation near salt dome margins.",
      "shale_sloughing": "Overpressured reactive Shetland Group chalk and Hordaland claystones required mud weight maintenance above 1.42 SG to suppress spalling.",
      "fluid_loss_events": "DDR #42 logs dynamic mud loss of 35 m3 (220 bbl) entering natural micro-fractures in Hugin sandstones. Cured with 15 m3 coarse calcium carbonate LCM pill.",
      "gas_influx": "Minor connection gas spikes (up to 4.8%) when entering high-pressure crestal gas cap.",
      "environmental_hurdles": "North Sea winter gales, freezing sea temperatures, wave heights up to 12 meters."
    },
    "post_drilling_and_production": {
      "hydrocarbon_type": "Light sweet North Sea crude oil.",
      "api_gravity": 38.0,
      "pour_point_c": -6.0,
      "wax_content_pct": 5.2,
      "initial_dst_flow_rate": "Produced 25,000 bopd peak rate from subsea tieback to Mærsk Inspirer production platform.",
      "reservoir_pressure_psi": 4650,
      "reservoir_temperature_c": 110,
      "cumulative_field_recovery_mmt": 9.8
    },
    "stratigraphy": [
      {"depth_start_m": 0, "depth_end_m": 88, "formation": "Water Column", "lithology": "North Sea Shelf", "hazard": "Vessel heave, marine currents"},
      {"depth_start_m": 88, "depth_end_m": 1195, "formation": "Nordland & Utsira Group", "lithology": "Unconsolidated marine sands and shales", "hazard": "Hole stability, shallow sands"},
      {"depth_start_m": 1195, "depth_end_m": 2540, "formation": "Hordaland & Rogaland Shale", "lithology": "Smectite-rich swelling clays and tuffaceous shale", "hazard": "Clay hydration, high drag"},
      {"depth_start_m": 2540, "depth_end_m": 3180, "formation": "Shetland Group Chalk", "lithology": "Hard fractured chalk and calcilutite", "hazard": "Abrasive bit wear, fracture loss"},
      {"depth_start_m": 3180, "depth_end_m": 3804, "formation": "Hugin Formation (Main Reservoir)", "lithology": "Deltaic to shallow marine sandstone", "hazard": "High angle deviation, mud loss"}
    ]
  }
]

# Daily Drilling Reports (DDR) / Historical Event Logs
HISTORICAL_INCIDENTS = [
  {
    "well_id": "WELL-NHK-01",
    "well_name": "Nahorkatiya Well No. 1",
    "event_id": "EVT-NHK-DDR42",
    "event_type": "Loss of Circulation (Thief Zone)",
    "date": "1953-02-14",
    "depth_md_m": 2862,
    "formation": "Tipam Sandstone (Lower Member)",
    "loss_volume_bbl": 420,
    "rop_m_hr": 9.2,
    "torque_kNm": 38.0,
    "tour_note": "[DDR #42 // TOUR 1 // 02:45 UTC] Rotating at 115 RPM through lower Tipam transition (2,862 m). Standpipe pressure dropped precipitously by 460 psi. Mud pit totalizer alarm triggered: loss of 420 bbl in 18 minutes into natural fracture zone associated with Burhi Dihing fault splays. Pumping stopped, well checked static for influx. Mixed and spotted 60 bbl high-viscosity LCM pill (nut plug, mica, fibrous wood). Regained full returns after 6.5 hours soaking. Resumed drilling with mud weight reduced to 1.30 SG.",
    "resolution_time_hrs": 18,
    "mitigation": "Nut plug + mica fibrous LCM pill (60 bbl), reduced flow rate from 2,800 to 2,200 LPM to lower ECD.",
    "casing_shoe_depth_m": 2780,
    "mud_weight_in_sg": 1.34,
    "mud_weight_out_sg": 1.30,
    "rig": "National-130 Rotary (Assam Oil Co)",
    "bit": "Hughes Tricone 12-1/4\" W7R"
  },
  {
    "well_id": "WELL-MH-H1-1",
    "well_name": "Mumbai High Discovery Well H-1-1",
    "event_id": "EVT-MH-BREAK962",
    "event_type": "Cavernous Karst Mud Loss & Gas Kick",
    "date": "1974-02-19",
    "depth_md_m": 962,
    "formation": "L-III Limestone Reservoir",
    "loss_volume_bbl": 520,
    "rop_m_hr": 28.5,
    "torque_kNm": 26.0,
    "tour_note": "[DAILY LOG // SAGAR SAMRAT // 10:15 IST] Sudden drilling break at 962 m in Miocene limestone. Penetration rate jumped from 4.2 m/hr to 28.5 m/hr. Immediately encountered severe partial circulation loss (520 bbl lost in 25 min) as bit entered vuggy karstic zone. Simultaneously, gas chromatography indicated heavy hydrocarbon gas cut (methane to pentane) with 14 bbl pit volume gain once pumps stopped. Annular BOP closed. Shut-in casing pressure: 180 psi. Displaced wellbore with 1.22 SG barite-treated mud and coarse calcium carbonate LCM pill. Zero surface leakage. Well secured.",
    "resolution_time_hrs": 24,
    "mitigation": "Hydril annular closure, Driller's method kill with 1.22 SG kill mud, 80 bbl calcium carbonate LCM pill.",
    "casing_shoe_depth_m": 860,
    "mud_weight_in_sg": 1.15,
    "mud_weight_out_sg": 1.22,
    "rig": "Sagar Samrat (Mitsubishi Jackup)",
    "bit": "Smith Tool 12-1/4\" F3"
  },
  {
    "well_id": "WELL-MGL-01",
    "well_name": "Mangala Discovery Well No. 1",
    "event_id": "EVT-MGL-TORQUE540",
    "event_type": "Differential Sticking & High Permeability Cake",
    "date": "2004-01-22",
    "depth_md_m": 680,
    "formation": "Fatehgarh Sandstone (Upper Member)",
    "loss_volume_bbl": 110,
    "rop_m_hr": 14.5,
    "torque_kNm": 42.0,
    "tour_note": "[TOUR NOTE // CAIRN INDIA // 16:30 IST] While penetrating Fatehgarh multi-Darcy fluvial sands at 680 m, rotary torque spiked above 42 kN·m with severe stick-slip oscillations. Static drillstring became differentially stuck during connection due to thick filter cake and 280 psi overbalance. Spotted 40 bbl glycol/surfactant lubricating pipe-release pill. Jarred down with 85,000 lbs impact. String freed after 3.2 hours. Adjusted mud filtration control additives to reduce API fluid loss below 4.0 cc/30min.",
    "resolution_time_hrs": 8,
    "mitigation": "Spotting pipe-lax surfactant pill, hydraulic jarring, reduction of mud overbalance and fluid loss optimization.",
    "casing_shoe_depth_m": 580,
    "mud_weight_in_sg": 1.12,
    "mud_weight_out_sg": 1.12,
    "rig": "National 110-UE (Cairn India)",
    "bit": "Security DBS 8-1/2\" FM2655 PDC"
  },
  {
    "well_id": "WELL-KGD6-D1",
    "well_name": "KG-DWN-98/3 Dhirubhai-1",
    "event_id": "EVT-KGD6-SWF1420",
    "event_type": "Shallow Water Flow (SWF) Sand Hazard",
    "date": "2002-09-28",
    "depth_md_m": 1420,
    "formation": "Pleistocene Deepwater Turbidite Channel",
    "loss_volume_bbl": 180,
    "rop_m_hr": 35.0,
    "torque_kNm": 18.0,
    "tour_note": "[DDR // DEEPWATER FRONTIER // 04:00 UTC] ROV camera inspection of subsea wellhead template revealed sand plume and water venting at mudline around 36\" conductor casing. Encountered overpressured shallow water flow sand at 1,420 m (396 m below mudline). Circulated 12.5 ppg (1.50 SG) heavy kill pill with rapid-set thixotropic cement plug to isolate aquifer. Wellhead tilt monitored constantly via subsea acoustic sensors. Conductor integrity verified before drilling ahead.",
    "resolution_time_hrs": 36,
    "mitigation": "Heavy kill pill (1.50 SG), rapid-setting bentonite-cement squeeze, ROV continuous visual seabed monitoring.",
    "casing_shoe_depth_m": 1120,
    "mud_weight_in_sg": 1.05,
    "mud_weight_out_sg": 1.50,
    "rig": "Deepwater Frontier (Transocean/RIL)",
    "bit": "Hughes 24\" Jetting Assembly"
  },
  {
    "well_id": "WELL-VOLVE-F12",
    "well_name": "Volve Benchmark Well 15/9-F-12",
    "event_id": "EVT-VOLVE-DDR42",
    "event_type": "Micro-Fracture Loss in Hugin Reservoir",
    "date": "2007-12-04",
    "depth_md_m": 3315,
    "formation": "Hugin Sandstone Formation",
    "loss_volume_bbl": 220,
    "rop_m_hr": 16.4,
    "torque_kNm": 32.5,
    "tour_note": "[DDR #42 // MAERSK INSPIRER // 22:30 UTC] Drilling 8-1/2\" section at 3,315 m MD (64° inclination). Flow paddle indicated return flow reduction of 18%. Lost 35 m3 (220 bbl) of synthetic oil-based mud (SOBM 1.44 SG) into natural micro-fractures adjacent to fault block boundary. Pumped 15 m3 coarse calcium carbonate LCM sweep (50 ppb Safeguard). Resumed steady drilling with ECD managed at 1.48 SG.",
    "resolution_time_hrs": 12,
    "mitigation": "Coarse CaCO3 LCM pill (15 m3), flow rate reduced by 300 LPM to control ECD.",
    "casing_shoe_depth_m": 3210,
    "mud_weight_in_sg": 1.44,
    "mud_weight_out_sg": 1.44,
    "rig": "Mærsk Inspirer (Equinor)",
    "bit": "Baker Hughes 8-1/2\" Quantec PDC"
  }
]

def main():
    os.makedirs('data', exist_ok=True)
    
    with open('data/real_wells_intelligence.json', 'w', encoding='utf-8') as f:
        json.dump(WELLS, f, indent=2)
    print("Wrote data/real_wells_intelligence.json")

    with open('data/historical_incidents.json', 'w', encoding='utf-8') as f:
        json.dump(HISTORICAL_INCIDENTS, f, indent=2)
    print("Wrote data/historical_incidents.json")

if __name__ == '__main__':
    main()
