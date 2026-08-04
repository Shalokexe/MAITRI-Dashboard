import unittest
import os
import sqlite3
from backend.vision.activity_suggester import MoodActivitySuggester

class TestMoodActivitySuggester(unittest.TestCase):
    def setUp(self):
        self.test_db = "tests/test_maitri_mood.db"
        self.suggester = MoodActivitySuggester(db_path=self.test_db)

    def tearDown(self):
        if os.path.exists(self.test_db):
            try:
                os.remove(self.test_db)
            except Exception:
                pass

    def test_stressed_mood_recommendation(self):
        rec = self.suggester.recommend_activities_for_mood("stressed", confidence=0.92)
        self.assertEqual(rec["detected_mood"], "Stressed")
        self.assertIn("Bio-Pulse AR", rec["primary_activity"])
        self.assertIn("Reflex Challenge", rec["suggested_game"])
        self.assertTrue(rec["air_gapped"])

    def test_fatigued_mood_recommendation(self):
        rec = self.suggester.recommend_activities_for_mood("fatigue", confidence=0.85)
        self.assertEqual(rec["detected_mood"], "Fatigue")
        self.assertIn("Micro-Nap Protocol", rec["recommended_task"])
        self.assertIn("Warm Amber", rec["circadian_lighting"])

    def test_calm_mood_recommendation(self):
        rec = self.suggester.recommend_activities_for_mood("calm", confidence=0.95)
        self.assertEqual(rec["detected_mood"], "Calm")
        self.assertIn("Docking Simulator", rec["suggested_game"])

    def test_db_logging(self):
        rec = self.suggester.recommend_activities_for_mood("happy", confidence=0.90)
        self.assertIn("REC-", rec["rec_id"])
        
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM mood_recommendations")
        count = cursor.fetchone()[0]
        conn.close()
        self.assertEqual(count, 1)

if __name__ == '__main__':
    unittest.main()
