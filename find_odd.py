'''
Given an array, find the int that appears an odd number of times.

find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
'''


def find_it(seq):
    '''
    count_dict = {i: seq.count(i) for i in seq}

    for k, v in count_dict.items():

        if v % 2 == 0:
            pass
        else:
            return k
    '''

    k = [v for v in seq if seq.count(v) % 2][0]

    return k

find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
