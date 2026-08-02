"""
MAITRI Offline Database Access Layer (SQLite)
Provides zero-internet local database management, CRUD operations, seed data generation,
and historical telemetry retrieval for the MAITRI Astronaut Assistant.
"""

import os
import sqlite3
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), "maitri_offline.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

def get_connection(db_path=DB_PATH):
    """Establishes and returns an SQLite database connection with row factory enabled."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path=DB_PATH, schema_path=SCHEMA_PATH):
    """Initializes SQLite database tables using the schema.sql DDL script."""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = get_connection(db_path)
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()
    conn.executescript(schema_sql)
    conn.commit()
    conn.close()
    print(f"[MAITRI DB] Offline database initialized successfully at: {db_path}")

def seed_sample_data(db_path=DB_PATH):
    """Seeds realistic initial mission data for Astronaut Cmdr. Shalok Dadhwal and telemetry logs."""
    conn = get_connection(db_path)
    cursor = conn.cursor()

    # 1. Astronaut Profile
    cursor.execute("SELECT COUNT(*) FROM astronaut_profile")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO astronaut_profile (astronaut_id, full_name, mission_name, role, stress_threshold, preferred_personality)
            VALUES (?, ?, ?, ?, ?, ?)
        """, ('ASTRO-706', 'Cmdr. Shalok Dadhwal', 'Artemis Deep-Space IX', 'Lead Systems & AI Engineer', 75.0, 'Empathetic & Calm'))

    # 2. Vitals & Telemetry History (Last 24 Hours mock data)
    cursor.execute("SELECT COUNT(*) FROM vitals_history")
    if cursor.fetchone()[0] == 0:
        now = datetime.now()
        sample_vitals = [
            ((now - timedelta(hours=i*2)).isoformat(), 68 + (i % 5), 98 - (i % 2), round(36.6 + (i*0.05 % 0.4), 1), round(22.0 + (i * 3.5 % 30), 1), 'NORMAL')
            for i in range(12)
        ]
        cursor.executemany("""
            INSERT INTO vitals_history (timestamp, heart_rate, spo2, body_temp, stress_index, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, sample_vitals)

    # 3. Emotion Logs
    cursor.execute("SELECT COUNT(*) FROM emotion_logs")
    if cursor.fetchone()[0] == 0:
        now = datetime.now()
        sample_emotions = [
            ((now - timedelta(hours=6)).isoformat(), 'Focused', 0.92, 'facial_analysis', 'Baseline focus during EVA prep'),
            ((now - timedelta(hours=3)).isoformat(), 'Calm', 0.88, 'voice_tone', 'Routine communication check'),
            ((now - timedelta(hours=1)).isoformat(), 'Elevated Stress', 0.76, 'facial_analysis', 'Minor alert during trajectory adjustment')
        ]
        cursor.executemany("""
            INSERT INTO emotion_logs (timestamp, emotion, confidence, source, notes)
            VALUES (?, ?, ?, ?, ?)
        """, sample_emotions)

    # 4. Sleep Records
    cursor.execute("SELECT COUNT(*) FROM sleep_records")
    if cursor.fetchone()[0] == 0:
        today = datetime.now().date()
        sample_sleep = [
            (str(today - timedelta(days=2)), 7.5, 2.2, 1.8, 88, 0, 'Optimal recovery cycle'),
            (str(today - timedelta(days=1)), 6.8, 1.9, 1.4, 79, 1, 'Minor noise disruption in Module B'),
            (str(today), 7.2, 2.1, 1.6, 84, 0, 'Restful sleep cycle achieved')
        ]
        cursor.executemany("""
            INSERT INTO sleep_records (log_date, duration_hours, deep_sleep_hours, rem_sleep_hours, quality_score, disruptions_count, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, sample_sleep)

    # 5. Alerts History
    cursor.execute("SELECT COUNT(*) FROM alerts")
    if cursor.fetchone()[0] == 0:
        now = datetime.now()
        sample_alerts = [
            ((now - timedelta(hours=12)).isoformat(), 'LOW', 'PSYCHOLOGICAL', 'Hydration & Break Reminder', 'High cognitive workload detected. Recommend 10min relaxation module.', 1, 'Completed 10m ambient music session'),
            ((now - timedelta(hours=2)).isoformat(), 'MEDIUM', 'PHYSICAL', 'Elevated Heart Rate Spike', 'Heart rate exceeded 90 bpm during resting interval.', 1, 'Vitals normalized within 5 mins')
        ]
        cursor.executemany("""
            INSERT INTO alerts (timestamp, severity, category, title, message, is_acknowledged, resolution_notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, sample_alerts)

    # 6. Conversation Logs
    cursor.execute("SELECT COUNT(*) FROM conversation_logs")
    if cursor.fetchone()[0] == 0:
        now = datetime.now()
        sample_chats = [
            ((now - timedelta(minutes=45)).isoformat(), 'astronaut', 'MAITRI, status report for lunar transfer orbit module.', 'Neutral', 'Mission Logistics'),
            ((now - timedelta(minutes=44)).isoformat(), 'maitri_ai', 'All life support systems operational, Cmdr. Shalok. Hull pressure stable at 101.3 kPa, SpO2 optimal at 98%.', 'Neutral', 'Psychological Companion'),
            ((now - timedelta(minutes=15)).isoformat(), 'astronaut', 'Feeling a bit fatigued after that 4-hour simulation session.', 'Fatigue', 'Empathetic Companion'),
            ((now - timedelta(minutes=14)).isoformat(), 'maitri_ai', 'Understood, Commander. I recommend a 15-minute relaxation audio session and a brief hydration check. Would you like me to start ambient music?', 'Empathetic', 'Psychological Companion')
        ]
        cursor.executemany("""
            INSERT INTO conversation_logs (timestamp, sender, message, detected_mood, bot_mode)
            VALUES (?, ?, ?, ?, ?)
        """, sample_chats)

    conn.commit()
    conn.close()
    print("[MAITRI DB] Sample offline telemetry and astronaut profile data seeded successfully.")

def log_emotion(emotion, confidence, source='facial_analysis', notes='', db_path=DB_PATH):
    """Inserts a new facial/voice emotion observation."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO emotion_logs (timestamp, emotion, confidence, source, notes)
        VALUES (?, ?, ?, ?, ?)
    """, (datetime.now().isoformat(), emotion, confidence, source, notes))
    conn.commit()
    conn.close()

def log_vitals(heart_rate, spo2, body_temp=36.8, stress_index=20.0, db_path=DB_PATH):
    """Logs vital signs and computes threshold status."""
    status = 'NORMAL'
    if heart_rate > 100 or spo2 < 94 or stress_index > 75:
        status = 'WARNING'
    if heart_rate > 120 or spo2 < 90 or stress_index > 90:
        status = 'CRITICAL'
        
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO vitals_history (timestamp, heart_rate, spo2, body_temp, stress_index, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (datetime.now().isoformat(), heart_rate, spo2, body_temp, stress_index, status))
    conn.commit()
    conn.close()
    return status

def get_latest_dashboard_data(db_path=DB_PATH):
    """Retrieves full state payload for rendering the offline HTML dashboard UI."""
    conn = get_connection(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM astronaut_profile LIMIT 1")
    profile = dict(cursor.fetchone() or {})

    cursor.execute("SELECT * FROM vitals_history ORDER BY id DESC LIMIT 10")
    vitals = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM emotion_logs ORDER BY id DESC LIMIT 5")
    emotions = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM sleep_records ORDER BY id DESC LIMIT 7")
    sleep = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT 10")
    alerts = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM conversation_logs ORDER BY id DESC LIMIT 15")
    conversations = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return {
        "profile": profile,
        "vitals": vitals,
        "emotions": emotions,
        "sleep": sleep,
        "alerts": alerts,
        "conversations": conversations
    }

if __name__ == "__main__":
    init_db()
    seed_sample_data()
    data = get_latest_dashboard_data()
    print(f"[MAITRI DB Test] Profile loaded: {data['profile'].get('full_name')}")
    print(f"[MAITRI DB Test] Recent vitals count: {len(data['vitals'])}")
