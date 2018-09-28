"""
Write a function named repeater() that takes two arguments (a string and an integer), 
and returns a new string where the input string is repeated that many times. For example:

repeater('a', 5)
should return

'aaaaa'
and

repeater('Na', 16)
should return

'NaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNa`
"""

def repeater(string, n):
    return string * n

