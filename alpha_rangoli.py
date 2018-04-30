"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)

Output Format

Print the alphabet rangoli in the format explained above.

Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""

import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(L[:0:-1]+L))

