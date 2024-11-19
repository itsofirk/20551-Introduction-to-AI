from consts import EMPTY_TILE, GOAL_STATE, DIRECTIONS, get_empty_index, get_coords


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
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(tuple(self.board))

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def book_heuristic(self):
        distance = 0
        for index, tile in enumerate(self.board):
            if tile != EMPTY_TILE:
                goal_index = GOAL_STATE.index(tile)
                current_row, current_col = get_coords(index)
                goal_row, goal_col = get_coords(goal_index)
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def heuristic(self):
        out_of_row = 0
        out_of_col = 0
        for index, tile in enumerate(self.board):
            if tile != EMPTY_TILE:
                goal_index = GOAL_STATE.index(tile)
                current_row, current_col = get_coords(index)
                goal_row, goal_col = get_coords(goal_index)
                if current_row != goal_row:
                    out_of_row += 1
                if current_col != goal_col:
                    out_of_col += 1
        return out_of_row + out_of_col

    def get_successors(self):
        successors = []
        empty_index = get_empty_index(self.board)
        row, col = get_coords(empty_index)

        for move in DIRECTIONS.values():
            new_row, new_col = row + move[0], col + move[1]  # "Move" the empty tile
            if 0 <= new_row < 3 and 0 <= new_col < 3:  # if within boundaries
                new_index = new_row * 3 + new_col
                new_board = self.board.copy()
                new_board[empty_index], new_board[new_index] = new_board[new_index], new_board[empty_index]
                action = new_board[empty_index]  # The tile that moved into the blank space
                successors.append(PuzzleState(new_board, self, action, self.depth + 1))
        return successors

    def print_board(self):
        """
        Ugly, yet efficient way to print the board 🙃
        """
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")

    @staticmethod
    def extract_path(state):
        path = []
        while state.parent is not None:
            path.append(state.action)
            state = state.parent
        path.reverse()
        return path
