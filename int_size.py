"""
Read four numbers, a,b ,c ,d and , and print the result of .

Input Format 
Integers a, b, c, and d  are given on four separate lines, respectively.

Sample Input

9
29
7
27
Sample Output

4710194409608608369201743232  
"""

a , b , c , d = int(input()) , int(input()) , int(input()) , int(input())
print(pow(a,b) + pow(c,d))