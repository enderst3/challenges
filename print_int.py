"""
Read an integer N .

Without using any string methods, try to print the following:
123...N

Note that "" represents the values in between.

N= 3
print out 123
"""

def print_int(n):
    num_list = []
    for i in range(1, n+1):
        num_list.append(i)
    for num in num_list:
        print(num, end='')