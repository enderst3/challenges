"""
Task 
Given 2 sets of integers, m and n, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either n or m but do not exist in both.

Input Format

The first line of input contains an integer, m. 
The second line contains m space-separated integers. 
The third line contains an integer,n . 
The fourth line contains m space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12
Easy
Submitted 30364 times
Max Score 10
Need Help?

View Discussions
View Editorial Solution
View Top Submissions
RATE THIS CHALLENGE

Download problem statement
Download sample test cases
Suggest Edits

"""

# set all inputs to a variable
# join the multi int inputs
a = input()
b = input().split()
c = input()
d = input().split()

# create sets
setb = set(b)
setd = set(d)

# get rid of any that are simular in each set
difb = setb.difference(setd)
difd = setd.difference(setb)

# create a sorted set.
# key int, means it uses int values of the union
# could use difb^difd also
set_union = sorted(difb.union(difd), key=int)

# print set_union
for i in set_union:
    print(i)


