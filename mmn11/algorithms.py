from collections import deque

from consts import GOAL_STATE
from puzzle_state import PuzzleState


def bfs(start_state: PuzzleState):
    frontier = deque([start_state])  # initialize queue with start state
    explored = set()
    nodes_expanded = 0
    current_state: PuzzleState | None = None

    while frontier:
        current_state = frontier.popleft()
        if current_state.board == GOAL_STATE:
            return current_state, nodes_expanded
        explored.add(current_state)
        nodes_expanded += 1
        for child in current_state.get_successors():
            if child not in explored and child not in frontier:
                frontier.append(child)
    return current_state, nodes_expanded


def dls(state: PuzzleState, limit: int):
    frontier = [state]
    explored = set()
    while frontier:
        current_state = frontier.pop()
        if current_state.board == GOAL_STATE:
            return current_state, len(explored)
        explored.add(current_state)
        if len(frontier) > limit:
            return None, len(explored)
        for child in current_state.get_successors():
            if child not in explored and child not in frontier:
                frontier.append(child)
    return None, len(explored)

def iddfs(start_state: PuzzleState):
    depth = 0
    nodes_expanded = 0
    while True:
        result, explored = dls(start_state, depth)
        nodes_expanded += explored
        if result is not None:
            return result, nodes_expanded
        depth += 1

algorithms = {
    'BFS': bfs,
    'IDDFS': iddfs
}
