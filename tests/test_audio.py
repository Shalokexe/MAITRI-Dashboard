"""
Unit Test Suite for MAITRI Audio Voice Tone Module
"""

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.audio.tone_analyzer import VoiceToneAnalyzer

class TestAudioModule(unittest.TestCase):
    def setUp(self):
        self.analyzer = VoiceToneAnalyzer()

    def test_analyzer_initialization(self):
        self.assertIsNotNone(self.analyzer)

    def test_audio_signal_analysis(self):
        sample = self.analyzer.generate_synthetic_voice_sample(duration_sec=0.5, frequency_hz=140.0)
        state, score, metrics = self.analyzer.analyze_audio_signal(sample)
        self.assertIsNotNone(state)
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 100.0)
        self.assertIn("pitch_hz", metrics)

if __name__ == "__main__":
    unittest.main()
