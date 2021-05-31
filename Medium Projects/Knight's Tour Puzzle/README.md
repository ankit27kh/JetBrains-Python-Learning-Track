This is the next project I completed on the track.

Objectives:

1. Set up the board. Ask for board dimension and starting position.

2. Ask the player whether they want to try the puzzle or see the solution with a line 'Do you want to try the puzzle? (y/n):'. If the user enters y, proceed to step 3. If the user enters n, proceed to step 4. In the case of any other input, ask the same question.

3. If the player wants to try the puzzle, check whether the board has a solution. If not, print 'No solution exists!' and end the game. Otherwise, let the player give the puzzle a try like in the previous stage.

4. If they want to see the solution, check whether the board has one. Print 'No solution exists!' in case there is none. If a solution exists, label the starting point as 1, then label each move with the next number until you have visited all the squares.

5. If the board is big and the number of moves exceeds 9, use spaces for the extra digits and align the text to the right.

---

NOTE: This project uses Warnsdorff's rule. I am not completely sure that it works in all cases.  
If the area of the board is larger than 25 and you choose to try the board, it will not check for a solution and directly ask you to play.  
Instead, if you choose to see to the solution, it might say no solution exists even when there is a solution in some cases where backtracking is required.  
This last point has not been fully verified.
