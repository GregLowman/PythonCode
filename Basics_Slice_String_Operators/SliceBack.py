"""Demonstrates reverse slicing and step-based slice notation on strings."""
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]  # Negative step requires start index > end index
print(backwards)
print()

challenge1 = letters[-10:-13:-1]
challenge2 = letters[4::-1]
challenge3 = letters[:-9:-1]
print(challenge1)
print()
print(challenge2)
print()
print(challenge3)

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)
print()

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
