'''
Return the middle character of the word. If the word's length is odd,
return the middle character. If the word's length is even,
return the middle 2 characters.

'test'
'testing'
'''


def middle(word):
    
    if len(word) % 2 == 0:
        print(word[len(word) // 2 - 1]+word[len(word) // 2])
        return word[len(word) // 2 - 1] + word[len(word) // 2]

    else:
        print(word[len(word) // 2])
        return word[len(word) // 2]

middle('test')
