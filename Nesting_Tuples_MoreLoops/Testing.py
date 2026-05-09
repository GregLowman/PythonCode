"""Build album/artist/year display strings from a tuple of album records using index access."""
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

full_list = (welcome, bad, budgie, imelda, metallica)
albums = " "
artist = " "
year = " "

for index, x in enumerate(full_list):
    albums += (full_list[index][0]) + " | "
    artist += (full_list[index][1]) + " | "
    year += (str(full_list[index][2])) + " | "

print("Albums include: \n", albums, "\n")
print("Artist includes: \n", artist, "\n")
print("Years include: \n", year, "\n")
