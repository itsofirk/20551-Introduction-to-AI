from consts import PLAYER_1, PLAYER_2, GameMode
from board import Board
from movers import InteractiveMover, RandomMover, BaseMover


class Game:
    def __init__(self):
        self.board = Board()
        self.players = {
            1: PLAYER_1,
            2: PLAYER_2
        }
        self.current_player = 1
        self.state_count = 0

    def switch_player(self):
        self.current_player = self.current_player % 2 + 1

    def start(self, mode, parameter):
        if mode == GameMode.INTERACTIVE:
            self.play(InteractiveMover.get_move)
        elif mode == GameMode.DISPLAY_ALL_ACTIONS:
            # self.play_display_all_actions(parameter)
            ...
        elif mode == GameMode.METHODICAL:
            self.play(..., parameter)
        elif mode == GameMode.RANDOM:
            self.play(RandomMover.get_move, parameter)
        self.display_final_result()

    def play(self, Mover: BaseMover, param=-1):
        self.display()
        while not self.is_game_over():
            self.state_count += 1
            player = self.players[self.current_player]
            legal_moves = self.board.get_legal_moves(player)
            if legal_moves:
                move = Mover.get_move(player, legal_moves)
                self.board.make_move(player, move)
                self.display(self.current_player, move, with_score=True)
            else:
                print(f"Player {self.current_player} has no legal moves. Skipping turn.\n")
            self.switch_player()
        self.display()
        self.display_final_result()

    def is_game_over(self):
        return self.board.is_full() or not any((self.board.has_any_moves(p) for p in self.players.values()))

    def display(self, player_num=None, move=None, with_score=False):
        print()
        if player_num and move:
            print(f'State {self.state_count}, Player {player_num} moved, Action {move}')
        else:
            print(f'State {self.state_count}')

        self.board.display()

        if with_score:
            score1, score2 = self.board.get_score()
            print(f'Result - Player 1: {score1} disks, Player 2: {score2} disks, Total: {score1 + score2} disks')

    def display_final_result(self):
        score1, score2 = self.board.get_score()
        print("Final Score:")
        print(f"Player 1: {score1} disks")
        print(f"Player 2: {score2} disks")
        if score1 > score2:
            print("Player X wins!")
        elif score2 > score1:
            print("Player O wins!")
        else:
            print("It's a tie!")
