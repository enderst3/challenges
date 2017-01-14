'''
write a function that takes a string of parentheses, and determines if the
order of the parentheses is valid.

>>> is_correct('()')
True
>>> is_correct(')(()))')
False
>>> is_correct("(' )")
True
>>> is_correct("(())((()())())")
True
'''


def is_correct(input_string):

    if input_string[0] == '(' and input_string[-1] == ')':

        open = []
        closed = []

        for char in input_string:
            if char == '(':
                open.append(char)

            elif char == ')':
                closed.append(char)

        if len(open) == len(closed):
            return True

        else:
            return False

    else:
        return False
