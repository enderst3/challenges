'''
This is a guess the number game.  Guess a number between 1 - 20.  The game
will count the number of guesses.

Idea from Invent with Python.
'''

import random

guesses_taken = 0

# asks user for name
user_name = input("Hello!  What is your name? ")

# picks random number using rancom
number = random.randint(1, 20)
print(user_name + ', I am thinking of a number between 1 and 20.')

# while loop to take guesses, and return info on the guess.
while guesses_taken < 6:
    guess = input('Try to guess the number. ')

    # turns string into an in to compare with random number.
    guess = int(guess)

    # add 1 to the number of guesses taken
    guesses_taken = guesses_taken + 1

    if guess > number:
        print("Your guess is too high.  Try again!")

    if guess < number:
        print("Your guess is too low.  Try again!")

    # breaks loop if number is guessed
    if guess == number:
        break
# if number is guessed
if guess == number:
    guesses_taken = str(guesses_taken)
    print("Way to go, " + user_name + "!  You guessed my number in " + guesses_taken + " guesses!")

# if number is not guessed in 6 trys
if guess != number:
    number = str(number)
    print("Sorry you didn't guess the number.  The number I was thinking was " + number)
