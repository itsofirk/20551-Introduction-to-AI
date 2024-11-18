from mmn11.consts import PUZZLE_SIZE, EMPTY_TILE, DIRECTIONS


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

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(self.board))

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

    def print_board(self):
        """
        Ugly, yet efficient way to print the board 🙃
        """
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
