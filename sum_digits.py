'''
print the sum of the digits in a number
'''


def sum_digits(num):
    '''
    num = abs(num)

    print(sum(map(int, str(num))))
    return sum(map(int, str(num)))
    '''
    print(sum(int(digit) for digit in str(abs(num))))
    return sum(int(digit) for digit in str(abs(num)))
sum_digits(123456)
sum_digits(10)
sum_digits(-196)
