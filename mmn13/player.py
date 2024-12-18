class Player:
    def __init__(self, player_color):
        self.color = player_color

    @staticmethod
    def get_move(color, legal_moves: list[tuple[int, int]]):
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
