"""Check whether a character entered by the user appears in a string using the 'in' operator."""
parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I dont need that letter")