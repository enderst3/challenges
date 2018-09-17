"""
You are given an array (which will have a length of at least 3, but could be very large) 
containing integers. The array is either entirely comprised of odd integers or entirely comprised of even 
integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)

"""

def find_outlier(integers):
    odd_list = []
    even_list = []
    for i in integers:
        if i % 2 != 0:
            odd_list.append(i)
        else:
             even_list.append(i)
    if len(odd_list) < len(even_list):
        return sum(odd_list)
    else:
        return sum(even_list)

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]