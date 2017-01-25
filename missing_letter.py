'''
Find the missing letter in the list
'''
import string


def find_missing_letter(chars):
    '''
    charset = string.ascii_lowercase if chars[0] >= 'a' else string.ascii_uppercase
    for letter in charset[charset.index(chars[0]):]:
        if letter not in chars:
            print(letter[0])
            return letter[0]
    '''

    newlist = []

    for i in range(ord(chars[0]), ((ord(chars[0])+len(chars) + 1))):
        newlist.append(chr(i))

    newitem = list(set(newlist) - set(chars))
    print(', '.join(newitem))
    return ', '.join(newitem)

find_missing_letter(['O', 'Q', 'R', 'S'])
find_missing_letter(['a', 'b', 'd', 'f'])
