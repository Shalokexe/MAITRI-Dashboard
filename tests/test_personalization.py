"""
Unit Test Suite for MAITRI Content Recommender & Personalization Engine
"""

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.personalization.content_recommender import ContentRecommenderEngine, PERSONALITY_PRESETS

class TestPersonalizationModule(unittest.TestCase):
    def setUp(self):
        self.recommender = ContentRecommenderEngine()

    def test_recommender_initialization(self):
        self.assertIsNotNone(self.recommender)

    def test_stress_recommendation(self):
        rec = self.recommender.get_recommendations_for_emotion(emotion="Elevated Stress", stress_index=75.0)
        self.assertEqual(rec["category"], "relaxation")
        self.assertIn("title", rec)
        self.assertIn("path", rec)

    def test_personality_mode_switch(self):
        success, info = self.recommender.set_personality_mode("NASA Flight Director")
        self.assertTrue(success)
        self.assertEqual(self.recommender.active_personality, "NASA Flight Director")
        self.assertIn("Concise", info["voice_style"])

if __name__ == "__main__":
    unittest.main()
