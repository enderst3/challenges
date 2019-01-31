"""
You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. 
Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

#Example:

a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13
"""

def mxdiflg(a1, a2):
    try:
        longer = a1 if len(a1) >= len(a2) else a2
        shorter = a2 if len(a1) >= len(a2) else a1
        return max([abs(len(x) - len(y)) for x in longer for y in shorter])
    except ValueError:
        return -1