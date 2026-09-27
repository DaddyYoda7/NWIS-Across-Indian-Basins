/**
 * NWIS Glacial Precision Framework Server
 * Node.js Server with Groq AI Chatbot, Supabase Data Integration & Static File Serving.
 */
require('dotenv').config();
const http = require('http');
const fs = require('fs');
const path = require('path');
const { testConnection } = require('./app/db/db');
const { 
  getWells, 
  getWellById, 
  getPPACData, 
  getHistoricalIncidents 
} = require('./app/api/data');
const { handleChat, handleAudioTranscription } = require('./app/api/chat');

const PORT = process.env.PORT || 3000;
const ROOT = path.resolve(__dirname);

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.txt': 'text/plain; charset=utf-8',
};

// Helper to parse JSON body
function parseJsonBody(req) {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
      if (body.length > 10 * 1024 * 1024) { // allow audio payload up to 10MB
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

const server = http.createServer(async (req, res) => {
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

  // ==========================================
  // REST API ROUTING
  // ==========================================
  if (pathname.startsWith('/api/')) {
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
      console.error(`[API Error ${pathname}]:`, apiError.message);
      return sendJson(res, 500, {
        success: false,
        error: apiError.message || 'Internal Server Error'
      });
    }
  }

  // ==========================================
  // STATIC FILE SERVING
  // ==========================================
  let sanitizedUrl = pathname;
  if (sanitizedUrl === '/') {
    sanitizedUrl = '/index.html';
  }

  const filePath = path.join(ROOT, decodeURIComponent(sanitizedUrl));

  // Prevent path traversal
  if (!filePath.startsWith(ROOT)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    return res.end('403 Forbidden');
  }

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      return res.end(`404 Not Found: ${sanitizedUrl}`);
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    res.writeHead(200, { 'Content-Type': contentType });
    fs.createReadStream(filePath).pipe(res);
  });
});

// Start Server
server.listen(PORT, () => {
  console.log('='.repeat(70));
  console.log('  NWIS Subsurface Intelligence — Groq AI & Glacial Precision Server');
  console.log('='.repeat(70));
  console.log(`  Portal URL:       http://localhost:${PORT}/index.html`);
  console.log(`  NWIS AI Chat:     http://localhost:${PORT}/#nwis-ai`);
  console.log(`  Data Endpoints:   GET /api/wells, GET /api/ppac, POST /api/chat`);
  console.log('='.repeat(70));
  console.log('  Modules:');
  console.log(`  - Command Center: http://localhost:${PORT}/#command-center`);
  console.log(`  - Well Explorer:  http://localhost:${PORT}/#well-explorer`);
  console.log(`  - Well Profile:   http://localhost:${PORT}/#well-intelligence`);
  console.log(`  - Historical:     http://localhost:${PORT}/#historical-intelligence`);
  console.log(`  - NWIS AI:        http://localhost:${PORT}/#nwis-ai`);
  console.log(`  - Risk Monitor:   http://localhost:${PORT}/#risk-monitor`);
  console.log(`  - Scenario Lab:   http://localhost:${PORT}/#scenario-lab`);
  console.log(`  - Reports:        http://localhost:${PORT}/#reports`);
  console.log(`  - Entry Gateway:  http://localhost:${PORT}/#gateway`);
  console.log('='.repeat(70));
});
