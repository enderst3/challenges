'''
Capitalize the first letter of each word in a string.

'the quick brown fox jumped over the lazy dog'
"I've got a fever for more cowbell"
'''


def cap_words(string):
    '''
    string = string.split(' ')

    output = []

    for word in string:
        word = word.capitalize()
        output.append(word)

    print(' '.join(word for word in output))
    return ' '.join(word for word in output)
    '''
    print(" ".join(word.capitalize() for word in string.split()))
    return " ".join(word.capitalize() for word in string.split())

cap_words("Luke I am your father")
cap_words("I've got a fever for more cowbell")
