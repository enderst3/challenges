# Treehouse tuples course

a = 5
b = 20

a, b = b, a

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

# Create a function that returns the multiplied value of the supplied arguments

def multiply(*args):
    output = 1
    for arg in args:
        output = output * arg
    print(output)


course_minutes = {'python basics': 232, 'django basics': 237, 'flask basics': 189, 'java basics': 133}

for course, minutes in course_minutes.items():
  print('{} is {} minutes long'.format(course, minutes))
    
for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
    print('{}: {}'.format(index+1, letter))


# create a function that takes a single string but returns a tuple of different
# string formats.  All upper, are lower, titlecase, and reversed

def stringcases(string):
    return (string.upper(), string.lower(), string.title(), string[::-1])


# create a function that takes 2 iterables.  should return a list of tuples.
# each tuple will hold the first item of each iterable, then the second and so on
# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

# def combo(iter1, iter2):
#     combo_list = []
#     for index, value in enumerate(iter1):
#         tuple = value, iter2[index]
#         combo_list.append(tuple)
#     return combo_list


def combo(iter1, iter2):
    return list(zip(iter1, iter2))
