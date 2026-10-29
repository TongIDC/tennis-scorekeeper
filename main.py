"""Command-line tennis scorekeeper. Run with: python main.py"""

from tennis import Match


def main():
    match = Match()
    print("Tennis scorekeeper (best of 3 sets).")
    print("Type 'a' or 'b' for who won the point, or 'q' to quit.")

    while match.winner is None:
        try:
            choice = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            choice = "q"

        if choice == "q":
            print("Bye!")
            return
        if choice not in ("a", "b"):
            print("Please type a, b or q.")
            continue

        match.point(choice)
        print(match.score())


if __name__ == "__main__":
    main()
