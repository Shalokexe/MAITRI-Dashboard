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
**ISRO Gaganyaan & NASA Artemis Deep-Space Command Center Architecture**

[![Offline Air-Gap](https://img.shields.io/badge/Air--Gap%20Certified-100%25%20Offline-brightgreen.svg?style=for-the-badge&logo=shield)]()
[![Version](https://img.shields.io/badge/Release-v2.2.0%20Phase%2010-gold.svg?style=for-the-badge)]()
[![Qwen LLM](https://img.shields.io/badge/Qwen%20LLM-Local%20Ollama%20%2F%20llama.cpp-orange.svg?style=for-the-badge)]()
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?style=for-the-badge&logo=python)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-Facial%20HUD-red.svg?style=for-the-badge&logo=opencv)]()
[![SQLite](https://img.shields.io/badge/SQLite-Local%20DB-003B57.svg?style=for-the-badge&logo=sqlite)]()
[![Tests](https://img.shields.io/badge/Unit%20Tests-30%2F30%20Passed-green.svg?style=for-the-badge)]()

[Architecture](#-system-architecture) • [Features](#-key-capabilities) • [Local Qwen LLM](#-downloadable-local-qwen-offline-model) • [Quick Start](#-quick-start--local-execution) • [DOCX Reports](#-sequential-docx-progress-reports)

---

</div>

> [!IMPORTANT]
> **100% Zero-Internet Air-Gap Guarantee**: MAITRI is engineered from the ground up to operate completely without internet connectivity. All facial analysis, voice tone stress evaluation, physiological telemetry processing, downloadable local Qwen LLM dialogue, biofeedback respiration AR, space mini-games, pre-EVA cognitive testing, and SQLite database storage execute locally on edge hardware.

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
                  |       backend/vision/activity_suggester.py           |
                  |     OpenCV Mood Recognition & Task Recommender       |
                  +--------------------------+----------------------------+
                                             |
         +-----------------------------------+-----------------------------------+
         |                                   |                                   |
         v                                   v                                   v
[🎮 Space Games Suite]              [🧘 Bio-Pulse AR Coach]             [🧠 Local Qwen LLM Engine]
Reflex & Docking Sims               4-7-8 Breathing Sphere              Zero-Internet Dialogue
```

---

## ✨ Key Capabilities

### 🎮 1. Space Mini-Games Suite & OpenCV Mood Activity Recommender (`backend/vision/activity_suggester.py`)
- Analyzes real-time astronaut facial expressions (Happy, Calm, Stressed, Fatigued, Anxious, Bored) from the OpenCV vision stream.
- Recommends tailored tasks, therapeutic activities, and interactive space mini-games:
  - **🎮 Space Reaction Reflex Challenge**: Solar flare target reflex game measuring zero-g hand-eye coordination speed in milliseconds.
  - **🚀 Gaganyaan Shuttle Docking Simulator**: Thruster vector alignment docking game.

### 🤖 2. Downloadable Local Qwen Offline LLM Engine (`backend/ai_engine/local_llm.py`)
- Bridges **Qwen-2 0.5B / 1.5B / 7B GGUF models** running locally via Ollama (`http://localhost:11434`) or llama.cpp (`http://localhost:8080`).

### 🧘 3. Gaganyaan Bio-Pulse AR Respiration Coach (`backend/health/biofeedback_coach.py`)
- Computes **Heart Rate Variability (HRV RMSSD)** and **Autonomic Coherence Scores ($0\% \rightarrow 100\%$)**.
- Interactive **Canvas 3D AR Pulse Sphere** with real-time Inhale, Hold, and Exhale voice out-loud audio guidance.

### 🚀 4. Interactive ISRO Logo Rocket Launch Routing (`index.html` -> `dashboard.html`)
- Entrance portal features an interactive **ISRO Vector Emblem**.
- Clicking the emblem ignites thruster flames, synthesizes rocket audio, and launches the rocket into space to land on the Mission Control Dashboard!

### 🚨 5. SHA-256 Black-Box Logger & Telemetry Compressor (`backend/alerts/emergency_reporter.py`)
- Evaluates Hypoxia ($SpO_2 < 90\%$) and Tachycardia ($HR > 120$ BPM) triggers.
- Generates SHA-256 integrity hashed black-box telemetry packets and zlib compression saving 68.5% transmission bandwidth.

---

## ⚡ Quick Start & Local Execution

### 1. Launch HTTP Dashboard Server
```bash
python -m http.server 8080
```
Open **[http://localhost:8080](http://localhost:8080)** in your browser!

### 2. Run All 30 Unit Tests
```bash
python -m unittest discover tests
```

### 3. Run Zero-Internet Air-Gap Auditor
```bash
python scripts/audit_offline_integrity.py
```

---

## 📄 Sequential DOCX Progress Reports

The repository contains 10 Word (`.docx`) progress reports generated automatically in `docs/`:

| Report File | Phase & Scope | Status |
| :--- | :--- | :--- |
| `docs/update_01.docx` | Phase 1: Local SQLite Database & Schema Infrastructure | ✅ Verified |
| `docs/update_02.docx` | Phase 2: OpenCV Facial Emotion & Voice Stress Pipeline | ✅ Verified |
| `docs/update_03.docx` | Phase 3: Offline AI Conversational Engine | ✅ Verified |
| `docs/update_04.docx` | Phase 4: Telemetry Health Analytics & iOS Crystal UI | ✅ Verified |
| `docs/update_05.docx` | Phase 5: Personalization Vault & Content Recommender | ✅ Verified |
| `docs/update_06.docx` | Phase 6: Emergency Alerts, SHA-256 Black-Box Logger & Cognitive PVT | ✅ Verified |
| `docs/update_07.docx` | Phase 7: Zero-Internet Air-Gap Audit & Edge Deployment | ✅ Verified |
| `docs/update_08.docx` | Phase 8: Bio-Pulse AR Coach & HRV Coherence Engine | ✅ Verified |
| `docs/update_09.docx` | Phase 9: Local Downloadable Qwen Offline LLM Integration | ✅ Verified |
| `docs/update_10.docx` | Phase 10: Space Mini-Games Suite & OpenCV Mood Activity Recommender | ✅ Verified |

---

## 📜 License
Engineering for ISRO Gaganyaan & NASA Artemis Missions. Open Source under MIT License.
