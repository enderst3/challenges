# first method to create a 1D list
n = 5 
list = [0] * n
print(list)

print("="*20)

# Second method to create a 1D list
n = 5
list = [0 for i in range(n)]
print(list)

print('='*20)

# Using first method to create a 2D list
rows, cols = (5, 5)
list = [[0]*cols]*rows
print(list)

print('='*20)

# Using second method to create a 2D list
rows, cols = (5, 5)
list = [[0 for i in range(cols)] for j in range(rows)]
print(list)

print('='*20)

# demonstrate working of both methods

rows, cols = (5, 5)

# method 1
list = [[0]*cols]*rows

# lets change the first element of the first row to 1 and prting the list
list[0][0] = 1

for row in list:
    print(row)
# outputs the following 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0]

# method 2
list = [[0 for i in range(cols)] for j in range(rows)]

# again in the list lets change the fire element of the first row to 1 then print list
list[0][0] = 1
for row in list:
    print(row)
# outputs the following as expected 
#[1, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0] 


print('='*20)
'''
We expect only the first element of first row to change to 1 but the first element of every
 row gets changed to 1 in method 2a. This peculiar functioning is because Python uses shallow 
 lists which we will try to understand.

In method 1a, Python doesn’t create 5 integer objects but creates only one integer object 
and all the indices of the array arr point to the same int object as shown.

If we assign the 0th index to a another integer say 1, then a new integer object is created
with the value of 1 and then the 0th index now points to this new int object as shown below

Similarly, when we create a 2d array as “arr = [[0]*cols]*rows” we are essentially the extending 
the above analogy.
1. Only one integer object is created.
2. A single 1d list is created and all its indices point to the same int object in point 1.
3. Now, arr[0], arr[1], arr[2] …. arr[n-1] all point to the same list object above in point 2.

Now lets change the first element in first row of “arr” as
arr[0][0] = 1

=> arr[0] points to the single list object we created we above.(Remember arr[1], arr[2] 
…arr[n-1] all point to the same list object too)
=> The assignment of arr[0][0] will create a new int object with the value 1 and arr[0][0] 
will now point to this new int object.(and so will arr[1][0], arr[2][0] …arr[n-1][0])

So when 2d arrays are created like this, changing values at a certain row will effect 
all the rows since there is essentially only one integer object and only one list object 
being referenced by the all the rows of the array.

As you would expect, tracing out errors caused by such usage of shallow lists is difficult. 
Hence the better way to declare a 2d array is
'''

# best way to create 2D  
rows, cols = (5, 5)
list = [[0 for i in range(cols)] for j in range(rows)]


# This method creates 5 separate list objects unlike method 2a. 
# One way to check this is using the ‘is’ operator which checks if 
# the two operands refer to the same object.

rows, cols = (5, 5)
# method 2
list = [[0 for i in range(cols)] for j in range(rows)]

# check if list[0] and list[1] refer to the same object
print(list[0] is list[1])
# prints False

# method 1
list = [[0]*cols]*rows

# check if list[0] and list[1] refer to the same object
# Prints True becaus ether eis only one list boject being created
print(list[0] is list[1])

print('='*20)
'''
here's the program that creates a numerical table with two rows and three columns, 
and then makes some manipulations with it:
'''
a = [[1, 2, 3], [4, 5, 6]]
print(a[0])
print(a[1])
b = a[0]
print(b)
print(a[0][2])
a[0][1] = 7
print(a)
print(b)
b[2] = 9
print(a[0])
print(b)
'''
The first element of a here — a[0] — is a list of numbers [1, 2, 3]. 
The first element of this new list is a[0][0] == 1; moreover, a[0][1] == 2, a[0][2] == 3, 
a[1][0] == 4, a[1][1] == 5, a[1][2] == 6.


'''

print('='*20)