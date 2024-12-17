from consts import PLAYER_1, PLAYER_2
from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.players = {
            PLAYER_1: Player(PLAYER_1),
            PLAYER_2: Player(PLAYER_2)
        }
        self.current_player = PLAYER_1

    def switch_player(self):
        self.current_player = PLAYER_2 if self.current_player == PLAYER_1 else PLAYER_1

    def play(self):
        while not self.is_game_over():
            self.board.display()
            player = self.players[self.current_player]
            legal_moves = self.board.get_legal_moves(self.current_player)
            if legal_moves:
                move = player.get_move(self.board)
                if move:
                    self.board.make_move(self.current_player, move)
                    print(f"Player {self.current_player} placed at {move}\n")
            else:
                print(f"Player {self.current_player} has no legal moves. Skipping turn.\n")
            self.switch_player()
        self.board.display()
        self.display_final_result()

    def is_game_over(self):
        return self.board.is_full() or (not self.board.has_any_moves(PLAYER_1) and not self.board.has_any_moves(PLAYER_2))

    def display_final_result(self):
        scores = self.board.get_score()
        print("Final Score:")
        print(f"Player {PLAYER_1}: {scores[PLAYER_1]} disks")
        print(f"Player {PLAYER_2}: {scores[PLAYER_2]} disks")
        if scores[PLAYER_1] > scores[PLAYER_2]:
            print("Player X wins!")
        elif scores[PLAYER_2] > scores[PLAYER_1]:
            print("Player O wins!")
        else:
            print("It's a tie!")
