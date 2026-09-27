# NWIS — Nearby Wells Intelligence System (Across Indian Basins)

**NWIS (Nearby Wells Intelligence System)** is an advanced subsurface intelligence and geomechanics monitoring platform designed for upstream oil & gas exploration across Indian sedimentary basins (Assam-Arakan, Mumbai Offshore, Cambay, Barmer, Krishna-Godavari, and more).

---

## 🚀 Key Features

- **🌐 Geospatial Satellite Intelligence Engine**:
  - Live high-resolution GIS map powered by Esri World Imagery.
  - Interactive Indian landmark discovery wells (Nahorkatiya NHK-01, Digboi Well No. 1, Mumbai High H-1-1, Mangala-1, KG-D6 Dhirubhai-1).
  - Spatial layer inspection, UTM EPSG:32646 coordinates, and wellhead telemetry.

- **🎙️ Real-Time NWIS AI Subsurface Copilot**:
  - Instant live streaming speech-to-text recognition.
  - Powered by ultra-fast Groq LLM inference (`openai/gpt-oss-120b`, `openai/gpt-oss-20b`, `qwen/qwen3.8-27b`).
  - Context-aware drilling risk analysis, geomechanical formation guidance, and Indian basin stratigraphy.

- **🤖 Interactive AI Mascot & Proactive Prompts**:
  - Zero-latency cursor eye-tracking mascot with smooth 3-second blinks.
  - Cyclic thought bubble displaying interactive subsurface prompts every 15 seconds.

- **📊 Comprehensive Indian Basins Analytics & PPAC Data**:
  - 32 structured tables of Ministry of Petroleum & Natural Gas (PPAC) production, consumption, refinery, pipeline, and infrastructure datasets.
  - Complete SQL schemas and sample geomechanics data across Barail, Tipam, and Surma formations.

- **⚡ Glacial Precision UI Design**:
  - Precision icon rail navigation with instant switching.
  - Command Center, Well Explorer, Well Intelligence (W-204 Profile), Historical Intelligence, Risk Monitor, Scenario Lab, and Decision Support.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, Vanilla JavaScript (ES6+ Modules), Tailwind CSS, Leaflet GIS, Google Fonts (IBM Plex Sans & Mono), Material Symbols.
- **Backend**: Node.js / Express server, SQLite (`better-sqlite3`), Python analytics suite (`execution/`).
- **AI / LLM Inference**: Groq Cloud API (`@groq/sdk`) with multi-model self-healing failover.
- **Data Layers**: DGH Indian NDR releases, PPAC Ready Reckoner datasets, IMD GIS boundary shapefiles.

---

## 📦 Getting Started

### 1. Installation
```bash
git clone https://github.com/DaddyYoda7/NWIS-Across-Indian-Basins.git
cd NWIS-Across-Indian-Basins
npm install
```

### 2. Environment Configuration
Create a `.env` file in the root directory:
```env
PORT=3000
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Launch the Server
```bash
npm start
# or: node server.js
```
Open **`http://localhost:3000`** in your browser.

---

## 📁 Repository Structure

```
├── app/
│   ├── api/             # Chat and data API endpoints
│   ├── assets/          # Minimalist NWIS SVG brand marks & icons
│   ├── css/             # Glacial precision UI design system
│   ├── db/              # Database initialization and connection
│   └── js/              # Mascot, router, data store
├── data/                # Spatial shapefiles, catalog, PPAC and historical JSON data
├── directives/          # Standard Operating Procedures & agent workflows
├── execution/           # Python execution scripts and database connectors
├── views/               # Modular HTML views (Gateway, AI, Command Center, Explorer)
├── index.html           # Main Single-Page Application shell
├── server.js            # Express server and Groq AI chat routing
└── README.md            # Project documentation
```

---

## 📄 License
This project is developed for the Smart India Hackathon (SIH) — Subsurface Oil & Gas Intelligence Track.
