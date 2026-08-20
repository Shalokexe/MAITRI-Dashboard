"""
Unit Tests for MAITRI Phase 14 Voice Command Engine & Spoken EVA Checklists
"""

import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.ai_engine.voice_commands import VoiceCommandEngine

class TestVoiceCommandEngine(unittest.TestCase):
    def setUp(self):
        self.engine = VoiceCommandEngine()

    def test_vitals_command_parsing(self):
        res = self.engine.parse_command("MAITRI check vitals")
        self.assertEqual(res["action"], "NAVIGATE_TAB")
        self.assertEqual(res["tab"], "vitals")

    def test_eclss_command_parsing(self):
        res = self.engine.parse_command("MAITRI run oxygen ECLSS check")
        self.assertEqual(res["action"], "ECLSS_DIAGNOSTIC")

    def test_f1_reflex_command_parsing(self):
        res = self.engine.parse_command("MAITRI launch F1 reflex game")
        self.assertEqual(res["action"], "OPEN_ROUTE")
        self.assertEqual(res["url"], "f1_reflex.html")

    def test_eva_checklist_step(self):
        step = self.engine.get_eva_step(2)
        self.assertEqual(step["step"], 2)
        self.assertIn("PLSS", step["title"])

if __name__ == '__main__':
    unittest.main()
