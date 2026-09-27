/**
 * NWIS Real Petroleum Data Store
 * Integrates:
 * 1. Ministry of Petroleum & Natural Gas (PPAC) Monthly Ready Reckoner (Aug/Sept 2026, 33 Tables)
 * 2. Authentic Indian Historical Oil Wells (Nahorkatiya-1, Digboi-1, Mumbai High H-1-1, Mangala-1, Ankleshwar-1, KG-D6-D1)
 * 3. Benchmark Well Datasets (Equinor Volve 15/9-F-12)
 * 4. Real Daily Drilling Reports (DDRs), lithology logs, and operational risk events
 */

const NWISDataStore = (function() {
  let _wells = [];
  let _incidents = [];
  let _ppac = {};
  let _activeWellId = 'WELL-NHK-01'; // Default: Nahorkatiya Well No. 1 (Assam-Arakan Basin)
  let _initialized = false;

  async function init() {
    if (_initialized) return;

    try {
      const [wellsRes, incidentsRes, ppacRes] = await Promise.all([
        fetch('/data/real_wells_intelligence.json').then(r => r.json()).catch(() => null),
        fetch('/data/historical_incidents.json').then(r => r.json()).catch(() => null),
        fetch('/data/ppac_all_tables.json').then(r => r.json()).catch(() => null)
      ]);

      if (wellsRes && Array.isArray(wellsRes) && wellsRes.length > 0) {
        _wells = wellsRes;
      }
      if (incidentsRes && Array.isArray(incidentsRes) && incidentsRes.length > 0) {
        _incidents = incidentsRes;
      }
      if (ppacRes && typeof ppacRes === 'object') {
        _ppac = ppacRes;
      }
      _initialized = true;
    } catch (e) {
      console.warn('NWISDataStore loading from local JSON fell back to default cache:', e);
    }
  }

  function getWells() {
    return _wells;
  }

  function getWellById(id) {
    return _wells.find(w => w.id === id || w.short_code === id) || _wells[0];
  }

  function getActiveWell() {
    return getWellById(_activeWellId);
  }

  function setActiveWell(id) {
    const found = _wells.find(w => w.id === id || w.short_code === id);
    if (found) {
      _activeWellId = found.id;
      // Dispatch custom event so all views reactively update
      window.dispatchEvent(new CustomEvent('nwis:activeWellChanged', { detail: found }));
    }
  }

  function getHistoricalIncidents(wellId) {
    if (!wellId) return _incidents;
    return _incidents.filter(i => i.well_id === wellId);
  }

  function getPPAC() {
    return _ppac;
  }

  function getPPACGlance() {
    if (!_ppac.table02_crude_oil_lng_pol_glance) return [];
    return _ppac.table02_crude_oil_lng_pol_glance;
  }

  function getPPACRefineries() {
    if (!_ppac.table08_refineries_capacity_processing) return [];
    return _ppac.table08_refineries_capacity_processing;
  }

  function getPPACCrudeRegimes() {
    if (!_ppac.table03_indigenous_crude_production_by_regime) return [];
    return _ppac.table03_indigenous_crude_production_by_regime;
  }

  function getPPACPipelines() {
    if (!_ppac.table09_crude_product_pipeline_network) return [];
    return _ppac.table09_crude_product_pipeline_network;
  }

  function getPPACGasStats() {
    if (!_ppac.table18_natural_gas_at_a_glance) return [];
    return _ppac.table18_natural_gas_at_a_glance;
  }

  function getPPACCapex() {
    if (!_ppac.table26_psu_capex) return [];
    return _ppac.table26_psu_capex;
  }

  function getPPACStateCNG_PNG() {
    if (!_ppac.table22_state_png_cng_status) return [];
    return _ppac.table22_state_png_cng_status;
  }

  return {
    init,
    getWells,
    getWellById,
    getActiveWell,
    setActiveWell,
    getHistoricalIncidents,
    getPPAC,
    getPPACGlance,
    getPPACRefineries,
    getPPACCrudeRegimes,
    getPPACPipelines,
    getPPACGasStats,
    getPPACCapex,
    getPPACStateCNG_PNG
  };
})();

// Auto-initialize on load
if (typeof window !== 'undefined') {
  window.NWISDataStore = NWISDataStore;
  document.addEventListener('DOMContentLoaded', () => {
    NWISDataStore.init();
  });
}
