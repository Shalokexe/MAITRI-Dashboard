"""
Unit Tests for MAITRI Phase 15 Popular Audiobook & Multi-Chapter Library Engine
"""

import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.entertainment.audiobook_library import AudiobookLibraryEngine

class TestAudiobookLibraryEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AudiobookLibraryEngine()

    def test_catalog_retrieval(self):
        cat = self.engine.get_catalog()
        self.assertEqual(len(cat), 5)
        titles = [b["title"] for b in cat]
        self.assertIn("The Psychology of Money", titles)
        self.assertIn("Atomic Habits", titles)

    def test_book_chapters(self):
        book = self.engine.get_book_by_id("BOOK-01")
        self.assertEqual(book["title"], "The Psychology of Money")
        self.assertEqual(len(book["chapters"]), 5)
        self.assertEqual(book["chapters"][0]["title"], "No One's Crazy")

    def test_save_listening_progress(self):
        saved = self.engine.save_progress("Cmdr. Shalok Dadhwal", "BOOK-01", 2, 345)
        self.assertTrue(saved)

if __name__ == '__main__':
    unittest.main()
