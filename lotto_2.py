import random

winning_numbers = []
ticket_numbers = []
draw_numbers = []
tickets = 0



def lotto_generator():
    for i in range(0,4):
        number = random.randint(1,10)
        while number in draw_numbers:
            number = random.randint(1,10)
        draw_numbers.append(number)
    print(draw_numbers.sort())

lotto_generator()