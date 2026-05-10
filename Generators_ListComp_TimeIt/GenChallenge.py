"""Generator challenge: yields absolute paths of all files matching a given extension under a root directory."""
import fnmatch
import os


def find_path(root, file_type):
    for path, directories, files, in os.walk(root):
        for artist in directories:
            artist_path = os.path.join(path, artist)
            for album_root, albums, _ in os.walk(artist_path):
                for album in albums:
                    album_path = os.path.join(album_root, album)
                for song_root, _, songs in os.walk(album_path):
                    for song in songs:
                        song_path = os.path.join(song_root, song)
                        absolute_path = os.path.abspath(song_path)
                        yield(absolute_path)


def answer(root, extension):
    for path, directories, files in os.walk(root):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)



file_list = answer("music", "emp3")

for f in file_list:
    print(f)