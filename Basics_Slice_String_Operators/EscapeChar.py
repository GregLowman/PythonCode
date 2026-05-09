"""Demonstrates escape characters, raw strings, and multi-line string literals."""
split_string = "This string has been \n split over \n several \n lines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting"')
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

print("""The pet shop owner said "No,no, \
 'e's uh,...he's resting". """)

another_split_string = """This string has been \
split over
several \
lines """

print(another_split_string)

print(r"c:\Users\Glowm\notes.txt")
print("c:\\Users\\Glowm\\notes.txt")
