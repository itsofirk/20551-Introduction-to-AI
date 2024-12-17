class Player:
    def __init__(self, player_type):
        self.player_type = player_type

    def get_move(self, board):
        legal_moves = board.get_legal_moves(self.player_type)
        if not legal_moves:
            return None
        while True:
            try:
                move = input(f"Player {self.player_type}, enter your move as 'row,col': ")
                row, col = map(int, move.strip().split(','))
                if (row, col) in legal_moves:
                    return (row, col)
                else:
                    print("Illegal move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as numbers separated by a comma.")
