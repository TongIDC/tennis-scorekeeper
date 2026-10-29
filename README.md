# Tennis scorekeeper

A small command-line tennis scorekeeper. Type `a` or `b` for who won each point.
It tracks points, games and sets (best of 3), including deuce/advantage and a
tiebreak at 6-6 in every set.

Requires Python 3.8+ and nothing else.

## Play

```
python main.py
```

Type `a` or `b` after each point, or `q` to quit.

## Test

```
python -m unittest -v
```

## Files

- `tennis.py`: the scoring rules (`Match` class)
- `main.py`: the command-line loop
- `test_tennis.py`: tests for the scoring rules
