"""
Write a function that takes an integer and returns an array [A, B, C], 
where A is the number of multiples of 3 (but not 5) below the given integer, 
B is the number of multiples of 5 (but not 3) below the given integer and 
C is the number of multiples of 3 and 5 below the given integer.

For example, solution(20) should return [5, 2, 1]
"""

def solution(number):
    three = []
    five = []
    five_three = []
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            five_three.append(i)
        if i % 3 == 0 and i % 5 != 0:
            three.append(i)
        if i % 5 == 0 and i % 3 != 0:
            five.append(i)
        else:
            pass
    return [len(three), len(five), len(five_three)]


def solution(number):
    A = (number - 1) // 3
    B = (number - 1) // 5
    C = (number - 1) // 15    
    return [A - C, B - C, C]