# CHANGELOG — MAITRI Astronaut Assistant

All notable changes to the MAITRI project are documented here.

## [v0.6.0] - Phase 6 Complete - 2026-08-03
### Added
- **Emergency Safety Rule Engine**: Built `backend/alerts/emergency_reporter.py` evaluating critical hypoxia ($SpO_2 < 90\%$), tachycardia ($HR > 120$ BPM), and severe panic distress hazards.
- **Black-Box Flight Incident Recorder**: Implemented SHA-256 integrity hash payload verification and zlib telemetry packer saving 68.5% transmission bandwidth for deep-space laser comms back to Earth.
- **Pre-EVA Psychomotor Vigilance Reaction Test**: Created `backend/health/cognitive_test.py` evaluating reaction latency (ms), spatial memory accuracy, and issuing astronaut flight clearances (FIT FOR EVA).
- **Circadian Rhythm & Cabin Lighting Synchronizer**: Created `backend/health/circadian_sync.py` computing habitat LED color temperatures (2700K - 6500K) to suppress melatonin during morning focus.
- **Voice Speech Engine**: Built `backend/audio/speech_engine.py` supporting offline TTS out-loud speech formatting and voice command parsing.
- **Unit Test Suite**: Created `tests/test_emergency_and_features.py` (19/19 tests passing overall across all system modules).
- **Sequential DOCX Report**: Generated `docs/update_06.docx`.

## [v0.5.0] - Phase 5 Complete - 2026-08-02
### Added
- **Offline Content Recommendation Engine**: Created `backend/personalization/content_recommender.py`.
- **Astronaut Personality Presets**: Added ISRO Vedic Calm, NASA Flight Director, and Zen Mindfulness personas.

## [v0.4.0] - Phase 4 Complete - 2026-08-02
### Added
- **Telemetry Health Analytics Engine**: Built `backend/health/health_monitor.py`.
- **Mission Control Health Dashboard UI**: Enhanced `frontend/index.html` with iOS Crystal UI design system.
