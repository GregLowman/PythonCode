"""Conditional expressions in loops: ternary chains for meal contents and FizzBuzz."""
menu = [
    ["egg", 'spam', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
    ['spam', 'egg', 'sausage', 'spam'],
    ['chicken', 'chips']
]

for meal in menu:
    print(meal, "contains sausage" if "sausage" in meal else "contains bacon" if "bacon" in meal else "contains egg")

print()

items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)
print()

for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal, item))
            break

for x in range(1, 31):
    fizzbuzz = "fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)
