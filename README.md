# 🚀 MAITRI: Multimodal AI for Total Resilience & Intelligence

<div align="center">

```
   ███╗   ███╗ █████╗ ██╗████████╗██████╗ ██╗    ███╗   ███╗███████╗████████╗██████╗ ██╗
   ████╗ ████║██╔══██╗██║╚══██╔══╝██╔══██╗██║    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██║
   ██╔████╔██║███████║██║   ██║   ██████╔╝██║    ██╔████╔██║█████╗     ██║   ██████╔╝██║
   ██║╚██╔╝██║██╔══██║██║   ██║   ██╔══██╗██║    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██╗██║
   ██║ ╚═╝ ██║██║  ██║██║   ██║   ██║  ██║██║    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██║
   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝
```

### *Production-Grade Offline Multimodal AI Assistant for Deep-Space Astronaut Resilience*
**NASA / ISRO Artemis-IX Lunar & Martian Habitat Architecture**

[![Offline Air-Gap](https://img.shields.io/badge/Air--Gap%20Certified-100%25%20Offline-brightgreen.svg?style=for-the-badge&logo=shield)]()
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?style=for-the-badge&logo=python)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-Facial%20HUD-red.svg?style=for-the-badge&logo=opencv)]()
[![SQLite](https://img.shields.io/badge/SQLite-Local%20DB-003B57.svg?style=for-the-badge&logo=sqlite)]()
[![Target Hardware](https://img.shields.io/badge/Edge%20Hardware-Jetson%20Nano%20%2F%20Pi%204%20%2F%20Laptop-9945FF.svg?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-orange.svg?style=for-the-badge)]()

[Architecture](#-system-architecture) • [Features](#-key-capabilities) • [Quick Start](#-quick-start--local-execution) • [Telemetry Spec](#-telemetry-specification) • [DOCX Reports](#-sequential-docx-progress-reports)

---

</div>

> [!IMPORTANT]
> **Zero-Internet Air-Gap Guarantee**: MAITRI is engineered from the ground up to operate completely without internet connectivity. All facial analysis, voice tone stress evaluation, physiological telemetry processing, AI companion dialogue, and SQLite database storage execute locally on edge hardware.

---

## 🛰️ System Architecture

```
                  +-------------------------------------------------------+
                  |         ASTRONAUT MULTIMODAL INPUT PIPELINE          |
                  +--------------------------+----------------------------+
                                             |
                   +-------------------------+-------------------------+
                   |                         |                         |
          [📷 OpenCV Vision]       [🎙️ Voice Stress]       [🫀 Vitals Telemetry]
          Facial Bounding Box      Pitch (F0) & RMS        Heart Rate, SpO2,
          Emotion & Fatigue        Vocal Perturbation      Temp, Sleep Scores
                   |                         |                         |
                   +-------------------------+-------------------------+
                                             |
                                             v
                  +-------------------------------------------------------+
                  |          backend/ai_engine/mood_rules.py             |
                  |          Dynamic Mood Router & Safety Guardrails     |
                  +--------------------------+----------------------------+
                                             |
         +-----------------------------------+-----------------------------------+
         |                                   |                                   |
         v                                   v                                   v
[🧘 Breathing Protocol]            [🧠 Offline AI Companion]          [📊 Mission Control UI]
4-7-8 Deep Breathing               Empathetic Dialogue Engine         Chart.js Telemetry
5-4-3-2-1 Grounding                Local Pattern Intent Matcher        Glassmorphism Dashboard
         |                                   |                                   |
         +-----------------------------------+-----------------------------------+
                                             |
                                             v
                  +-------------------------------------------------------+
                  |           backend/db/maitri_offline.db               |
                  |          SQLite Air-Gapped Local Storage             |
                  +-------------------------------------------------------+
```

---

## 🌟 Key Capabilities

### 1. 📷 OpenCV Facial Emotion & Stress HUD (`backend/vision/`)
* **Real-time Face Detection**: Tracks astronaut facial bounding boxes with custom high-contrast HUD overlays.
* **Micro-Expression Intensity Analysis**: Classifies facial state into 6 categories: *Focused / Neutral*, *Calm & Relaxed*, *Elevated Stress*, *Fatigue / Exhaustion*, *Anxious / High Alert*, and *Joyful / Positive*.

### 2. 🎙️ Voice Tone & Vocal Perturbation Analyzer (`backend/audio/`)
* **Acoustic Signal Processing**: Extracts Fundamental Frequency ($F_0$), RMS energy, jitter/shimmer perturbations, and speech tempo (wpm).
* **Vocal Stress Index**: Computes composite stress score ($0-100\%$) to detect vocal strain before overt behavioral symptoms manifest.

### 3. 🧠 Air-Gapped AI Companion & Mood Router (`backend/ai_engine/`)
* **Psychological Intervention Routing**: Automatically matches multimodal emotion states to evidence-based coping protocols (4-7-8 deep breathing, 5-4-3-2-1 sensory grounding, hydration reminders).
* **SQLite Dialogue Persistence**: Stores full conversational history in local database.

### 4. 🫀 Telemetry Health Analytics Dashboard (`backend/health/` & `frontend/`)
* **Physiological Safety Bounds**: Evaluates Heart Rate (50-100 BPM), SpO2 ($95\%+$), Temperature ($36-37.5\,^\circ\text{C}$), and Stress Index ($<65/100$).
* **Interactive Chart.js Visualization**: Live trend graphs, stacked sleep breakdown charts (Deep/REM/Light), and alert tickers.

---

## 🚀 Quick Start & Local Execution

### 1. Clone & Setup Workspace
```bash
git clone https://github.com/Shalokexe/MAITRI-Dashboard.git
cd MAITRI-Dashboard
```

### 2. Initialize SQLite Offline Database
```bash
python backend/db/database.py
```

### 3. Launch Mission Control Dashboard UI
Open `frontend/index.html` (or `index.html`) in any modern web browser.

### 4. Run System Test Suite
```bash
python -m unittest discover tests
```

### 5. Generate Sequential DOCX Status Reports
```bash
python scripts/generate_docx_report.py 4
```

---

## 📋 Telemetry Specification

| Telemetry Metric | Nominal Bounds | Warning Threshold | Critical Threshold | Action Triggered |
| :--- | :--- | :--- | :--- | :--- |
| **Heart Rate** | $60 - 90 \text{ BPM}$ | $>100 \text{ BPM}$ | $>120 \text{ BPM}$ | Alert Trigger & Rest Protocol |
| **Blood Oxygen (SpO2)** | $96\% - 100\%$ | $<95\%$ | $<90\%$ | Hypoxia Warning & Oxygen Check |
| **Stress Index** | $0 - 50 / 100$ | $>65 / 100$ | $>85 / 100$ | 4-7-8 Breathing Intervention |
| **Core Temperature** | $36.2 - 37.2 \,^\circ\text{C}$ | $>37.5 \,^\circ\text{C}$ | $>38.5 \,^\circ\text{C}$ | Thermal Control Alert |
| **Sleep Quality Score**| $75 - 100$ | $<70$ | $<50$ | Workload Reduction Protocol |

---

## 📑 Sequential DOCX Progress Reports

MAITRI maintains formal Microsoft Word documentation generated sequentially in `docs/`:

| Report File | Phase Covered | Key Integrations | Status |
| :--- | :--- | :--- | :--- |
| [`docs/update_01.docx`](docs/update_01.docx) | **Phase 1** | Project Architecture, SQLite DB, Web UI, DOCX Generator | ✅ Complete |
| [`docs/update_02.docx`](docs/update_02.docx) | **Phase 2** | OpenCV Face HUD, Voice Tone Analyzer, Vitals Stubs | ✅ Complete |
| [`docs/update_03.docx`](docs/update_03.docx) | **Phase 3** | Offline AI Companion, Mood Router, Breathing Protocols | ✅ Complete |
| [`docs/update_04.docx`](docs/update_04.docx) | **Phase 4** | Health Analytics Engine, Chart.js Vitals Dashboard | ✅ Complete |
| `docs/update_05.docx` | **Phase 5** | Personalization & Offline Entertainment Vault | ⏳ Scheduled |
| `docs/update_06.docx` | **Phase 6** | Emergency Alert Rules & Ground-Control Reports | ⏳ Scheduled |
| `docs/update_07.docx` | **Phase 7** | Edge Device Deployment & Zero-Internet Optimization | ⏳ Scheduled |

---

## 👨‍🚀 Lead Developer & Systems Architect
**Cmdr. Shalok Dadhwal** ([@Shalokexe](https://github.com/Shalokexe))  
*Lead AI Systems Engineer & Spacecraft Software Developer*  
*Chandigarh University — B.E. Computer Science (AI & ML)*
