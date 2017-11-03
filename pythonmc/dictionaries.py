truck = {'make': 'Ford', 'model': 'F-150', 'color': 'yellow', 'engine': '5.4L'}
print(truck['make'])
print(truck['color'])

print('=' * 50)

fruit = {'orange': 'a sweet citrus fruit',
         'apple': 'good for making cider',
         'lemon': 'a sour citrus fruit',
         'grape': 'good for making wine',
         'lime': 'like a lemon, but green'}
print(fruit['lemon'])

print('=' * 50)

# how to append dictionary
fruit['kiwi'] = 'fuzzy and brown, but green in the middle' 
print(fruit)
# you can change the value the same way
fruit['orange'] = 'great for juice'
print(fruit)

# to delete a key and value.  
# del fruit['kiwi']
# print(fruit)

# to clear a dictionary
# fruit.clear()

print('=' * 50)

'''
# to look for a key in a dictionary and print value
while True:
    dict_key = input('Please enter a fruit: ')
    if dict_key == 'quit': # allows user to exit loop
        break
    description = fruit.get(dict_key, 'We dont have a ' + dict_key) # a different way of doing what is below
    print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print('We dont have a ' + dict_key)
'''

# to print the key
for key in fruit:
    print(key)

print('=' * 50)

# to print the value
for description in fruit: 
    print(fruit[description])

print('=' * 50)

# order will always be different

# to keep the order the same when printing the dictionary
# ordered_keys = list(fruit.keys()) # makes a list of keys
# # print(ordered_keys)

# ordered_keys.sort() # sorts the list
# ordered_keys = sorted(list(fruit.keys())) # create varible is needed later
# for key in ordered_keys:
#     print(key + ' - ' + fruit[key])

# most simplified way of printing and orders list.
# use if you dont need a variable like above
for food in sorted(fruit.keys()):
    print(food + ' - ' + fruit[food])

print('=' * 50)

# .items() is the iterator turns into list of tuple
# will not be in order unless sorted
for key, value in fruit.items():
    print(key + ' - ' + value)

print('=' * 50)

# prints key and value without converting to tuple
# will not be in order unless sorted
for food in fruit:
    print(food + ' - ' + fruit[food])
# print(fruit[key])

print('=' * 50)

# items() turns the dict into a list of tuples
f_list_tuple = fruit.items()
print(f_list_tuple)

print('=' * 50)

# tuple(.items()) will turn the dict into a tuple of tuples
fruit_tuple = tuple(fruit.items())
print(fruit_tuple)

print('=' * 50)

for fruit in fruit_tuple:
    item, description = fruit
    print(item + ' - ' + description)

 print('=' * 50)

 