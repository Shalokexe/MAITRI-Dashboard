# CHANGELOG — MAITRI Astronaut Assistant

All notable changes to the MAITRI project are documented here.

## [v2.3.0] - Phase 11 Complete (ISRO Grandmaster AI Chess Agent & Spoken Taunts) - 2026-08-04
### Added
- **ISRO Grandmaster AI Chess Engine**: Built `backend/games/chess_agent.py` featuring Minimax Alpha-Beta search, piece positional evaluation, and SQLite match tracking (`chess_matches`).
- **Interactive Space Crystal Chessboard**: Created 8x8 Canvas board with saffron & cyan piece rendering and interactive movement controls.
- **Spoken AI Taunts & Tactical Hints**: Integrated human-like agent commentary ("A bold move, Cmdr. Shalok, but my knight fork threatens your rook!") with voice out-loud synthesis.
- **Chess Agent Unit Tests**: Created `tests/test_chess_agent.py` expanding test suite to 34/34 passing unit tests.
- **Phase 11 Word Report**: Generated `docs/update_11.docx` expanding report series.

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
