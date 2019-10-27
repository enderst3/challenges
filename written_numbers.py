"""
Write a function that asks for a number in base-10 that's between 1 and 99
then prints out the name of it in English.

>>> written(42)
'fourty-two'

>>> written(1)
'one'

>>> written(99)
'ninety-nine'

"""

ones_teens = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
            16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def written(number):
    if number >= 1 and number < 19:
        # print(ones_teens[number])
        return ones_teens[number]
    elif number >= 20 and number < 100:
        first_digit, second_digit = divmod(number, 10)
        return tens[first_digit - 2] + '-' + ones_teens[second_digit]