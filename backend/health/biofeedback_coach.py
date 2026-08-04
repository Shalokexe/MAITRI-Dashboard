"""
MAITRI Offline Space AI — Phase 8: Biofeedback Respiration & HRV Coherence Engine
Calculates Heart Rate Variability (HRV) metrics, parasympathetic tone, and controls
guided space-grade biofeedback breathing exercises (4-7-8 and Box Breathing).
"""

import time
import math
import sqlite3
from typing import Dict, List, Any, Optional

class BiofeedbackCoach:
    def __init__(self, db_path: str = "backend/db/maitri_offline.db"):
        self.db_path = db_path
        self._init_db_schema()

    def _init_db_schema(self) -> None:
        """Ensure biofeedback_sessions table exists in SQLite DB."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS biofeedback_sessions (
                    session_id TEXT PRIMARY KEY,
                    astronaut_id TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    technique TEXT NOT NULL,
                    duration_seconds INTEGER NOT NULL,
                    pre_hrv REAL NOT NULL,
                    post_hrv REAL NOT NULL,
                    coherence_score REAL NOT NULL,
                    status TEXT NOT NULL
                )
            """)
            conn.commit()
            conn.close()
        except Exception as e:
            # Fallback for transient sqlite paths
            pass

    def calculate_hrv_rmssd(self, rr_intervals_ms: List[float]) -> float:
        """
        Calculate Root Mean Square of Successive Differences (RMSSD) for HRV.
        RMSSD is the primary indicator of parasympathetic nervous system activity.
        """
        if len(rr_intervals_ms) < 2:
            return 45.0  # Nominal baseline HRV in ms

        diffs_sq = [(rr_intervals_ms[i+1] - rr_intervals_ms[i]) ** 2 for i in range(len(rr_intervals_ms) - 1)]
        mean_diff_sq = sum(diffs_sq) / len(diffs_sq)
        rmssd = math.sqrt(mean_diff_sq)
        return round(rmssd, 2)

    def compute_coherence_score(self, hrv_rmssd: float, target_rmssd: float = 65.0) -> float:
        """Compute 0-100% Autonomic Coherence Score."""
        score = (hrv_rmssd / target_rmssd) * 100.0
        return round(min(100.0, max(0.0, score)), 1)

    def get_breathing_pace(self, technique: str = "4-7-8") -> Dict[str, Any]:
        """
        Returns breathing cycle intervals in seconds for guided AR visualizer.
        - 4-7-8: Relaxing (Inhale 4s, Hold 7s, Exhale 8s)
        - Box: Tactical Focus (Inhale 4s, Hold 4s, Exhale 4s, Hold 4s)
        """
        if technique.lower() == "box":
            return {
                "technique": "Box Breathing (Tactical Focus)",
                "inhale_s": 4.0,
                "hold_1_s": 4.0,
                "exhale_s": 4.0,
                "hold_2_s": 4.0,
                "cycle_duration_s": 16.0,
                "recommended_cycles": 5,
                "instruction": "Equal phase box breathing for rapid focus under high cognitive load."
            }
        else: # Default 4-7-8
            return {
                "technique": "4-7-8 Deep Relaxation (Melatonin & HRV Sync)",
                "inhale_s": 4.0,
                "hold_1_s": 7.0,
                "exhale_s": 8.0,
                "hold_2_s": 0.0,
                "cycle_duration_s": 19.0,
                "recommended_cycles": 4,
                "instruction": "Extended exhalation stimulates the vagus nerve and activates parasympathetic recovery."
            }

    def log_session(
        self,
        astronaut_id: str,
        technique: str,
        duration_seconds: int,
        pre_hrv: float,
        post_hrv: float
    ) -> Dict[str, Any]:
        """Log completed biofeedback session to SQLite database."""
        session_id = f"BIO-{int(time.time())}"
        coherence = self.compute_coherence_score(post_hrv)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        status = "COMPLETED"

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO biofeedback_sessions 
                (session_id, astronaut_id, timestamp, technique, duration_seconds, pre_hrv, post_hrv, coherence_score, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (session_id, astronaut_id, timestamp, technique, duration_seconds, pre_hrv, post_hrv, coherence, status))
            conn.commit()
            conn.close()
        except Exception as e:
            pass

        return {
            "session_id": session_id,
            "astronaut_id": astronaut_id,
            "timestamp": timestamp,
            "technique": technique,
            "duration_seconds": duration_seconds,
            "hrv_improvement_pct": round(((post_hrv - pre_hrv) / pre_hrv) * 100.0, 1),
            "coherence_score": coherence,
            "status": status
        }
