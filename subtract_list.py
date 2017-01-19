'''
subtract one list from another.
'''


def subtract_list(list_1, list_2):

    print([x for x in list_1 if x not in list_2])
    return [x for x in list_1 if x not in list_2]

subtract_list([1, 2], [2])
subtract_list([1, 2, 2], [1])
subtract_list([1, 2, 2], [])
