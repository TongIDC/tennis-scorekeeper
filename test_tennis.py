"""Tests for the scoring rules. Run with: python -m unittest -v"""

import unittest

from tennis import Match


def play(match, points):
    """Play a string of points, e.g. "aabba"."""
    for p in points:
        match.point(p)


def win_games(match, player, count):
    play(match, player * 4 * count)


class TestGames(unittest.TestCase):
    def test_love_game(self):
        m = Match()
        play(m, "aaa")
        self.assertEqual(m.point_score(), "40-0")
        m.point("a")
        self.assertEqual(m.games, [1, 0])
        self.assertEqual(m.points, [0, 0])

    def test_deuce_and_advantage(self):
        m = Match()
        play(m, "aaabbb")
        self.assertEqual(m.point_score(), "Deuce")
        m.point("a")
        self.assertEqual(m.point_score(), "Advantage A")
        m.point("b")
        self.assertEqual(m.point_score(), "Deuce")
        m.point("b")
        self.assertEqual(m.point_score(), "Advantage B")
        m.point("b")
        self.assertEqual(m.games, [0, 1])


class TestSets(unittest.TestCase):
    def test_six_four_wins_set(self):
        m = Match()
        win_games(m, "b", 4)
        win_games(m, "a", 6)
        self.assertEqual(m.finished_sets, [(6, 4)])
        self.assertEqual(m.sets, [1, 0])

    def test_six_five_does_not_win_set(self):
        m = Match()
        win_games(m, "b", 5)
        win_games(m, "a", 6)
        self.assertEqual(m.sets, [0, 0])
        win_games(m, "a", 1)
        self.assertEqual(m.finished_sets, [(7, 5)])

    def reach_six_all(self):
        m = Match()
        for _ in range(6):
            win_games(m, "a", 1)
            win_games(m, "b", 1)
        self.assertTrue(m.in_tiebreak)
        return m

    def test_tiebreak_seven_five(self):
        m = self.reach_six_all()
        play(m, "aaaaaabbbbb")
        self.assertEqual(m.point_score(), "Tiebreak 6-5")
        m.point("a")
        self.assertEqual(m.finished_sets, [(7, 6)])
        self.assertFalse(m.in_tiebreak)

    def test_tiebreak_needs_two_point_lead(self):
        m = self.reach_six_all()
        play(m, "ab" * 6)  # 6-6 in the tiebreak
        m.point("a")
        self.assertEqual(m.sets, [0, 0])  # 7-6 is not enough
        m.point("a")
        self.assertEqual(m.sets, [1, 0])


class TestMatch(unittest.TestCase):
    def test_straight_sets(self):
        m = Match()
        win_games(m, "a", 12)
        self.assertEqual(m.winner, "a")
        self.assertEqual(m.score(), "Match won by A! (6-0 6-0)")

    def test_three_sets(self):
        m = Match()
        win_games(m, "a", 6)
        win_games(m, "b", 6)
        self.assertIsNone(m.winner)
        win_games(m, "b", 6)
        self.assertEqual(m.winner, "b")

    def test_no_points_after_match(self):
        m = Match()
        win_games(m, "a", 12)
        with self.assertRaises(ValueError):
            m.point("b")

    def test_invalid_player(self):
        with self.assertRaises(ValueError):
            Match().point("c")


if __name__ == "__main__":
    unittest.main()
