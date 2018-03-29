# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

dict = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
        'Kenneth Love': ['Python Basics', 'Python Collections', 'Python the hard way']}

# length of dict
def num_teachers(dict):
    return len(dict)

# total number of courses
def num_courses(dict):
    class_list = []
    for v in dict.values():
        for course in v:
            class_list.append(course)
    return len(class_list)

# list of course names
def courses(dict):
    class_list = []
    for v in dict.values():
        for course in v:
            class_list.append(course)
    return class_list

# teacher with most courses
def most_courses(dict):
    courses = 0
    teacher = ''
    for k, v in dict.items():
        if len(v) > courses:
            courses = len(v)
            teacher = k
    return teacher

# return a list of lists with teacher, and number of courses
def stats(dict):
    lista = []
    for k, v in dict.items():
        lista.append([k, len(v)])
    return lista