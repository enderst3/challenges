"""
Task
Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example
For n = 152, the output should be 52;

For n = 1001, the output should be 101.

Input/Output
[input] integer n

Constraints: 10 ≤ n ≤ 1000000.

[output] an integer

"""

def delete_digit(n):
  n = str(n)
  high_number = 0
  for i in range(len(n)):
      number = int(n[0:i]+n[i+1:])
      if number > high_number:
          high_number = number
  return high_number