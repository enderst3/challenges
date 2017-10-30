# ip = input('enter an ip address: ')
# print(ip.count('.'))


color_list = ['red', 'green', 'orange']
color_list.append('blue')
for color in color_list:
    print('I have {} paint.'.format(color))


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
# numbers.sort()
print(sorted(numbers))