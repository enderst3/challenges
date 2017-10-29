# Write a programs that asks for name and age
# Check to see if the person is over 13 and under 30

name = input('Please enter your name: ')
age = int(input('Hello {}!  Please enter your age: '.format(name)))

if age <= 18 or age >= 30:
    print('Sorry {}.  You are unable to enter.'.format(name))
else:
    print('{}, you are able to enter this room.'.format(name))