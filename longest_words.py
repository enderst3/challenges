'''
connect the longest strings in a list using the number of words given
'''


def longest(start_list, num):

    if num < 1:
        print("")
        return ''
    else:
        print(''.join(sorted(start_list, key=len, reverse=True)[:num]))

longest(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
longest(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
longest([], 3)

'''
def longest_consec(strarr, k):

  if k < 1:

    return ""

  words = ["".join(strarr[i:i+k]) for i in range(len(strarr)-k+1)]

  return max(words, key=len, default="")

 '''
