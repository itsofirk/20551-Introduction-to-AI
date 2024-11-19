PUZZLE_SIZE = 3
EMPTY_TILE = 0

GOAL_STATE = [EMPTY_TILE, 1, 2, 3, 4, 5, 6, 7, 8]
DIRECTIONS = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}


# helpers
def get_empty_index(board):
    return board.index(EMPTY_TILE)


def get_coords(idx):
    return divmod(idx, PUZZLE_SIZE)


def is_solvable(board):
    inv_count = 0
    tiles = [tile for tile in board if tile != 0]
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inv_count += 1
    return inv_count % 2 == 0