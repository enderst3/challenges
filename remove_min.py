'''
Given an array of integers, remove the smallest value. If there are multiple
elements with the same value, remove the one with a lower index.
If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.
'''


def remove_smallest(numbers):

    if numbers == []:
        print(numbers)
        return numbers

    else:
        numbers.remove(min(numbers))
        print(numbers)
        return numbers

remove_smallest([])
remove_smallest([5, 3, 2, 1, 4])
remove_smallest([1, 2, 3, 4, 5])
remove_smallest([1, 2, 3, 1, 1])
