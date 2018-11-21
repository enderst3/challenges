"""
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

For example an array [2, 3, 9] equals 239, add one would return an array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (language equivalent) for invalid inputs
"""

def up_array(arr):
    # check to see if a list, or if neg or int over 9 
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None
    else:
        # second part makes a string out of the list, and increments 1
        # brackets make it a list, and the first loop makes the sting into a list
        return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
      