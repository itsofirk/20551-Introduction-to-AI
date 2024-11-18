"""
author: @itsofirk
description: 8-Tiles Puzzle solver using 4 different algorithms
"""
import argparse

PUZZLE_SIZE = 3

EMPTY_TILE = 0
DIRECTIONS = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}


class PuzzleState:
    def __init__(self, board: list[int], parent: 'PuzzleState' = None, action: int = None, depth=0, cost=0):
        """
        :param board: a list of 9 integers representing the board
        :param parent: a reference to the parent state
        :param action: the tile that was moved to get to this state
        :param depth: how far from the initial state
        :param cost: g(n) for A* search
        """
        self.board = board
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost

    def get_successors(self):
        successors = []
        empty_index = self.board.index(EMPTY_TILE)
        moves = []

        row, col = self._get_empty_coords()


        for move in DIRECTIONS.values():
            new_row, new_col = row + move[0], col + move[1]  # "Move" the empty tile
            if 0 <= new_row < 3 and 0 <= new_col < 3:  # if within boundaries
                new_index = new_row * 3 + new_col
                new_board = self.board.copy()
                new_board[empty_index], new_board[new_index] = new_board[new_index], new_board[empty_index]
                action = new_board[empty_index]  # The tile that moved into the blank space
                successors.append(PuzzleState(new_board, self, action, self.depth + 1))
        return successors

    def _get_empty_index(self):
        return self.board.index(EMPTY_TILE)

    def _get_empty_coords(self):
        return divmod(self._get_empty_index(), PUZZLE_SIZE)

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
    _board = parse_args()
    main(_board)