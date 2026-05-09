"""List the public methods of shelve.Shelf to explore the shelve module interface."""
import shelve

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)

