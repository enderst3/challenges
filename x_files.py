"""
if an integer in range is divisible 3 retun X, if divisible by 5 return Files, 
if divisible by both return x files.
"""

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(i, '- X-Files')
    if i % 3 == 0:
        print(i, '- X')
    if i % 5 == 0:
        print(i, '- Files')
    else:
        print(i)