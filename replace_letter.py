'''
Write a function that given an input string. replaces every letter with its position in the
 alphabet, amd returns a space separated string of the result.

 in: "The sun sets at twelve 'o clock"
 out: '"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"'
'''


def alphabet(input_string):

    input_string = input_string.lower()

    output_numbers = []

    for letter in input_string:

        number = ord(letter) - 96

        if number > 0:
            output_numbers.append(number)

        else:
            pass

    return ' '.join(str(num) for num in output_numbers)

alphabet("The sun sets at twelve 'o clock")
