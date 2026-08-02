"""
Unit Test Suite for MAITRI Offline AI Conversation Engine
"""

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.ai_engine.offline_companion import OfflineCompanionAI
from backend.ai_engine.mood_rules import MoodResponseRouter

class TestAIEngineModule(unittest.TestCase):
    def setUp(self):
        self.ai = OfflineCompanionAI()
        self.router = MoodResponseRouter()

    def test_companion_initialization(self):
        self.assertIsNotNone(self.ai)
        self.assertIsNotNone(self.router)

    def test_mood_routing(self):
        res = self.router.route_response("I am stressed", detected_emotion="Elevated Stress", vocal_stress=80.0)
        self.assertEqual(res["mode"], "Stress Reduction & Breathwork")
        self.assertIsNotNone(res["intervention"])

    def test_dialogue_generation(self):
        resp = self.ai.generate_reply("Check my vitals", detected_emotion="Focused / Neutral", vocal_stress=15.0)
        self.assertIn("reply", resp)
        self.assertIn("mode", resp)
        self.assertIn("72 BPM", resp["reply"])

if __name__ == "__main__":
    unittest.main()
