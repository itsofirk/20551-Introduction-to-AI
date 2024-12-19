import random
from movers.base_mover import BaseMover


class RandomMover(BaseMover):
    @staticmethod
    def get_move(color, board):
        legal_moves = board.get_legal_moves(color)
        return random.choice(legal_moves)
