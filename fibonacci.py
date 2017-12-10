'''
Fibonacci Sequence
'''

a, b = 0, 1
'''
multiple assignment
same as
a = 0
b = 1
'''

for i in range(0, 10): # for loop to go through the range, and print a
    print(a)
    a, b = b, a + b
    '''
    everything on the right is calculated before being asigned on to varibles
    same as
    old_a = a
    a = b
    b = old_a + b
    '''

'''
Fibonacci generator
'''

def fib(number):
    a,b = 0,1
    for i in range(0, number):
        yield('{}: {}').format(i+1, a)# yield is the generator
        a, b = b, a+b

for item in fib(10):# for loop to print each prior loop/item, also calls generator
    print(item)
