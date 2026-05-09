"""Demonstrate str.split() on whitespace and a delimiter, then convert split values to integers."""
panagram = """The quick brown
fox jumps\t over
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))
print()

generated_list = [
    '9', ' ',
    '2', '2', '3', ' ',
    '3', '7', '2', ' ',
    '0', '3', '6', ' ',
    '8', '5', '4', ' ',
    '7', '7', '5', ' ',
    '8', '0', '7',
]

values = "".join(generated_list)

values_list = values.split()
print(values_list)
new_list = []

for number in values_list:
    new_list.append(int(number))
print(new_list)
