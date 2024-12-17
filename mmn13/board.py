from consts import PLAYER_1, PLAYER_2, EMPTY, DIRECTIONS


class Board:
    def __init__(self, size=8):
        self.size = size
        self.grid = [[EMPTY for _ in range(size)] for _ in range(size)]
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

    def _is_in_bounds(self, row, col):
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
                    if self._is_in_bounds(nr, nc) and self.grid[nr][nc] == opponent:
                        while self._is_in_bounds(nr, nc) and self.grid[nr][nc] == opponent:
                            nr += dr
                            nc += dc
                        if self._is_in_bounds(nr, nc) and self.grid[nr][nc] == EMPTY:
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
            while self._is_in_bounds(r, c) and self.grid[r][c] == opponent:
                temp_flips.append((r, c))
                r += dr
                c += dc
            if self._is_in_bounds(r, c) and self.grid[r][c] == player:
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
