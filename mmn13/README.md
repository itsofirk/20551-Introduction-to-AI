# Reversi - mmn 13

## 1. The Game

### 1. The state space

A reversi game is typically played on a square board, in our case an 8×8 board, 
which makes it very easy to represent using a (8, 8) matrix.  
Each cell contains one of three symbols: `X`, `O`, or the empty cell representation `-`.  
The state space has `3^n` different states, which in our case translates into `~3×10³⁰` possible states.
	
### 2. Initial State

The initial state is defined as follows:

```
̲ ̲|̲ ̲0̲ ̲1̲ ̲2̲ ̲3̲ ̲4̲ ̲5̲ ̲6̲ ̲7̲
0| - - - - - - - -  
1| - - - - - - - -  
2| - - - - - - - -  
3| - - - X O - - -   
4| - - - O X - - -  
5| - - - - - - - -  
6| - - - - - - - -  
7| - - - - - - - - 
```

### 3. Players

There are two Players
- Player 1 is represented by `X`
- Player 2 is represented by `O`
	
### 4. Actions

An action is defined by placing a disk on the board (In practice, using the coordinates of the board):
- An action is represented by a pair of numbers `(x, y)` where:
	- `x` is the row number (from top to bottom).
	- `y` is the column number (from left to right)

For example, `(3, 2)` means placing a disk in the 4th row and 3rd column.  

### 5. Transition Model

When a player makes a move, the transition model updates the game state through the following steps:

1. **Place the Disk**: Set the cell in `(x, y)` with the player's disk.

2. **Flip Opponent's Disks**:
   - **Directions to Check**: There are eight directions to look for opponent disks to flip:
     - Up, Down, Left, Right
     - Diagonally up-left, up-right, down-left, down-right
   - **Flipping Process**:
     - For each direction, move step by step from the new disk.
     - Collect all consecutive opponent disks.
     - If you reach another disk of the player's color without any empty spaces, flip all the collected opponent disks to the player's color.

3. **Update the Board**: After flipping the necessary disks, the board reflects the new state.

4. **Switch Player**: Change the turn to the other player.

### 6. Terminal States

The game ends when one of the following happens:
- The board is full, meaning no more moves can be made.
- Both players have no more move.

The winning player is the one who has more disks on the board.

### 7. Utility

The Utility function is calculated based on the difference in the number of disks each player has on the board when the game ends.
`Utility = (Number of Player’s Disks) − (Number of Opponent’s Disks)`  

**Purpose**: This utility value determines the outcome of the game.
Positive values indicate a win for the player, while negative values indicate a win for the opponent.

By implementing this utility function, the program can effectively determine the best possible moves by maximizing the player's disk count while minimizing the opponent's, 
ultimately leading to an optimal strategy for winning the game.

### Bad States Examples

- **Illegal State:**  
    It is illegal to place a disk that has no opponent disks to flip, especially if it has no surrounding disks.
```
̲ ̲|̲ ̲0̲ ̲1̲ ̲2̲ ̲3̲ ̲4̲ ̲5̲ ̲6̲ ̲7̲
0| - - - - - - - -  
1| - - - - - - - -  
2| - - - - - - - -  
3| - - - X O - - -   
4| - - - O X - - -  
5| - - - - - - - -  
6| - - - - - - - -  
7| x - - - - - - - 
```

- **Unreachable State:**  
    Since there is no way to remove disks from the board it is impossible to reach a state where the initial disks are missing.
```
̲ ̲|̲ ̲0̲ ̲1̲ ̲2̲ ̲3̲ ̲4̲ ̲5̲ ̲6̲ ̲7̲
0| - - - - - - - -  
1| - - - - - - - -      
2| - - - - - - - -  
3| - - - - - - - -   
4| - - - - - - - -  
5| - - - - - - - -  
6| X O - - - - - -  
7| O X - - - - - -
```

### Player Strategies

The code introduces a `BaseMover` interface so that various move-selection strategies can be easily swapped in.

1. `InteractiveMover`: Prompts moves directly from the user via the console.
2. `RandomMover`: Picks moves uniformly at random, helpful for generating diverse states.
3. `MethodicalMover`: Uses a simple numeric rule `(row % (col+1))` to deterministically choose moves.

This modular design allows testing different approaches by simply changing the mover class.


## 2. Heuristic Functions

At this stage, we introduce two different heuristic evaluation functions, `H1` and `H2`.
Both functions take a board state and return a numeric value estimating its quality for a specific player. 
These heuristics are used to guide move selection one step ahead, meaning that each player will choose actions that appear best according to the chosen heuristic.

### H1 – Disk Count Difference  
H1 calculates the difference between the number of the current player's disks and the opponent's disks:  
`H1(state, color) = (Number of Current Player Disks) - (Number of Opponent Disks)`  
_Motivation_: A higher positive value implies that the current player is leading in disk count, thus is presumably in a better position.

### H2 – Weighted Board Control  
H2 sort of expands H1, it considers the disk count as well as assigns higher importance to certain strategic positions on the board.
For example, corner cells are typically more valuable, as they cannot be flipped once placed. Edges might be slightly more valuable than central squares.  

 - The weighting scheme:
   - Corners: +3 points per owned corner
   - Edges (non-corner): +1 point per owned edge disk
   - Other positions: 0 points beyond their normal count (already reflected by disk count)

```
H2(state, color) = (Number of Current Player Disks - Number of Opponent Disks) + \
                    3*(Current Player Corners - Opponent Corners) + \
                    (Current Player Edges - Opponent Edges)
```

_Motivation_: This heuristic values both advantage by quantity and quality of positioning.

### Example States and Heuristic Computation

#### State A (6 disks)
```
̲ ̲|̲ ̲0̲ ̲1̲ ̲2̲ ̲3̲ ̲4̲ ̲5̲ ̲6̲ ̲7̲
0| - - - - - - - - 
1| - - - - - - - - 
2| - - - - X O - - 
3| - - - X O - - - 
4| - - - O X - - - 
5| - - - - - - - - 
6| - - - - - - - - 
7| - - - - - - - -
```

- Current player: Player 1
- Count: Player 1 = 4, Player 2 = 2
 
1. `H1 = (Player 1 count) - (Player 2 count) = 4 - 2 = 2`
2. Corners: None owned by Player 1 or Player 2.  
   Edges: no edge advantage here since all disks are central.
   `H2 = (4 - 2) + 3*(0 - 0) + (0 - 0) = 2`

### State B (24 disks)
```
̲ ̲|̲ ̲0̲ ̲1̲ ̲2̲ ̲3̲ ̲4̲ ̲5̲ ̲6̲ ̲7̲
0| O O X X - - - - 
1| O X X X O - - - 
2| O X O X X - - - 
3| X X O O X - - - 
4| X O X O X - - - 
5| - - - - - - - - 
6| - - - - - - - - 
7| - - - - - - - -
```
- Current player: Player 1
- Count Player 1 = 14, Player 2 = 10

1. `H1 = (Player 1 count) - (Player 2 count) = 10 - 9 = 1`
2. Corners: Player 2 owns 1 corner.  
   Edges: Player 1 owns 4, Player 2 owns 3.
   `H2 = (14 - 10) + 3*(0 - 1) + (4 - 3) = 4 - 3 + 1 = 2`    
   H2 penalizes Player 1 here because Player 2 owns a corner and also has more edge control.

### State C (33 disks)
```
̲ ̲|̲ ̲0̲ ̲1̲ ̲2̲ ̲3̲ ̲4̲ ̲5̲ ̲6̲ ̲7̲ 
0| - X X X X X X X
1| O X O - O O - -
2| - X - O O O - -
3| O X O O O - - -
4| - X - O O - - -
5| X X O O O - - -
6| - - O - O O - -
7| - - - - - - O -
```

- Current player: Player 2
- Count Player 1 = 13 disks, Player 2 = 20 disks

1. `H1 = (Player 2 count) - (Player 1 count) = 20 - 13 = 7`
2. Corners: Player 1 owns 1 corner.  
   Edges: Player 1 owns 7, Player 2 owns 2.
   `H2 = (20 - 13) + 3*(0 - 1) + (2 - 7) = 7 - 3 - 5 = -1`