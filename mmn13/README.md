# Reversi Game Implementation

## 1A. Demonstration of the Transition Model

### Overview

The transition model explains how the game changes when a player makes a move.  
When a player places a disk on the board, some of the opponent's disks might be flipped to the player's color. The transition model handles this process and updates the game state accordingly.

### Actions

An action is defined by placing a disk on the board (In practice, using the coordinates of the board):

- An action is represented by a pair of numbers `(x, y)` where:
  - `x` is the row number (from top to bottom).
  - `y` is the column number (from left to right).

For example, `(3, 2)` means placing a disk in the 4th row and 3rd column.

### Checking Valid Actions

Before a player can make a move, we need to make sure it's valid. An action `(x, y)` is valid if:

1. `(x, y)` is empty.
2. Placing a disk there will flip at least one of the opponent's disks. This happens if the new disk creates a straight line (horizontal, vertical, or diagonal) between the new disk and another disk of the player's color, with one or more opponent disks in between.

### Transition Model

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

### Simple Example

Imagine the board looks like this before the move (Player 1 is `x` and Player 2 is `o`):

```
̲ ̲|̲ ̲0̲ ̲1̲ ̲2̲ ̲3̲ ̲4̲ ̲5̲ ̲6̲ ̲7̲
0| - - - - - - - -  
1| - - - - - - - -  
2| - - - - - - - -  
3| - - - x o - - -   
4| - - - o x - - -  
5| - - - - - - - -  
6| - - - - - - - -  
7| - - - - - - - - 
```


**Player 1 plays `(2, 3)`**:

1. **Place `x` in `(2, 3)`**

2. **Check Directions**:
   - **Down Direction `(1, 0)`**:
     - Next cell `(3, 3)` has `x` (Player 1).
     - No opponent disks to flip in this direction.
   - **Down-Right Direction `(1, 1)`**:
     - Next cell `(3, 4)` has `o` (Player 2).
     - Next cell `(4, 5)` is `E` (empty), so no flip in this direction.
   - **Right Direction `(0, 1)`**:
     - Next cell `(2, 4)` is `E` (empty), so no flip.
   - **Other Directions**:
     - No opponent disks to flip.

3. **Result**:
   - Only the new disk is placed. No disks are flipped in this example.

**Updated Board**:

