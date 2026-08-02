# CHANGELOG — MAITRI Astronaut Assistant

All notable changes to the MAITRI project are documented here.

## [v0.1.0] - Phase 1 Complete - 2026-08-02
### Added
- **Project Folder Architecture**: Established clean separation between backend, frontend, media, docs, and scripts.
- **Offline SQLite Database Layer**: Created `backend/db/schema.sql` and `backend/db/database.py` managing 8 core telemetry and astronaut profile tables.
- **Mission Control Web Dashboard**: Refactored `frontend/index.html`, `style.css`, and `app.js` with futuristic dark sci-fi UI, glassmorphism telemetry cards, real-time vitals graphs using Chart.js, and camera visualizer.
- **Automated DOCX Progress Reporting**: Implemented `scripts/generate_docx_report.py` using `python-docx` to generate `docs/update_01.docx`.
- **GitHub Repository Ready Structure**: Added `requirements.txt`, `README.md`, `CHANGELOG.md`, and `.gitignore`.
