import unittest
import os
import sqlite3
from backend.games.chess_agent import MAITRIChessAgent

class TestMAITRIChessAgent(unittest.TestCase):
    def setUp(self):
        self.test_db = "tests/test_maitri_chess.db"
        self.agent = MAITRIChessAgent(db_path=self.test_db)
        self.initial_board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    def tearDown(self):
        if os.path.exists(self.test_db):
            try:
                os.remove(self.test_db)
            except Exception:
                pass

    def test_board_evaluation(self):
        score = self.agent.evaluate_board(self.initial_board)
        self.assertEqual(score, 0.0)

    def test_agent_commentary_generation(self):
        com = self.agent.generate_agent_commentary("e2e4", is_check=True)
        self.assertIn("Checkmate", com["taunt"])
        self.assertIn("Tactical Advice", com["hint"])

    def test_move_selection(self):
        res = self.agent.select_best_move(self.initial_board)
        self.assertIn("best_move", res)
        self.assertIn("agent_taunt", res)
        self.assertIn("astronaut_hint", res)
        self.assertTrue(res["air_gapped"])

    def test_match_logging(self):
        res = self.agent.log_match_result(
            astronaut_id="ASTRO-ISRO-706",
            difficulty="Orbital Specialist",
            total_moves=24,
            winner="Cmdr. Shalok",
            final_eval=3.5
        )
        self.assertEqual(res["status"], "LOGGED")
        self.assertIn("CHESS-", res["match_id"])

if __name__ == '__main__':
    unittest.main()
