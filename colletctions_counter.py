"""
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Sample Code

>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]


Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
Explanation

Customer 1: Purchased size 6 shoe for $55. 
Customer 2: Purchased size 6 shoe for $45. 
Customer 3: Size 6 no longer available, so no purchase. 
Customer 4: Purchased size 4 shoe for $40. 
Customer 5: Purchased size 18 shoe for $60. 
Customer 6: Size 10 not available, so no purchase.

total money earned = 55+45+40+60 = 200
"""


from collections import Counter


n = int(input())
s = Counter(map(int,input().split()))
x = int(input())
total = []

for i in range(x):
    a,b = map(int,input().split())
    if s[a] > 0:
	    total.append(b)
	    s.subtract(Counter([a]))

print(sum(total))