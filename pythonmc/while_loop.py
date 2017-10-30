# simple loop
i = 0 # sets the counter at 0
while i < 10:
    print('i is now {}'.format(i))
    i += 1 # increments the counter

exits = ['east', 'south']

chosen_exit = ''
while chosen_exit not in exits:
    chosen_exit = input('Choose a direction(north, south, east, or west): ')
    if chosen_exit == 'quit':
        print('Game over')
        break

else:
    print('You made it out!')