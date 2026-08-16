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
[![Version](https://img.shields.io/badge/Release-v2.3.0%20Phase%2011-gold.svg?style=for-the-badge)]()
[![Qwen LLM](https://img.shields.io/badge/Qwen%20LLM-Local%20Ollama%20%2F%20llama.cpp-orange.svg?style=for-the-badge)]()
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?style=for-the-badge&logo=python)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-Facial%20HUD-red.svg?style=for-the-badge&logo=opencv)]()
[![SQLite](https://img.shields.io/badge/SQLite-Local%20DB-003B57.svg?style=for-the-badge&logo=sqlite)]()
[![Tests](https://img.shields.io/badge/Unit%20Tests-34%2F34%20Passed-green.svg?style=for-the-badge)]()

[Architecture](#-system-architecture) • [Features](#-key-capabilities) • [Local Qwen LLM](#-downloadable-local-qwen-offline-model) • [Quick Start](#-quick-start--local-execution) • [DOCX Reports](#-sequential-docx-progress-reports) • [Roadmap](#-upcoming-version-roadmap-v240--phase-12)

---

</div>

> [!IMPORTANT]
> **100% Zero-Internet Air-Gap Guarantee**: MAITRI is engineered from the ground up to operate completely without internet connectivity. All facial analysis, voice tone stress evaluation, physiological telemetry processing, downloadable local Qwen LLM dialogue, biofeedback respiration AR, AI Grandmaster Chess with spoken taunts, pre-EVA cognitive testing, and SQLite database storage execute locally on edge hardware.

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
                  |         backend/games/chess_agent.py                 |
                  |   ISRO Grandmaster AI Chess Engine & Spoken Taunts    |
                  +--------------------------+----------------------------+
                                             |
         +-----------------------------------+-----------------------------------+
         |                                   |                                   |
         v                                   v                                   v
[♟️ Space Crystal Chessboard]         [🎮 Space Games Suite]              [🧘 Bio-Pulse AR Coach]
Minimax AI vs Astronaut             Reflex & Docking Sims               4-7-8 Breathing Sphere
```

---

## ✨ Key Capabilities

### ♟️ 1. ISRO Grandmaster AI Chess Agent with Spoken Taunts (`backend/games/chess_agent.py`)
- Minimax Alpha-Beta chess engine with positional evaluation heuristics.
- **Human-like Spoken Commentary & Taunts**: Spoken out-loud agent dialogue ("A bold move, Cmdr. Shalok, but my knight fork threatens your rook!") with real-time tactical hints.
- **Interactive Space Crystal Canvas Board**: 8x8 crystal board with saffron/cyan space pieces and move history logging in SQLite (`chess_matches`).

### 🎮 2. Space Mini-Games Suite & OpenCV Mood Activity Recommender (`backend/vision/activity_suggester.py`)
- Maps OpenCV detected astronaut emotions (Happy, Calm, Stressed, Fatigued, Anxious, Bored) to targeted tasks and mini-games.

### 🤖 3. Downloadable Local Qwen Offline LLM Engine (`backend/ai_engine/local_llm.py`)
- Bridges **Qwen-2 0.5B / 1.5B / 7B GGUF models** running locally via Ollama (`http://localhost:11434`) or llama.cpp (`http://localhost:8080`).

### 📚 4. Astronaut Deep-Space Audiobook & E-Book Library Platform (Phase 12)
- **Leisure & Relaxation Companion**: Offline digital audiobook & e-book shelf designed so astronauts never feel alone in deep space.
- **Audiobook Player Widget**: Built-in time scrubber, play/pause controls, chapter selection, and spoken narration synthesizers.
- **Offline Library Storage**: Books stored locally in SQLite (`library_books`) with zero internet required.

---

## ⚡ Quick Start & Local Execution

### 1. Launch HTTP Dashboard Server
```bash
python -m http.server 8080
```
Open **[http://localhost:8080](http://localhost:8080)** in your browser!

### 2. Run All 34 Unit Tests
```bash
python -m unittest discover tests
```

---

## 📄 Sequential DOCX Progress Reports

The repository contains 12 Word (`.docx`) progress reports generated automatically in `docs/`:

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
| `docs/update_11.docx` | Phase 11: Grandmaster AI Chess Agent & Spoken Taunts | ✅ Verified |
| `docs/update_12.docx` | Phase 12: Astronaut Deep-Space Audiobook & E-Book Library | ✅ Verified |

---

## 🔮 Upcoming Version Roadmap (v2.4.0 & Phase 12)

| Target Release | Phase & Module | Upcoming Key Features & Core Enhancements | Status |
| :--- | :--- | :--- | :--- |
| `v2.4.0` | **Phase 12: Multi-Astronaut Telemetry Matrix** | **Group Coherence & Crew Sync**: Simultaneous multi-crew biometric stress tracking, collective HRV monitoring, and crew interaction friction diagnostics. | 🚀 In Development |
| `v2.5.0` | **Phase 13: Local WebGPU / Wasm Engine** | **Zero-Latency In-Browser LLM Execution**: Direct GPU acceleration for offline Qwen LLM inference without local HTTP socket bottlenecks. | 📅 Planned |
| `v2.6.0` | **Phase 14: Automated EVA Assistance** | **Spoken EVA Checklist & Emergency Guidance**: Voice-driven procedural checklists with live bio-telemetry safety boundary enforcement. | 📅 Planned |

### 🎯 Key Upgrades in Upcoming Version v2.4.0 (Phase 12):
- **Multi-Crew Dashboard HUD**: Real-time side-by-side telemetry overlays for up to 4 astronauts.
- **Inter-Crew Dynamic Stress Index**: Algorithmic scoring of team cohesion and cognitive burnout during long-duration deep-space simulations.
- **Expanded Test Coverage**: Adding comprehensive multi-crew edge case tests to expand suite past 40 unit tests.
- **Automated Update 12 DOCX Report**: Generation of `docs/update_12.docx` upon phase completion.

---

## 📜 License
Engineering for ISRO Gaganyaan & NASA Artemis Missions. Open Source under MIT License.
