"""Tennis scoring rules: points, games, sets, deuce/advantage and tiebreaks."""

POINT_NAMES = ["0", "15", "30", "40"]


class Match:
    def __init__(self, best_of=3):
        self.sets_to_win = best_of // 2 + 1
        self.sets = [0, 0]
        self.games = [0, 0]
        self.points = [0, 0]
        self.finished_sets = []  # games score of each completed set, e.g. (6, 4)
        self.winner = None  # "a" or "b" once the match is over

    @property
    def in_tiebreak(self):
        return self.games == [6, 6]

    def point(self, player):
        """Record a point won by player "a" or "b"."""
        if self.winner is not None:
            raise ValueError("The match is already over.")
        if player not in ("a", "b"):
            raise ValueError(f"Player must be 'a' or 'b', not {player!r}.")

        i = 0 if player == "a" else 1
        self.points[i] += 1

        # A normal game needs 4 points, a tiebreak 7; both need a 2-point lead.
        target = 7 if self.in_tiebreak else 4
        if self.points[i] >= target and self.points[i] - self.points[1 - i] >= 2:
            self._win_game(i)

    def _win_game(self, i):
        self.points = [0, 0]
        self.games[i] += 1
        mine, theirs = self.games[i], self.games[1 - i]
        # 6 games with a 2-game lead, or 7 (that is 7-5, or 7-6 after a tiebreak).
        if (mine >= 6 and mine - theirs >= 2) or mine == 7:
            self._win_set(i)

    def _win_set(self, i):
        self.finished_sets.append(tuple(self.games))
        self.games = [0, 0]
        self.sets[i] += 1
        if self.sets[i] == self.sets_to_win:
            self.winner = "a" if i == 0 else "b"

    def point_score(self):
        a, b = self.points
        if self.in_tiebreak:
            return f"Tiebreak {a}-{b}"
        if a >= 3 and b >= 3:
            if a == b:
                return "Deuce"
            return "Advantage " + ("A" if a > b else "B")
        return f"{POINT_NAMES[a]}-{POINT_NAMES[b]}"

    def score(self):
        """A one-line summary of the current score."""
        set_scores = " ".join(f"{a}-{b}" for a, b in self.finished_sets)
        if self.winner is not None:
            return f"Match won by {self.winner.upper()}! ({set_scores})"
        line = (
            f"Sets {self.sets[0]}-{self.sets[1]} | "
            f"Games {self.games[0]}-{self.games[1]} | "
            f"{self.point_score()}"
        )
        if set_scores:
            line += f"   (previous sets: {set_scores})"
        return line
