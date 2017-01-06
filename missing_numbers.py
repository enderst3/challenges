'''
Write a function that finds missing numbers from a list.
'''


def missing_numbers(num_list):

    num_list = [int(num) for num in num_list.split(' ')]

    output = []

    for num in range(min(num_list), max(num_list)):
        if num not in num_list:
            output.append(num)

    return output

print(missing_numbers('10 13 15 12'))
print(missing_numbers('1 5'))

'''
Find the missing number, starting from 1,  if none missing return 0, if more
than one return the first missing number, if there is a non-numeric number
return 1.
'''


def missing_numbers(num_list):

    try:
        num_list = list(map(int, num_list.split()))
        num_list.sort()

    except ValueError:
        return 1

    last_num = 0

    for num in num_list:

        if num != last_num + 1:
            return last_num + 1

        last_num = num
    return 0


print(missing_numbers('1 3 5 2 a'))
print(missing_numbers('1 2 3 4 5'))
print(missing_numbers('1 3 5 2'))
print(missing_numbers('1 5'))
