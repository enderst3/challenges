"""
A set is an unordered collection of elements without duplicate entries. 
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, 
she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Sample Input

10
161 182 161 154 176 170 167 171 170 174
Sample Output

169.375
"""

def average(array):
    return float(sum(set(array)) / len(set(array)))