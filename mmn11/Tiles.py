"""
author: @itsofirk
description: 8-Tiles Puzzle solver using 4 different algorithms
"""
import argparse
from algorithms import algorithms
from puzzle_state import PuzzleState


def main(board):
    start_state = PuzzleState(board)

    print("Initial board:")
    start_state.print_board()

    for name, algorithm in algorithms.items():
        result_state, nodes_expanded = algorithm(start_state)
        if result_state is not None:
            path = PuzzleState.extract_path(result_state)
            print(f"Algorithm: {name}")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Path to Goal: {path}\n")
        else:
            print(f"Algorithm: {name}")
            print("No solution found.\n")


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
