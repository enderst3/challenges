# guess a number 1 - 1000
# allow as many guesses as necessary
# tell user higher or lower on next guess
# correct guess will end program
# enter 0 to exit

import random

answer = random.randint(1, 1000)
guess = 0 # for while loop needs to be intialized outside the number range

while guess != answer:
    guess = int(input('Please guess a number between 1 and 1000.  Enter 0 to exit: '))
    if guess == 0:
        print('You have exited he game.')
        break
    elif guess < answer:
        print("Please guess higher")
    elif guess > answer:  
        print("Please guess lower")
    else:
        print("Well done, you guessed it")