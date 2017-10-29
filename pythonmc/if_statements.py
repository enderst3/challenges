# guess a number between one and 50

import random

guess = int(input('Guess a number between 1 and 50: '))
number = random.randint(1,50)

if guess != number:
    if guess < number:
        guess = int(input('Please guess higher: '))
    else:
        guess = int(input('Please guess lower: '))
    if guess == number:
        print('Great guess!  You are a winner!')
    else:
        print('Sorry!  You should have guessed ' + str(number) + '!')
else:
    print('Great guess!  You are a winner!')


