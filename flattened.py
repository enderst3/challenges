'''
Code to flatten nested lists

flatten([[5,2,89],["a", "b", "c", "d"],[12,53,90]])
flatten([[45], [36], [5, 7], [9], [9], [8, 76], [12, 22, 83, 45]])
flatten([[[45], [36]], [5, 7], [9], [9], [8, 76], [[12, 22, 83, 45]]])
'''


def flatten(start_list):
    flattened = []
    for sub_list in start_list:

        if type(sub_list) is list:
            flattened.extend(sub_list)

        else:
            flattened.append(sub_list)

    print(flattened)
    return flattened

flatten([[5, 2, 89], ["a", "b", "c", "d"], [12, 53, 90]])
