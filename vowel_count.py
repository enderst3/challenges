"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.
"""

def getCount(inputStr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = []
    for i in inputStr:
        if i.lower() in vowels:
            count.append(i)
    return len(count)

def getCount(inputStr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([i for i in inputStr if i.lower() in vowels])