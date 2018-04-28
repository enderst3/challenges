"""
Swap the cases of a a given string
"""

def swap_case(s):
    swapped = ''
    for char in s:
        if char.isupper():
            swapped = swapped + char.lower()          
        else:
            swapped = swapped + char.upper()
   
    return swapped