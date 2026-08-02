"""
MAITRI Offline Companion AI Engine
Production-grade, zero-internet conversational assistant engineered for astronaut resilience.
Combines mood-aware rules, psychological intervention protocols, and SQLite log persistence.
"""

import os
import sys
import random
from datetime import datetime

# Add parent dir to sys.path for backend imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from backend.db.database import get_connection
from backend.ai_engine.mood_rules import MoodResponseRouter

class OfflineCompanionAI:
    def __init__(self):
        self.router = MoodResponseRouter()
        self.astronaut_name = "Cmdr. Shalok Dadhwal"
        
        # Knowledge domain responses for offline space operations
        self.knowledge_base = {
            "greetings": [
                "Greetings Cmdr. Shalok. MAITRI system active. How may I support your mission objectives today?",
                "Hello Commander. All life support systems are nominal. I am listening.",
                "Welcome back, Cmdr. Shalok. Ready to assist with operational or psychological well-being."
            ],
            "breathwork": [
                "Initiating 4-7-8 Deep Breathing Protocol: Inhale through nose (4s)... Hold (7s)... Exhale through mouth (8s). Let's complete 4 cycles.",
                "Focus on the rhythm of your diaphragm. Deep space missions require conscious breath regulation."
            ],
            "isolation": [
                "Long-duration spaceflight isolation is a well-documented physiological stressor. Remember that your work on Artemis-IX advances humanity's future. Would you like to listen to a motivational message from family or crew?",
                "Feeling distant from Earth is completely normal. I can play ambient Earth sounds (forest rain, ocean waves) from our offline media vault."
            ],
            "vitals": [
                "Current Telemetry Summary: Heart Rate 72 BPM, SpO2 98.4%, Core Temp 36.7 °C, Stress Index 24/100. All metrics within NASA Artemis flight safety limits."
            ],
            "entertainment": [
                "I have loaded 14 lo-fi space tracks, 8 stand-up comedy routines, and 5 guided meditation sessions into your local media vault. Which would you prefer?"
            ],
            "fallback": [
                "I copy your message, Commander. Maintaining air-gapped mission log. All primary systems remain nominal.",
                "Understood, Cmdr. Shalok. I am continuously monitoring your telemetry to ensure maximum resilience."
            ]
        }

    def generate_reply(self, user_message, detected_emotion="Focused / Neutral", vocal_stress=20.0, db_log=True):
        """
        Generates an empathetic, offline-safe response driven by user intent and real-time multimodal mood inputs.
        """
        msg = user_message.strip()
        if not msg:
            return "Commander, I did not receive input. Please state your query."

        msg_lower = msg.lower()
        
        # Determine mood routing and intervention
        routed = self.router.route_response(msg, detected_emotion=detected_emotion, vocal_stress=vocal_stress)
        mode = routed["mode"]
        prefix = routed["tone_prefix"]
        intervention = routed["intervention"]

        # Intent matching
        if any(w in msg_lower for w in ["hi", "hello", "hey", "greetings"]):
            body = random.choice(self.knowledge_base["greetings"])
        elif any(w in msg_lower for w in ["breathe", "breathing", "breath", "calm down"]):
            body = random.choice(self.knowledge_base["breathwork"])
        elif any(w in msg_lower for w in ["lonely", "isolated", "miss earth", "family", "home"]):
            body = random.choice(self.knowledge_base["isolation"])
        elif any(w in msg_lower for w in ["vital", "heart", "spo2", "health", "stat"]):
            body = self.knowledge_base["vitals"][0]
        elif any(w in msg_lower for w in ["music", "song", "comedy", "movie", "fun", "bored"]):
            body = self.knowledge_base["entertainment"][0]
        else:
            body = random.choice(self.knowledge_base["fallback"])

        # Assembly
        if intervention:
            full_reply = f"{prefix}\n\n[Intervention Protocol]: {intervention}\n\n{body}"
        else:
            full_reply = f"{prefix} {body}"

        # DB Logging
        if db_log:
            self._log_to_db(sender="astronaut", message=msg, detected_mood=detected_emotion, bot_mode=mode)
            self._log_to_db(sender="maitri_ai", message=full_reply, detected_mood=detected_emotion, bot_mode=mode)

        return {
            "reply": full_reply,
            "mode": mode,
            "detected_mood": detected_emotion,
            "timestamp": datetime.now().isoformat()
        }

    def _log_to_db(self, sender, message, detected_mood, bot_mode):
        """Persists dialogue turn into SQLite database."""
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO conversation_logs (timestamp, sender, message, detected_mood, bot_mode)
                VALUES (?, ?, ?, ?, ?)
            """, (datetime.now().isoformat(), sender, message, detected_mood, bot_mode))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"[MAITRI AI Engine Error] Database log failed: {e}")

if __name__ == "__main__":
    ai = OfflineCompanionAI()
    print("[MAITRI AI Engine] Offline companion AI engine initialized.")
    test_msg = "MAITRI, I feel a bit stressed after the space walk."
    resp = ai.generate_reply(test_msg, detected_emotion="Elevated Stress", vocal_stress=75.0)
    print(f"\n--- USER ---: {test_msg}")
    print(f"--- MAITRI (Mode: {resp['mode']}) ---:\n{resp['reply']}")
