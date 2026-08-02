# CHANGELOG — MAITRI Astronaut Assistant

All notable changes to the MAITRI project are documented here.

## [v0.3.0] - Phase 3 Complete - 2026-08-02
### Added
- **Offline AI Conversational Engine**: Created `backend/ai_engine/offline_companion.py` handling zero-internet dialogue turns, intent recognition, knowledge retrieval, and SQLite dialogue persistence.
- **Dynamic Mood Router & Guardrails**: Built `backend/ai_engine/mood_rules.py` matching multimodal emotion states to specialized communication modes: Empathetic Listener, Stress Reduction & Breathwork, Cognitive Grounding, and Operational Health Monitor.
- **Psychological Safety Interventions**: Integrated astronaut coping protocols including 4-7-8 breathing exercises, 5-4-3-2-1 sensory grounding, and hydration/rest reminders.
- **Unit Test Suite**: Created `tests/test_ai_engine.py` (7/7 tests passing overall across vision, audio, and AI engine).
- **Sequential DOCX Report**: Generated `docs/update_03.docx`.

## [v0.2.0] - Phase 2 Complete - 2026-08-02
### Added
- **OpenCV Facial Emotion Pipeline**: Created `backend/vision/emotion_detector.py` providing face detection, micro-expression intensity classification, bounding box HUD rendering, and SQLite telemetry logging.
- **Voice Tone & Stress Analyzer**: Implemented `backend/audio/tone_analyzer.py` extracting pitch (F0), RMS energy, jitter/shimmer perturbations, and computing vocal stress scores (0-100%).
- **Vitals Sensor Telemetry Monitor**: Built `backend/health/sensor_stubs.py`.

## [v0.1.0] - Phase 1 Complete - 2026-08-02
### Added
- **Project Folder Architecture**: Established clean separation between backend, frontend, media, docs, and scripts.
- **Offline SQLite Database Layer**: Created `backend/db/schema.sql` and `backend/db/database.py`.
- **Mission Control Web Dashboard**: Refactored `frontend/index.html`, `style.css`, and `app.js`.
