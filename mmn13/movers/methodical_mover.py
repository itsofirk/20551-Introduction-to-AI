from movers.base_mover import BaseMover


class MethodicalMover(BaseMover):
    @staticmethod
    def get_move(color, board):
        '''return the highest modulo between row and col'''
        legal_moves = board.get_legal_moves(color)
        return sorted(legal_moves, key=lambda move: move[0] % (move[1]+1))[0]
