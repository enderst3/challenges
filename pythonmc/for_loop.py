for i in range(1, 10):
    print('i is now {}'.format(i))

number = "123,456,789"
for i in range(0, len(number)):
    print(number[i])

number = "123,456,789,012,345"
clean_number = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        clean_number = clean_number + number[i]
print(int(clean_number))

for color in ['red', 'blue', 'green', 'yellow']:
    print('This car is ' + color)

# range with a step
for i in range (0, 20, 2):
    print('i is {}'.format(i))

# show multiplication tables
for i in range(1, 13):
    for j in range(1, 13):
        print('{1} * {0} = {2}'.format(i, j, i*j))
    print('------------------')

# skip juice in shopping list
shopping_list = ['pasta', 'rice', 'juice', 'eggs', 'ham', 'bacon']
for item in shopping_list:
    if item == 'juice':
        continue
    print('I need to buy ' + item)

# look for an item in a list 
meats = ['bacon', 'sausage', 'steak', 'chicken', 'fish']
meat_wanted = ''
for meat in meats:
    if meat == 'chicken':
        meat_wanted = meat
        break
if meat_wanted:
    print('We have the meat you want')
else:
    print('Sorry we dont have the meat you want')
