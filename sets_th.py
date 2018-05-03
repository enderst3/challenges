'''
Let's write some functions to explore set math a bit more. 
We're going to be using this COURSES dict in all of the examples. Don't change it, though!

So, first, write a function named covers that accepts a single parameter, 
a set of topics. Have the function return a list of courses from COURSES 
where the supplied set and the course's value (also a set) overlap.

For example, covers({"Python"}) would return ["Python Basics"].

set.difference() = - returns new set that are not in the other set

set.intersection() = & new set with elements common to both sets

set.symmetric_difference() = ^ returns items that are not in both sets

set.union() = | returns common items that are in both sets


'''

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topic):
    course = []
    # key is the course name and the value is the set
    for key, value in COURSES.items():
        # & = .intersection()
        # we are checking to see if the topic is in the key
        # looks for anything in common
        if value & topic:
            course.append(key)
    return course

"""
OK, let's create something a bit more refined. 
Create a new function named covers_all that takes a single set as an argument. 
Return the names of all of the courses, in a list, where all of the topics in the supplied set are covered.

For example, covers_all({"conditions", "input"}) would return ["Python Basics", "Ruby Basics"]. 
Java Basics and PHP Basics would be excluded because they don't include both of those topics.

"""

def covers_all(topic):
    course = []
    # key is the course name and the value is the set
    for key, value in COURSES.items():
        # & = .intersection()
        # we are checking to see if the topic is in the value
        # it has to == the topic
        if value & topic == topic:
            course.append(key)
    return course