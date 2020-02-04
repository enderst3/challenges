'''
def exchange_with(a, b):
    a.reverse()
    b.reverse()
    a[:], b[:] = list(b), list(a)
'''

a = ["1", "2", "3", "4", "5", "6", "7"]
b = ["a", "b", "c"]

def exchange_with(a, b):
    a.reverse()
    b.reverse()
    a[:], b[:] = list(b), list(a)