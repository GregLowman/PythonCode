"""Demonstrates string concatenation, repetition, and membership operators."""
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1+string2+string3+string4+string5)

print("he's " "probably " "pining  " "for the " "fjords")

print("Hello " * 5)

print("hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "Friday"
print("day" in today)
print("Fri" in today)
print("thur" in today)
print("parrot" in "fjord")
