"""
Unit Tests for MAITRI Phase 13 Multi-Astronaut Telemetry & Crew Sync Matrix Engine
"""

import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.health.crew_sync import CrewSyncMatrixEngine

class TestCrewSyncMatrix(unittest.TestCase):
    def setUp(self):
        self.engine = CrewSyncMatrixEngine()

    def test_crew_telemetry_generation(self):
        result = self.engine.generate_crew_telemetry(simulate_friction=False)
        self.assertEqual(result["crew_count"], 4)
        self.assertGreaterEqual(result["group_cohesion_score"], 80.0)
        self.assertFalse(result["friction_warning"])
        self.assertEqual(len(result["readings"]), 4)

    def test_crew_friction_simulation(self):
        result = self.engine.generate_crew_telemetry(simulate_friction=True)
        self.assertTrue(result["friction_warning"])
        astro4 = next(r for r in result["readings"] if r["id"] == "ASTRO-04")
        self.assertIn("STRESS", astro4["mood"])

if __name__ == '__main__':
    unittest.main()
