This is the next project I did on the track. Biggest yet. Enjoyed it.

This is a game of Dominoes with the computer. The rules of the game are as described in the project and are not mentioned here.

Objectives:
1. Generate a full domino set. Each domino is represented as a list of two numbers. A full domino set is a list of 28 unique dominoes.
2. Split the full domino set between the players and the stock by random. You should get three parts: Stock pieces (14 domino elements), Computer pieces (7 domino elements), and Player pieces (7 domino elements).
3. Determine the starting piece and the first player. Modify the parts accordingly. You should get four parts with domino pieces and one string indicating the player that goes first: either "player" or "computer".
4. If the starting piece cannot be determined (no one has a double domino), reshuffle, and redistribute the pieces (step 3).
5. Print the header using seventy equal sign characters (=).
6. Print the number of dominoes remaining in the stock – 'Stock size:' [number].
7. Print the number of dominoes the computer has – 'Computer pieces:' [number].
8. Print the domino snake. At this stage, it consists of the only starting piece.
9. Print the player's pieces, 'Your pieces:', and then one piece per line, enumerated.
10. Print the status of the game:
	If status = "computer", print "Status: Computer is about to make a move. Press Enter to continue..."
	If status = "player", print "Status: It's your turn to make a move. Enter your command."
11. At the end of the game, print one of the following phrases:
	Status: The game is over. You won!
	Status: The game is over. The computer won!
	Status: The game is over. It's a draw!
12. Print only the first and the last three pieces of the domino snake separated by three dots if it exceeds six dominoes in length.
13. Add a game loop that will repeat the following steps until the game ends:
	Display the current playing field .
	If it's a user's turn, prompt the user for a move and apply it. If the input is invalid (a not-integer or it exceeds limitations), request a new input with the following message: Invalid input. Please try again..
	If it's a computer's turn, prompt the user to press Enter, AI will make the move.
	Switch turns.
14. Verify that the move entered by the player is legal (requirement #1).
	 If not, request a new input with the following message: 'Illegal move. Please try again.'.
15. Place dominoes with the correct orientation (requirement #2).
16. The AI should use the following algorithm to calculate the score:
	Count the number of 0's, 1's, 2's, etc., in your hand, and in the snake.
	Each domino in your hand receives a score equal to the sum of appearances of each of its numbers.
	The AI will now attempt to play the domino with the largest score, trying both the left and the right sides of the snake. If the rules prohibit this move, the AI will move down the score list and try another domino. The AI will skip the turn if it runs out of options.
