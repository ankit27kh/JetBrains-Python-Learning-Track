This is the next project I completed on this track.

Objectives:

1. Read an integer N from the input. This integer represents the maximum number of students for each department.

2. Read the file named "applicants.txt". For example, Willie McBride 76 45 79 80 100 Physics Engineering Mathematics. (Scores are in order of physics, chemistry, math, computer science, special exam). (Subjects are in order of preference 1, 2, 3).

3. Choose the best score for a student in the ranking: either the mean score for the final exam(s) or the special exam's score. Each department has there own preference. Physics - (physics + math), Chemistry - (Chemistry), Math - (Math), Biotech - (Chemistry + Physics), Engineering - (Computer Science + Math)

4. There should be no more than N accepted applicants for each department; use the same principles for sorting.

5. Output the names and the student's best score, either the mean finals score or the special exam's score to individual files for each department.