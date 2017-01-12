'''
sort the letters in a string alphabetically.
'''


def sort_letters(words):
    '''
    if words == '' or words == None:
        print('Invalid String!')
    else:
        print(''.join(sorted(words)))
    '''

    if not words:
        print("Invalid String!")
        return "Invalid String!"
    print(''.join(sorted(words)))
    return "".join(sorted(words))


sort_letters('Hello World')
sort_letters('goodbye!')
sort_letters('')
sort_letters(None)
