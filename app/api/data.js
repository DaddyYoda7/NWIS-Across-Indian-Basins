/**
 * NWIS Supabase Data & PPAC API Controller
 */
const fs = require('fs');
const path = require('path');
const { query } = require('../db/db');

const ROOT = path.resolve(__dirname, '../../');

function getJsonData(relPath) {
  try {
    const fullPath = path.join(ROOT, relPath);
    if (fs.existsSync(fullPath)) {
      return JSON.parse(fs.readFileSync(fullPath, 'utf8'));
    }
  } catch (e) {
    console.error(`Error loading JSON from ${relPath}:`, e.message);
  }
  return null;
}

/**
 * Get all wells
 */
async function getWells() {
  const wells = getJsonData('data/real_wells_intelligence.json');
  return wells || [];
}

/**
 * Get single well by ID or short code
 */
async function getWellById(id) {
  const wells = await getWells();
  return wells.find(w => w.id === id || w.short_code === id) || null;
}

/**
 * Get PPAC dataset
 */
async function getPPACData() {
  const ppac = getJsonData('data/ppac_all_tables.json');
  return ppac || {};
}

/**
 * Get Historical Incidents
 */
async function getHistoricalIncidents(wellId) {
  const incidents = getJsonData('data/historical_incidents.json') || [];
  if (!wellId) return incidents;
  return incidents.filter(i => i.well_id === wellId);
}

module.exports = {
  getWells,
  getWellById,
  getPPACData,
  getHistoricalIncidents
};
