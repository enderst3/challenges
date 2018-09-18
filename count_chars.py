"""
The main idea is to count all the occuring characters(UTF-8) in string. 
If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }
"""

def count(string):
    dict = {}
    for i in string:
        dict[i] = dict.get(i,0)+1
    return dict