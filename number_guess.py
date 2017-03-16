'''
This is a guess the number game.  Guess a number between 1 - 20.  The game
will count the number of guesses.

Idea from Invent with Python.
'''

import random

guesses_taken = 0

print("Hello!  What is your name?")
user_name = input()

number = random.randint(1,20)
print(user_name + ', I am thinking of a number between 1 and 20.')


while guesses_taken < 6:
    print('Try to guess the number.')
    guess = input()
    guess = int(guess)

    guesses_taken = guesses_taken + 1

    if guess < number:
        print("Your guess is too low.  Try again!")

    if guess > number:
        print("Your guess is too high.  Try again!")

    if guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken)
    print("Way to go, " + user_name + "!  You guessed my number in " + guesses_taken + " guesses!")

if guess != number:
    number = str(number)
    print("Sorry you didn't guess the number.  The number I was thinking was " + number )
