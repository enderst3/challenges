"""
Simple enough this one - you will be given an array. The values in the array will either be numbers or strings, 
or a mix of both. You will not get an empty array, nor a sparse one.

Your job is to return a single array that has first the numbers sorted in ascending order, 
followed by the strings sorted in alphabetic order. The values must maintain their original type.

Note that numbers written as strings are strings and must be sorted with the other strings.
"""

def db_sort(arr): 
    int_list = []
    str_list = []
    for i in arr:
        if type(i) is int:
            int_list.append(i)
        else:
            str_list.append(i)
    return sorted(int_list) + sorted(str_list)

def db_sort(arr): 
    return sorted(arr, key=lambda x: (isinstance(x,str),x))