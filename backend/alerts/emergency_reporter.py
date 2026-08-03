"""
MAITRI Emergency Detection & Ground-Control Flight Reporter
Provides real-time emergency safety rule evaluation (Hypoxia, Tachycardia, Severe Panic),
black-box flight incident logging with SHA-256 hashes, and compact deep-space telemetry compression.
"""

import os
import sys
import json
import hashlib
import zlib
from datetime import datetime

# Add parent dir to sys.path for backend imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from backend.db.database import get_connection

class EmergencyReporterEngine:
    def __init__(self, astronaut_id="ASTRO-706"):
        self.astronaut_id = astronaut_id

    def evaluate_emergency_rules(self, heart_rate, spo2, body_temp, stress_index, emotion="Focused / Neutral"):
        """
        Evaluates immediate critical life safety hazards.
        """
        emergency_triggers = []
        severity = "NOMINAL"

        if spo2 < 90.0:
            severity = "CRITICAL"
            emergency_triggers.append({
                "category": "PHYSICAL",
                "title": "HYPOXIA CRITICAL HAZARD",
                "message": f"Blood oxygen saturation dropped to {spo2}%. Immediate emergency O2 mask deployment required."
            })

        if heart_rate > 120:
            severity = "CRITICAL" if severity == "CRITICAL" else "HIGH"
            emergency_triggers.append({
                "category": "PHYSICAL",
                "title": "TACHYCARDIA SURGE",
                "message": f"Resting heart rate reached {heart_rate} BPM. Abort high-intensity EVA tasks."
            })

        if stress_index > 85.0 or "Anxious" in emotion:
            if severity == "NOMINAL": severity = "MEDIUM"
            emergency_triggers.append({
                "category": "PSYCHOLOGICAL",
                "title": "SEVERE PSYCHOLOGICAL DISTRESS",
                "message": f"Cortisol stress index peaked at {stress_index}/100. Initiating automated 4-7-8 breathing and ambient calm music."
            })

        # Persist triggered alerts to SQLite
        for alert in emergency_triggers:
            self._log_alert_to_db(severity, alert["category"], alert["title"], alert["message"])

        return {
            "severity": severity,
            "has_emergency": len(emergency_triggers) > 0,
            "triggers": emergency_triggers,
            "timestamp": datetime.now().isoformat()
        }

    def generate_blackbox_flight_packet(self):
        """
        Compiles 24-hour black-box incident telemetry payload with SHA-256 integrity hash verification.
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM astronaut_profile LIMIT 1")
        profile = dict(cursor.fetchone() or {})

        cursor.execute("SELECT * FROM vitals_history ORDER BY id DESC LIMIT 10")
        vitals = [dict(r) for r in cursor.fetchall()]

        cursor.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT 5")
        alerts = [dict(r) for r in cursor.fetchall()]

        conn.close()

        payload = {
            "mission": "Artemis-IX Deep Space",
            "astronaut": profile.get("full_name", "Cmdr. Shalok Dadhwal"),
            "vitals_summary": vitals,
            "recent_alerts": alerts,
            "exported_at": datetime.now().isoformat()
        }

        raw_json = json.dumps(payload, sort_keys=True)
        sha256_hash = hashlib.sha256(raw_json.encode('utf-8')).hexdigest()

        # Compressed telemetry payload for low-bandwidth deep-space transmission
        compressed_bytes = zlib.compress(raw_json.encode('utf-8'))
        compression_ratio = round(100.0 * (1.0 - len(compressed_bytes) / len(raw_json)), 1)

        return {
            "payload_json": payload,
            "sha256_hash": sha256_hash,
            "raw_size_bytes": len(raw_json),
            "compressed_size_bytes": len(compressed_bytes),
            "compression_savings_percent": compression_ratio
        }

    def _log_alert_to_db(self, severity, category, title, message):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO alerts (severity, category, title, message)
                VALUES (?, ?, ?, ?)
            """, (severity, category, title, message))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"[MAITRI Alert Engine Error] Alert log failed: {e}")

if __name__ == "__main__":
    reporter = EmergencyReporterEngine()
    print("[MAITRI Emergency Reporter] Ground control emergency reporter engine initialized.")
    eval_res = reporter.evaluate_emergency_rules(heart_rate=125, spo2=89.5, body_temp=37.8, stress_index=88.0, emotion="Anxious / High Alert")
    print(f"[MAITRI Emergency Test] Severity: {eval_res['severity']}, Triggers Count: {len(eval_res['triggers'])}")
    blackbox = reporter.generate_blackbox_flight_packet()
    print(f"[MAITRI Blackbox Test] SHA-256: {blackbox['sha256_hash'][:16]}..., Saved: {blackbox['compression_savings_percent']}% bandwidth")
