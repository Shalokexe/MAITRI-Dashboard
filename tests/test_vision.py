"""
Unit Test Suite for MAITRI OpenCV Vision Module
"""

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.vision.emotion_detector import FacialEmotionAnalyzer

class TestVisionModule(unittest.TestCase):
    def setUp(self):
        self.analyzer = FacialEmotionAnalyzer()

    def test_analyzer_initialization(self):
        self.assertIsNotNone(self.analyzer)

    def test_synthetic_frame_processing(self):
        frame, results = self.analyzer.generate_synthetic_frame()
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)
        res = results[0]
        self.assertIn("bbox", res)
        self.assertIn("emotion", res)
        self.assertIn("confidence", res)
        self.assertGreaterEqual(res["confidence"], 0.0)
        self.assertLessEqual(res["confidence"], 1.0)

if __name__ == "__main__":
    unittest.main()
