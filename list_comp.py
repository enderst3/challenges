"""
Let’s learn about list comprehensions!
You are given three integers X, Y and Z representing the dimensions of a 
cuboid along with an integer. 
You have to print a list of all possible coordinates given by (i, j, k)
 on a 3D grid where the sum of i+j+k is not equal to N .
  Here, 0<=i<=X; 0<=j<=Y; 0<=k<=Z.

Input Format

Four integers X,Y,Z and N each on four separate lines, respectively.

Constraints

Print the list in lexicographic increasing order.

Sample Input

1

1

1

2

Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Solution:

First we have read all the values x, y, z, n input from user
and convert those values to integer. Then we use list comprehension.

Here we have applied a list comprehension inside the print function.
It sum up to, for all the value of i in x+1, for all the value of j in y+1, 
for all the value of k in z+1, if the value of i+j+k is not equal to n, 
append the value of [ i , j, k ] in list. 
After all the loop have run their course, the list is print out.
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n)])
