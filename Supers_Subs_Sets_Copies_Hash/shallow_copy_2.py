"""Show that a shallow copy shares the same inner list objects as the original."""
lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]
animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

things = animals.copy()

print(things["teddy"])
print(animals["teddy"])

print()

teddy_list.append("toy")
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via `things`")
print(things["teddy"])
print(animals["teddy"])
