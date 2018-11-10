"""
You are given an initial 2-value array (x). You will use this to calculate a score.

If both values in (x) are numbers, the score is the sum of the two. If only one is a number, the score is that number. If neither is a number, return 'Void!'.

Once you have your score, you must return an array of arrays. Each sub array will be the same as (x) and the number of sub arrays should be equal to the score.

For example:

if (x) == ['a', 3] you should return [['a', 3], ['a', 3], ['a', 3]]
"""

def explode(arr): 
    if type(arr[0]) != int and type(arr[1]) != int:
        return 'Void!'
    else:
        if type(arr[0]) != int:
            return [arr] * arr[1]
        elif type(arr[1]) != int:
            return [arr]* arr[0]
        else:
            return [arr] * sum(arr)


def explode(arr):  
    return [arr] * sum(v for v in arr if isinstance(v,int)) or 'Void!'