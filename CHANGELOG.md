# CHANGELOG — MAITRI Astronaut Assistant

All notable changes to the MAITRI project are documented here.

## [v2.2.0] - Phase 10 Complete (Space Mini-Games & OpenCV Mood Recommender) - 2026-08-04
### Added
- **OpenCV Mood Recognition Activity Engine**: Built `backend/vision/activity_suggester.py` mapping detected astronaut facial emotions to personalized activities, tasks, and mini-games.
- **Space Reaction Reflex Challenge**: Interactive Canvas mini-game testing zero-gravity hand-eye coordination & reaction speed (ms).
- **Gaganyaan Shuttle Docking Simulator**: Zero-g thruster vector alignment docking game.
- **Activity Suggester Unit Tests**: Created `tests/test_activity_suggester.py` expanding test suite to 30/30 passing unit tests.
- **Phase 10 Word Report**: Generated `docs/update_10.docx` expanding report series.

## [v2.1.0] - Phase 9 Complete (Local Qwen LLM Engine & Edge Inference) - 2026-08-04
### Added
- **Local Offline Qwen LLM Engine**: Created `backend/ai_engine/local_llm.py` supporting Qwen 0.5B/1.5B/7B local model inference via Ollama (`http://localhost:11434`) and llama.cpp (`http://localhost:8080`).
- **Zero-Internet Fallback Adapter**: Implemented zero-delay edge rule engine fallback if local model daemon is initializing.
- **Local LLM Test Suite**: Created `tests/test_local_llm.py` expanding test suite to 26/26 passing unit tests.
- **Phase 9 Word Report**: Generated `docs/update_09.docx` documenting offline LLM model quantization, GGUF runtimes, and Jetson/Edge PC hardware execution.

## [v2.0.0] - Phase 8 Complete (Bio-Pulse AR Coach & Multi-Page Rocket Launch) - 2026-08-04
### Added
- **Gaganyaan Bio-Pulse AR Respiration Coach**: Built `backend/health/biofeedback_coach.py` for Heart Rate Variability (HRV RMSSD) calculation, Autonomic Coherence scoring, and 4-7-8 / Box Breathing pace control.
- **AR Coherence Sphere Canvas**: Created interactive Canvas-rendered glowing AR pulse sphere with real-time Inhale/Hold/Exhale voice coaching.
- **Interactive Multi-Page Rocket Launch Routing**: Built `index.html` Entrance Portal with clickable ISRO emblem launching rocket animation into `dashboard.html`.
- **Biofeedback Unit Testing**: Created `tests/test_biofeedback.py` expanding test suite to 23/23 passing unit tests.
- **Phase 8 Word Report**: Generated `docs/update_08.docx` expanding report series.

## [v1.0.0] - Phase 7 Complete (Final Release) - 2026-08-03
### Added
- **Zero-Internet Air-Gap Auditor**: Created `scripts/audit_offline_integrity.py` scanning 27 code files to verify 100% offline air-gap compliance.
- **Space-Grade Edge Deployment Scripts**: Created `scripts/deploy_edge.sh` (Linux/Jetson/Pi) and `scripts/deploy_edge.bat` (Windows).
- **Sequential DOCX Report**: Generated `docs/update_07.docx` completing the 7-part documentation series (`update_01.docx` through `update_07.docx`).
- **Complete Test Coverage**: Verified 19/19 unit tests passing across all backend AI, vision, audio, health, personalization, and emergency modules.
