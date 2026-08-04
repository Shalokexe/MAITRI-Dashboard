# CHANGELOG — MAITRI Astronaut Assistant

All notable changes to the MAITRI project are documented here.

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

## [v0.6.0] - Phase 6 Complete - 2026-08-03
### Added
- **Emergency Safety Rule Engine**: Built `backend/alerts/emergency_reporter.py`.
- **Black-Box Flight Incident Recorder**: Implemented SHA-256 integrity hash verification and zlib telemetry compressor.
- **Pre-EVA Psychomotor Vigilance Reaction Test**: Created `backend/health/cognitive_test.py`.
- **Circadian Rhythm Lighting Synchronizer**: Created `backend/health/circadian_sync.py`.
- **Voice Speech Engine**: Built `backend/audio/speech_engine.py` (TTS out-loud synthesis & voice command parsing).

## [v0.5.0] - Phase 5 Complete - 2026-08-02
### Added
- **Offline Content Recommendation Engine**: Created `backend/personalization/content_recommender.py`.
- **Astronaut Personality Presets**: Added ISRO Vedic Calm, NASA Flight Director, and Zen Mindfulness personas.

## [v0.4.0] - Phase 4 Complete - 2026-08-02
### Added
- **Telemetry Health Analytics Engine**: Built `backend/health/health_monitor.py`.
- **Mission Control Health Dashboard UI**: Enhanced `frontend/index.html` with iOS Crystal UI design system.

## [v0.3.0] - Phase 3 Complete - 2026-08-02
### Added
- **Offline AI Conversational Engine**: Created `backend/ai_engine/offline_companion.py`.

## [v0.2.0] - Phase 2 Complete - 2026-08-02
### Added
- **OpenCV Facial Emotion Pipeline**: Created `backend/vision/emotion_detector.py`.
- **Voice Tone & Stress Analyzer**: Implemented `backend/audio/tone_analyzer.py`.

## [v0.1.0] - Phase 1 Complete - 2026-08-02
### Added
- **Local SQLite Database Infrastructure**: Created schema for `vitals`, `emotions`, and `conversations`.
