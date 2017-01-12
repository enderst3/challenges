'''
count the number of duplicate letters in a string
'''


def count_duplicates(word):
    '''
    word = word.lower()
    letter_count = {}
    duplicates = []
    for letter in word:
        letter_count[letter] = word.count(letter)

    for k, v in letter_count.items():
        if v >= 2:
            duplicates.append(k)
    print(len(duplicates))
    '''
    print(len([letter for letter in set(word.lower()) if word.lower().count(letter) > 1]))
    return len([letter for letter in set(word.lower()) if word.lower().count(letter) > 1])

count_duplicates("totally")
count_duplicates("aabBccdeefgG")
count_duplicates("count")
