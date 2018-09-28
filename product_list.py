"""
Calculate the product of all elements in an array.

In Python, if the array is empty or None, return None.

"""

# numpy 
import numpy

def product(numbers):
    if numbers == [] or numbers == None:
        return None
    else:
        return numpy.prod(numbers)

# reduce 
from functools import reduce 

def product(numbers):
    if numbers == [] or numbers == None:
        return None
    else:
        return reduce((lambda x, y: x * y),numbers)
