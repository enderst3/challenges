# its important to close the file after using it

cities = ['Portland', 'Seattle', 'Denver', 'Salt Lake City', 'Las Vegas', 'Kansas City', 'Oakland']

# file will be created if it doesn't exist.  Will be over written if it does exist.
with open('cities.txt', 'w') as city_file: # the w means write to cities.txt.
    for city in cities:
        print(city, file=city_file)# file means write to text file. 

