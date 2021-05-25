This is the first project I completed in the 'Medium' projects category.

Objectives:
1. With the first message, the program should ask for a difficulty level:

	1 - simple operations with numbers 2-9

	2 - integral squares 11-29

2. A user enters an answer.

	For the first difficulty level: the task is a simple math operation; the answer is the result of the operation.

	For the second difficulty level: the task is an integer; the answer is the square of this number.

	In case of another input: ask to re-enter. Repeat until the format is correct.

3. The application gives 5 tasks to a user.

4. The user receives one task, prints the answer.

	If the answer contains a typo, print 'Incorrect format.' and ask to re-enter the answer. Repeat until the answer is in the correct format.

	If the answer is a number, print 'Right!' or 'Wrong!' Go to the next question.

5. After five answers, print 'Your mark is N/5.' where N is the number of correct answers.

6. Output 'Would you like to save your result to the file? Enter yes or no.'

	In case of 'yes', 'YES', 'y', 'Yes': the app should ask the username and write 'Name: n/5 in level X (<level description>).' (X stands for the level number) in the 'results.txt' file. For example — 'Alex: 3/5 in level 1 (simple operations with numbers 2-9).'

	The results should be saved to the file immediately after the user gave the positive answer to the question 'Would you like to save your result to the file?'

	If the file 'results.txt' does not exist, you should create it.

7. In case of 'no' or any other word: exit the program.