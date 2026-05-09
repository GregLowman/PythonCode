"""Read a mixed string of numbers with arbitrary separators and print their sum."""
number = input("Please enter a series of numbers, using any separators you like: ")
seperator = ""

for char in number:
    if not char.isnumeric():
        seperator = seperator + char

values = "".join(char if char not in seperator else " " for char in number).split()
print(sum([int(val) for val in values]))
