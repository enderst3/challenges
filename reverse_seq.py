"""
Get the number n (n>0) to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]

"""

def reverse_seq(n):
    return [i for 1 in range(n,0,-1)]


def reverse_seq(n):
    out = []
    for i in range(1, n+1):
        out.append(i)
    out.reverse()
    return out