class BaseMover:
    @staticmethod
    def get_move(color: str, legal_moves: list[tuple[int, int]]):
        raise NotImplementedError