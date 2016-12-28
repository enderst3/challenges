'''
Find the index of the vowels in a given word.
'hello world'
'super'
'python'
'''


def find_vowels(word):
    '''
    vowels = []
    for k, v in enumerate(word):
        if v.lower() in 'aeiouy':
            vowels.append(k)
    print(vowels)
    return(vowels)
    '''
    vowels = [k for k, v in enumerate(word) if v.lower() in 'aeiouy']

    print(vowels)
    return(vowels)
find_vowels('hello world')
