/**
 * Vercel Serverless Function Handler for NWIS API
 * Handles all /api/* routes (Chatbot, Wells, PPAC, Incidents, DB Health)
 */
const path = require('path');
const { testConnection } = require('../app/db/db');
const { 
  getWells, 
  getWellById, 
  getPPACData, 
  getHistoricalIncidents 
} = require('../app/api/data');
const { handleChat, handleAudioTranscription } = require('../app/api/chat');

// Helper to parse JSON body
function parseJsonBody(req) {
  return new Promise((resolve, reject) => {
    if (req.body) {
      return resolve(typeof req.body === 'string' ? JSON.parse(req.body) : req.body);
    }
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
      if (body.length > 10 * 1024 * 1024) {
        reject(new Error('Payload too large'));
      }
    });
    req.on('end', () => {
      try {
        if (!body.trim()) return resolve({});
        resolve(JSON.parse(body));
      } catch (err) {
        reject(new Error('Invalid JSON format'));
      }
    });
    req.on('error', reject);
  });
}

// Helper to send JSON responses
function sendJson(res, statusCode, data) {
  res.writeHead(statusCode, {
    'Content-Type': 'application/json; charset=utf-8',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, X-Requested-With',
    'Cache-Control': 'no-cache, no-store, must-revalidate'
  });
  res.end(JSON.stringify(data, null, 2));
}

module.exports = async function handler(req, res) {
  // CORS & Security headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Requested-With');
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');

  // Handle OPTIONS preflight
  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    return res.end();
  }

  const urlObj = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  const pathname = urlObj.pathname;

  try {
    // 1. Groq AI Chatbot Endpoint
    if (pathname === '/api/chat' && req.method === 'POST') {
      const body = await parseJsonBody(req);
      const result = await handleChat(body);
      return sendJson(res, 200, result);
    }

    // 1b. Audio Transcription Endpoint (Groq Whisper)
    if (pathname === '/api/transcribe' && req.method === 'POST') {
      const body = await parseJsonBody(req);
      const result = await handleAudioTranscription(body.audio, body.mimeType);
      return sendJson(res, 200, result);
    }

    // 2. Supabase Health & Connection Info
    if (pathname === '/api/db/health' && req.method === 'GET') {
      const health = await testConnection();
      return sendJson(res, health.connected ? 200 : 503, health);
    }

    // 3. Wells Data API
    if (pathname === '/api/wells' && req.method === 'GET') {
      const wells = await getWells();
      return sendJson(res, 200, { success: true, count: wells.length, wells });
    }

    if (pathname.startsWith('/api/wells/') && req.method === 'GET') {
      const wellId = pathname.replace('/api/wells/', '');
      const well = await getWellById(wellId);
      if (!well) {
        return sendJson(res, 404, { success: false, error: `Well '${wellId}' not found.` });
      }
      return sendJson(res, 200, { success: true, well });
    }

    // 4. PPAC Ready Reckoner Tables API
    if (pathname === '/api/ppac' && req.method === 'GET') {
      const ppac = await getPPACData();
      return sendJson(res, 200, { success: true, ppac });
    }

    // 5. Historical Incidents API
    if (pathname === '/api/incidents' && req.method === 'GET') {
      const wellId = urlObj.searchParams.get('well_id');
      const incidents = await getHistoricalIncidents(wellId);
      return sendJson(res, 200, { success: true, count: incidents.length, incidents });
    }

    // Route Not Found
    return sendJson(res, 404, { success: false, error: `API endpoint ${pathname} not found.` });

  } catch (apiError) {
    console.error(`[Vercel API Error ${pathname}]:`, apiError.message);
    return sendJson(res, 500, {
      success: false,
      error: apiError.message || 'Internal Server Error'
    });
  }
};
