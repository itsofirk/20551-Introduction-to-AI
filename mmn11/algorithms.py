from consts import GOAL_STATE
from puzzle_state import PuzzleState


def bfs(start_state: PuzzleState):
    from collections import deque

    frontier = deque([start_state])  # initialize queue with start state
    explored = set()
    nodes_expanded = 0

    while frontier:
        current_state = frontier.popleft()
        if current_state.board == GOAL_STATE:
            return current_state, nodes_expanded
        explored.add(current_state)
        nodes_expanded += 1
        for child in current_state.get_successors():
            if tuple(child.board) not in explored and child not in frontier:
                frontier.append(child)
    return None, nodes_expanded
