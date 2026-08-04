"""
MAITRI Offline Space AI — Phase 10: OpenCV Mood Activity & Task Recommender
Analyzes real-time astronaut facial expressions and mood metrics from OpenCV vision stream,
mapping emotional states to targeted therapeutic activities, operational tasks, and mini-games.
"""

import time
import sqlite3
from typing import Dict, List, Any

class MoodActivitySuggester:
    def __init__(self, db_path: str = "backend/db/maitri_offline.db"):
        self.db_path = db_path
        self._init_db_schema()

    def _init_db_schema(self) -> None:
        """Ensure mood_recommendations table exists in SQLite database."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS mood_recommendations (
                    rec_id TEXT PRIMARY KEY,
                    astronaut_id TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    detected_mood TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    primary_activity TEXT NOT NULL,
                    suggested_game TEXT NOT NULL,
                    recommended_task TEXT NOT NULL
                )
            """)
            conn.commit()
            conn.close()
        except Exception:
            pass

    def recommend_activities_for_mood(
        self,
        dominant_emotion: str,
        confidence: float = 0.88,
        astronaut_id: str = "ASTRO-ISRO-706"
    ) -> Dict[str, Any]:
        """
        Maps OpenCV detected facial emotion to tailor-made space activities.
        """
        emotion = dominant_emotion.lower().strip()

        if emotion in ["stress", "stressed", "anxious", "anxiety", "fear"]:
            primary_act = "4-7-8 Bio-Pulse AR Respiration Cycle"
            game = "Space Reaction Reflex Challenge (Low Stress Mode)"
            task = "Review Habitat Life Support Logs & Listen to Lo-Fi Ambient Vault Track"
            circadian_color = "4000K Neutral Warm"

        elif emotion in ["fatigue", "fatigued", "tired", "sad", "drowsy"]:
            primary_act = "Circadian LED Warm Amber Shift (2700K) & Hydration Refill"
            game = "Constellation Memory Matrix (Relaxed Pacing)"
            task = "20-Minute Micro-Nap Protocol & Melatonin Recovery Cycle"
            circadian_color = "2700K Warm Amber"

        elif emotion in ["happy", "calm", "focused", "nominal"]:
            primary_act = "Pre-EVA Spacewalk Readiness Check & Telemetry Audit"
            game = "Gaganyaan Shuttle Docking Simulator (Hard Mode)"
            task = "Execute Routine Orbital Guidance Calibration & Crew Status Report"
            circadian_color = "6500K Blue-Enriched Daylight"

        else: # Neutral / Bored
            primary_act = "Offline Media Vault Comedy Clip & Social Crew Call"
            game = "Space Reaction Reflex Challenge (Speed Mode)"
            task = "Inspect Zero-G Water Recirculation Filters & Log Daily Entry"
            circadian_color = "5000K Daylight"

        rec_id = f"REC-{int(time.time())}"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

        # Log recommendation to SQLite DB
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO mood_recommendations 
                (rec_id, astronaut_id, timestamp, detected_mood, confidence, primary_activity, suggested_game, recommended_task)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (rec_id, astronaut_id, timestamp, emotion, confidence, primary_act, game, task))
            conn.commit()
            conn.close()
        except Exception:
            pass

        return {
            "rec_id": rec_id,
            "astronaut_id": astronaut_id,
            "timestamp": timestamp,
            "detected_mood": emotion.capitalize(),
            "confidence_pct": round(confidence * 100.0, 1),
            "primary_activity": primary_act,
            "suggested_game": game,
            "recommended_task": task,
            "circadian_lighting": circadian_color,
            "air_gapped": True
        }
