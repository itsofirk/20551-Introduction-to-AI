from enum import Enum

PLAYER_1 = 'X'
PLAYER_2 = 'O'
EMPTY = '-'

# Directions for move checking: Up, Up-Right, Right, Down-Right, Down, Down-Left, Left, Up-Left
DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1),
              (1, 0), (1, -1), (0, -1), (-1, -1)]


class GameMode(Enum):
    DISPLAY_ALL_ACTIONS = 1
    METHODICAL = 2
    RANDOM = 3
    INTERACTIVE = 4
