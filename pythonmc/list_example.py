'''

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

numbers = [even, odd]
print(numbers) # prints a list of lists

# nested loops will print list then each number
for number_list in numbers:
    print(number_list)
    for number in number_list:
        print(number)

# both lists are the same
list_1 = []
list_2 = list()

# will print each character in the string as a list of strings
print(list('hello world'))

'''

# add to the programs below so that if it finds a meal without spam
# it prings out each of the ingredients of the meal.
menu = []
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'bacon', 'sausage', 'spam'])
menu.append(['spam','egg', 'spam', 'spam', 'bacon', 'spam'])
menu.append(['spam', 'egg', 'sausage', 'spam'])

for meal in menu:
    if not 'spam' in meal:
        print(meal)# prints list
        for item in meal: 
            print(item)# prints items in list
