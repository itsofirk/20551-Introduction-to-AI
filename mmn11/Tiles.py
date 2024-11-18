"""
author: @itsofirk
description: 8-Tiles Puzzle solver using 4 different algorithms
"""
import argparse

def print_board(board: list):
    """
    Ugly, yet efficient way to print the board 🙃
    :param board:
    :return:
    """
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")


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
    board = parse_args()
    main()