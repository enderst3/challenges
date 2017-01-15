'''
Given 3 ints, abc, return their sum.  if one of the values is 13 then it does not count
towards the sum and values to its right do not count.  If a is 13 b, and c do not count.
if a is 13 the return would be 0.

1 iterate through list
2 look for 13
3 if 13 found break loop
4 append any numbers to list
5 return sum of list
'''


def give_sum(numbers):

    sum_list = []

    for i in numbers:

        if i != 13:
            sum_list.append(i)

        else:
            break

    print(sum(sum_list))

numbers = [4, 13, 6]

give_sum(numbers)
