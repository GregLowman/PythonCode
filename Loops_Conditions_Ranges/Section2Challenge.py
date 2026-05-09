"""Challenge: admit users to a party only if they are between 18 and 30 years old."""
name = input("Hi, what is your name? ")
age = int(input("How old are you, {}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to the party {}".format(name))
else:
    print("Sorry {}, you cannot enter".format(name))
