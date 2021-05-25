This is the next project I completed on the track. This is a good project.

Objectives:
1. Set the minimal length of the string of zeros and ones that the user should enter. Let's choose the value 100: this will allow you to collect enough statistics without taking too much of the user's time.
2. Filter out inappropriate symbols from each user input.
3. Append the processed string to the general string containing all the data from the input.
4. Keep asking the user for new input strings and appending them to the general string until the length of the general string is equal or exceeds 100. If it exceeds 100, don't remove extra symbols: 100 symbols are the minimum required length, but the more data we have, the better.
5. Output the final data string.
6. Count how many times a certain character (0 or 1) follows a specific triad of numbers (All possible 3 digit combinations).
7. Ask the user to enter test strings or type 'enough' to exit the game. Each test string must be preprocessed (in order to leave only "0" and "1" symbols). After that, you should launch the prediction algorithm and calculate the number of correctly guessed symbols. After each iteration, you should show the player's balance with the message Your capital is now $X, where X is the player's virtual capital. Initial capital is $1000.
8. It would be great if you kept updating the system by allowing it to learn from the test data as well. However, this update should happen only after the prediction and the verification stages are done: let's be honest with the user.
9. Finish the game with the words Game over!.
