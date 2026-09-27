-- ============================================================
-- PPAC "Snapshot of India's Oil & Gas Data" (Aug'2026 issue)
-- Schema for eRTMAC-NWIS Postgres backend
-- Source: Petroleum Planning & Analysis Cell (PPAC), MoPNG
-- Report month: Aug-2026 | Issue: Sept-26
-- ============================================================

CREATE SCHEMA IF NOT EXISTS ppac;

-- Table 2: Crude oil, LNG & POL at a glance
CREATE TABLE ppac.crude_oil_lng_pol_glance (
    metric TEXT PRIMARY KEY,
    unit TEXT,
    fy2024_25 NUMERIC,
    fy2025_26_p NUMERIC,
    aug_2025 NUMERIC,
    aug_2026 NUMERIC,
    apr_aug_2025_26 NUMERIC,
    apr_aug_2026_27 NUMERIC
);

-- Table 3: Indigenous crude oil production by regime
CREATE TABLE ppac.crude_production_by_regime (
    regime TEXT PRIMARY KEY,
    fy2024_25 NUMERIC,
    fy2025_26_p NUMERIC,
    aug_2025 NUMERIC,
    aug_2026 NUMERIC,
    apr_aug_2025_26 NUMERIC,
    apr_aug_2026_27 NUMERIC
);

-- Table 4: Domestic vs overseas production
CREATE TABLE ppac.domestic_overseas_production (
    metric TEXT PRIMARY KEY,
    unit TEXT,
    fy2024_25 NUMERIC,
    fy2025_26_p NUMERIC,
    aug_2025 NUMERIC,
    aug_2026 NUMERIC,
    apr_aug_2025_26 NUMERIC,
    apr_aug_2026_27 NUMERIC
);

-- Table 5: HS / LS crude processing
CREATE TABLE ppac.hs_ls_crude_processing (
    crude_type TEXT PRIMARY KEY,
    fy2024_25 NUMERIC,
    fy2025_26_p NUMERIC,
    aug_2025 NUMERIC,
    aug_2026 NUMERIC,
    apr_aug_2025_26 NUMERIC,
    apr_aug_2026_27 NUMERIC
);
CREATE TABLE ppac.hs_share_pct (
    metric TEXT PRIMARY KEY,
    fy2024_25 NUMERIC, fy2025_26_p NUMERIC,
    aug_2025 NUMERIC, aug_2026 NUMERIC,
    apr_aug_2025_26 NUMERIC, apr_aug_2026_27 NUMERIC
);

-- Table 6: Crude oil import value/quantity by fiscal year
CREATE TABLE ppac.crude_oil_imports_by_year (
    fiscal_year TEXT PRIMARY KEY,
    rs_crore NUMERIC,
    quantity_mmt NUMERIC,
    usd_million NUMERIC
);

-- Table 7: Self-sufficiency in petroleum products
CREATE TABLE ppac.self_sufficiency (
    metric TEXT PRIMARY KEY,
    fy2024_25 NUMERIC, fy2025_26_p NUMERIC,
    aug_2025 NUMERIC, aug_2026 NUMERIC,
    apr_aug_2025_26 NUMERIC, apr_aug_2026_27 NUMERIC
);

-- Table 8: Refineries — installed capacity & crude processed
CREATE TABLE ppac.refineries (
    sl_no INTEGER,
    refinery TEXT PRIMARY KEY,
    commissioned_year TEXT,
    refinery_group TEXT,
    installed_capacity_mmtpa_2026_04_01 NUMERIC,
    crude_processed_fy2024_25 NUMERIC,
    crude_processed_fy2025_26_p NUMERIC,
    crude_processed_fy2026_27_target NUMERIC,
    crude_processed_aug_2025_26_p NUMERIC,
    crude_processed_aug_2026_27_target NUMERIC,
    crude_processed_aug_2026_27_p NUMERIC,
    crude_processed_apr_aug_2025_26_p NUMERIC,
    crude_processed_apr_aug_2026_27_target NUMERIC,
    crude_processed_apr_aug_2026_27_p NUMERIC
);

-- Table 9: Crude oil & product pipeline network
CREATE TABLE ppac.pipeline_network (
    pipeline_type TEXT,
    operator TEXT,
    length_km NUMERIC,
    capacity_mmtpa NUMERIC,
    PRIMARY KEY (pipeline_type, operator)
);

-- Table 10: Gross Refining Margins
CREATE TABLE ppac.refining_margins (
    company TEXT PRIMARY KEY,
    fy2021_22 NUMERIC, fy2022_23 NUMERIC, fy2023_24 NUMERIC,
    fy2024_25 NUMERIC, fy2025_26 NUMERIC, apr_jun_2026_27 NUMERIC
);

-- Table 11: Production/consumption by petroleum product
CREATE TABLE ppac.product_production_consumption (
    product TEXT PRIMARY KEY,
    fy2024_25_prod NUMERIC, fy2024_25_cons NUMERIC,
    fy2025_26_p_prod NUMERIC, fy2025_26_p_cons NUMERIC,
    aug_2025_prod NUMERIC, aug_2025_cons NUMERIC,
    aug_2026_prod NUMERIC, aug_2026_cons NUMERIC,
    apr_aug_2025_26_prod NUMERIC, apr_aug_2025_26_cons NUMERIC,
    apr_aug_2026_27_prod NUMERIC, apr_aug_2026_27_cons NUMERIC
);

-- Table 11A: Monthly POL consumption report
CREATE TABLE ppac.pol_consumption_report (
    category TEXT,
    product TEXT PRIMARY KEY,
    aug_2025_tmt NUMERIC,
    aug_2026_tmt NUMERIC,
    aug_2026_pct_share NUMERIC,
    aug_growth_pct NUMERIC,
    fy2025_26_tmt NUMERIC,
    fy2026_27_tmt NUMERIC,
    fy2026_27_growth_pct NUMERIC,
    fy2026_27_pct_share NUMERIC
);

-- Table 11B: Regionwise consumption (MS/HSD/LPG/ATF)
CREATE TABLE ppac.regionwise_consumption (
    id SERIAL PRIMARY KEY,
    product TEXT,
    region TEXT,
    fy2025_26_tmt NUMERIC,
    fy2026_27_tmt NUMERIC,
    growth_pct NUMERIC
);

-- Table 12: Kerosene allocation vs upliftment
CREATE TABLE ppac.kerosene_allocation (
    fiscal_year TEXT PRIMARY KEY,
    allocation_kl NUMERIC,
    upliftment_kl NUMERIC
);

-- Table 13: Ethanol blending programme
CREATE TABLE ppac.ethanol_blending (
    ethanol_supply_year TEXT PRIMARY KEY,
    ethanol_blended_cr_litres NUMERIC,
    ethanol_storage_cr_litres NUMERIC,
    ethanol_received_cr_litres NUMERIC,
    avg_blending_pct NUMERIC
);

-- Table 14: Industry marketing infrastructure by company
CREATE TABLE ppac.marketing_infrastructure (
    company TEXT PRIMARY KEY,
    retail_outlets_total NUMERIC,
    rural_retail_outlets NUMERIC,
    sko_ldo_agencies NUMERIC,
    lpg_distributors_total NUMERIC,
    lpg_bottling_plants NUMERIC,
    lpg_bottling_capacity_tmtpa NUMERIC
);
CREATE TABLE ppac.alternate_fuel_infrastructure (
    fuel_type TEXT PRIMARY KEY,
    total_ros_with_alt_fuel NUMERIC
);

-- Table 15: LPG consumption
CREATE TABLE ppac.lpg_consumption (
    metric TEXT PRIMARY KEY,
    fy2025_26 NUMERIC, fy2026_27_p NUMERIC,
    aug_2025_26 NUMERIC, aug_2026_27_p NUMERIC,
    apr_aug_2025_26 NUMERIC, apr_aug_2026_27_p NUMERIC
);

-- Table 16: LPG marketing time series
CREATE TABLE ppac.lpg_marketing_timeseries (
    as_on_date TEXT PRIMARY KEY,
    lpg_active_domestic_customers_lakh NUMERIC,
    lpg_coverage_pct NUMERIC,
    pmuy_beneficiaries_lakh NUMERIC,
    lpg_distributors_no NUMERIC,
    auto_lpg_dispensing_stations_no NUMERIC,
    bottling_plants_no NUMERIC
);

-- Table 17: Regionwise LPG marketing snapshot
CREATE TABLE ppac.regionwise_lpg_marketing (
    region TEXT PRIMARY KEY,
    lpg_active_domestic_customers_lakh NUMERIC,
    non_pmuy_customers_lakh NUMERIC,
    pmuy_beneficiaries_lakh NUMERIC,
    lpg_distributors_no NUMERIC,
    auto_lpg_dispensing_stations_no NUMERIC,
    bottling_plants_no NUMERIC
);

-- Table 18: Natural gas at a glance
CREATE TABLE ppac.natural_gas_glance (
    metric TEXT PRIMARY KEY,
    fy2024_25 NUMERIC, fy2025_26_p NUMERIC,
    aug_2025_26_p NUMERIC, aug_2026_27_target NUMERIC, aug_2026_27_p NUMERIC,
    apr_aug_2025_26_p NUMERIC, apr_aug_2026_27_target NUMERIC, apr_aug_2026_27_p NUMERIC
);
CREATE TABLE ppac.natural_gas_yearly_trend (
    metric TEXT PRIMARY KEY,
    fy2022_23 NUMERIC, fy2023_24 NUMERIC, fy2024_25 NUMERIC,
    fy2025_26 NUMERIC, apr_aug_2026_27_p NUMERIC
);
CREATE TABLE ppac.gas_production_by_regime_share (
    id SERIAL PRIMARY KEY,
    period TEXT,
    regime TEXT,
    pct_share NUMERIC
);

-- Table 19: CBM gas development
CREATE TABLE ppac.cbm_gas_development (
    metric TEXT PRIMARY KEY,
    value NUMERIC,
    unit TEXT
);

-- Table 19A: CBG (SATAT) status
CREATE TABLE ppac.cbg_status (
    metric TEXT PRIMARY KEY,
    value NUMERIC,
    unit TEXT
);

-- Table 20: Common carrier gas pipeline network
CREATE TABLE ppac.gas_pipeline_network (
    operator TEXT PRIMARY KEY,
    operational_length_km NUMERIC,
    operational_capacity_mmscmd NUMERIC,
    under_construction_length_km NUMERIC
);

-- Table 21: LNG terminals
CREATE TABLE ppac.lng_terminals (
    location TEXT PRIMARY KEY,
    promoter TEXT,
    capacity_mmtpa_2026_09_01 NUMERIC,
    capacity_utilisation_pct_apr_aug26 NUMERIC
);

-- Table 22: State-wise PNG/CNG status  — key table for GIS layer
CREATE TABLE ppac.state_png_cng_status (
    state_ut TEXT PRIMARY KEY,
    cng_stations NUMERIC,
    png_domestic NUMERIC,
    png_commercial NUMERIC,
    png_industrial NUMERIC
);

-- Table 23: Domestic gas price / ceiling
CREATE TABLE ppac.domestic_gas_price_ceiling (
    period TEXT PRIMARY KEY,
    domestic_gas_calculated_price_usd_mmbtu NUMERIC,
    gas_ceiling_price_ongc_oil_usd_mmbtu NUMERIC,
    hp_ht_ceiling_price_usd_mmbtu NUMERIC
);

-- Table 24: CNG/PNG city prices
CREATE TABLE ppac.cng_png_prices (
    city TEXT PRIMARY KEY,
    cng_rs_kg NUMERIC,
    png_rs_scm NUMERIC,
    source_date TEXT
);

-- Table 26: PSU capex
CREATE TABLE ppac.psu_capex (
    company TEXT PRIMARY KEY,
    fy2023_24 NUMERIC, fy2024_25 NUMERIC, fy2025_26 NUMERIC,
    fy2026_27_target NUMERIC, apr_aug_2026_27_p NUMERIC
);

-- Table 27: Conversion factors (static reference tables)
CREATE TABLE ppac.weight_to_volume_conversion (
    product TEXT PRIMARY KEY,
    weight_mt NUMERIC,
    volume_kl NUMERIC,
    barrel_bbl NUMERIC
);
CREATE TABLE ppac.general_conversions (
    id SERIAL PRIMARY KEY,
    from_unit TEXT,
    to_unit TEXT,
    factor NUMERIC
);

-- ============================================================
-- COPY commands — run from the directory containing the csv/ folder
-- psql -d your_db -f sql/schema.sql
-- \copy statements below load each CSV (adjust path as needed)
-- ============================================================
\copy ppac.crude_oil_lng_pol_glance FROM 'csv/table02_crude_oil_lng_pol_glance.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.crude_production_by_regime FROM 'csv/table03_indigenous_crude_production_by_regime.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.domestic_overseas_production FROM 'csv/table04_domestic_overseas_production.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.hs_ls_crude_processing FROM 'csv/table05_hs_ls_crude_processing.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.hs_share_pct FROM 'csv/table05b_hs_share_pct.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.crude_oil_imports_by_year FROM 'csv/table06_crude_oil_imports_by_year.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.self_sufficiency FROM 'csv/table07_self_sufficiency_petroleum_products.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.refineries FROM 'csv/table08_refineries_capacity_processing.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.pipeline_network FROM 'csv/table09_crude_product_pipeline_network.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.refining_margins FROM 'csv/table10_gross_refining_margins.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.product_production_consumption FROM 'csv/table11_production_consumption_by_product.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.pol_consumption_report FROM 'csv/table11a_pol_consumption_report_aug26.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.regionwise_consumption(product,region,fy2025_26_tmt,fy2026_27_tmt,growth_pct) FROM 'csv/table11b_regionwise_consumption_aug26.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.kerosene_allocation FROM 'csv/table12_kerosene_allocation_upliftment.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.ethanol_blending FROM 'csv/table13_ethanol_blending_summary.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.marketing_infrastructure FROM 'csv/table14_industry_marketing_infrastructure.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.alternate_fuel_infrastructure FROM 'csv/table14b_alternate_fuel_infrastructure.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.lpg_consumption FROM 'csv/table15_lpg_consumption.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.lpg_marketing_timeseries FROM 'csv/table16_lpg_marketing_timeseries.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.regionwise_lpg_marketing FROM 'csv/table17_regionwise_lpg_marketing.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.natural_gas_glance FROM 'csv/table18_natural_gas_at_a_glance.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.natural_gas_yearly_trend FROM 'csv/table18b_natural_gas_yearly_trend.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.gas_production_by_regime_share(period,regime,pct_share) FROM 'csv/table18c_gas_production_by_regime_share.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.cbm_gas_development FROM 'csv/table19_cbm_gas_development.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.cbg_status FROM 'csv/table19a_cbg_status.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.gas_pipeline_network FROM 'csv/table20_common_carrier_gas_pipeline.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.lng_terminals FROM 'csv/table21_lng_terminals.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.state_png_cng_status FROM 'csv/table22_state_png_cng_status.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.domestic_gas_price_ceiling FROM 'csv/table23_domestic_gas_price_ceiling.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.cng_png_prices FROM 'csv/table24_cng_png_prices_selected_cities.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.psu_capex FROM 'csv/table26_psu_capex.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.weight_to_volume_conversion FROM 'csv/table27a_weight_to_volume_conversion.csv' WITH (FORMAT csv, HEADER true, NULL '');
\copy ppac.general_conversions(from_unit,to_unit,factor) FROM 'csv/table27b_general_conversions.csv' WITH (FORMAT csv, HEADER true, NULL '');
