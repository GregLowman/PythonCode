"""Print meals from a menu: spam-free meals list their items; spam-containing meals report their spam count."""
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

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count("spam")))

