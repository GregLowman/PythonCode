"""Demonstrate any() and all() with truthy/falsy values and empty-string checks."""
entries = [1, 2, 3, 4, 5]

print(f"Entries: {entries}")
print(f"all: {all(entries)}")
print(f"any: {any(entries)}")
print("*" * 40)

print("Iterable with a 'False' value")
entries_with_zero = [1, 2, 0, 4, 5]
print(f"Entries: {entries_with_zero}")

print(f"all: {all(entries_with_zero)}")
print(f"any: {any(entries_with_zero)}")
print("*" * 40)

name = ""
if name:
    print(f"Hello {name}")
else:
    print("Welcome, person with no name")

print("*" * 40)
