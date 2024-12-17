import copy
import numpy as np

PLAYER_1 = 'x'
PLAYER_2 = 'o'
EMPTY = '-'

# Directions for move checking: N, NE, E, SE, S, SW, W, NW
DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1),
              (1, 0), (1, -1), (0, -1), (-1, -1)]


class Board:
    def __init__(self, size=8):
        self.size = size
        self.grid = np.zeros((size, size), dtype=str)
        self.grid.fill(EMPTY)
        self.init_board()

    def init_board(self):
        center = self.size // 2
        self.grid[center - 1][center - 1] = PLAYER_2
        self.grid[center][center] = PLAYER_2
        self.grid[center - 1][center] = PLAYER_1
        self.grid[center][center - 1] = PLAYER_1

    def display(self):
        for row in self.grid:
            print(''.join(row))

    def _in_bounds(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def get_opponent(self, player):
        return PLAYER_2 if player == PLAYER_1 else PLAYER_1

    def get_legal_moves(self, player):
        legal_moves = set()
        opponent = self.get_opponent(player)
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] != player:
                    continue
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if self._in_bounds(nr, nc) and self.grid[nr][nc] == opponent:
                        while self._in_bounds(nr, nc) and self.grid[nr][nc] == opponent:
                            nr += dr
                            nc += dc
                        if self._in_bounds(nr, nc) and self.grid[nr][nc] == EMPTY:
                            legal_moves.add((nr, nc))
        return list(legal_moves)

    def make_move(self, player, move):
        flips = self.get_flips(player, move)
        if not flips:
            return False  # Illegal move
        self.grid[move[0]][move[1]] = player
        for r, c in flips:
            self.grid[r][c] = player
        return True

    def get_flips(self, player, move):
        flips = []
        opponent = self.get_opponent(player)
        for dr, dc in DIRECTIONS:
            r, c = move[0] + dr, move[1] + dc
            temp_flips = []
            while self._in_bounds(r, c) and self.grid[r][c] == opponent:
                temp_flips.append((r, c))
                r += dr
                c += dc
            if self._in_bounds(r, c) and self.grid[r][c] == player:
                flips.extend(temp_flips)
        return flips

    def has_any_moves(self, player):
        return len(self.get_legal_moves(player)) > 0

    def is_full(self):
        for row in self.grid:
            if EMPTY in row:
                return False
        return True

    def get_score(self):
        p1 = sum(row.count(PLAYER_1) for row in self.grid)
        p2 = sum(row.count(PLAYER_2) for row in self.grid)
        return {PLAYER_1: p1, PLAYER_2: p2}

    def copy(self):
        new_board = Board(self.size)
        new_board.grid = copy.deepcopy(self.grid)
        return new_board


class AIPlayer:
    def __init__(self, player_type, depth=3):
        self.player_type = player_type
        self.depth = depth

    def get_move(self, board):
        _, move = self.minimax(board, self.depth, True, -float('inf'), float('inf'))
        return move

    def minimax(self, board, depth, maximizing_player, alpha, beta):
        if depth == 0 or board.is_full() or (not board.has_any_moves(PLAYER_1) and not board.has_any_moves(PLAYER_2)):
            return self.evaluate(board), None

        player = self.player_type if maximizing_player else board.get_opponent(self.player_type)
        legal_moves = board.get_legal_moves(player)

        if not legal_moves:
            return self.minimax(board, depth - 1, not maximizing_player, alpha, beta)

        best_move = None
        if maximizing_player:
            max_eval = -float('inf')
            for move in legal_moves:
                new_board = board.copy()
                new_board.make_move(player, move)
                eval, _ = self.minimax(new_board, depth - 1, False, alpha, beta)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in legal_moves:
                new_board = board.copy()
                new_board.make_move(player, move)
                eval, _ = self.minimax(new_board, depth - 1, True, alpha, beta)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def evaluate(self, board):
        score = board.get_score()
        return score[self.player_type] - score[board.get_opponent(self.player_type)]


class Game:
    def __init__(self, board_size=8, ai_depth=3):
        self.board = Board(board_size)
        self.players = {
            PLAYER_1: AIPlayer(PLAYER_1, ai_depth),
            PLAYER_2: AIPlayer(PLAYER_2, ai_depth)
        }
        self.current_player = PLAYER_1
        self.state_history = []
        self.state_count = 0
        self.state_history.append((self.state_count, self.board.copy()))

    def switch_player(self):
        self.current_player = PLAYER_2 if self.current_player == PLAYER_1 else PLAYER_1

    def play(self, display_all_actions=False, num_moves=None):
        while not self.is_game_over():
            if num_moves is not None and self.state_count >= num_moves:
                break
            player = self.players[self.current_player]
            legal_moves = self.board.get_legal_moves(self.current_player)
            if legal_moves:
                move = player.get_move(self.board)
                if move:
                    if display_all_actions:
                        self.display_state_before_move()
                    success = self.board.make_move(self.current_player, move)
                    if success:
                        self.state_count += 1
                        self.state_history.append((self.state_count, self.board.copy()))
                        if display_all_actions:
                            self.display_state_after_move(move)
            self.switch_player()
        self.display_final_result()

    def is_game_over(self):
        return self.board.is_full() or (
                    not self.board.has_any_moves(PLAYER_1) and not self.board.has_any_moves(PLAYER_2))

    def display_state_before_move(self):
        state_num, board_state = self.state_history[-1]
        print(f"State {state_num}")
        board_state.display()

    def display_state_after_move(self, move):
        prev_state_num, prev_board = self.state_history[-2]
        new_state_num, new_board = self.state_history[-1]
        print(f"State {new_state_num}, Player {self.current_player} moved, Action {move}")
        new_board.display()
        scores = new_board.get_score()
        print(
            f"Result – Player {PLAYER_1}: {scores[PLAYER_1]} disks, Player {PLAYER_2}: {scores[PLAYER_2]} disks, Total: {scores[PLAYER_1] + scores[PLAYER_2]} disks\n")

    def display_final_result(self):
        scores = self.board.get_score()
        print("Final Board:")
        self.board.display()
        print(f"Final Score – Player {PLAYER_1}: {scores[PLAYER_1]} disks, Player {PLAYER_2}: {scores[PLAYER_2]} disks")
        if scores[PLAYER_1] > scores[PLAYER_2]:
            print("Player 1 (x) wins!")
        elif scores[PLAYER_2] > scores[PLAYER_1]:
            print("Player 2 (o) wins!")
        else:
            print("It's a tie!")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Reversi Game Simulation')
    parser.add_argument('--displayAllActions', type=int, default=0,
                        help='Number of disk in state to display all actions')
    parser.add_argument('--num', type=int, default=None,
                        help='Number of moves to simulate')
    args = parser.parse_args()

    game = Game()
    game.play(display_all_actions=bool(args.displayAllActions), num_moves=args.num)


if __name__ == "__main__":
    main()
