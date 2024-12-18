import random
from movers.base_mover import BaseMover


class RandomMover(BaseMover):
    @staticmethod
    def get_move(color, legal_moves: list[tuple[int, int]]):
        return random.choice(legal_moves)
