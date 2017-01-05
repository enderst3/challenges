'''
write a function that adds "err" to the end of every word whose last letter is
a consonant (not a vowel, y counts as a consonant).
if upper add 'ERR'
"Punctuation? is, important!  double space also"
"Hello from the other siiiiideeee"
"This, is. another! test? case to check your beautiful code."
"Hello, I am Mr Bob."
"hI, hi. hI hi skY! sky? skY sky"
THIS, is crazy!
'''


def err_bob(string):
    '''
    new_string = string.split(' ')
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    output = []

    for word in new_string:
        if word == '':
            output.append(word)

        elif word[-1].isalpha():
            if word[-1] in vowels:
                output.append(word)
            elif word[-1].isupper():
                output.append(word+'ERR')
            else:
                output.append(word+'err')

        else:
            if word[-2] in vowels:
                output.append(word)
            elif word[-2].isupper():
                output.append(word[:-1]+'ERR'+word[-1])
            else:
                output.append(word[:-1]+'err'+word[-1])

    print(' '.join(word for word in output))
    return ' '.join(word for word in output)
    '''
    result = ""
    for k, v in enumerate(string):
        result += v
        if k == len(string)-1 or string[k+1] in " .,:;!?":
            if v.islower() and v not in "aeiou":
                result += "err"
            if v.isupper() and v not in "AEIOU":
                result += "ERR"
    print(result)
    return result
err_bob("Punctuation? is, important!  double space also")
