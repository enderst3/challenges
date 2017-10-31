# Create a list of items either strings or numbers
# then create an iterator using the iter() function and for loop using next().

my_list = ['spam', 'bacon', 'sausage', 'eggs']

my_iterator = iter(my_list)

# these do the same thing

for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)

print("======")

for item in my_list:
    print(item)