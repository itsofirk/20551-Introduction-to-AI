from movers.base_mover import BaseMover


def single_moves_factory(legal_moves: list[tuple[int, int]]):
    for move in legal_moves:
        class SingleMoveMover(BaseMover):
            @staticmethod
            def get_move(color, _legal_moves: list[tuple[int, int]]):
                return move
        yield move, SingleMoveMover
