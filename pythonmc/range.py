my_list = list(range(10))
print(my_list)

even = list(range(0, 10, 2)) # start stop step [0:10:2]
odd = list(range(1, 10, 2))

print(even)
print(odd)

my_string = 'abcdefghijklmnopqrstuvwxyz'
print(my_string.index('e')) # output 4
print(my_string[4]) # output e

decimals = range(0, 100)
my_range = decimals[3:40:3]
print(my_range == range(3, 40, 3)) # will print true they are the same
range_1 = range(0, 5, 2)
range_2 = range(0, 6, 2)
print(list(range_1))
print(list(range_2))
print(range_1 == range_2) # true

r = range(0, 100)
print(r)

for i in r[::-2]: # will count from 99 to 0 by 2 because of -2
    print(i)

print('=' * 10)

for i in range(99, 0, -2): # will count from 99 to 0 by 2 because of -2
    print(i)

print('=' * 10)

print(range(0, 100)[::-2] == range(99, 0, -2)) #true

for i in range(0, 99, -2):
    print(i) # will not print anything  no way to count from 0, needs to start at 99 not 0

backstring = 'egugnal lufrewop yrev a si nohtyp'
print(backstring[::-1])

r = range(0, 10)
for i in r[::-1]:
    print(i)

o = range(0, 100, 4)
print(o)
for i in o:
    print(i)
p = o[::5]
print(p)
for i in p:
    print(i)
