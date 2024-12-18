### A. Demonstration of the Transition Model

Let's look at the following board state:
```
̲ ̲|̲ ̲0̲ ̲1̲ ̲2̲ ̲3̲ ̲4̲ ̲5̲ ̲6̲ ̲7̲
0| - - - - - - - -  
1| - - - - - - - -  
2| - - - - X O - -  
3| - - - X O - - -  
4| - - X X X - - -  
5| - - - - - - - -  
6| - - - - - - - -  
7| - - - - - - - -
```
this state consists of 7 disks. it was reached after 3 moves, which means its player 2's turn.  
The possible moves are (5, 2), (1, 4), (5, 4), (2, 3), (3, 2) .

State 3:
- - - - - - - -  
- - - - - - - -  
- - - - X O - -  
- - - X O - - -  
- - X O X - - -  
- - O - - - - -  
- - - - - - - -  
- - - - - - - -

State 3, Player 2 moved, Action ()

Result – Player 1: 4 disks, Player 2: 1 disk, Total: 5 disks