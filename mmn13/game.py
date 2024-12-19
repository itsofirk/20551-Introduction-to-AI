from typing import Type
from copy import deepcopy

from helpers import PLAYER_1, PLAYER_2, GameMode
from board import Board
from movers import InteractiveMover, MethodicalMover, RandomMover, BaseMover, single_moves_factory


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

    def start(self, mode, param):
        match mode:
            case GameMode.INTERACTIVE:
                self.play(InteractiveMover, InteractiveMover)
            case GameMode.DISPLAY_ALL_ACTIONS:
                self.play_until_disk_count_reached(param)
                print("Reached target disk count.\nDisplaying all actions...")
                self.display_all_actions()
            case GameMode.METHODICAL:
                self.play(MethodicalMover, MethodicalMover, param)
            case GameMode.RANDOM:
                self.play(RandomMover, RandomMover, param)
            case GameMode.CUSTOM:
                Mover1, Mover2 = param
                self.play(Mover1, Mover2)

    def play(self, Mover1: Type[BaseMover], Mover2: Type[BaseMover], moves_to_play=None):
        if moves_to_play is None:
            moves_to_play = self.board.size ** 2
        self.display()
        for _ in range(moves_to_play):
            if self.is_game_over():
                break
            Mover = Mover1 if self.current_player == 1 else Mover2
            self.make_move(Mover)
        self.display()
        self.display_final_result()

    def play_until_disk_count_reached(self, target_disks):
        while not self.is_game_over():
            score1, score2 = self.board.get_score()
            total = score1 + score2
            if total >= target_disks:
                break
            self.make_move(RandomMover)

    def is_game_over(self):
        return self.board.is_full() or not any((self.board.has_any_moves(p) for p in self.players.values()))

    def make_move(self, Mover: Type[BaseMover]):
        player = self.players[self.current_player]
        move = Mover.get_move(player, self.board)
        if move:
            self.state_count += 1
            self.board.make_move(player, move)
            self.display(self.current_player, move, with_score=True)
        else:
            print(f"Player {self.current_player} has no legal moves. Skipping turn.\n")
        self.switch_player()

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

    def display_all_actions(self):
        current_player = self.players[self.current_player]
        legal_moves = self.board.get_legal_moves(current_player)

        backup_board = deepcopy(self.board)
        backup_state_count = self.state_count
        backup_current_player = self.current_player

        for move, SingleMoveMover in single_moves_factory(legal_moves):
            self.board = deepcopy(backup_board)
            self.state_count = backup_state_count

            print()
            print(f"State {self.state_count}")
            self.board.display()
            self.make_move(SingleMoveMover)
            self.display(backup_current_player, move, with_score=True)


    def display_final_result(self):
        score1, score2 = self.board.get_score()
        print("Final Score:")
        print(f"Player 1: {score1} disks")
        print(f"Player 2: {score2} disks")
        if score1 > score2:
            print("Player 1 wins!")
        elif score2 > score1:
            print("Player 2 wins!")
        else:
            print("It's a tie!")
