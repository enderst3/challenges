"""
Task
Your task is to find the similarity of given sorted arrays a and b, which is defined as follows:

you take the number of elements which are present in both arrays and divide it by the number of elements 
which are present in at least one array.

It also can be written as a formula similarity(A, B) = #(A ∩ B) / #(A ∪ B), where #(C) 
is the number of elements in C, ∩ is intersection of arrays, ∪ is union of arrays.

This is known as Jaccard similarity.

The result is guaranteed to fit any floating-point type without rounding.

Example
For a = [1, 2, 4, 6, 7] and b = [2, 3, 4, 7]:

elements [2, 4, 7] are present in both arrays;
elements [1, 2, 3, 4, 6, 7] are present in at least one of the arrays.
So the similarity equals to 3 / 6 = 0.5.
"""

def similarity(a, b):
    sim = []
    for i in a:
        if i in b:
            sim.append(i)
    return len(sim)/len(list(set(a+b)))

"""
Solution using sets
def similarity(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b)
"""