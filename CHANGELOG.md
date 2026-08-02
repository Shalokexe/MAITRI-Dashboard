# CHANGELOG — MAITRI Astronaut Assistant

All notable changes to the MAITRI project are documented here.

## [v0.2.0] - Phase 2 Complete - 2026-08-02
### Added
- **OpenCV Facial Emotion Pipeline**: Created `backend/vision/emotion_detector.py` providing face detection, micro-expression intensity classification, bounding box HUD rendering, and SQLite telemetry logging.
- **Voice Tone & Stress Analyzer**: Implemented `backend/audio/tone_analyzer.py` extracting pitch (F0), RMS energy, jitter/shimmer perturbations, and computing vocal stress scores (0-100%).
- **Vitals Sensor Telemetry Monitor**: Built `backend/health/sensor_stubs.py` handling Heart Rate, SpO2, core temperature, and sleep quality logging with automated threshold warning triggers.
- **Unit Test Suite**: Created `tests/test_vision.py` and `tests/test_audio.py` verifying vision and voice tone inference pipelines under 100% offline conditions.
- **Sequential DOCX Report**: Generated `docs/update_02.docx`.

## [v0.1.0] - Phase 1 Complete - 2026-08-02
### Added
- **Project Folder Architecture**: Established clean separation between backend, frontend, media, docs, and scripts.
- **Offline SQLite Database Layer**: Created `backend/db/schema.sql` and `backend/db/database.py` managing 8 core telemetry and astronaut profile tables.
- **Mission Control Web Dashboard**: Refactored `frontend/index.html`, `style.css`, and `app.js` with futuristic dark sci-fi UI.
- **Automated DOCX Progress Reporting**: Implemented `scripts/generate_docx_report.py` saving `docs/update_01.docx`.
