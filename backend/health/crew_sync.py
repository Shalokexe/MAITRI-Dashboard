"""
MAITRI Multi-Astronaut Telemetry & Crew Sync Matrix (Phase 13)
Tracks side-by-side biometrics for up to 4 crew members, calculates collective
group cohesion indices, and diagnoses inter-crew interaction friction in deep space.
"""

import os
import sys
import random
from datetime import datetime

# Add parent dir to sys.path for backend imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from backend.db.database import get_connection

DEFAULT_CREW = [
    {"id": "ASTRO-01", "name": "Cmdr. Shalok Dadhwal", "role": "Commander", "hr_base": 72, "spo2_base": 98.4, "stress_base": 14.2},
    {"id": "ASTRO-02", "name": "Lt. Cmdr. Ananya Sharma", "role": "Pilot / Avionics", "hr_base": 75, "spo2_base": 98.8, "stress_base": 16.5},
    {"id": "ASTRO-03", "name": "Dr. Vikram Sarabhai II", "role": "Payload Specialist", "hr_base": 68, "spo2_base": 99.1, "stress_base": 12.0},
    {"id": "ASTRO-04", "name": "Specialist Rahul Verma", "role": "Flight Engineer", "hr_base": 74, "spo2_base": 98.2, "stress_base": 18.1}
]

class CrewSyncMatrixEngine:
    def __init__(self, crew_members=None):
        self.crew = crew_members or DEFAULT_CREW

    def generate_crew_telemetry(self, simulate_friction=False):
        """Generates real-time side-by-side telemetry for all crew members."""
        readings = []
        total_stress = 0.0

        for member in self.crew:
            if simulate_friction and member["id"] == "ASTRO-04":
                hr = random.randint(102, 120)
                spo2 = round(random.uniform(92.5, 95.0), 1)
                stress = round(random.uniform(68.0, 85.0), 1)
                hrv = round(random.uniform(25.0, 38.0), 1)
                mood = "ELEVATED STRESS / FRICTION"
            else:
                hr = int(member["hr_base"] + random.randint(-3, 4))
                spo2 = round(min(100.0, member["spo2_base"] + random.uniform(-0.4, 0.4)), 1)
                stress = round(max(5.0, member["stress_base"] + random.uniform(-3.0, 4.0)), 1)
                hrv = round(random.uniform(62.0, 78.0), 1)
                mood = "NOMINAL / CALM"

            total_stress += stress

            readings.append({
                "id": member["id"],
                "name": member["name"],
                "role": member["role"],
                "heart_rate": hr,
                "spo2": spo2,
                "stress_index": stress,
                "hrv": hrv,
                "mood": mood
            })

        # Calculate Group Cohesion Score (100% minus average crew stress penalty)
        avg_stress = total_stress / len(self.crew)
        cohesion_score = round(max(50.0, min(99.8, 100.0 - (avg_stress * 0.85))), 1)

        friction_warning = False
        if avg_stress > 35.0 or simulate_friction:
            friction_warning = True

        result = {
            "timestamp": datetime.now().isoformat(),
            "crew_count": len(self.crew),
            "group_cohesion_score": cohesion_score,
            "average_crew_stress": round(avg_stress, 1),
            "friction_warning": friction_warning,
            "readings": readings
        }

        self._log_crew_sync(result)
        return result

    def _log_crew_sync(self, result):
        """Persists crew synchronization snapshot into SQLite DB."""
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            # Ensure crew_sync_logs table exists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS crew_sync_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    cohesion_score REAL NOT NULL,
                    avg_stress REAL NOT NULL,
                    friction_warning INTEGER NOT NULL
                )
            """)
            
            cursor.execute("""
                INSERT INTO crew_sync_logs (timestamp, cohesion_score, avg_stress, friction_warning)
                VALUES (?, ?, ?, ?)
            """, (result["timestamp"], result["group_cohesion_score"], result["average_crew_stress"], 1 if result["friction_warning"] else 0))
            
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"[MAITRI Crew Sync Error] DB log failed: {e}")

if __name__ == "__main__":
    engine = CrewSyncMatrixEngine()
    data = engine.generate_crew_telemetry()
    print(f"[MAITRI Crew Sync Engine] Cohesion Score: {data['group_cohesion_score']}%")
    for r in data['readings']:
        print(f"  - {r['name']} ({r['role']}): HR {r['heart_rate']} BPM | Stress {r['stress_index']}")
