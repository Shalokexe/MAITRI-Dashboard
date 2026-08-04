import unittest
import os
import sqlite3
from backend.health.biofeedback_coach import BiofeedbackCoach

class TestBiofeedbackCoach(unittest.TestCase):
    def setUp(self):
        self.test_db = "tests/test_maitri_bio.db"
        self.coach = BiofeedbackCoach(db_path=self.test_db)

    def tearDown(self):
        if os.path.exists(self.test_db):
            try:
                os.remove(self.test_db)
            except Exception:
                pass

    def test_hrv_rmssd_calculation(self):
        rr_intervals = [800.0, 850.0, 790.0, 840.0, 810.0]
        rmssd = self.coach.calculate_hrv_rmssd(rr_intervals)
        self.assertIsInstance(rmssd, float)
        self.assertGreater(rmssd, 0)

    def test_coherence_score(self):
        score = self.coach.compute_coherence_score(hrv_rmssd=65.0, target_rmssd=65.0)
        self.assertEqual(score, 100.0)

        score_low = self.coach.compute_coherence_score(hrv_rmssd=32.5, target_rmssd=65.0)
        self.assertEqual(score_low, 50.0)

    def test_breathing_pace_structures(self):
        pace_478 = self.coach.get_breathing_pace("4-7-8")
        self.assertEqual(pace_478["inhale_s"], 4.0)
        self.assertEqual(pace_478["hold_1_s"], 7.0)
        self.assertEqual(pace_478["exhale_s"], 8.0)

        pace_box = self.coach.get_breathing_pace("box")
        self.assertEqual(pace_box["cycle_duration_s"], 16.0)

    def test_db_session_logging(self):
        res = self.coach.log_session(
            astronaut_id="ASTRO-ISRO-706",
            technique="4-7-8",
            duration_seconds=120,
            pre_hrv=42.0,
            post_hrv=64.0
        )
        self.assertEqual(res["status"], "COMPLETED")
        self.assertEqual(res["coherence_score"], 98.5)
        self.assertIn("BIO-", res["session_id"])

if __name__ == '__main__':
    unittest.main()
