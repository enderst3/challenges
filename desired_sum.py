'''
How many years will it take you to get your desired_sum?

years(1000, 0.05, 0.18, 1100)
'''


def years(principal, interest, tax, desired_sum):

    years = 0

    while principal < desired_sum:

        principal = principal + ((interest*principal)*(1-tax))
        years += 1

    print(years)
    return years

years(1000, 0.05, 0.18, 1100)
