"""Add items to a set and use dict.fromkeys to deduplicate a list while preserving order."""
numbers = set()

print(numbers, type(numbers))

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

unique_data = set(data)
print(unique_data)

unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))
