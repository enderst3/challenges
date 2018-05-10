"""
Task

You are given a date. Your task is to find what the day is on that date.

Output Format

Output the correct day in capital letters.

Sample Input

08 05 2015
Sample Output

WEDNESDAY
Explanation

The day on August 5th 2015 was WEDNESDAY.
"""

import datetime

print(datetime.datetime.strptime(input(), '%m %d %Y').strftime('%A').upper())