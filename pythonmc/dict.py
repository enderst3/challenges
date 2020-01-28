fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# # del fruit["lemon"]
# # fruit.clear()
# # print(fruit)
# print(fruit["tomato"])
print(fruit)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we don't have a " + dict_key)

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
