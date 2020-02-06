'''
Jumping number is the number that All adjacent digits in it differ by 1.

Given a number, Find if it is Jumping or not .
'''

def jumping_number(number):
    # convert number to list of ints
    n = [int[d] for d in str(num)]
    # iterate through list if math more than 1 return not
    if any(abs(n[i]-n[i+1])!=1 for i in range(len(n)-1)):
        return "Not!!"
    return "Jumping!!"

