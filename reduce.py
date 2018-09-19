"""
Given an array of integers (x), return the result of multiplying the values together in order. Example:

[1, 2, 3] --> 6
"""

import functools

def grow(arr):
    arr.sort(key=int)
    return functools.reduce(lambda x,y: x*y, arr)
    

from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x*y, arr)