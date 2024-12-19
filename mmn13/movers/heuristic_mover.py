from copy import deepcopy

from board import Board
from helpers import PLAYER_1, PLAYER_2
from movers.base_mover import BaseMover


class HeuristicMover(BaseMover):
    @staticmethod
    def get_move(color: str, board: Board):
        legal_moves = board.get_legal_moves(color)
        if not legal_moves:
            return None

        best_move = None
        best_value = float('-inf')
        for move in legal_moves:
            temp_board = deepcopy(board)
            temp_board.make_move(color, move)
            val = HeuristicMover.heuristic(color, temp_board)
            if val > best_value:
                best_value = val
                best_move = move
        return best_move

    @staticmethod
    def heuristic(color: str, board: Board):
        return NotImplemented


class H1Mover(HeuristicMover):
    @staticmethod
    def heuristic(color: str, board: Board):
        score1, score2 = board.get_score()
        if color == PLAYER_1:
            return score1 - score2
        return score2 - score1

class H2Mover(HeuristicMover):
    @staticmethod
    def heuristic(color: str, board: Board):
        score1, score2 = board.get_score()
        corners1, corners2, edges1, edges2 = H2Mover.count_corners_and_edges(board)
        if color == PLAYER_1:
            return H2Mover.weights(score1, corners1, edges1, score2, corners2, edges2)
        return H2Mover.weights(score2, corners2, edges2, score1, corners1, edges1)

    @staticmethod
    def count_corners_and_edges(board: Board):
        corners1 = 0
        corners2 = 0
        edges1 = 0
        edges2 = 0

        corners = [(0, 0), (board.size - 1, 0), (0, board.size - 1), (board.size - 1, board.size - 1)]
        edges = ([(0, i) for i in range(1, board.size - 1)] +
                 [(i, 0) for i in range(1, board.size - 1)] +
                 [(i, board.size - 1) for i in range(1, board.size - 1)] +
                 [(board.size - 1, i) for i in range(1, board.size - 1)])
        for cr, cc in corners:
            if board.grid[cr][cc] == PLAYER_1:
                corners1 += 1
            elif board.grid[cr][cc] == PLAYER_2:
                corners2 += 1
        for er, ec in edges:
            if board.grid[er][ec] == PLAYER_1:
                edges1 += 1
            elif board.grid[er][ec] == PLAYER_2:
                edges2 += 1
        return corners1, corners2, edges1, edges2

    @staticmethod
    def weights(curr_score, curr_corners, curr_edges, opp_score, opp_corners, opp_edges):
        return (curr_score - opp_score) + \
            3 * (curr_corners - opp_corners) + \
            (curr_edges - opp_edges)
