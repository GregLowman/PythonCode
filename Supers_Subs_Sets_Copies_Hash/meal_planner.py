"""Meal planner: pick a recipe, check pantry stock, and build a shopping list."""
from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a tuple containing `item` and `amount` to the `data` dict."""
    data[item] = data.setdefault(item, 0) + amount


display_dict = {}
needed_items = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key
while True:
    print("Please choose your recipe")
    print("-" * 40)
    for key, value in display_dict.items():
        print(f"{key} - {value} ")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        print(display_dict[choice])
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking Ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy: {quantity_to_buy} of {food_item}")
                add_shopping_item(needed_items, food_item, quantity_to_buy)

for items in sorted(needed_items.items()):
    print(items)
