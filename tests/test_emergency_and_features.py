"""
Unit Test Suite for MAITRI Emergency Alerting, Cognitive Readiness, & Circadian Sync Modules
"""

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.alerts.emergency_reporter import EmergencyReporterEngine
from backend.health.cognitive_test import CognitiveReadinessTester
from backend.health.circadian_sync import CircadianLightingSynchronizer
from backend.audio.speech_engine import OfflineSpeechEngine

class TestEmergencyAndFeatures(unittest.TestCase):
    def setUp(self):
        self.emergency_engine = EmergencyReporterEngine()
        self.cognitive_tester = CognitiveReadinessTester()
        self.circadian_sync = CircadianLightingSynchronizer()
        self.speech_engine = OfflineSpeechEngine()

    def test_emergency_rule_evaluation(self):
        res = self.emergency_engine.evaluate_emergency_rules(heart_rate=130, spo2=88.0, body_temp=38.0, stress_index=90.0)
        self.assertEqual(res["severity"], "CRITICAL")
        self.assertTrue(res["has_emergency"])
        self.assertGreaterEqual(len(res["triggers"]), 2)

    def test_blackbox_compression(self):
        pkt = self.emergency_engine.generate_blackbox_flight_packet()
        self.assertIn("sha256_hash", pkt)
        self.assertGreater(pkt["compression_savings_percent"], 20.0)

    def test_cognitive_pvt_test(self):
        res = self.cognitive_tester.evaluate_cognitive_test([210, 215, 220, 205, 225], memory_accuracy_percent=96.0)
        self.assertIn("FIT FOR EVA", res["eva_clearance_status"])
        self.assertGreaterEqual(res["cognitive_score"], 85.0)

    def test_circadian_lighting(self):
        res = self.circadian_sync.compute_lighting_schedule()
        self.assertIn("color_temp_kelvin", res)
        self.assertIn("spectral_type", res)

    def test_speech_command_parsing(self):
        cmd = self.speech_engine.parse_voice_command("MAITRI start cognitive reaction test")
        self.assertEqual(cmd["intent"], "START_COGNITIVE_TEST")

if __name__ == "__main__":
    unittest.main()
