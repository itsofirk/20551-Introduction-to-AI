import argparse

from helpers import GameMode
from game import Game
from movers.heuristic_mover import H1Mover, H2Mover

HEURISTICS = {"H1": H1Mover, "H2": H2Mover}

def main():
    args = parse_args()
    game = Game()

    mode = GameMode.INTERACTIVE
    parameter = None

    if args.displayAllActions is not None:
        mode = GameMode.DISPLAY_ALL_ACTIONS
        parameter = args.displayAllActions
    elif args.methodical is not None:
        mode = GameMode.METHODICAL
        parameter = args.methodical
    elif args.random is not None:
        mode = GameMode.RANDOM
        parameter = args.random
    if args.heuristics:
        M1 = M2 = HEURISTICS[args.heuristics[0]]
        if len(args.heuristics) == 2:
            M2 = HEURISTICS[args.heuristics[1]]
        mode = GameMode.CUSTOM
        parameter = (M1, M2)

    game.start(mode, parameter)


def parse_args():
    parser = argparse.ArgumentParser(description="Reversi Game")

    # Mutually exclusive flags for game modes
    mode_group = parser.add_mutually_exclusive_group(required=False)
    mode_group.add_argument("--displayAllActions", type=int,
                            help="Display all possible actions after reaching a given total number of disks")
    mode_group.add_argument("--methodical", type=int,
                            help="Play a given number of moves methodically")
    mode_group.add_argument("--random", type=int,
                            help="Play a given number of moves randomly")

    # Positional arguments for heuristics
    parser.add_argument("heuristics", nargs='*', choices=["H1", "H2"],
                        help="Specify one or two heuristics (e.g., H1, H2 H1).")

    args = parser.parse_args()

    # Validate positional arguments
    if len(args.heuristics) > 2:
        parser.error("You can provide at most two heuristics (e.g., H1 or H1 H2).")

    return args

if __name__ == "__main__":
    main()
