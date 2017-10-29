for i in range(1, 10):
    print('i is now {}'.format(i))

number = "123,456,789"
for i in range(0, len(number)):
    print(number[i])

number = "123,456,789,012,345"
clean_number = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        clean_number = clean_number + number[i]
print(int(clean_number))

