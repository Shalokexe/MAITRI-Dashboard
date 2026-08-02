# CHANGELOG — MAITRI Astronaut Assistant

All notable changes to the MAITRI project are documented here.

## [v0.5.0] - Phase 5 Complete - 2026-08-02
### Added
- **Offline Content Recommendation Engine**: Created `backend/personalization/content_recommender.py` matching astronaut real-time emotional state to local media catalog items (comedy, lo-fi space music, binaural sleep audio, motivational crew recordings).
- **Astronaut Personality Presets**: Added customizable companion personas: ISRO Vedic Calm, NASA Flight Director, and Zen Mindfulness.
- **Personalization Unit Test Suite**: Created `tests/test_personalization.py` (14/14 tests passing overall).
- **Sequential DOCX Report**: Generated `docs/update_05.docx`.

## [v0.4.0] - Phase 4 Complete - 2026-08-02
### Added
- **Telemetry Health Analytics Engine**: Built `backend/health/health_monitor.py`.
- **Mission Control Health Dashboard UI**: Enhanced `frontend/index.html` with dynamic vitals gauges & Chart.js visualizers.

## [v0.3.0] - Phase 3 Complete - 2026-08-02
### Added
- **Offline AI Conversational Engine**: Created `backend/ai_engine/offline_companion.py`.
- **Dynamic Mood Router & Guardrails**: Built `backend/ai_engine/mood_rules.py`.

## [v0.2.0] - Phase 2 Complete - 2026-08-02
### Added
- **OpenCV Facial Emotion Pipeline**: Created `backend/vision/emotion_detector.py`.
- **Voice Tone & Stress Analyzer**: Implemented `backend/audio/tone_analyzer.py`.
