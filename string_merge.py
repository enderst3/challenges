"""
Given two words and a letter, return a single word that's a combination of both words, 
merged at the point where the given letter first appears in each word. 
he returned word should have the beginning of the first word and the ending of the second, 
with the dividing letter in the middle. You can assume both words will contain the dividing letter.

Examples
string_merge("hello", "world", "l")      ==>  "held"
string_merge("coding", "anywhere", "n")  ==>  "codinywhere"
string_merge("jason", "samson", "s")     ==>  "jasamson"
string_merge("wonderful", "people", "e") ==>  "wondeople"
"""

def string_merge(string1, string2, letter):
    splice_1 = string1.index(letter)
    splice_2 = string2.index(letter)
    return string1[:splice_1] + string2[splice_2:]