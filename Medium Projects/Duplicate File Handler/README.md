This is the next project I completed.

Objectives:

Stage 1:  
1. Accept a command-line argument that is a root directory with files and folders. Print Directory is not specified if there is no command-line argument;

2. Iterate over folders and print file names with their paths. The direction of the slashes in the printed out paths do not matter. Tests are platform independent, so different style of slashes ("/" or "\") are valid.

Stage 2:  
1. Accept a command-line argument that is a root directory with files and folders. Print Directory is not specified if there is no command-line argument;

2. Read user input that specifies the file format. Empty input should match any file format;

3. Print a menu with two sorting options: Descending and Ascending. They both represent the respective order by size of groups of files. Read the input. Print Wrong option if any other input is entered. Repeat until a correct input is provided;

4. Iterate over folders and print the information about files of the same size: their size, path, and names.

Stage 3:  
1. Ask for duplicates check;

2. Read user input: yes or no . Print Wrong option if any other input is received. Repeat until a user provides a valid answer. If the input is yes, get the hash of files of the same size; group the files of the same hash, assign numbers to these files. Otherwise, the program should stop the operation;

3. Assign numbers to lines with files after hashing. You should assign numbers to files based on the total number of files in output. It is needed for the purpose of the next stage.

4. Print the information about the files of the same outputs along with their hashes. Sort the group of files by size as in the previous stage. You don't have to sort hash subgroups.

Stage 4:  
1. Ask a user whether they want to delete files. Expect either yes or no as the answer. Print Wrong option if it receives any other input. Repeat until a user provides a valid answer. If yes, read what files a user wants to delete. Otherwise, abort the program;

2. Read a sequence of files that a user wants to delete. Input should contain only file numbers separated by spaces. Print Wrong format if it receives empty string or any other input. Repeat until a user provides a valid answer;

3. Print the total freed up space in bytes.
