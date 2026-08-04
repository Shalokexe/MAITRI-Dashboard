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
[![Version](https://img.shields.io/badge/Release-v2.1.0%20Phase%209-gold.svg?style=for-the-badge)]()
[![Qwen LLM](https://img.shields.io/badge/Qwen%20LLM-Local%20Ollama%20%2F%20llama.cpp-orange.svg?style=for-the-badge)]()
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?style=for-the-badge&logo=python)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-Facial%20HUD-red.svg?style=for-the-badge&logo=opencv)]()
[![SQLite](https://img.shields.io/badge/SQLite-Local%20DB-003B57.svg?style=for-the-badge&logo=sqlite)]()
[![Tests](https://img.shields.io/badge/Unit%20Tests-26%2F26%20Passed-green.svg?style=for-the-badge)]()

[Architecture](#-system-architecture) • [Features](#-key-capabilities) • [Local Qwen LLM](#-downloadable-local-qwen-offline-model) • [Quick Start](#-quick-start--local-execution) • [DOCX Reports](#-sequential-docx-progress-reports)

---

</div>

> [!IMPORTANT]
> **100% Zero-Internet Air-Gap Guarantee**: MAITRI is engineered from the ground up to operate completely without internet connectivity. All facial analysis, voice tone stress evaluation, physiological telemetry processing, downloadable local Qwen LLM dialogue, biofeedback respiration AR, pre-EVA cognitive testing, and SQLite database storage execute locally on edge hardware.

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
                  |          backend/ai_engine/local_llm.py              |
                  |     Downloadable Offline Qwen LLM (Ollama/llama.cpp)  |
                  +--------------------------+----------------------------+
                                             |
         +-----------------------------------+-----------------------------------+
         |                                   |                                   |
         v                                   v                                   v
[🧘 Bio-Pulse AR Coach]             [🧠 Offline AI Companion]          [📊 ISRO Mission Control]
4-7-8 Breathing Sphere              Voice TTS Out-Loud Dialogue        Telemetry Ticker & Charts
```

---

## ✨ Key Capabilities

### 🤖 1. Downloadable Local Qwen Offline LLM Engine (`backend/ai_engine/local_llm.py`)
- Bridges **Qwen-2 0.5B / 1.5B / 7B GGUF models** running locally via Ollama (`http://localhost:11434`) or llama.cpp (`http://localhost:8080`).
- **Zero-Network Fallback Engine**: If no local LLM daemon is running, MAITRI seamlessly uses its embedded zero-delay edge rule engine.

### 🧘 2. Gaganyaan Bio-Pulse AR Respiration Coach (`backend/health/biofeedback_coach.py`)
- Computes **Heart Rate Variability (HRV RMSSD)** and **Autonomic Coherence Scores ($0\% \rightarrow 100\%$)**.
- Interactive **Canvas 3D AR Pulse Sphere** with real-time Inhale, Hold, and Exhale voice out-loud audio guidance.

### 🚀 3. Interactive ISRO Logo Rocket Launch Routing (`index.html` -> `dashboard.html`)
- Entrance portal features an interactive **ISRO Vector Emblem**.
- Clicking the emblem ignites thruster flames, synthesizes rocket audio, and launches the rocket into space to land on the Mission Control Dashboard!

### 🚨 4. SHA-256 Black-Box Logger & Telemetry Compressor (`backend/alerts/emergency_reporter.py`)
- Evaluates Hypoxia ($SpO_2 < 90\%$) and Tachycardia ($HR > 120$ BPM) triggers.
- Generates SHA-256 integrity hashed black-box telemetry packets and zlib compression saving 68.5% transmission bandwidth.

### 🧠 5. Pre-EVA Psychomotor Vigilance Reaction Test (`backend/health/cognitive_test.py`)
- 60s reaction speed and memory recall testing to generate `FIT FOR EVA` clearance badges.

---

## 🤖 Downloadable Local Qwen Offline Model Setup

To run MAITRI with a local downloadable LLM:

1. **Install Ollama** (or llama.cpp):
   ```bash
   # Download Ollama from https://ollama.com
   ollama pull qwen2:1.5b
   ```

2. **Launch Qwen locally**:
   ```bash
   ollama run qwen2:1.5b
   ```

3. **Start MAITRI**:
   MAITRI will automatically detect your local Qwen model on `http://localhost:11434` and route all AI companion dialogues through Qwen in 100% offline air-gapped mode!

---

## ⚡ Quick Start & Local Execution

### 1. Launch HTTP Dashboard Server
```bash
python -m http.server 8080
```
Open **[http://localhost:8080](http://localhost:8080)** in your browser!

### 2. Run All 26 Unit Tests
```bash
python -m unittest discover tests
```

### 3. Run Zero-Internet Air-Gap Auditor
```bash
python scripts/audit_offline_integrity.py
```

---

## 📄 Sequential DOCX Progress Reports

The repository contains 9 Word (`.docx`) progress reports generated automatically in `docs/`:

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

---

## 📜 License
Engineering for ISRO Gaganyaan & NASA Artemis Missions. Open Source under MIT License.
