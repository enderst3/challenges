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

ones_teens = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def written(number):
    if number >= 1 and number < 19:
        # print(ones_teens[number])
        return ones_teens[number]