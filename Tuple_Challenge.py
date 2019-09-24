# Given the tuple below that represents the Imelda May album "More Mayhem", write
# Code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

# imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# print(imelda)

# title, artist, year, track1, track2, track3, track4 = imelda
# print(title, artist, year)
# print(track1,end="\t")
# print(track2, end="\t")
# print(track3, end="\t")
# print(track4, end="\t")

# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# for song in tracks:
#     track, title = song
#     print("\t Track number is {}, Title: {}".format(track, title))

imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])
print("For first time declared imelda tuple {}".format(imelda))

imelda[3].append((5, "All for You"))

print("After including the 5th track imelda tuple is now {}".format(imelda))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))

print("After the appending the 6th track after unpacking, the imelda tuple now {}".format(imelda))
# Unpacking the tuple and printing individually
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\t Track number {}, Title: {}".format(track, title))


