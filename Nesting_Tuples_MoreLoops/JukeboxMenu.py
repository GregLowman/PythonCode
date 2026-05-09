"""Interactive jukebox menu: choose an album then a song from the nested NestedData tracklist."""
from NestedData import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (Invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        song_list = albums[choice - 1][SONG_LIST_INDEX]
    else:
        break

    print("Please choose your song (Invalid choice returns to albums) : ")
    for index, (track_number, songs) in enumerate(song_list):
        print("{}: {}".format(index + 1, songs))

    song_choice = int(input())
    if 1 <= song_choice <= len(song_list):
        title = song_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))
        print("=" * 40)
    else:
        print("Returning to Albums")

