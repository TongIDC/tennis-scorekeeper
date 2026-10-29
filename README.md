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

## Web version (for your phone)

Play it live at **https://tongidc.github.io/tennis-scorekeeper/**. Open that
link on your phone and bookmark it or add it to your home screen. You can also
open `index.html` straight from this folder in any browser. No server or install
is needed.

Type the player names, then tap **Point** for whoever won each point. **Undo**
takes back the last point. The score is saved in the browser, so a reload or
locked phone won't lose the match.

The scoring rules in `index.html` are a direct port of `tennis.py`. Open
[the live site with `#test`](https://tongidc.github.io/tennis-scorekeeper/#test)
(or `index.html#test` locally) to run the same checks as `test_tennis.py` in the
browser.

## Test

```
python -m unittest -v
```

## Files

- `tennis.py`: the scoring rules (`Match` class)
- `main.py`: the command-line loop
- `test_tennis.py`: tests for the scoring rules
- `index.html`: the web version (scoring rules, page and self-check in one file)
- `manifest.webmanifest`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`:
  the home-screen name and icon for the web version
