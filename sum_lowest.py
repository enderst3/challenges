'''
Return the sum of the two lowest positive integers in a list.
'''


def lowest_two(num_list):
    '''
    num_list = sorted(num_list)
    sum_lowest = sum(num_list[:2])
    print(sum_lowest)
    return sum_lowest
    '''
    sum_lowest = sum(sorted(num_list)[:2])
    print(sum_lowest)
    return sum_lowest

lowest_two([19, 16, 24, 4, 36])
