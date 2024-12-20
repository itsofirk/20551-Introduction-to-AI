from movers.base_mover import BaseMover


class InteractiveMover(BaseMover):
    @staticmethod
    def get_move(color, board):
        legal_moves = board.get_legal_moves(color)
        if not legal_moves:
            return None
        while True:
            try:
                move = input(f"Player {color}, enter your move as 'row,col': ")
                row, col = move.strip().split(',')
                row, col = int(row), int(col)
                if (row, col) in legal_moves:
                    return row, col
                else:
                    print("Illegal move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as numbers separated by a comma.")
