"""
Write a simple program that, when run, prompts the user for input then prints a result.

Program should ask the user for the number of dice they want to roll as well as the number of sides per die.
"""

import random

def dice_roll():
    dice_number = int(input("How mand dies would you like to roll? "))
    dice_sides = int(input("how man sides do you want your dice to have? "))

    rolls = range(dice_number)
    die = 1

    for result in rolls:
        roll = random.randint(1, dice_sides)
        print("Die {} Rolled: {}".format(die, roll))
        die += 1
    return True

dice_roll()