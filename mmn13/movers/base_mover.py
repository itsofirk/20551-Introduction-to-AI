from board import Board


class BaseMover:
    @staticmethod
    def get_move(color: str, board: Board):
        raise NotImplementedError