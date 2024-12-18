import argparse

from consts import GameMode
from game import Game

def main():
    args = parse_args()
    game = Game()

    if args.displayAllActions is not None:
        mode = GameMode.DISPLAY_ALL_ACTIONS
        parameter = args.displayAllActions
    elif args.methodical is not None:
        mode = GameMode.METHODICAL
        parameter = args.methodical
    elif args.random is not None:
        mode = GameMode.RANDOM
        parameter = args.random
    elif args.interactive:
        mode = GameMode.INTERACTIVE
        parameter = None

    game.play(mode, parameter)


def parse_args():
    parser = argparse.ArgumentParser(description="Reversi Game")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--displayAllActions", type=int,
                       help="Display all possible actions after reaching a given total number of disks")
    group.add_argument("--methodical", type=int, help="Play a given number of moves methodically")
    group.add_argument("--random", type=int, help="Play a given number of moves randomly")
    group.add_argument("--interactive", action="store_true", help="Play interactively")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
