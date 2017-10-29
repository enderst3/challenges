# Create a function that takes 2 numbers in form 
# of a string as an input, and outputs the sum (also as a string):

def sum_str(a, b):
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    return str(int(a) + int(b))

print(sum_str('4', '6'))
print(sum_str('72', '19'))