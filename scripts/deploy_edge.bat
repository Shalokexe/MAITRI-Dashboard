@echo off
REM MAITRI Space-Grade Edge System Deployment Script (Windows Laptop / Edge PC)
echo 🚀 MAITRI Space-Grade Edge System Deployment Initializing...

python backend\db\database.py
python scripts\audit_offline_integrity.py
python -m unittest discover tests

echo 🌐 Starting Mission Control Local Web Dashboard on http://localhost:8080...
python -m http.server 8080
