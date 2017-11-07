# its important to close the file after using it

# cities = ['Portland', 'Seattle', 'Denver', 'Salt Lake City', 'Las Vegas', 'Kansas City', 'Oakland']

# # file will be created if it doesn't exist.  Will be over written if it does exist.
# with open('cities.txt', 'w') as city_file: # the w means write to cities.txt.
#     for city in cities:
#         print(city, file=city_file)# file means write to text file. 
        
cities = []

with open('cities.txt', 'r') as city_file: # opens file as read only 'r'
    for city in city_file:
        # cities.append(city)
        cities.append(city.strip('\n')) # takes out '\n' in the list. 
                                        # strip only removes chars from the start or end of a string
print(cities)
for city in cities:
    print(city)

# dead = 'Young Loud and Snotty', 'The Dead Boys', 1979, (
#     (1, 'Sonic Reducer'), (2, 'All This and More'), (3, 'What is Love'), (4, 'Not Anymore'))

# with open ('dead_boys.txt', 'w') as dead_file:
#     print(dead, file=dead_file)

with open('dead_boys.txt', 'r') as dead_file:
    contents = dead_file.readline()

dead = eval(contents) # eval is not a good way to deal with data external to the program
                      # because the data could contain damaging contents to the program

print(dead)
title, artist, year, tracks = dead
print(title)
print(artist)
print(year)
