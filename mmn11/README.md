# 20551-Introduction-to-AI
# 8-Tiles Puzzle Solver

## Overview

This program solves the classic 8-Tiles Puzzle using 4 different search algorithms:

1. **Breadth-First Search (BFS)**
2. **Iterative Deepening Depth-First Search (IDDFS)**
3. **Greedy Best-First Search (GBFS)**
4. **A\* Search**

### Main Data Structures

- **`PuzzleState` Class**: Represents each state of the puzzle, including the current board configuration, parent state, action taken to reach the state, depth, and cost.
- **Frontier**: Implemented using different data structures for each algorithm:
  - **BFS**: Uses a `deque` for FIFO queue behavior.
  - **IDDFS**: Uses recursion.
  - **GBFS and A***: Use a priority queue implemented with `heapq` to order nodes based on heuristic values.

### Functions

- **`get_successors`**: Generates all possible successor states by moving the blank tile in one of the four directions (up, down, left, right).
- **`heuristic`**: Calculates the heuristic value for a given state based on the number of tiles out of their correct row and column.
- **`extract_path`**: Traces back from the goal state to the initial state to determine the sequence of moves taken.

## State and Action Representation

### States

Each state of the puzzle is represented as a list of 9 integers. The number `0` represents the blank tile. For example:

Initial State:   
1 2 3  
4 5 0  
6 7 8  
Is represented as:
```python
[1, 2, 3, 4, 5, 0, 6, 7, 8]
```

### Actions
Actions are represented by the tile number that is moved into the blank space. 
Since moving the blank tile in one direction is equivalent to moving an adjacent tile 
into the blank space, specifying the tile number uniquely determines the action. 
This approach ensures a deterministic and simplified action space without needing to specify directions.

## Heuristic Function for GBFS and A*

The heuristic function used in both Greedy Best-First Search (GBFS) and A* Search 
is based on the number of tiles out of their correct row and correct column.

### Admissibility and Consistency
#### Admissible: 
A heuristic is admissible if it never overestimates the true cost to reach the goal. 
In this case, the heuristic is admissible because the minimum number of moves required
to align a tile with its correct row and column is exactly what the heuristic counts. 
It does not overestimate since each out-of-place row or column represents 
at least one move needed.

#### Consistent:
This heuristic is consistent because moving a tile affects only its row and column, 
and the heuristic decreases by at most one for each move, maintaining the consistency condition.

## Optimal Solution
| Algorithm  | Optimality                                                                                                                                                                                                              |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BFS        | Yes. BFS guarantees by defintion finding the shortest path to the goal state in terms of the number of moves because it explores all nodes at a given depth before moving to the next depth level.                      |
| IDDFS      | Yes. IDDFS also guarantees finding the shortest path to the goal state by incrementally increasing the depth limit and performing depth-limited searches, ensuring that the first solution found is the optimal one.    |
| GBFS       | No. GBFS does not guarantee finding the shortest path because it prioritizes nodes based solely on the heuristic, potentially leading to suboptimal paths if the heuristic leads the search away from the optimal path. |
| A\* Search | Yes. A\* Search guarantees finding the shortest path to the goal when the heuristic used is both admissible and consistent, which is the case with the chosen heuristic in this program.                                |


## Example Usage
all executions shall be done like this:
```bash
python Tiles.py 1 2 3 4 5 6 7 8 0
```

1. sanity checks:  
`0 1 2 3 4 5 6 7 8` - expecting zero moves  
`1 2 0 3 4 5 6 7 8` - expecting two move

2. if not solvable:  
`0 2 1 3 4 5 6 7 8` - expecting error message

3. provided example:  
`1 4 0 5 8 2 3 6 7` - takes a reasonable amount of time

4. hard example:  
`0 1 2 3 5 7 8 6 4` - takes forever

### Hard example output
```bash
> python.exe Tiles.py 0 1 2 3 5 7 8 6 4 
```
```
Initial board:
 0 | 1 | 2
---+---+---
 3 | 5 | 7
---+---+---
 8 | 6 | 4
Algorithm: BFS
Nodes Expanded: 18596
Path to Goal: [3, 8, 6, 5, 7, 4, 5, 7, 8, 6, 7, 8, 4, 5, 8, 7, 6, 3]

Algorithm: IDDFS
Nodes Expanded: 115025033
Path to Goal: [3, 8, 6, 5, 7, 4, 5, 7, 8, 6, 7, 8, 4, 5, 8, 7, 6, 3]

Algorithm: GBFS
Nodes Expanded: 597
Path to Goal: [3, 5, 7, 4, 6, 7, 5, 3, 1, 5, 4, 2, 5, 1, 3, 4, 7, 6, 2, 5, 1, 7, 4, 8, 6, 4, 8, 3, 7, 1, 5, 8, 4, 2, 8, 5, 1, 7, 3, 4, 7, 1, 5, 8, 2, 7, 4, 6, 7, 2, 8, 4, 2, 7, 6, 3, 1, 2, 4, 5, 2, 1]

Algorithm: A*
Nodes Expanded: 373
Path to Goal: [3, 8, 6, 5, 7, 4, 5, 7, 8, 6, 7, 8, 4, 5, 8, 7, 6, 3]
```