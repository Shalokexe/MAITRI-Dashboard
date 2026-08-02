# CHANGELOG — MAITRI Astronaut Assistant

All notable changes to the MAITRI project are documented here.

## [v0.4.0] - Phase 4 Complete - 2026-08-02
### Added
- **Telemetry Health Analytics Engine**: Built `backend/health/health_monitor.py` calculating overall health scores (0-100), evaluating physiological safety bounds for HR/SpO2/Temp/Stress, and compiling 24-hour telemetry trend analytics.
- **Mission Control Health Dashboard UI**: Enhanced `frontend/index.html`, `style.css`, and `app.js` with vitals gauges, alert badge status indicators, and Chart.js trend visualizers.
- **Health Test Suite**: Created `tests/test_health.py` (11/11 tests passing overall across vision, audio, AI companion, and health).
- **Sequential DOCX Report**: Generated `docs/update_04.docx`.
- **World-Class GitHub README**: Redesigned `README.md` with ASCII header banners, badges, system architecture flowcharts, and telemetry specifications table.

## [v0.3.0] - Phase 3 Complete - 2026-08-02
### Added
- **Offline AI Conversational Engine**: Created `backend/ai_engine/offline_companion.py`.
- **Dynamic Mood Router & Guardrails**: Built `backend/ai_engine/mood_rules.py`.

## [v0.2.0] - Phase 2 Complete - 2026-08-02
### Added
- **OpenCV Facial Emotion Pipeline**: Created `backend/vision/emotion_detector.py`.
- **Voice Tone & Stress Analyzer**: Implemented `backend/audio/tone_analyzer.py`.
- **Vitals Sensor Telemetry Monitor**: Built `backend/health/sensor_stubs.py`.

## [v0.1.0] - Phase 1 Complete - 2026-08-02
### Added
- **Project Folder Architecture**: Established clean separation between backend, frontend, media, docs, and scripts.
- **Offline SQLite Database Layer**: Created `backend/db/schema.sql` and `backend/db/database.py`.
