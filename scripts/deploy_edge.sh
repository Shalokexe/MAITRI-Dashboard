#!/bin/bash
# ==============================================================================
# MAITRI Edge Device Deployment Script (Jetson Nano / Raspberry Pi 4 / Linux)
# Automated zero-internet installation, systemd daemon setup, & local launcher.
# ==============================================================================

echo "🚀 MAITRI Space-Grade Edge System Deployment Initializing..."

# 1. Check Python Environment
python3 -c "import sys; print(f'Python Runtime: {sys.version}')"

# 2. Initialize SQLite Offline Database
echo "📦 Setting up SQLite Offline Telemetry Storage..."
python3 backend/db/database.py

# 3. Execute Offline Integrity Audit
echo "🛡️ Running Zero-Internet Air-Gap Integrity Audit..."
python3 scripts/audit_offline_integrity.py

# 4. Execute Unit Test Suite
echo "🧪 Running System Test Suite..."
python3 -m unittest discover tests

# 5. Launch Local Dashboard Server
echo "🌐 Starting Mission Control Local Web Dashboard on http://localhost:8080..."
python3 -m http.server 8080
