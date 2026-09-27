import csv, os

OUT = "/home/claude/ppac_extract/csv"
os.makedirs(OUT, exist_ok=True)

def write_csv(name, header, rows):
    path = os.path.join(OUT, name)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(r)
    print(f"wrote {path} ({len(rows)} rows)")

REPORT_MONTH = "2026-08"   # data month (Aug'2026)
REPORT_ISSUE = "2026-09"   # issue month (Sept'26 ready reckoner)

# ---------------------------------------------------------------
# Table 2: Crude oil, LNG and petroleum products at a glance
# ---------------------------------------------------------------
header = ["metric","unit","fy2024_25","fy2025_26_p","aug_2025","aug_2026",
          "apr_aug_2025_26","apr_aug_2026_27"]
rows = [
 ["oil_oil_equiv_gas_production","MTOE",64.8,62.7,5.4,5.1,23.7,25.5],
 ["crude_oil_production_india","MMT",28.7,28.0,2.4,2.3,11.9,11.4],
 ["consumption_petroleum_products","MMT",239.2,241.6,19.1,18.6,100.1,96.2],
 ["production_petroleum_products","MMT",283.8,284.9,23.5,24.3,117.7,116.1],
 ["gross_natural_gas_production","MMSCM",36113,34776,2971,2830,11754,14075],
 ["natural_gas_consumption","MMSCM",71314,68753,5847,5708,22869,28666],
 ["gross_petroleum_imports_mmt","MMT",243.2,245.8,19.6,19.0,101.1,100.7],
 ["gross_petroleum_imports_usd_bn","USD Billion",137.2,123.4,9.9,11.7,50.4,74.8],
 ["crude_oil_imports_mmt","MMT",294.1,292.0,24.1,21.7,122.1,111.9],
 ["crude_oil_imports_usd_bn","USD Billion",160.8,144.2,11.7,13.0,59.8,81.8],
 ["pol_export_mmt","MMT",50.9,46.2,4.5,2.7,21.0,11.2],
 ["pol_export_usd_bn","USD Billion",23.7,20.8,1.8,1.4,9.4,6.9],
 ["pol_imports_mmt","MMT",65.1,61.4,5.7,4.9,25.7,21.5],
 ["pol_imports_usd_bn","USD Billion",44.4,41.1,3.5,5.0,15.9,21.7],
 ["lng_imports_mmscm","MMSCM",35720,34427,2912,2915,11269,14782],
 ["lng_imports_usd_bn","USD Billion",14.9,13.4,1.2,1.2,5.6,6.8],
 ["net_oil_gas_imports_usd_bn","USD Billion",131.3,116.4,9.3,9.3,49.6,66.8],
 ["petroleum_imports_pct_gross_imports","%",22.3,18.6,18.8,18.4,19.5,22.5],
 ["petroleum_exports_pct_gross_exports","%",10.2,9.3,10.1,11.3,8.7,10.1],
 ["import_dependency_crude_oil","%",88.3,88.7,87.6,87.5,88.3,88.1],
 ["import_dependency_oil_gas","%",80.0,80.7,79.2,79.4,81.5,80.2],
]
write_csv("table02_crude_oil_lng_pol_glance.csv", header, rows)

# ---------------------------------------------------------------
# Table 3: Indigenous crude oil production (MMT) by regime
# ---------------------------------------------------------------
header = ["regime","fy2024_25","fy2025_26_p","aug_2025","aug_2026","apr_aug_2025_26","apr_aug_2026_27"]
rows = [
 ["nomination",21.9,21.2,1.8,1.8,9.0,8.9],
 ["dsf",0.04,0.03,0.002,0.002,0.01,0.01],
 ["pre_nelp",4.2,3.7,0.3,0.2,1.6,1.3],
 ["nelp",2.54,2.94,0.258,0.27,1.31,1.17],
 ["oalp",0.03,0.02,0.002,0.001,0.01,0.01],
 ["total_crude_oil_condensate",28.7,28.0,2.4,2.3,11.9,11.4],
 ["out_of_which_crude_oil",26.5,26.0,2.2,2.2,11.1,10.7],
 ["out_of_which_condensate",2.2,2.0,0.2,0.2,0.9,0.8],
]
write_csv("table03_indigenous_crude_production_by_regime.csv", header, rows)

# ---------------------------------------------------------------
# Table 4: Domestic and overseas oil & gas production (Indian companies)
# ---------------------------------------------------------------
header = ["metric","unit","fy2024_25","fy2025_26_p","aug_2025","aug_2026","apr_aug_2025_26","apr_aug_2026_27"]
rows = [
 ["total_domestic_production","MMTOE",64.8,62.7,5.4,5.1,23.7,25.5],
 ["overseas_production","MMTOE",20.2,19.2,1.5,1.6,8.1,7.9],
]
write_csv("table04_domestic_overseas_production.csv", header, rows)

# ---------------------------------------------------------------
# Table 5: HS & LS crude oil processing (MMT)
# ---------------------------------------------------------------
header = ["crude_type","fy2024_25","fy2025_26_p","aug_2025","aug_2026","apr_aug_2025_26","apr_aug_2026_27"]
rows = [
 ["high_sulphur_crude",213.8,214.2,17.3,17.9,87.8,85.3],
 ["low_sulphur_crude",54.8,57.9,5.0,5.3,25.2,27.7],
 ["total_crude_processed_mmt",268.6,272.1,22.3,23.1,113.0,113.0],
 ["total_crude_processed_mn_bbl_day",5.39,5.46,5.28,5.47,5.42,5.41],
 ["total_crude_processed_mn_bbl",1968.9,1994.6,163.6,169.7,828.7,828.4],
]
write_csv("table05_hs_ls_crude_processing.csv", header, rows)
write_csv("table05b_hs_share_pct.csv", ["metric","fy2024_25","fy2025_26_p","aug_2025","aug_2026","apr_aug_2025_26","apr_aug_2026_27"],
          [["hs_crude_pct_of_total",79.6,78.7,77.7,77.2,77.7,75.5]])

# ---------------------------------------------------------------
# Table 6: Quantity and value of crude oil imports (by year)
# ---------------------------------------------------------------
header = ["fiscal_year","rs_crore","quantity_mmt","usd_million"]
rows = [
 ["2022-23", 1260372, 232.7, 133366],
 ["2023-24", 1160618, 243.2, 137174],   # note: source table ordering ambiguous, verify vs PDF p.11
 ["2024-25", 1105176, 245.8, 157531],
 ["2025-26", 1092248, None, 123379],
]
write_csv("table06_crude_oil_imports_by_year.csv", header, rows)

# ---------------------------------------------------------------
# Table 7: Self-sufficiency in petroleum products (MMT)
# ---------------------------------------------------------------
header = ["metric","fy2024_25","fy2025_26_p","aug_2025","aug_2026","apr_aug_2025_26","apr_aug_2026_27"]
rows = [
 ["indigenous_crude_oil_processing",26.5,25.7,2.2,2.2,11.0,10.8],
 ["products_from_indigenous_crude",24.7,24.0,2.1,2.0,10.3,10.1],
 ["products_from_fractionators_incl_lpg_gas",3.3,3.4,0.3,0.3,1.4,1.3],
 ["total_production_from_indig_crude_condensate",28.0,27.4,2.4,2.3,11.7,11.4],
 ["total_domestic_consumption",239.2,243.2,19.1,18.6,100.1,96.2],
 ["pct_self_sufficiency",11.7,11.3,12.4,12.5,11.7,11.9],
]
write_csv("table07_self_sufficiency_petroleum_products.csv", header, rows)

# ---------------------------------------------------------------
# Table 8/8b: Refineries installed capacity & crude processing (MMTPA / MMT)
# ---------------------------------------------------------------
header = ["sl_no","refinery","commissioned_year","group","installed_capacity_mmtpa_2026_04_01",
          "crude_processed_fy2024_25","crude_processed_fy2025_26_p","crude_processed_fy2026_27_target",
          "crude_processed_aug_2025_26_p","crude_processed_aug_2026_27_target","crude_processed_aug_2026_27_p",
          "crude_processed_apr_aug_2025_26_p","crude_processed_apr_aug_2026_27_target","crude_processed_apr_aug_2026_27_p"]
rows = [
 [1,"Barauni","1964","IOCL",6.0,6.5,6.4,None,0.5,0.6,0.5,2.7,3.0,2.6],
 [2,"Koyali","1965","IOCL",13.7,15.3,13.2,None,0.7,1.2,1.4,4.5,5.1,7.3],
 [3,"Haldia","1975","IOCL",8.0,6.9,8.5,None,0.7,0.6,0.8,3.7,3.5,3.7],
 [4,"Mathura","1982","IOCL",8.0,8.1,10.0,None,0.7,0.7,0.8,4.1,4.0,3.7],
 [5,"Panipat","1998","IOCL",15.0,15.4,15.9,None,1.3,1.3,0.6,6.6,6.3,5.5],
 [6,"Guwahati","1962","IOCL",1.2,1.2,1.3,None,0.1,0.1,0.1,0.5,0.5,0.6],
 [7,"Digboi","1901","IOCL",0.65,0.8,0.7,None,0.1,0.1,0.1,0.3,0.3,0.3],
 [8,"Bongaigaon","1979","IOCL",2.70,2.8,3.0,None,0.3,0.3,0.2,1.3,1.3,1.3],
 [9,"Paradip","2016","IOCL",15.0,14.7,16.3,None,1.4,1.4,1.3,7.0,6.9,6.2],
 [None,"IOCL_TOTAL",None,"IOCL",70.3,71.6,75.5,None,5.8,6.1,5.7,30.6,30.8,31.0],
 [10,"Manali","1969","CPCL",10.5,10.5,11.7,None,1.1,0.0,1.0,5.1,2.0,4.9],
 [11,"CBR","1993","CPCL",0.0,0.0,0.0,None,0.0,0.0,0.0,0.0,0.0,0.0],
 [None,"CPCL_TOTAL",None,"CPCL",10.5,10.5,11.7,None,1.1,0.0,1.0,5.1,2.0,4.9],
 [12,"Mumbai","1955","BPCL",12.0,15.5,16.0,None,1.4,1.3,1.3,6.7,6.5,6.5],
 [13,"Kochi","1966","BPCL",15.5,17.2,17.6,None,1.6,1.5,1.5,7.6,7.4,7.4],
 [14,"Bina","2011","BPCL",7.8,7.7,7.4,None,0.2,0.4,0.7,2.9,3.0,3.5],
 [None,"BPCL_TOTAL",None,"BPCL",35.3,40.4,41.0,None,3.2,3.2,3.6,17.2,16.9,17.4],
 [15,"Numaligarh","1999","OIL/BPCL",3.0,3.1,3.1,None,0.2,0.3,0.3,1.3,1.3,1.3],
 [16,"Tatipaka","2001","ONGC",0.07,0.07,0.007,None,0.0,None,0.006,0.03,None,0.03],
 [17,"MRPL-Mangalore","1996","ONGC",18.0,16.8,None,None,1.5,1.5,1.2,6.4,6.6,7.0],
 [None,"ONGC_TOTAL",None,"ONGC",18.1,16.8,None,None,1.5,1.5,1.2,6.5,6.6,7.0],
 [18,"Mumbai","1954","HPCL",10.0,10.0,None,None,0.9,0.8,0.9,4.2,4.1,4.3],
 [19,"Visakh","1957","HPCL",15.3,16.0,None,None,1.3,1.3,1.3,6.9,6.2,6.5],
 [None,"HPCL_TOTAL",None,"HPCL",25.3,26.0,None,None,2.2,2.1,2.2,11.1,10.4,10.8],
 [20,"HMEL-Bathinda","2012","HMEL",13.0,11.7,None,None,1.1,1.1,1.1,5.2,5.5,5.6],
 [21,"HRRL-Pachpadra","2026","HRRL",0.0,0.0,None,None,None,None,None,None,None,0.3],
 [22,"RIL-Jamnagar (DTA)","1999","RIL",35.0,33.6,None,None,3.0,2.9,3.0,13.3,14.6,12.9],
 [23,"RIL-Jamnagar (SEZ)","2008","RIL",31.2,33.7,None,None,2.9,2.5,3.3,14.4,12.8,15.8],
 [24,"NEL-Vadinar","2006","NEL",20.5,18.9,None,None,1.4,1.8,1.7,8.2,8.5,6.0],
 [None,"ALL_INDIA_TOTAL_MMT",None,"ALL",268.6,272.0,None,None,22.3,21.5,23.1,113.0,109.3,113.0],
]
write_csv("table08_refineries_capacity_processing.csv", header, rows)

# ---------------------------------------------------------------
# Table 9: Major crude oil and product pipeline network (as on 01.09.2026)
# ---------------------------------------------------------------
header = ["pipeline_type","operator","length_km","capacity_mmtpa"]
rows = [
 ["crude_oil","ONGC",1284,60.6],
 ["crude_oil","OIL",1196,9.0],
 ["crude_oil","Cairn/Others",688,10.7],
 ["crude_oil","HMEL",1017,11.3],
 ["crude_oil","IOCL",5322,63.8],
 ["crude_oil","BPCL",937,7.8],
 ["crude_oil","TOTAL",10443,163.1],
 ["products","ONGC",654,1.7],
 ["products","IOCL",13347,80.6],
 ["products","BPCL",3025,25.2],
 ["products","HPCL",5439,42.6],
 ["products","Others",2399,10.2],
 ["products","TOTAL",24864,160.3],
]
write_csv("table09_crude_product_pipeline_network.csv", header, rows)

# ---------------------------------------------------------------
# Table 10: Gross Refining Margins (GRM) of refineries ($/bbl)
# ---------------------------------------------------------------
header = ["company","fy2021_22","fy2022_23","fy2023_24","fy2024_25","fy2025_26","apr_jun_2026_27"]
rows = [
 ["IOCL",11.25,19.52,12.05,4.80,None,2.15],
 ["BPCL",9.09,20.24,14.14,6.82,11.74,4.88],
 ["HPCL",7.19,12.09,9.08,5.74,8.79,3.08],
 ["CPCL",8.85,12.48,8.64,4.22,9.28,3.22],
 ["MRPL",8.72,9.88,10.36,4.45,None,3.88],
 ["NRL",43.46,35.82,29.72,19.95,29.20,21.41],
 ["BORL",11.00,None,None,None,None,None],
]
write_csv("table10_gross_refining_margins.csv", header, rows)

# ---------------------------------------------------------------
# Table 11: Production and consumption of petroleum products (MMT)
# ---------------------------------------------------------------
header = ["product","fy2024_25_prod","fy2024_25_cons","fy2025_26_p_prod","fy2025_26_p_cons",
          "aug_2025_prod","aug_2025_cons","aug_2026_prod","aug_2026_cons",
          "apr_aug_2025_26_prod","apr_aug_2025_26_cons","apr_aug_2026_27_prod","apr_aug_2026_27_cons"]
rows = [
 ["LPG",12.8,31.3,13.1,33.2,1.1,2.8,1.2,2.3,5.3,13.4,6.6,11.2],
 ["MS",48.3,40.0,49.8,42.6,4.3,3.5,4.1,3.8,20.5,17.8,20.2,19.0],
 ["NAPHTHA",17.9,13.2,18.4,11.7,1.4,1.1,1.5,0.8,7.9,4.9,7.5,4.2],
 ["ATF",17.8,9.0,16.4,9.2,1.4,0.7,1.1,0.7,7.1,3.7,6.0,3.7],
 ["SKO",1.0,0.4,1.0,0.5,0.1,0.0,0.1,0.0,0.5,0.2,0.4,0.2],
 ["HSD",118.2,91.4,120.8,94.7,9.7,6.6,10.1,7.0,49.9,38.9,49.4,40.8],
 ["LDO",0.6,0.8,0.7,1.0,0.1,0.1,0.0,0.0,0.3,0.4,0.2,0.3],
 ["LUBES",1.3,4.6,1.5,5.0,0.1,0.4,0.1,0.4,0.6,1.9,0.7,1.8],
 ["FO_LSHS",10.9,6.5,10.3,6.4,1.0,0.5,1.2,0.5,4.3,2.5,5.2,2.7],
 ["BITUMEN",5.3,8.3,5.4,8.7,0.2,0.4,0.3,0.4,1.9,3.2,1.4,2.2],
 ["PET_COKE",15.0,22.1,14.8,18.4,1.2,2.2,1.2,1.6,6.0,8.8,5.4,6.8],
 ["OTHERS",34.8,11.6,32.7,10.4,2.8,0.8,3.3,0.8,13.3,4.3,12.9,3.3],
 ["ALL_INDIA",283.8,239.2,284.9,241.6,23.5,19.1,24.3,18.6,117.7,100.1,116.1,96.2],
]
write_csv("table11_production_consumption_by_product.csv", header, rows)

# ---------------------------------------------------------------
# Table 11A: POL consumption report - August 26 (TMT)
# ---------------------------------------------------------------
header = ["category","product","aug_2025_tmt","aug_2026_tmt","aug_2026_pct_share","aug_growth_pct",
          "fy2025_26_tmt","fy2026_27_tmt","fy2026_27_growth_pct","fy2026_27_pct_share"]
rows = [
 ["Sensitive","LPG",2833,2347,12.6,-17.1,13423,11172,-16.8,11.6],
 ["Sensitive","SKO",34,40,0.2,17.2,176,177,0.4,0.2],
 ["Sensitive","Sub_Total",2867,2388,12.8,-16.7,13599,11349,-16.5,11.8],
 ["Major_Decontrolled","HSD",6577,7023,37.7,6.8,38891,40774,4.8,42.4],
 ["Major_Decontrolled","MS",3544,3836,20.6,8.2,17791,19029,7.0,19.8],
 ["Major_Decontrolled","Naphtha",1065,828,4.4,-22.3,4891,4166,-14.8,4.3],
 ["Major_Decontrolled","ATF",710,726,3.9,2.1,3698,3716,0.5,3.9],
 ["Major_Decontrolled","Bitumen",369,442,2.4,20.0,3213,2166,-32.6,2.3],
 ["Major_Decontrolled","FO_LSHS",501,525,2.8,4.9,2486,2733,9.9,2.8],
 ["Major_Decontrolled","Lubes_Greases",373,416,2.2,11.6,1921,1820,-5.2,1.9],
 ["Major_Decontrolled","LDO",80,47,0.3,-41.8,419,250,-40.3,0.3],
 ["Major_Decontrolled","Sub_Total",13219,13843,74.4,4.7,73310,74654,1.8,77.6],
 ["Other_Minor","Pet_Coke",2239,1599,8.6,-28.6,8835,6815,-22.9,7.1],
 ["Other_Minor","Others",818,777,4.2,-5.0,4329,3342,-22.8,3.5],
 ["Other_Minor","Sub_Total",3056,2376,12.8,-22.3,13164,10157,-22.8,10.6],
 ["Total","Total",19143,18606,100.0,-2.8,100073,96160,-3.9,100.0],
]
write_csv("table11a_pol_consumption_report_aug26.csv", header, rows)

# ---------------------------------------------------------------
# Table 11B: Regionwise MS, HSD, LPG, ATF consumption (TMT) Aug26
# ---------------------------------------------------------------
header = ["product","region","fy2025_26_tmt","fy2026_27_tmt","growth_pct"]
rows = [
 ["MS","TOTAL",6449,None,8.2],   # total bar approx; growth label directly on chart
 ["MS","EAST",393,430,9.3],
 ["MS","NORTH",1184,1288,8.8],
 ["MS","SOUTH",1072,1177,9.8],
 ["MS","WEST",895,941,5.1],
 ["HSD","TOTAL",6573,7020,6.8],
 ["HSD","EAST",782,837,7.1],
 ["HSD","NORTH",2002,2117,5.7],
 ["HSD","SOUTH",2040,2182,7.0],
 ["HSD","WEST",1749,1884,7.7],
 ["LPG","TOTAL",2790,2338,-16.2],
 ["LPG","EAST",499,417,-16.5],
 ["LPG","NORTH",918,758,-17.5],
 ["LPG","SOUTH",754,651,-13.7],
 ["LPG","WEST",626,519,-17.1],
 ["ATF","TOTAL",710,725,2.1],
 ["ATF","EAST",47,41,-12.9],
 ["ATF","NORTH",264,288,9.4],
 ["ATF","SOUTH",224,214,-4.4],
 ["ATF","WEST",176,182,3.5],
]
write_csv("table11b_regionwise_consumption_aug26.csv", header, rows)

# ---------------------------------------------------------------
# Table 12: Kerosene (PDS) allocation vs upliftment (KL)
# ---------------------------------------------------------------
header = ["fiscal_year","allocation_kl","upliftment_kl"]
rows = [
 ["2023-24",971796,383479],
 ["2024-25",416784,295277],
 ["2025-26",518430,363466],
 ["2026-27_P",248753,149326],
]
write_csv("table12_kerosene_allocation_upliftment.csv", header, rows)

# ---------------------------------------------------------------
# Table 13: Ethanol blending programme
# ---------------------------------------------------------------
header = ["ethanol_supply_year","ethanol_blended_cr_litres","ethanol_storage_cr_litres",
          "ethanol_received_cr_litres","avg_blending_pct"]
rows = [
 ["2023-24",1022.4,None,1040.1,None],
 ["2024-25",None,None,None,None],
 ["2025-26",None,84.6,None,20.0],
 ["Nov25_Aug26",894.7,84.5,938.2,20.0],
]
write_csv("table13_ethanol_blending_summary.csv", header, rows)

# ---------------------------------------------------------------
# Table 14: Industry marketing infrastructure (as on 01.09.2026)
# ---------------------------------------------------------------
header = ["company","retail_outlets_total","rural_retail_outlets","sko_ldo_agencies",
          "lpg_distributors_total","lpg_bottling_plants","lpg_bottling_capacity_tmtpa"]
rows = [
 ["IOCL",43270,14061,3830,12948,101,11123],
 ["BPCL",25592,6835,927,6284,57,5400],
 ["HPCL",25238,6433,1638,6393,56,6515],
 ["RIL_RBML_RSIL",2304,135,None,None,2,180],
 ["NEL",7108,2162,None,None,None,None],
 ["SHELL",338,85,None,None,None,None],
 ["MRPL_Others",287,78,None,None,None,None],
 ["TOTAL",104137,29789,6395,25625,216,23218],
]
write_csv("table14_industry_marketing_infrastructure.csv", header, rows)

header2 = ["fuel_type","total_ros_with_alt_fuel"]
rows2 = [
 ["CNG_LNG",7744],
 ["EV_Charging",29580],
 ["Auto_LPG",416],
 ["Compressed_Bio_Gas_outlets",503],
]
write_csv("table14b_alternate_fuel_infrastructure.csv", header2, rows2)

# ---------------------------------------------------------------
# Table 15: LPG consumption (TMT)
# ---------------------------------------------------------------
header = ["metric","fy2025_26","fy2026_27_p","aug_2025_26","aug_2026_27_p","apr_aug_2025_26","apr_aug_2026_27_p"]
rows = [
 ["lpg_active_domestic_customers_lakh",None,None,None,None,None,None],  # see table16 for stock figures
 ["lpg_consumption_tmt",13423.2,11172.3,2833.1,2347.4,None,None],
]
write_csv("table15_lpg_consumption.csv", header, rows)

# ---------------------------------------------------------------
# Table 16: LPG marketing at a glance (time series, as on 1 April unless noted)
# ---------------------------------------------------------------
header = ["as_on_date","lpg_active_domestic_customers_lakh","lpg_coverage_pct",
          "pmuy_beneficiaries_lakh","lpg_distributors_no","auto_lpg_dispensing_stations_no",
          "bottling_plants_no"]
rows = [
 ["2014",1486,56.2,None,13896,678,187],
 ["2015",1663,61.9,200.3,15930,681,187],
 ["2016",1988,72.8,356,17916,676,188],
 ["2017",2243,80.9,719,18786,675,189],
 ["2018",2654,94.3,802,20146,672,190],
 ["2019",2787,97.5,800,23737,661,192],
 ["2020",2895,99.8,899.0,24670,657,196],
 ["2021",3053,None,958.6,25083,651,200],
 ["2022",3140,None,1032.7,25269,601,202],
 ["2023",3242,None,1033.0,25386,526,208],
 ["2024",3297,None,1057.6,25481,468,210],
 ["2025",3339,None,1057,25566,443,211],
 ["2026",3277,None,1058,25607,364,214],
 ["2026-09-01",None,None,1057,25625,334,216],
]
write_csv("table16_lpg_marketing_timeseries.csv", header, rows)

# ---------------------------------------------------------------
# Table 17: Region-wise LPG marketing (as on 01.09.2026)
# ---------------------------------------------------------------
header = ["region","lpg_active_domestic_customers_lakh","non_pmuy_customers_lakh",
          "pmuy_beneficiaries_lakh","lpg_distributors_no","auto_lpg_dispensing_stations_no",
          "bottling_plants_no"]
rows = [
 ["North",993.0,679.7,313.3,8196,54,66],
 ["North-East",127.3,63.5,63.8,1121,0,11],
 ["East",675.6,334.7,340.9,5219,27,34],
 ["West",682.8,455.8,227.0,5438,44,51],
 ["South",798.7,686.5,112.2,5651,209,54],
 ["Total",3277.5,2220.3,1057.2,25625,334,216],
]
write_csv("table17_regionwise_lpg_marketing.csv", header, rows)

# ---------------------------------------------------------------
# Table 18: Natural gas at a glance (MMSCM)
# ---------------------------------------------------------------
header = ["metric","fy2024_25","fy2025_26_p","aug_2025_26_p","aug_2026_27_target","aug_2026_27_p",
          "apr_aug_2025_26_p","apr_aug_2026_27_target","apr_aug_2026_27_p"]
rows = [
 ["gross_production",36113,34776,2971,3029,2830,11754,14817,14075],
 ["nomination_field",21971,21580,1837,1959,1804,7200,9553,8890],
 ["private_jv",14143,13195,1133,1070,1026,4555,5264,5185],
 ["net_production_excl_flare",35594,34326,2935,None,2792,11600,None,13884],
 ["lng_import",35720,34427,2912,None,2915,11269,None,14782],
 ["total_consumption_incl_internal",71314,68753,5847,None,5708,22869,None,28666],
 ["total_consumption_bcm",71.3,68.8,5.8,None,5.7,22.9,None,28.7],
 ["import_dependency_pct",50.1,50.1,49.8,None,51.1,49.3,None,51.6],
]
write_csv("table18_natural_gas_at_a_glance.csv", header, rows)

header2 = ["metric","fy2022_23","fy2023_24","fy2024_25","fy2025_26","apr_aug_2026_27_p"]
rows2 = [
 ["gross_natural_gas_production_mmscm",34450,36438,36113,34776,14075],
 ["natural_gas_consumption_incl_internal_mmscm",59969,67512,71314,68542,28666],
]
write_csv("table18b_natural_gas_yearly_trend.csv", header2, rows2)

header3 = ["period","regime","pct_share"]
rows3 = [
 ["Aug_2026","Nomination",64.2],["Aug_2026","PSC",32.5],["Aug_2026","RSC",0.7],["Aug_2026","CBM",2.6],
 ["Aug_2025","Nomination",61.8],["Aug_2025","PSC",35.1],["Aug_2025","RSC",0.7],["Aug_2025","CBM",2.4],
 ["Apr_Aug_2026","Nomination",63.2],["Apr_Aug_2026","PSC",33.6],["Apr_Aug_2026","RSC",0.7],["Apr_Aug_2026","CBM",2.5],
 ["Apr_Aug_2025","Nomination",61.4],["Apr_Aug_2025","PSC",35.7],["Apr_Aug_2025","RSC",0.7],["Apr_Aug_2025","CBM",2.3],
]
write_csv("table18c_gas_production_by_regime_share.csv", header3, rows3)

# ---------------------------------------------------------------
# Table 19: Coal Bed Methane (CBM) gas development in India
# ---------------------------------------------------------------
header = ["metric","value","unit"]
rows = [
 ["prognosticated_cbm_resources",91.8,"TCF"],
 ["established_cbm_resources",12.1,"TCF"],
 ["cbm_resources_33_blocks",62.4,"TCF"],
 ["total_coal_bearing_area_mopng_dgh",21177,"sq_km"],
 ["area_awarded",14536,"sq_km"],
 ["blocks_awarded",40,"nos (one block awarded twice)"],
 ["exploration_initiated_area",11578,"sq_km"],
 ["production_cbm_aug_2026",73.56,"MMSCM"],
 ["production_cbm_apr_aug_2026",347.22,"MMSCM"],
]
write_csv("table19_cbm_gas_development.csv", header, rows)

# ---------------------------------------------------------------
# Table 19A: Status of CBG (SATAT) projects (as on 01.09.2026)
# ---------------------------------------------------------------
header = ["metric","value","unit"]
rows = [
 ["cbg_plants_commissioned_sale_started",None,"No. of plants"],
 ["sale_of_cbg_2022_23",12.1,"TMT"],
 ["sale_of_cbg_2023_24",None,"TMT"],
 ["sale_of_cbg_2024_25",None,"TMT"],
 ["sale_of_cbg_2025_26",None,"TMT"],
 ["sale_of_cbg_2026_27_apr_aug",None,"TMT"],
 ["cgd_network_ga_with_cbg_sale",598,"Nos (Tripartite Agreements)"],
]
write_csv("table19a_cbg_status.csv", header, rows)

# ---------------------------------------------------------------
# Table 20: Common Carrier Natural Gas pipeline network (as on 31.03.2026)
# ---------------------------------------------------------------
header = ["operator","operational_length_km","operational_capacity_mmscmd",
          "under_construction_length_km"]
rows = [
 ["GAIL",18302,240.1,823],
 ["GSPL",2894,74.8,337],
 ["PIL",1485,85.0,310],
 ["IOCL",1370,25.2,784],
 ["AGCL",107,2.4,None],
 ["RGPL",304,3.5,None],
 ["GGL",73,5.1,None],
 ["DFPCL",42,0.7,None],
 ["ONGC",30,3.5,220],
 ["GIGL",1419,42.1,1172],
 ["GTIL",0,None,None],
 ["Others",321,None,None],
 ["TOTAL_OPERATIONAL",26348,None,3646],
]
write_csv("table20_common_carrier_gas_pipeline.csv", header, rows)

# ---------------------------------------------------------------
# Table 21: Existing LNG terminals
# ---------------------------------------------------------------
header = ["location","promoter","capacity_mmtpa_2026_09_01","capacity_utilisation_pct_apr_aug26"]
rows = [
 ["Dahej","Petronet LNG Ltd (PLL)",22.5,68.21],
 ["Hazira","Shell Energy India Pvt Ltd",6.0,27.3],
 ["Dabhol","Konkan LNG Limited",5.0,6.1],
 ["Kochi","Petronet LNG Ltd (PLL)",5.0,24.26],
 ["Ennore","Indian Oil LNG Pvt Ltd",5.0,None],
 ["Mundra","Adani Total Private Limited",5.0,45.2],
 ["Dhamra","HPCL LNG Limited",5.0,None],
 ["Chhara","GSPC LNG Limited",5.0,None],
 ["TOTAL",None,58.5,None],
]
write_csv("table21_lng_terminals.csv", header, rows)

# ---------------------------------------------------------------
# Table 22: PNG connections and CNG stations by state (as on 31.07.2026)
# ---------------------------------------------------------------
header = ["state_ut","cng_stations","png_domestic","png_commercial","png_industrial"]
rows = [
 ["Andhra Pradesh",222,293633,756,68],
 ["Andhra Pradesh, Karnataka & Tamil Nadu",52,18894,66,53],
 ["Assam",49,81180,1652,492],
 ["Bihar",212,284185,402,65],
 ["Bihar & Jharkhand",42,15549,36,1],
 ["Bihar & Uttar Pradesh",36,64196,0,0],
 ["Chandigarh (UT), Haryana, Punjab & Himachal Pradesh",37,34529,290,102],
 ["Chhattisgarh",70,21956,2,22],
 ["Dadra & Nagar Haveli (UT)",6,15922,80,70],
 ["Daman & Diu (UT)",4,5621,146,72],
 ["Daman and Diu & Gujarat",21,12503,121,0],
 ["Goa",16,20891,124,62],
 ["Gujarat",1090,3968551,26082,5997],
 ["Haryana",576,618942,2163,3224],
 ["Haryana & Himachal Pradesh",12,820,12,5],
 ["Haryana & Punjab",31,3540,13,0],
 ["Himachal Pradesh",21,14405,73,20],
 ["Jharkhand",136,191443,394,45],
 ["Karnataka",522,619668,1067,508],
 ["Kerala",226,148452,436,52],
 ["Kerala & Puducherry",33,14490,41,0],
 ["Madhya Pradesh",385,339049,957,720],
 ["Madhya Pradesh and Chhattisgarh",9,0,0,0],
 ["Madhya Pradesh and Rajasthan",44,2897,8,0],
 ["Madhya Pradesh and Uttar Pradesh",22,105,2,5],
 ["Maharashtra",1224,4533745,6645,1427],
 ["Maharashtra & Gujarat",114,239130,48,79],
 ["Maharashtra and Madhya Pradesh",19,283,1,0],
 ["Meghalaya",4,0,0,0],
 ["National Capital Territory of Delhi (UT)",459,1994439,5080,1909],
 ["Odisha",161,192425,347,12],
 ["Puducherry",11,0,0,4],
 ["Puducherry & Tamil Nadu",9,920,14,1],
 ["Punjab",264,134906,1207,416],
 ["Punjab & Rajasthan",35,41422,0,0],
 ["Rajasthan",455,516804,826,1936],
 ["Tamil Nadu",494,137414,255,157],
 ["Telangana",235,266977,273,221],
 ["Telangana and Karnataka",15,146,6,8],
 ["Tripura",30,71872,569,48],
 ["UT of Jammu and Kashmir",3,0,0,0],
 ["Uttar Pradesh",1297,2314764,4693,4406],
 ["Uttar Pradesh & Rajasthan",57,34541,140,352],
 ["Uttar Pradesh and Uttarakhand",41,19424,4,0],
 ["Uttarakhand",46,86902,257,182],
 ["West Bengal",249,169376,58,11],
 ["Grand_Total",9096,17546911,55346,22752],
]
write_csv("table22_state_png_cng_status.csv", header, rows)

# ---------------------------------------------------------------
# Table 23: Domestic Natural Gas price and gas price ceiling (GCV basis, USD/MMBtu)
# ---------------------------------------------------------------
header = ["period","domestic_gas_calculated_price_usd_mmbtu","gas_ceiling_price_ongc_oil_usd_mmbtu",
          "hp_ht_ceiling_price_usd_mmbtu"]
rows = [
 ["Apr2024-Sep2024",6.75,6.50,None],
 ["Oct2024-Mar2025",6.75,6.50,None],
 ["Apr2025-Sep2025",6.75,6.50,None],
 ["Oct2025-Mar2026",6.75,6.50,9.72],
 ["Apr2026-Sep2026",6.75,6.50,8.9],
]
write_csv("table23_domestic_gas_price_ceiling.csv", header, rows)

# ---------------------------------------------------------------
# Table 24: CNG/PNG prices (selected cities)
# ---------------------------------------------------------------
header = ["city","cng_rs_kg","png_rs_scm","source_date"]
rows = [
 ["Delhi",None,53.00,"August 26"],
 ["Mumbai",88.00,None,"August 26"],
]
write_csv("table24_cng_png_prices_selected_cities.csv", header, rows)

# ---------------------------------------------------------------
# Table 26: Capital expenditure of PSU oil companies (Rs crores)
# ---------------------------------------------------------------
header = ["company","fy2023_24","fy2024_25","fy2025_26","fy2026_27_target","apr_aug_2026_27_p"]
rows = [
 ["ONGC_Ltd",34551,61110,34939,30000,12103],
 ["ONGC_Videsh_Ltd_OVL",3262,5023,5387,7265,3504],
 ["Oil_India_Ltd_OIL",5390,7624,11623,8653,4510],
 ["GAIL_India_Ltd",10388,10258,8669,11518,6855],
 ["Indian_Oil_Corp_Ltd_IOCL",38660,37557,31411,32700,8823],
 ["Bharat_Petroleum_Corp_Ltd_BPCL",11002,16508,19863,25000,8859],
 ["Hindustan_Petroleum_Corp_Ltd_HPCL",13842,13630,14358,9641,2264],
 ["Mangalore_Refinery_Petrochem_Ltd_MRPL",1513,1006,1316,836,293],
 ["Chennai_Petroleum_Corp_Ltd_CPCL",561,660,694,610,171],
 ["Numaligarh_Refinery_Ltd_NRL",8585,9038,8317,7500,2339],
 ["Balmer_Lawrie_Co_Ltd_BL",47,50,59,40,17],
 ["Engineers_India_Ltd_EIL",108,72,86,60,10],
 ["TOTAL",127908,162537,136721,133823,49748],
]
write_csv("table26_psu_capex.csv", header, rows)

# ---------------------------------------------------------------
# Table 27: Conversion factors
# ---------------------------------------------------------------
header = ["product","weight_mt","volume_kl","barrel_bbl"]
rows = [
 ["LPG",1,1.844,11.60],
 ["Petrol_MS",1,1.411,8.88],
 ["Furnace_Oil_FO",1,1.210,7.61],
 ["Diesel_HSD",1,1.285,8.08],
 ["Kerosene_SKO",1,1.288,8.10],
 ["ATF",1,1.172,7.37],
 ["LDO",1,1.0424,6.74],
 ["Crude_Oil",1,1.170,7.33],
]
write_csv("table27a_weight_to_volume_conversion.csv", header, rows)

header2 = ["from_unit","to_unit","factor"]
rows2 = [
 ["1 US Barrel (bbl)","litres",159],
 ["1 US Barrel (bbl)","US Gallons",42],
 ["1 Kilocalorie (kcal)","kJ",4.187],
 ["1 US Gallon","litres",3.78],
 ["1 Kilo litre (KL)","bbl",6.29],
 ["1 Million barrels per day","MMTPA",49.8],
 ["1 Kilocalorie (kcal)","Btu",3.968],
 ["1 Kilowatt-hour (kWh)","kcal",860],
 ["1 Standard Cubic Metre (SCM)","Cubic Feet",35.31],
 ["1 MMBTU","SCM (@10000 kcal/SCM)",25.2],
 ["1 Billion Cubic Metres (BCM)/year of Gas","MMSCMD",2.74],
 ["1 Trillion Cubic Feet (TCF) of Gas Reserve","MMSCMD",3.88],
 ["1 Million Metric Tonne Per Annum (MMTPA) of LNG","MMSCMD",3.60],
 ["1 MT of LNG","SCM",1325],
 ["1 Kilowatt-hour (kWh)","Btu",3412],
 ["Power generation from 1 MMSCMD of gas","MW",220],
 ["Gas required for 1 MW power generation","SCM/day",4541],
 ["200 Nautical Miles","Kilometers",370.4],
]
write_csv("table27b_general_conversions.csv", header2, rows2)

print("DONE")
