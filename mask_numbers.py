'''
Given an input string "mask" all of the characters with a "#"
except for the last for characters.

In: '123456789'  >>  out: '#####6789'
'''


def mask(numbers):

    last_four = numbers[-4:]
    mask = numbers[0:-4:]

    final_list = []

    for num in mask:
        num = '#'
        final_list.append(num)

    print(''.join(final_list)+last_four)

mask('12345678912345')
