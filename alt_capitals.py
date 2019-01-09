"""
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, 
and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!
"""

def capitalize(s):
    new_s = ''
    for i in range(0, len(s)):    
        if i % 2 == 0:
            new_s += s[i].upper()
        else:
            new_s += s[i]       
    print([new_s, new_s.swapcase()])
    return [new_s, new_s.swapcase()]


def capitalize(s):
    new_s = ''
    for k,v  in enumerate(s):    
        if k % 2 == 0:
            new_s += v.upper()
        else:
            new_s += v       
    print([new_s, new_s.swapcase()])
    return [new_s, new_s.swapcase()]