'''
A simple text game.  Using random, and timer.
'''

import random
import time

# intro text
def intro():
    print("You are in a the land of dragons.  There are 2 caves in front of you,")
    print(" you see two caves in front you.  In one there is a friendly dragon, ")
    print("that will share his treasure with you.  In the other cave the dragon")
    print(" the dragon is far from friendly.  He is hungry and will probably eat you!")
    print()

# choose the cave input and while loop to keep asking until loop broken.
def choose_cave():
    cave = ""
    while cave != '1' and cave != '2':
        cave = input('Which cave will you go into? (1 or 2): ')
        print()
    return cave

# cave text, delayed printing because of the timer.  Random used to chooe caves.
def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(2)
    print("It's dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you!  He opens in jaws and...")
    print()
    time.sleep(4)

    friendly_cave = random.randint(1,2)

    if chosen_cave == str(friendly_cave):
        print("Gives you a treasure chest filled with gold and jewels!  You're rich, and alive!")
        print()

    else:
        print("fire shoots out of his mouth and burns you to a crisp!  You're dead!")
        print()

play_again = 'yes'

# while loop to start game over if yes or y given as input
while play_again =='yes' or play_again == 'y':

    intro()

    cave_number = choose_cave()

    check_cave(cave_number)

    play_again = input("Do you want to play again? (yes or no): ")
