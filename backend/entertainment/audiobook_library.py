"""
MAITRI Popular Audiobook & Multi-Chapter Library Engine (Phase 15)
Provides an offline deep-space library of 5 popular audiobooks with chapter breakdowns
and tracks astronaut listening progress in SQLite.
"""

import os
import sys
from datetime import datetime

# Add parent dir to sys.path for backend imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from backend.db.database import get_connection

POPULAR_AUDIOBOOKS = [
    {
        "id": "BOOK-01",
        "title": "The Psychology of Money",
        "author": "Morgan Housel",
        "category": "Behavioral Finance & Mindset",
        "duration": "5h 48m",
        "cover_color": "#38BDF8",
        "chapters": [
            {"num": 1, "title": "No One's Crazy", "duration": "14:20", "summary": "Personal financial decisions are shaped by unique life experiences."},
            {"num": 2, "title": "Luck & Risk", "duration": "16:45", "summary": "Nothing is as good or as bad as it seems. Respect the role of luck."},
            {"num": 3, "title": "Never Enough", "duration": "12:10", "summary": "When rich people do crazy things because they lack a sense of enough."},
            {"num": 4, "title": "Confounding Compounding", "duration": "18:30", "summary": "Warren Buffett's skill is investing, but his secret is time."},
            {"num": 5, "title": "Freedom & Wealth", "duration": "15:00", "summary": "Controlling your time is the highest dividend money pays."}
        ]
    },
    {
        "id": "BOOK-02",
        "title": "Atomic Habits",
        "author": "James Clear",
        "category": "Self-Mastery & Performance",
        "duration": "5h 35m",
        "cover_color": "#A855F7",
        "chapters": [
            {"num": 1, "title": "The Surprising Power of Atomic Habits", "duration": "15:40", "summary": "1% improvements compounding daily lead to massive long-term results."},
            {"num": 2, "title": "How Your Habits Shape Your Identity", "duration": "17:10", "summary": "Focus on who you wish to become, not just what you want to achieve."},
            {"num": 3, "title": "The 4 Laws of Behavior Change", "duration": "14:50", "summary": "Make it obvious, attractive, easy, and satisfying."},
            {"num": 4, "title": "Make It Obvious & Attractive", "duration": "19:15", "summary": "Design environment triggers that automate good choices."},
            {"num": 5, "title": "The Secret to Results That Last", "duration": "16:20", "summary": "Consistency beats intensity. Small routines create mastery."}
        ]
    },
    {
        "id": "BOOK-03",
        "title": "Astrophysics for People in a Hurry",
        "author": "Neil deGrasse Tyson",
        "category": "Space Exploration & Science",
        "duration": "3h 41m",
        "cover_color": "#F472B6",
        "chapters": [
            {"num": 1, "title": "The Greatest Story Ever Told", "duration": "18:25", "summary": "The origin of the universe from the Big Bang to stellar nucleosynthesis."},
            {"num": 2, "title": "On Earth as in the Heavens", "duration": "16:00", "summary": "Universal physical laws operating across deep space and planetary systems."},
            {"num": 3, "title": "Let There Be Light", "duration": "15:30", "summary": "Cosmic microwave background radiation illuminating cosmic origins."},
            {"num": 4, "title": "Between the Galaxies", "duration": "14:10", "summary": "The vast voids, intergalactic gas clouds, and dark matter filaments."},
            {"num": 5, "title": "Dark Matter & Dark Energy", "duration": "20:00", "summary": "The unseen forces driving cosmic expansion."}
        ]
    },
    {
        "id": "BOOK-04",
        "title": "Cosmos",
        "author": "Carl Sagan",
        "category": "Astronomy & Humanity",
        "duration": "14h 20m",
        "cover_color": "#FDE047",
        "chapters": [
            {"num": 1, "title": "The Shores of the Cosmic Ocean", "duration": "22:15", "summary": "Exploring the 100 billion galaxies in the observable universe."},
            {"num": 2, "title": "One Voice in the Cosmic Fugue", "duration": "24:00", "summary": "Evolution of life on Earth and potential extraterrestrial biology."},
            {"num": 3, "title": "The Harmony of Worlds", "duration": "20:45", "summary": "Kepler's laws of planetary motion and the dawn of modern astronomy."},
            {"num": 4, "title": "Heaven & Hell", "duration": "21:30", "summary": "Comparing Earth's climate stability to the runaway greenhouse of Venus."},
            {"num": 5, "title": "Blues for a Red Planet", "duration": "23:10", "summary": "The robotic exploration and future terraforming of Mars."}
        ]
    },
    {
        "id": "BOOK-05",
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "category": "Mindfulness & Mental Resilience",
        "duration": "7h 30m",
        "cover_color": "#34D399",
        "chapters": [
            {"num": 1, "title": "You Are Not Your Mind", "duration": "19:40", "summary": "Disidentifying from compulsive thinking and finding inner presence."},
            {"num": 2, "title": "Consciousness: The Way Out of Pain", "duration": "17:50", "summary": "Dissolving the psychological pain-body through conscious awareness."},
            {"num": 3, "title": "Moving Deeply into the Now", "duration": "21:15", "summary": "Surrendering resistance to the present moment in deep isolation."},
            {"num": 4, "title": "Mind Strategies for Avoiding the Now", "duration": "18:00", "summary": "Overcoming anxiety driven by future anticipation or past regret."},
            {"num": 5, "title": "The State of Presence", "duration": "16:30", "summary": "Maintaining unwavering stillness during mission stress."}
        ]
    }
]

class AudiobookLibraryEngine:
    def __init__(self):
        self.catalog = POPULAR_AUDIOBOOKS

    def get_catalog(self):
        """Returns full audiobook library catalog with chapters."""
        return self.catalog

    def get_book_by_id(self, book_id):
        """Retrieves specific audiobook details by ID."""
        for book in self.catalog:
            if book["id"] == book_id:
                return book
        return self.catalog[0]

    def save_progress(self, astronaut_name, book_id, chapter_num, timestamp_sec):
        """Persists astronaut listening progress into SQLite database."""
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS audiobook_progress (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    astronaut_name TEXT NOT NULL,
                    book_id TEXT NOT NULL,
                    chapter_num INTEGER NOT NULL,
                    timestamp_sec INTEGER NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """)
            
            cursor.execute("""
                INSERT INTO audiobook_progress (astronaut_name, book_id, chapter_num, timestamp_sec, updated_at)
                VALUES (?, ?, ?, ?, ?)
            """, (astronaut_name, book_id, chapter_num, timestamp_sec, datetime.now().isoformat()))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"[MAITRI Audiobook Error] DB progress save failed: {e}")
            return False

if __name__ == "__main__":
    engine = AudiobookLibraryEngine()
    cat = engine.get_catalog()
    print(f"[MAITRI Audiobook Library] Total Books: {len(cat)}")
    for b in cat:
        print(f"  - 📘 {b['title']} by {b['author']} ({len(b['chapters'])} Chapters)")
