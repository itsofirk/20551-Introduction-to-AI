from movers.base_mover import BaseMover


def single_moves_factory(legal_moves: list[tuple[int, int]]):
    for move in legal_moves:
        class SingleMoveMover(BaseMover):
            @staticmethod
            def get_move(color, board):
                return move
        yield move, SingleMoveMover
