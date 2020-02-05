'''
exchange the elements of two arrays in-place in a way that their new content is also reversed.
'''

a = ["1", "2", "3", "4", "5", "6", "7"]
b = ["a", "b", "c"]

def exchange_with(a, b):
    a, b = b, a
    a.reverse()
    b.reverse()
    print(a, b)
   


    