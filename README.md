# MAITRI: Multimodal AI for Total Resilience and Intelligence 🚀

[![Offline Air-Gap Certified](https://img.shields.io/badge/Offline-100%25-brightgreen.svg)]()
[![Target Hardware](https://img.shields.io/badge/Target-Jetson%20Nano%20%2F%20Pi%204%20%2F%20Laptop-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-orange.svg)]()

**MAITRI** is an advanced, offline-first multimodal AI assistant engineered specifically for astronauts on long-duration space missions (e.g. Artemis Moon/Mars habitats). Built to operate under zero-internet conditions, MAITRI acts as a psychological companion, health telemetry monitor, multimodal emotion analyzer, and personalized media engine.

---

## 🌟 Key Features

1. **Multimodal Emotion Detection Engine**: Real-time facial emotion recognition (OpenCV / PyTorch) and vocal stress tone analysis.
2. **Offline AI Psychological Companion**: Rule-enhanced empathetic conversational agent tailored for deep-space isolation and stress reduction.
3. **Astronaut Health Telemetry Dashboard**: Live monitoring for Heart Rate (BPM), SpO2 saturation, Body Temperature, Stress Index, and Sleep Quality trends via Chart.js.
4. **Offline Personalization & Entertainment**: Local media vault for offline stand-up comedy, lo-fi space ambient tracks, guided relaxation, and motivational crew recordings.
5. **Ground-Control Incident & Alert Logging**: Real-time threshold anomaly triggers and local event logging stored in SQLite (`maitri_offline.db`).
6. **Sequential DOCX Mission Reports**: Automated progress and incident logging engine (`scripts/generate_docx_report.py`) saving reports sequentially in `docs/update_XX.docx`.

---

## 📁 Repository Structure

```
MAITRI-Dashboard/
├── backend/
│   ├── db/
│   │   ├── schema.sql              # SQLite database structure DDL
│   │   └── database.py             # Offline database access layer & seeding
│   ├── vision/                     # OpenCV facial analysis pipeline
│   ├── audio/                      # Voice tone & stress analyzer
│   ├── ai_engine/                  # Conversational companion logic
│   ├── health/                     # Telemetry monitoring engine
│   ├── personalization/            # Content recommender logic
│   └── alerts/                     # Incident logger & safety rules
├── frontend/
│   ├── index.html                  # Mission Control Sci-Fi UI Layout
│   ├── style.css                   # Glassmorphism & Cyberpunk Space Design System
│   └── app.js                      # Controller & Chart.js graph initializer
├── media/                          # Local offline entertainment vault
├── docs/
│   └── update_01.docx              # Sequential Phase 1 Status Report
├── scripts/
│   └── generate_docx_report.py     # DOCX status report generator script
├── requirements.txt                # Offline Python dependencies
├── CHANGELOG.md                    # Project milestones & changelog
└── README.md                       # Comprehensive documentation
```

---

## 🚀 Quick Start & Local Execution

### 1. Initialize SQLite Database
```bash
python backend/db/database.py
```

### 2. Launch Mission Control Dashboard UI
Open `frontend/index.html` (or `index.html`) in any modern web browser.

### 3. Generate Sequential DOCX Reports
```bash
python scripts/generate_docx_report.py 1
```

---

## 📊 Phase-Wise Development Roadmap

- [x] **Phase 1: Project Foundation & Offline Database Architecture**
- [ ] **Phase 2: Multimodal Input Pipeline (OpenCV & Voice Analyzer)**
- [ ] **Phase 3: Offline AI Conversation Engine**
- [ ] **Phase 4: Health Monitoring Dashboard & Visualizations**
- [ ] **Phase 5: Personalization & Offline Entertainment**
- [ ] **Phase 6: Alerting & Ground-Control Reporting**
- [ ] **Phase 7: Offline Optimization & Edge Hardware Deployment**

---

## 👨‍🚀 Lead Developer
**Cmdr. Shalok Dadhwal** ([@Shalokexe](https://github.com/Shalokexe))  
*Deep-Space AI Systems Architect & Lead Software Engineer*
