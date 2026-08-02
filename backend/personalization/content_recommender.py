"""
MAITRI Offline Content Recommender & Astronaut Personalization Engine
Manages air-gapped media vault, recommends personalized entertainment (comedy, music, relaxation, motivation),
and toggles astronaut personality modes (ISRO Vedic Calm, NASA Flight Director, Zen Mindfulness).
"""

import os
import sys
import random
from datetime import datetime

# Add parent dir to sys.path for backend imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from backend.db.database import get_connection

PERSONALITY_PRESETS = {
    "ISRO Vedic Calm": {
        "voice_style": "Soothing & Empathetic",
        "greeting": "Namaste Cmdr. Shalok. Inner harmony is key to deep-space resilience. How may I assist you?",
        "stress_prompt": "Let us pause and restore balance with diaphragmatic breathing and gentle ambient ragas."
    },
    "NASA Flight Director": {
        "voice_style": "Concise & Data-Driven",
        "greeting": "Commander Shalok, telemetry check nominal. State operational requirements.",
        "stress_prompt": "Cortisol index elevated. Recommending immediate 10-minute workstation isolation and hydration."
    },
    "Zen Mindfulness": {
        "voice_style": "Quiet & Grounded",
        "greeting": "Peaceful moment, Commander. Breathe with the silence of the cosmos.",
        "stress_prompt": "Notice the tension without judgment. Let go with each slow exhalation."
    }
}

MEDIA_CATALOG = {
    "comedy": [
        {"title": "Zero-Gravity Spills & Space Stand-up Vol. 1", "path": "media/comedy/space_humor_01.mp3", "duration": "08:15"},
        {"title": "Lunar Habitat Bloopers & Crew Jokes", "path": "media/comedy/crew_bloopers.mp3", "duration": "05:40"}
    ],
    "music": [
        {"title": "Orbital Sunrise Lo-Fi Beats", "path": "media/music/orbital_sunrise_lofi.mp3", "duration": "15:00"},
        {"title": "Deep Cosmos Alpha Wave Focus", "path": "media/music/alpha_wave_focus.mp3", "duration": "20:00"}
    ],
    "relaxation": [
        {"title": "Earth Rain & Forest Binaural Sleep Track", "path": "media/relaxation/earth_rain_binaural.mp3", "duration": "30:00"},
        {"title": "Zero-G Floating Guided Meditation", "path": "media/relaxation/zero_g_meditation.mp3", "duration": "12:30"}
    ],
    "motivational": [
        {"title": "Message from Artemis Flight Operations Ground Control", "path": "media/motivational/ground_control_msg.mp3", "duration": "03:20"},
        {"title": "Family Voice Note & Earth Well-Wishes", "path": "media/motivational/family_voice_note.mp3", "duration": "04:10"}
    ]
}

class ContentRecommenderEngine:
    def __init__(self, astronaut_id="ASTRO-706"):
        self.astronaut_id = astronaut_id
        self.active_personality = "ISRO Vedic Calm"

    def get_recommendations_for_emotion(self, emotion="Focused / Neutral", stress_index=20.0):
        """
        Selects optimal media category based on astronaut real-time emotional state.
        """
        if "Stress" in emotion or stress_index > 60.0:
            category = "relaxation"
            reason = "High stress index detected. Recommending binaural sleep track and guided imagery."
        elif "Fatigue" in emotion:
            category = "music"
            reason = "Fatigue detected. Recommending uplifting orbital lo-fi ambient music."
        elif "Anxious" in emotion:
            category = "motivational"
            reason = "Anxiety markers elevated. Recommending family voice note and ground control message."
        else:
            category = random.choice(["comedy", "music"])
            reason = "Nominal baseline. Recommending light-hearted stand-up humor or focus music."

        catalog_items = MEDIA_CATALOG.get(category, MEDIA_CATALOG["music"])
        selected_item = random.choice(catalog_items)

        # Log recommendation to SQLite
        self._log_recommendation_to_db(category, selected_item["title"], selected_item["path"], reason)

        return {
            "category": category,
            "title": selected_item["title"],
            "path": selected_item["path"],
            "duration": selected_item["duration"],
            "reason": reason,
            "personality_mode": self.active_personality,
            "timestamp": datetime.now().isoformat()
        }

    def set_personality_mode(self, mode_name):
        """Toggles active astronaut personality preset."""
        if mode_name in PERSONALITY_PRESETS:
            self.active_personality = mode_name
            self._update_profile_db(mode_name)
            return True, PERSONALITY_PRESETS[mode_name]
        return False, None

    def _log_recommendation_to_db(self, media_type, title, content_path, reason):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO recommendations (media_type, title, content_path, reason)
                VALUES (?, ?, ?, ?)
            """, (media_type, title, content_path, reason))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"[MAITRI Personalization Error] DB log failed: {e}")

    def _update_profile_db(self, mode_name):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE astronaut_profile
                SET preferred_personality = ?
                WHERE astronaut_id = ?
            """, (mode_name, self.astronaut_id))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"[MAITRI Personalization Error] Profile update failed: {e}")

if __name__ == "__main__":
    recommender = ContentRecommenderEngine()
    print("[MAITRI Personalization] Content recommender engine initialized.")
    rec = recommender.get_recommendations_for_emotion(emotion="Elevated Stress", stress_index=72.0)
    print(f"[MAITRI Personalization Test] Category: {rec['category']}, Item: {rec['title']} ({rec['duration']})")
    print(f"[MAITRI Personalization Test] Reason: {rec['reason']}")
