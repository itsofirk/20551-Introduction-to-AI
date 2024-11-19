from collections import deque
import heapq

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
    if state.board == GOAL_STATE:
        return state, 0
    if limit <= 0:
        return None, 0
    nodes_expanded = 0
    for child in state.get_successors():
        result, child_expanded = dls(child, limit - 1)
        nodes_expanded += child_expanded + 1
        if result is not None:
            return result, nodes_expanded
    return None, nodes_expanded

def iddfs(start_state: PuzzleState):
    depth = 0
    total_nodes_expanded = 0
    while True:
        result, nodes_expanded = dls(start_state, depth)
        total_nodes_expanded += nodes_expanded
        if result is not None:
            return result, total_nodes_expanded
        depth += 1


def gbfs(start_state: PuzzleState):
    frontier = []
    heapq.heappush(frontier, (start_state.heuristic(), start_state))
    explored = set()
    nodes_expanded = 0

    while frontier:
        _, current_state = heapq.heappop(frontier)
        if current_state.board == GOAL_STATE:
            return current_state, nodes_expanded
        explored.add(current_state)
        nodes_expanded += 1
        for child in current_state.get_successors():
            if child not in explored:
                h = child.heuristic()
                heapq.heappush(frontier, (h, child))
    return None, nodes_expanded

def a_star(start_state: PuzzleState):
    frontier = []
    start_state.cost = 0
    heapq.heappush(frontier, (start_state.heuristic(), start_state))
    explored = {}
    nodes_expanded = 0

    while frontier:
        _, current_state = heapq.heappop(frontier)
        if current_state.board == GOAL_STATE:
            return current_state, nodes_expanded
        explored[current_state] = current_state.cost
        nodes_expanded += 1
        for child in current_state.get_successors():
            child.cost = current_state.cost + 1
            if child not in explored or child.cost < explored.get(child, float('inf')):
                explored[child] = child.cost
                f = child.cost + child.heuristic()
                heapq.heappush(frontier, (f, child))
    return None, nodes_expanded




algorithms = {
    'BFS': bfs,
    'IDDFS': iddfs,
    'GBFS': gbfs,
    'A*': a_star
}
