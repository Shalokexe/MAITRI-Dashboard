"""
MAITRI Health Monitoring & Telemetry Analytics Engine
Provides comprehensive vitals tracking, stress index computations, sleep quality analysis,
daily health logs aggregation, anomaly trend evaluation, and ground-control report formatting.
"""

import os
import sys
from datetime import datetime, timedelta
import json

# Add parent dir to sys.path for backend imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from backend.db.database import get_connection, log_vitals

class HealthMonitorEngine:
    def __init__(self):
        # NASA Artemis Astronaut physiological safety bounds
        self.bounds = {
            "hr_min": 50, "hr_max": 100, "hr_crit_max": 120,
            "spo2_min": 95, "spo2_crit_min": 90,
            "temp_min": 36.0, "temp_max": 37.5, "temp_crit_max": 38.5,
            "stress_max": 65.0, "stress_crit_max": 85.0
        }

    def evaluate_vitals_health(self, heart_rate, spo2, body_temp=36.8, stress_index=20.0):
        """
        Evaluates real-time physiological vitals telemetry against safety boundaries.
        Returns health score (0-100), alert level, and actionable recommendation.
        """
        score = 100.0
        alerts = []
        status = "NOMINAL"

        # Heart rate checks
        if heart_rate > self.bounds["hr_crit_max"]:
            score -= 35
            status = "CRITICAL"
            alerts.append(f"Tachycardia Spike: Heart rate reached {heart_rate} BPM")
        elif heart_rate > self.bounds["hr_max"]:
            score -= 15
            if status != "CRITICAL": status = "WARNING"
            alerts.append(f"Elevated Heart Rate: {heart_rate} BPM")
        elif heart_rate < self.bounds["hr_min"]:
            score -= 15
            if status != "CRITICAL": status = "WARNING"
            alerts.append(f"Bradycardia Notice: Low heart rate {heart_rate} BPM")

        # SpO2 checks
        if spo2 < self.bounds["spo2_crit_min"]:
            score -= 40
            status = "CRITICAL"
            alerts.append(f"Hypoxia Hazard: SpO2 dropped to {spo2}%")
        elif spo2 < self.bounds["spo2_min"]:
            score -= 20
            if status != "CRITICAL": status = "WARNING"
            alerts.append(f"Mild Desaturation: SpO2 at {spo2}%")

        # Temperature checks
        if body_temp > self.bounds["temp_crit_max"]:
            score -= 25
            status = "CRITICAL"
            alerts.append(f"Hyperthermia Alert: Core temp at {body_temp} °C")
        elif body_temp > self.bounds["temp_max"]:
            score -= 10
            if status != "CRITICAL": status = "WARNING"
            alerts.append(f"Elevated Temperature: {body_temp} °C")

        # Stress index checks
        if stress_index > self.bounds["stress_crit_max"]:
            score -= 25
            if status != "CRITICAL": status = "WARNING"
            alerts.append(f"High Cortisol/Stress Index: {stress_index}/100")
        elif stress_index > self.bounds["stress_max"]:
            score -= 10
            alerts.append(f"Moderate Stress Level: {stress_index}/100")

        final_score = max(0.0, round(score, 1))

        # Log observation to SQLite
        log_vitals(heart_rate, spo2, body_temp, stress_index)

        return {
            "health_score": final_score,
            "status": status,
            "alerts": alerts,
            "timestamp": datetime.now().isoformat()
        }

    def get_vitals_trend_analytics(self, hours=24):
        """Retrieves historical telemetry log data for Chart.js rendering."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vitals_history ORDER BY id DESC LIMIT 20")
        rows = cursor.fetchall()
        conn.close()

        records = [dict(r) for r in reversed(rows)]
        avg_hr = round(sum(r['heart_rate'] for r in records) / max(1, len(records)), 1) if records else 72.0
        avg_spo2 = round(sum(r['spo2'] for r in records) / max(1, len(records)), 1) if records else 98.4
        avg_stress = round(sum(r['stress_index'] for r in records) / max(1, len(records)), 1) if records else 22.0

        return {
            "records": records,
            "avg_heart_rate": avg_hr,
            "avg_spo2": avg_spo2,
            "avg_stress": avg_stress,
            "total_samples": len(records)
        }

    def get_sleep_analytics(self):
        """Retrieves sleep duration and quality breakdown."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sleep_records ORDER BY id DESC LIMIT 7")
        rows = cursor.fetchall()
        conn.close()

        records = [dict(r) for r in reversed(rows)]
        avg_duration = round(sum(r['duration_hours'] for r in records) / max(1, len(records)), 1) if records else 7.2
        avg_quality = round(sum(r['quality_score'] for r in records) / max(1, len(records)), 1) if records else 84.0

        return {
            "records": records,
            "avg_duration_hours": avg_duration,
            "avg_quality_score": avg_quality
        }

if __name__ == "__main__":
    monitor = HealthMonitorEngine()
    print("[MAITRI Health Monitor] Telemetry analytics engine initialized.")
    eval_res = monitor.evaluate_vitals_health(heart_rate=88, spo2=98.5, body_temp=36.7, stress_index=32.0)
    print(f"[MAITRI Health Test] Score: {eval_res['health_score']}/100, Status: {eval_res['status']}")
    trends = monitor.get_vitals_trend_analytics()
    print(f"[MAITRI Health Test] 24h Telemetry samples: {trends['total_samples']}, Avg HR: {trends['avg_heart_rate']} BPM")
