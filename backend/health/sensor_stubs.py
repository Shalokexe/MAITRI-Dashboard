"""
MAITRI Health Engine — Telemetry Sensor Stubs & Anomaly Monitor
Simulates and processes real-time astronaut vitals (Heart Rate, SpO2, Temperature, Stress Index)
and sleep quality telemetry, enforcing astronaut safety boundaries and SQLite telemetry logging.
"""

import os
import sys
import random
from datetime import datetime

# Add parent dir to sys.path for backend imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from backend.db.database import log_vitals, get_connection

class TelemetrySensorMonitor:
    def __init__(self):
        # Baseline physiological parameters for Cmdr. Shalok
        self.hr_baseline = 72
        self.spo2_baseline = 98.4
        self.temp_baseline = 36.7
        self.stress_baseline = 24.0

    def generate_telemetry_reading(self, simulate_anomaly=False):
        """Generates a realistic astronaut vitals telemetry packet."""
        if simulate_anomaly:
            heart_rate = random.randint(105, 128)
            spo2 = round(random.uniform(91.0, 94.5), 1)
            temp = round(random.uniform(37.6, 38.2), 1)
            stress_index = round(random.uniform(78.0, 92.0), 1)
        else:
            heart_rate = int(self.hr_baseline + random.randint(-4, 6))
            spo2 = round(min(100.0, self.spo2_baseline + random.uniform(-0.6, 0.6)), 1)
            temp = round(self.temp_baseline + random.uniform(-0.2, 0.2), 1)
            stress_index = round(max(5.0, self.stress_baseline + random.uniform(-4.0, 6.0)), 1)

        status = log_vitals(heart_rate, spo2, temp, stress_index)

        reading = {
            "heart_rate": heart_rate,
            "spo2": spo2,
            "body_temp": temp,
            "stress_index": stress_index,
            "status": status,
            "timestamp": datetime.now().isoformat()
        }
        return reading

    def log_sleep_record(self, duration_hours, deep_hours, rem_hours, quality_score, notes=""):
        """Logs a completed sleep cycle record."""
        conn = get_connection()
        cursor = conn.cursor()
        today_str = datetime.now().strftime("%Y-%m-%d")
        
        cursor.execute("""
            INSERT INTO sleep_records (log_date, duration_hours, deep_sleep_hours, rem_sleep_hours, quality_score, notes)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(log_date) DO UPDATE SET
                duration_hours=excluded.duration_hours,
                quality_score=excluded.quality_score
        """, (today_str, duration_hours, deep_hours, rem_hours, quality_score, notes))
        
        conn.commit()
        conn.close()
        return True

if __name__ == "__main__":
    monitor = TelemetrySensorMonitor()
    print("[MAITRI Health] Telemetry sensor monitor initialized.")
    nominal = monitor.generate_telemetry_reading(simulate_anomaly=False)
    print(f"[MAITRI Health Test] Nominal Reading: HR={nominal['heart_rate']} BPM, SpO2={nominal['spo2']}%, Status={nominal['status']}")
    anomaly = monitor.generate_telemetry_reading(simulate_anomaly=True)
    print(f"[MAITRI Health Test] Anomaly Reading: HR={anomaly['heart_rate']} BPM, SpO2={anomaly['spo2']}%, Status={anomaly['status']}")
