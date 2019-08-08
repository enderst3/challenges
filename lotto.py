'''
This will be the base for my new lotto project
'''

#Lottery Numbers - www.101computing.net/lottery-numbers

import random

#Initialise an empty list that will be used to store the 6 lucky numbers!
lotteryNumbers = []
winning_numbers = []
draws = 0

for i in range (0,6):
  number = random.randint(1,10)
  #Check if this number has already been picked and ...
  while number in lotteryNumbers:
    # ... if it has, pick a new number instead 
    number = random.randint(1,10)
  
  #Now that we have a unique number, let's append it to our list.
  lotteryNumbers.append(number)

#Sort the list in ascending order
lotteryNumbers.sort()
print(lotteryNumbers)
'''
while winning_numbers.sort() != lotteryNumbers:
    for i in range (0,2):
        draw_number = random.randint(1,10)
        #Check if this number has already been picked and ...
        while draw_number in winning_numbers:
            # ... if it has, pick a new number instead 
            draw_number = random.randint(1,10)
        
        #Now that we have a unique number, let's append it to our list.
        winning_numbers.append(draw_number)
        draws += 1
        print(draws)
        
winning_numbers.sort()
print(winning_numbers)
'''
#Display the lsit on screen:
# print(">>> Today's lottery numbers are: ") 
# print(lotteryNumbers)
# print("It took {} draws for you to win the lottery!".format(draws))
