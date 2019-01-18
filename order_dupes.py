"""
In this Kata, you will remove the left-most duplicates from an int array and return the result.

For example:
solve([3,4,4,3,6,3]) = [4,6,3]

-- remove the 3 in index 0 and index 3
-- remove the 4 in index 1

"""
def solve(arr): 
    dups = [] # new list
    for number in arr[::-1]: # loop thru in reverse
        if number not in dups: 
            dups.append(number) # append list
    print(dups)
    print(dups[::-1])
    return dups[::-1] # return reverse list