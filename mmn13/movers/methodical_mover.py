from movers.base_mover import BaseMover


class MethodicalMover(BaseMover):
    @staticmethod
    def get_move(color, legal_moves: list[tuple[int, int]]):
        '''return the highest modulo between row and col'''
        return sorted(legal_moves, key=lambda move: move[0] % move[1])[0]
