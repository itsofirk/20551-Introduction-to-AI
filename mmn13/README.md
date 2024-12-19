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