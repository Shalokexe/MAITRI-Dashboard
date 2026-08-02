"""
Unit Test Suite for MAITRI Health Monitor Engine
"""

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.health.health_monitor import HealthMonitorEngine

class TestHealthModule(unittest.TestCase):
    def setUp(self):
        self.engine = HealthMonitorEngine()

    def test_engine_initialization(self):
        self.assertIsNotNone(self.engine)

    def test_nominal_vitals_evaluation(self):
        res = self.engine.evaluate_vitals_health(heart_rate=72, spo2=98.4, body_temp=36.7, stress_index=20.0)
        self.assertEqual(res["status"], "NOMINAL")
        self.assertEqual(res["health_score"], 100.0)

    def test_critical_vitals_evaluation(self):
        res = self.engine.evaluate_vitals_health(heart_rate=130, spo2=88.0, body_temp=38.8, stress_index=90.0)
        self.assertEqual(res["status"], "CRITICAL")
        self.assertLess(res["health_score"], 50.0)
        self.assertGreater(len(res["alerts"]), 0)

    def test_vitals_trend_analytics(self):
        trends = self.engine.get_vitals_trend_analytics()
        self.assertIn("records", trends)
        self.assertIn("avg_heart_rate", trends)

if __name__ == "__main__":
    unittest.main()
