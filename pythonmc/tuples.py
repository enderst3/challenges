#  tuples are immutable orders set of data
# examples
# t = 'a', 'b', 'c' # this is a tuple without parentheses
# print(t)
# print('a', 'b', 'c')
# print(('a', 'b', 'c'))

sd = 'Mommys Little Monster', 'Social Distortion', 1983
iggy = 'Raw Power', 'Iggy and the Stooges', 1973
clash = 'London Calling', 'The Cash', 1979 # will change clash below
dead = 'Young Loud and Snotty', 'The Dead Boys', 1979, (
    (1, 'Sonic Reducer'), (2, 'All This and More'), (3, 'What is Love'), (4, 'Not Anymore'))
print(sd)
print(iggy[1])

# to change an item in a tuple
clash = clash[0], 'The Clash', clash[2]
print(clash)

for info in sd:
    print(info)

a, b = 12, 13
print(a)
print(b)

# unpacking tuples
title, artist, year = iggy
print(title)
print(artist)
print(year)

title, artist, year, tracks = dead
print(title)
print(artist)
print(year)
print(tracks)
for track in tracks:
    print(track)
    print(track[1])
    print('    ',track[0], track[1])
print('=' * 30)

#  Challenge
# unpack the dead tuple, indent the track and track number by one tab

title, artist, year, tracks = dead
print(title)
print(artist)
print(year)
for song in tracks:
    # print('    ',song[0], song[1])
    track, title = song
    print('\t{} {}'.format(track, title))

# change to a list of tuples
    
dead = 'Young Loud and Snotty', 'The Dead Boys', 1979, (
    [(1, 'Sonic Reducer'), (2, 'All This and More'), (3, 'What is Love'), (4, 'Not Anymore')])
dead[3].append((5,"Ain't Nothin to Do")) 

print(dead)

title, artist, year, tracks = dead
tracks.append((6, 'Hey Little Girl'))
print(dead)

print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print('\t{} {}'.format(track, title))