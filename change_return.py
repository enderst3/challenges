"""
Calculate the smallest number of coins needed to represent an amount of cents
less than 100.

>>> make_change(94)
3 quarters
1 dimes
1 nickles
4 pennies

"""

def make_change(change):
    quarters = change // 25
    change = change % 25
    dimes = change // 10
    change = change % 10
    nickles = change // 5
    change = change % 5

    print("{} quarters\n{} dimes\n{} nickles\n{} pennies".format(quarters, dimes, nickles, change))

