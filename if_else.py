"""
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""

if __name__ == '__main__':
    n = int(input())
    if n % 2 != 0:
        print('Weird')
    elif ((n % 2 == 0) and (n in range(6, 21))):
        print('Weird')
    else:
        print('Not Weird')