/**
 * NWIS AI Chatbot Engine Powered by Groq Cloud
 * Versatile conversational AI assistant equipped with full domain knowledge of NWIS, Indian oil wells, and PPAC statistics.
 */
const https = require('https');
const fs = require('fs');
const path = require('path');

const GROQ_API_KEY = process.env.GROQ_API_KEY || '';
const PRIMARY_MODEL = process.env.GROQ_MODEL || 'openai/gpt-oss-120b';
const FALLBACK_MODEL = 'openai/gpt-oss-20b';
const SECONDARY_FALLBACK = 'qwen/qwen3.8-27b';

const ROOT = path.resolve(__dirname, '../../');

function loadSystemKnowledge() {
  try {
    const wellsPath = path.join(ROOT, 'data/real_wells_intelligence.json');
    if (fs.existsSync(wellsPath)) {
      const wells = JSON.parse(fs.readFileSync(wellsPath, 'utf8'));
      return wells.map(w => 
        `• [${w.id}: ${w.name}] Basin: ${w.basin}, Field: ${w.field}, Depth: ${w.total_depth_md_m}m, Primary: ${w.target_formation}, History: ${w.discovery_history?.how_found || ''}`
      ).join('\n');
    }
    return '';
  } catch (err) {
    return '';
  }
}

const KNOWLEDGE_BASE = loadSystemKnowledge();

const SYSTEM_PROMPT = `You are "NWIS AI", an intelligent, versatile, and friendly conversational assistant.

Capabilities:
1. General Assistant: Help with any general questions, everyday conversation, coding, explanations, writing, math, or creative requests.
2. NWIS & Subsurface Domain: Provide accurate, authoritative answers on Indian petroleum basins, drilling engineering, Nahorkatiya NHK-01, Digboi, Mumbai High, Mangala, Ankleshwar, KG-D6, and PPAC statistics when asked.
3. Site Navigation Links: Direct users with markdown links like [Command Center](#command-center), [Well Explorer](#well-explorer), [Well Profile](#well-intelligence), [Historical Intelligence](#historical-intelligence), [Risk Monitor](#risk-monitor), [Scenario Lab](#scenario-lab), [Reports](#reports).

Reference Data:
${KNOWLEDGE_BASE}`;

/**
 * Handle chat conversation request with Groq Cloud API with multi-tier fallback
 */
async function handleChat({ message, history = [], activeWellId = null }) {
  if (!message || typeof message !== 'string' || !message.trim()) {
    throw new Error('Message is required.');
  }

  const messages = [
    { role: 'system', content: SYSTEM_PROMPT }
  ];

  if (Array.isArray(history) && history.length > 0) {
    const recentHistory = history.slice(-4);
    for (const h of recentHistory) {
      if (h.role && h.content) {
        messages.push({ role: h.role, content: h.content });
      }
    }
  }

  messages.push({ role: 'user', content: message.trim() });

  try {
    return await executeGroqCompletion(PRIMARY_MODEL, messages);
  } catch (err) {
    console.warn(`[Groq Primary Model ${PRIMARY_MODEL} failed, trying ${FALLBACK_MODEL}]:`, err.message);
    try {
      return await executeGroqCompletion(FALLBACK_MODEL, messages);
    } catch (err2) {
      console.warn(`[Groq Model ${FALLBACK_MODEL} failed, trying ${SECONDARY_FALLBACK}]:`, err2.message);
      return await executeGroqCompletion(SECONDARY_FALLBACK, messages);
    }
  }
}

function executeGroqCompletion(modelName, messages) {
  const payload = JSON.stringify({
    model: modelName,
    messages,
    temperature: 0.6,
    max_tokens: 800,
    top_p: 0.95
  });

  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'api.groq.com',
      port: 443,
      path: '/openai/v1/chat/completions',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${GROQ_API_KEY}`,
        'Content-Length': Buffer.byteLength(payload)
      }
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => { data += chunk; });
      res.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          if (res.statusCode >= 200 && res.statusCode < 300) {
            const reply = parsed.choices && parsed.choices[0] && parsed.choices[0].message
              ? parsed.choices[0].message.content
              : 'I could not generate a response. Please try again.';
            resolve({
              success: true,
              reply,
              model: modelName
            });
          } else {
            reject(new Error(parsed.error ? parsed.error.message : `Groq API returned status ${res.statusCode}`));
          }
        } catch (e) {
          reject(new Error(`Failed to parse Groq API response: ${e.message}`));
        }
      });
    });

    req.on('error', (e) => {
      reject(new Error(`Network error connecting to Groq AI: ${e.message}`));
    });

    req.write(payload);
    req.end();
  });
}

/**
 * Transcribe base64 audio buffer using Groq Whisper API
 */
async function handleAudioTranscription(base64Audio, mimeType = 'audio/webm') {
  if (!base64Audio) throw new Error('Audio data is required.');
  
  const buffer = Buffer.from(base64Audio, 'base64');
  const boundary = '----WebKitFormBoundary' + Math.random().toString(36).substring(2);
  const ext = mimeType.includes('wav') ? 'wav' : (mimeType.includes('mp4') ? 'm4a' : 'webm');
  const filename = `recording.${ext}`;

  const header = `--${boundary}\r\nContent-Disposition: form-data; name="model"\r\n\r\nwhisper-large-v3-turbo\r\n--${boundary}\r\nContent-Disposition: form-data; name="file"; filename="${filename}"\r\nContent-Type: ${mimeType}\r\n\r\n`;
  const footer = `\r\n--${boundary}--\r\n`;

  const payload = Buffer.concat([
    Buffer.from(header, 'utf8'),
    buffer,
    Buffer.from(footer, 'utf8')
  ]);

  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'api.groq.com',
      port: 443,
      path: '/openai/v1/audio/transcriptions',
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${GROQ_API_KEY}`,
        'Content-Type': `multipart/form-data; boundary=${boundary}`,
        'Content-Length': payload.length
      }
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => { data += chunk; });
      res.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          if (res.statusCode >= 200 && res.statusCode < 300) {
            resolve({
              success: true,
              text: parsed.text || ''
            });
          } else {
            reject(new Error(parsed.error ? parsed.error.message : `Whisper transcription failed (status ${res.statusCode})`));
          }
        } catch (err) {
          reject(new Error('Failed parsing Whisper response: ' + err.message));
        }
      });
    });

    req.on('error', (err) => {
      reject(new Error('Whisper network error: ' + err.message));
    });

    req.write(payload);
    req.end();
  });
}

module.exports = {
  handleChat,
  handleAudioTranscription
};
