'''
This will be the base for my new lotto project
'''

#Lottery Numbers - www.101computing.net/lottery-numbers

import random

#Initialise an empty list that will be used to store the 6 lucky numbers!
lotteryNumbers = []

for i in range (0,6):
  number = random.randint(1,50)
  #Check if this number has already been picked and ...
  while number in lotteryNumbers:
    # ... if it has, pick a new number instead 
    number = random.randint(1,50)
  
  #Now that we have a unique number, let's append it to our list.
  lotteryNumbers.append(number)

#Sort the list in ascending order
lotteryNumbers.sort()

#Display the lsit on screen:
print(">>> Today's lottery numbers are: ") 
print(lotteryNumbers)