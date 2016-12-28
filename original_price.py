'''
 Return the original price of a product, the return type must be of type
 decimal and the number must be rounded to two decimal places.
'''
from decimal import Decimal


def discover_original_price(disc_price, sale_percent):
    '''
    original_price = disc_price / (1-(sale_percent*0.01))
    original_price = round(original_price, 2)
    print(original_price)
    return(original_price)
    '''

    original_price = round(disc_price/((100-sale_percent) * 0.01), 2)
    print(original_price)
    return(original_price)
discover_original_price(458.2, 17.13)
