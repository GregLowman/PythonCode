"""Remove all spam items from each meal in a menu using a while loop."""
menu = [
    ["egg", "spam"],
    ["egg", "bacon"],
    ["egg", "bacon", "spam"],
    ["egg", "sausage", "bacon"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

print("Store Menu: ")
for meal in menu:
    while "spam" in meal:
        meal.remove("spam")
    print(meal, end=", ")
    print("-" * 50)
