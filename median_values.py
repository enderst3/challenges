"""
Your non-profit company has assigned you the task of calculating some simple statistics on donations. 
You have a very LONG array of integers, representing various amounts of donations your company has been given. 
In particular, you're interested in the median value for donations.

The median is the middle number of a sorted list of numbers. If the list is of even length, 
the 2 middle values are averaged.

Write a function that takes an array of integers as an argument and returns the 
median of those integers.

Note:
The sorting step is vital

median([33,99,100,30,29,50]) // =>  41.5
median([3,2,1]) // => 2
"""

def median(values):
    values.sort()
    if len(values) % 2 != 0:
        print(values[len(values)//2])
        return values[len(values)//2]
    val1 = int((len(values)/2)-1)
    val2 = int((len(values)/2)+1)
    print(sum(a[val1:val2]) / 2)
    return sum(a[val1:val2]) / 2

median([33,99,100,30,29,50])
median([3,2,1])   