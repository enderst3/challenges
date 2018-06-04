"""
The defaultdict tool is a container in the collections class of Python. 
It's similar to the usual dictionary (dict) container, but it has one difference: 
The value fields' data type is specified upon initialization. 
For example:

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
This prints:

('python', ['awesome', 'language'])
('something-else', ['not relevant'])
In this challenge, you will be given 2 integers, n and m. There are  words, which might repeat, in word group a. 
There are m words belonging to word group b. For each m words, check whether the word has appeared in group a or not. 
Print the indices of each occurrence of m in group a. If it does not appear, print -1.


"""

from collections import defaultdict

n,m=[int(x) for x in input().split(' ')]
lis=[]
d=defaultdict(list)
for i in range(1,n+1):
    d[input()].append(i)
for _ in range(m):
    lis.append(input())
for x in lis:
    if x in d:
        print(' '.join(map(str,d[x])))
    else:
        print(-1)