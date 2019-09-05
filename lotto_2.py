import random

winning_numbers = []
ticket_numbers = []

def ticket_draw():
    # ticket numbers
    for i in range(0,2):
        number = random.randint(1,5)
        while number in ticket_numbers:
            number = random.randint(1,5)
        ticket_numbers.append(number)
    ticket_numbers.sort()

    # winning numbers
    for i in range(0,2):
        number = random.randint(1,5)
        while number in winning_numbers:
            number = random.randint(1,5)
        winning_numbers.append(number)
    winning_numbers.sort()
    
    # check to see if you won
    if ticket_numbers == winning_numbers:
        print("Your ticket {}".format(ticket_numbers))
        print("Winning numbers {}".format(winning_numbers))
        print('Congratulations!  You won!')
    else:
        print("Sorry you lose")
        print("Your ticket {}".format(ticket_numbers))
        print("Winning numbers {}".format(winning_numbers))
          
ticket_draw()
