'''
Write a function that finds the shortest possible text snippet in a given string, containing all of the target words
in an input list of strings.

The function will take a string and a list as input, and returns a string as output, and return the earliest match.
If there are no matches it returns none.

In: 'many students are writing code', [students, code]
Out: 'students are writing code'

In: 'a b c d a', [a, c, d]
Out: 'c d a'
'''


def target_words(input_string, input_list):

    input_string = list(input_string)
    output_list = []

    for i in input_list:
        if i in input_string:


    print(output_list)

target_words('a b c d a', ['a', 'c', 'd'])
