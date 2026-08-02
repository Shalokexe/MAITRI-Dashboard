-- MAITRI Offline Database Schema (SQLite)
-- Database: maitri_offline.db

CREATE TABLE IF NOT EXISTS astronaut_profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    astronaut_id TEXT UNIQUE NOT NULL,
    full_name TEXT NOT NULL,
    mission_name TEXT DEFAULT 'Artemis-IX',
    role TEXT DEFAULT 'Mission Specialist',
    stress_threshold REAL DEFAULT 75.0,
    preferred_personality TEXT DEFAULT 'Empathetic & Calm',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS emotion_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    emotion TEXT NOT NULL,          -- Happy, Neutral, Stressed, Anxious, Fatigue, Sad
    confidence REAL NOT NULL,       -- 0.0 to 1.0
    source TEXT NOT NULL,           -- facial_analysis, voice_tone, manual_checkin
    notes TEXT
);

CREATE TABLE IF NOT EXISTS vitals_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    heart_rate INTEGER NOT NULL,    -- bpm
    spo2 INTEGER NOT NULL,          -- percentage (e.g. 98)
    body_temp REAL DEFAULT 36.8,    -- celsius
    stress_index REAL NOT NULL,     -- 0 to 100
    status TEXT DEFAULT 'NORMAL'    -- NORMAL, WARNING, CRITICAL
);

CREATE TABLE IF NOT EXISTS sleep_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_date DATE UNIQUE NOT NULL,
    duration_hours REAL NOT NULL,
    deep_sleep_hours REAL DEFAULT 0.0,
    rem_sleep_hours REAL DEFAULT 0.0,
    quality_score INTEGER NOT NULL,  -- 0 to 100
    disruptions_count INTEGER DEFAULT 0,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    severity TEXT NOT NULL,         -- LOW, MEDIUM, HIGH, CRITICAL
    category TEXT NOT NULL,         -- PSYCHOLOGICAL, PHYSICAL, SYSTEM, ENVIRONMENT
    title TEXT NOT NULL,
    message TEXT NOT NULL,
    is_acknowledged INTEGER DEFAULT 0,
    resolution_notes TEXT
);

CREATE TABLE IF NOT EXISTS recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    media_type TEXT NOT NULL,       -- comedy, music, relaxation, motivation
    title TEXT NOT NULL,
    content_path TEXT NOT NULL,
    reason TEXT NOT NULL,
    feedback_rating INTEGER DEFAULT 0  -- 1 to 5 stars
);

CREATE TABLE IF NOT EXISTS conversation_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sender TEXT NOT NULL,           -- astronaut, maitri_ai
    message TEXT NOT NULL,
    detected_mood TEXT DEFAULT 'Neutral',
    bot_mode TEXT DEFAULT 'Psychological Companion'
);

CREATE TABLE IF NOT EXISTS system_updates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phase_number INTEGER NOT NULL,
    phase_title TEXT NOT NULL,
    summary TEXT NOT NULL,
    docx_report_path TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
