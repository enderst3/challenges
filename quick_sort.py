'''
write a function that sorts a list.
'''


def quicksort(start_list):
    if len(start_list) < 1:
        print(start_list)
        return start_list

    else:
        print(sorted(start_list))
        return sorted(start_list)

quicksort([17, -5, 3, -15])
quicksort([3, 0, 7, 5, 1, 2, 9, 8, 4, 6])
quicksort([])
quicksort([9])
