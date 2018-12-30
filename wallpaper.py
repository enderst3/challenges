"""
John wants to decorate a room with wallpaper. 
He has been said that making sure he has the right amount of wallpaper is more complex than it sounds. 
He wants a fool-proof method to getting it right.

John knows that the rectangular room has a length of l meters, a width of w meters, a height of h meters. 
The standard width of the rolls he wants to buy is 52 centimeters. The length of a roll is 10 meters. 
He bears in mind however, that it’s best to have an extra length of wallpaper handy in case of 
mistakes or miscalculations so he wants to buy a length 15% greater than the one he needs.

Last time he did these calculations he caught a headache so could you help John? Your function 
wallpaper(l, w, h) should return as a plain English word in lower case the number of rolls he must buy.

#Example: wallpaper(4, 3.5, 3) should return "ten"

#Notes:

all rolls (even with incomplete width) are put edge to edge
0 <= l, w, h (floating numbers), it can happens that w x h x l is zero
the integer r (number of rolls) will always be less or equal to 20

"""

def wallpaper(l, w, h):

    num_dict = {0:"zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 
                9: "nine", 10: "ten", 11:"eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 
                16:"sixteen", 17:"seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"}

    wall_area = 1.15 * ((2*l*h) + (2*w*h))
    wallpaper = 0.52 * 10
    to_buy = wall_area / wallpaper

    for k,v in num_dict.items():
        if l == 0 or w == 0 or h == 0:
            return 'zero'
        elif int(k) == round(to_buy + 0.5):
            return v


from math import ceil

num_dict = {0:"zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 
9: "nine", 10: "ten", 11:"eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 
16:"sixteen", 17:"seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"}

def wallpaper(l, w, h):
    return "zero" if w*l==0 else num_dict[ceil((2*l+2*w) * h * 1.15 / 5.2)]