number = "123,456,789,012,345"
clean_number = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        # clean_number = clean_number + number[i]
        clean_number += number[i] # this is a cleaner more efficient way to do the above
print(int(clean_number))

greeting = 'Good '
greeting += 'morning '
print(greeting)

greeting *= 5
print(greeting)

# += -= are samples of binary operators