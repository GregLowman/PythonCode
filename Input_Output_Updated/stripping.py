"""Demonstrate str.strip(), removeprefix(), and removesuffix() on a line read from a text file."""
filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().strip()

print(first)


chars = "' Twasebv"

for character in first:
    if character in chars:
        print(f"Removing '{character}'")
    else:
        break

print('*' * 80)

for character in first[::-1]:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

chars = "' Twastirlb"
no_apostrophe = first.strip(chars)
print(no_apostrophe)

print('*' * 80)
print('*' * 80)

twas_remove = first.removeprefix("'Twas")
print(twas_remove)
toves_removed = first.removesuffix('toves')
print(toves_removed)
