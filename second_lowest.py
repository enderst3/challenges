"""
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade,
order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; 
the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics;
if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output
Berry
Harry
Explanation
There are  students in this class whose names and grades are assembled to build the following list:
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], 
['Akriti', 41],['Harsh', 39]]
The lowest grade of 37.2 belongs to Tina. 
The second lowest grade of 37.1 belongs to both Harry and Berry, 
so we order their names alphabetically and print each name on a new line.

"""



if __name__ == '__main__':
    students = []
    student_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score]) # create a list names and scores
        student_scores.append(score) # create a list of scores
    
    score_set = set(list(student_scores)) # create set of scores
    lowest = min(score_set) # find lowest
    score_set.remove(lowest) # remove lowest
    second_lowest = min(score_set) # find second lowest
    students.sort() # sort students list
    for student in students: # loop through and find and print any that match
        if student[1] == second_lowest:
            print(student[0])