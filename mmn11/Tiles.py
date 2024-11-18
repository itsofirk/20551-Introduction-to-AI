"""
author: @itsofirk
description: 8-Tiles Puzzle solver using 4 different algorithms
"""
import argparse

from consts import GOAL_STATE
from puzzle_state import PuzzleState


def main(board: list):
    print("Initial board:")
    print_board(board)


def parse_args():
    args = argparse.ArgumentParser(
        description="8-Tiles Puzzle solver using 4 different algorithms",
        epilog="author: @itsofirk"
    )
    args.add_argument("board", nargs=9, type=int)
    args = args.parse_args()
    return args.board


if __name__ == "__main__":
    _board = parse_args()
    main(_board)