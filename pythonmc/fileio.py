# jabber = open('/Users/Todd/Documents/challenges/pythonmc/sample.txt', 'r') # open opens a file r = read only

# for line in jabber:
#     # print(line) # will print entire file
#     if 'jabberwock' in line.lower(): # converts text to lowercase then looks for jabberwock
#         print(line, end='')

# jabber.close() # closes file  Always close when done with a file

# this is better way to do the above
with open('sample.txt', 'r') as jabber: # with will close the file when done with it
    for line in jabber:
        if 'JAB' in line.upper():
            print(line, end='')

print('=' * 40)

# while loop to get rid of the double spacing
with open('sample.txt', 'r') as jabber:
    line = jabber.readline() # returns a long string after reading the entire file
    while line:
        print(line, end='')
        line = jabber.readline()

print('=' * 40)

# this example will read the file and make a list using readlines() to be used as needed
with open('sample.txt', 'r') as jabber:
    lines = jabber.readlines() # returns a list of string after reading the entire file
print(lines)

for line in lines:
    print(line, end='') # end='' will get rid of the \n in the list

print('=' * 40)