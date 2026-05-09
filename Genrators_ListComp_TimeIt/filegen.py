"""Step-through explorer for a music directory tree — prints path splits and song details."""
import os

root = "music"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        input()
        first_split = os.path.split(path)
        print(first_split)
        input()
        second_split = os.path.split(first_split[0])
        print(second_split)
        input()
        for f in files:
            song_details = f[:-5].split(' - ')
            print(song_details)
            input()
        print("*" * 40)
